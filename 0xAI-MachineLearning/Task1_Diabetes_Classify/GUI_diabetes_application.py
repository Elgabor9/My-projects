
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import pandas as pd
import pickle
import os

MODEL_PATH = "./model/log_reg_model.pkl"  # change to decision_tree_model.pkl or random_forest_model.pkl if you prefer

def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found at {path}. Train and save the model first from the notebooks.")
    with open(path, "rb") as f:
        return pickle.load(f)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diabetes Classifier")
        self.geometry("520x520")

        self.model = None
        try:
            self.model = load_model()
        except Exception as e:
            messagebox.showwarning("Model", f"Could not load model: {e}")

        # Inputs
        self.vars = {
            "gender": tk.StringVar(value="Male"),
            "age": tk.DoubleVar(value=40.0),
            "hypertension": tk.StringVar(value="0"),
            "heart_disease": tk.StringVar(value="0"),
            "smoking_history": tk.StringVar(value="never"),
            "bmi": tk.DoubleVar(value=28.0),
            "hba1c_level": tk.DoubleVar(value=5.6),
            "blood_glucose_level": tk.DoubleVar(value=120.0),
        }

        row = 0
        ttk.Label(self, text="Gender").grid(row=row, column=0, sticky="w", padx=8, pady=6)
        ttk.Combobox(self, textvariable=self.vars["gender"], values=["Male","Female","Other"]).grid(row=row, column=1, padx=8, pady=6)
        row += 1

        ttk.Label(self, text="Age").grid(row=row, column=0, sticky="w", padx=8, pady=6)
        ttk.Entry(self, textvariable=self.vars["age"]).grid(row=row, column=1, padx=8, pady=6)
        row += 1

        ttk.Label(self, text="Hypertension (0/1)").grid(row=row, column=0, sticky="w", padx=8, pady=6)
        ttk.Combobox(self, textvariable=self.vars["hypertension"], values=["0","1"]).grid(row=row, column=1, padx=8, pady=6)
        row += 1

        ttk.Label(self, text="Heart Disease (0/1)").grid(row=row, column=0, sticky="w", padx=8, pady=6)
        ttk.Combobox(self, textvariable=self.vars["heart_disease"], values=["0","1"]).grid(row=row, column=1, padx=8, pady=6)
        row += 1

        ttk.Label(self, text="Smoking History").grid(row=row, column=0, sticky="w", padx=8, pady=6)
        ttk.Combobox(self, textvariable=self.vars["smoking_history"], values=["never","current","former","ever","not current","No Info"]).grid(row=row, column=1, padx=8, pady=6)
        row += 1

        ttk.Label(self, text="BMI").grid(row=row, column=0, sticky="w", padx=8, pady=6)
        ttk.Entry(self, textvariable=self.vars["bmi"]).grid(row=row, column=1, padx=8, pady=6)
        row += 1

        ttk.Label(self, text="HbA1c Level").grid(row=row, column=0, sticky="w", padx=8, pady=6)
        ttk.Entry(self, textvariable=self.vars["hba1c_level"]).grid(row=row, column=1, padx=8, pady=6)
        row += 1

        ttk.Label(self, text="Blood Glucose Level").grid(row=row, column=0, sticky="w", padx=8, pady=6)
        ttk.Entry(self, textvariable=self.vars["blood_glucose_level"]).grid(row=row, column=1, padx=8, pady=6)
        row += 1

        ttk.Button(self, text="Predict", command=self.predict).grid(row=row, column=0, columnspan=2, pady=16)

        self.result_var = tk.StringVar(value="Prediction: -")
        ttk.Label(self, textvariable=self.result_var, font=("Arial", 14)).grid(row=row+1, column=0, columnspan=2, pady=6)

    def predict(self):
        try:
            if self.model is None:
                self.model = load_model()
            # Build a single-row DataFrame
            data = {
                "gender": [self.vars["gender"].get()],
                "age": [float(self.vars["age"].get())],
                "hypertension": [int(self.vars["hypertension"].get())],
                "heart_disease": [int(self.vars["heart_disease"].get())],
                "smoking_history": [self.vars["smoking_history"].get()],
                "bmi": [float(self.vars["bmi"].get())],
                "hba1c_level": [float(self.vars["hba1c_level"].get())],
                "blood_glucose_level": [float(self.vars["blood_glucose_level"].get())],
            }
            X = pd.DataFrame(data)
            proba = None
            if hasattr(self.model, "predict_proba"):
                proba = self.model.predict_proba(X)[:,1][0]
            pred = self.model.predict(X)[0]
            if proba is not None:
                self.result_var.set(f"Prediction: {'Diabetes' if pred==1 else 'No Diabetes'} (p={proba:.3f})")
            else:
                self.result_var.set(f"Prediction: {'Diabetes' if pred==1 else 'No Diabetes'}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = App()
    app.mainloop()
