import re
'''
My code is adding candidates to the voting system
Candidates can be removed to
you can vote to candidates
At the end of the voting system, the winner is displayed
'''
class VotingSystem:
    def __init__(self):
        self.__votes = {}

    def add_candidate(self, name):

        name = name.strip() # This is for when the user enters a space at the beginning or end of the name.
        if re.fullmatch(r"(?=.*[A-Za-z])[A-Za-z _]+", name):# checks if the name is valid or not.
            # This is for checking if the name contains only letters and spaces or underscores as the name shouldn't be (__) or (" ").
            if name not in self.__votes: # Here we check if the candidate already exists.
                self.__votes[name] = 0
                print(f"Candidate '{name}' added successfully")
            else:
                print("Candidate already exists")
        else:
            print("Candidate name should contain only letters and (spaces or underscores)")

    def remove_candidate(self, name):

        if name in self.__votes: # Here we check if the candidate exists.
            del self.__votes[name]
            print(f"Candidate '{name}' removed successfully")
        else:
            print("Candidate not found")

    def vote_to_candidate(self, name):

        # check if the candidate exists (Encapsulation)
        if name in self.__votes:
            self.__votes[name]+=1
            print(f"Voting for '{name}' done successfully")
        else:
            print("Candidate not found")

    def display_the_winner(self):

        if not self.__votes: #Here we check if there is no candidate in the voting system.
            print("No candidates in the voting system")
            return
        max_votes = max(self.__votes.values())
        winners = [candidate for candidate, votes in self.__votes.items() if votes == max_votes]
        # Here the code checks if there is a tie between the candidates with the same number of votes.
        if len(winners) == 1:
            print(f"The winner is : {winners[0]} with {max_votes} votes")
        else:
            print(f"Tie between: {', '.join(winners)} with {max_votes} votes each")
