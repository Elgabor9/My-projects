'''
first my code takes the user's name and save it in a dict then it asks the user what he wants to do
the user can perform addition,subtraction,multiplication and division in every time
the user can do more than one operation of the same type at a time
if the user input is not valid then it will ask the user again
'''
name=input("What is your name: ")
names={"user":name}
print("Hello ",names["user"],"\U00002764")
uses=0
while True:
    if uses==0:
        user=input("How can i help you today \U0001F607: ")
        uses+=1
    else:
        user=input("What opperation do you want to perform now?: ")
    if user=="add":
        first_no=int(input("Enter first number: "))
        second_no=int(input("Enter second number: "))
        sum=first_no+second_no
        print("Here is the result of the addition you requested ",names["user"]," : ",sum)

        user=input("Do you want to add another number? \U0001F914: ")
        while user=="yes" or user=="YES" or user=="Yes" or user=="YEs" or user=="YeS" or user=="yES" or user=="yEs" or user=="yeS":
            #here it checks if the user wants to add more numbers
            add_more=int(input("Enter the number you want to add: "))
            sum+=add_more
            print("Here is the result of the addition you requested ",names["user"]," : ",sum)
            user=input("Do you want to add another number? \U0001F914: ")

    elif user=="sub":
        first_no=int(input("Enter first number: "))
        second_no=int(input("Enter second number: "))
        diff=first_no-second_no
        print("Here is the result of the subtraction you requested ",names["user"]," : ",diff)

        user = input("Do you want to subtract another number? \U0001F914: ")
        while user == "yes" or user == "YES" or user == "Yes" or user == "YEs" or user == "YeS" or user == "yES" or user == "yEs" or user == "yeS":
            #here it checks if the user wants to subtract more numbers
            diff_more = int(input("Enter the number you want to subtract: "))
            diff -= diff_more
            print("Here is the result of the subtraction you requested ", names["user"], " : ", diff)
            user = input("Do you want to subtract another number? \U0001F914: ")

    elif user=="mult":
        first_no=int(input("Enter first number: "))
        second_no=int(input("Enter second number: "))
        mul=first_no*second_no
        print("Here is the result of the multiplication you requested ",names["user"]," : ",mul)

        user = input("Do you want to multiply another number? \U0001F914: ")
        while user == "yes" or user == "YES" or user == "Yes" or user == "YEs" or user == "YeS" or user == "yES" or user == "yEs" or user == "yeS":
            #here it checks if the user wants to multiply more numbers
            mult_more = int(input("Enter the number you want to multiply: "))
            mul *= mult_more
            print("Here is the result of the multiplication you requested ", names["user"], " : ", mul)
            user = input("Do you want to multiply another number? \U0001F914: ")

    elif user=="div":
        first_no=int(input("Enter first number: "))
        second_no=int(input("Enter second number: "))
        divi=first_no/second_no
        print("Here is the result of the division you requested ",names["user"]," : ",divi)

        user = input("Do you want to divide another number? \U0001F914: ")
        while user == "yes" or user == "YES" or user == "Yes" or user == "YEs" or user == "YeS" or user == "yES" or user == "yEs" or user == "yeS":
            #here it checks if the user wants to divide more numbers
            div_more = int(input("Enter the number you want to divide: "))
            divi *= div_more
            print("Here is the result of the division you requested ", names["user"], " : ", divi)
            user = input("Do you want to divided another number? \U0001F914: ")

    else:
        print("Sorry",names["user"],"I did not understand you","\U0001f62d")
        #here if the user input is not valid then it will ask the user again