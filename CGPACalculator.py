import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

class CGPACalculator:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("CGPA and GPA Calculator")

        self.grade_points = {
            'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0,
            'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'F': 0.0
        }

        # Format the grade point table as a string
        grade_point_table_text = "Grade    Marks Range    Grade Point\n"
        grade_point_table_text += "-----------------------------------\n"
        grade_point_table_text += "A+       90-100        4.00\n"
        grade_point_table_text += "A        80-89         4.00\n"
        grade_point_table_text += "A-       75-79         3.67\n"
        grade_point_table_text += "B+       70-74         3.33\n"
        grade_point_table_text += "B        65-69         3.00\n"
        grade_point_table_text += "B-       60-64         2.67\n"
        grade_point_table_text += "C+       55-59         2.33\n"
        grade_point_table_text += "C        50-54         2.00\n"
        grade_point_table_text += "F         0-49         0.00"

        # Display the grade point table on the main page
        grade_point_label = tk.Label(self.window, text=grade_point_table_text, font=("Courier", 10), justify="left", anchor="w")
        grade_point_label.grid(row=0, column=2, rowspan=10, padx=10, pady=10, sticky="n")

        self.displayEntries()

    def displayEntries(self):
        # CGPA and Credit Hours Input
        tk.Label(self.window, text="Enter current CGPA:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_cgpa = tk.Entry(self.window)
        self.entry_cgpa.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.window, text="Enter total credit hours earned:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_credit_hours = tk.Entry(self.window)
        self.entry_credit_hours.grid(row=1, column=1, padx=10, pady=5)

        # Number of subjects input
        tk.Label(self.window, text="Enter number of subjects:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_num_subjects = tk.Entry(self.window)
        self.entry_num_subjects.grid(row=2, column=1, padx=10, pady=5)

        # Button to create subject input fields
        tk.Button(self.window, text="Create Subject Inputs", command=self.create_subject_inputs).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Frame to hold dynamic subject input fields
        self.frame_subject_inputs = tk.Frame(self.window)
        self.frame_subject_inputs.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Button to calculate CGPA
        tk.Button(self.window, text="Calculate CGPA", command=self.calculate_cgpa).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Label to display the result
        self.result_label = tk.Label(self.window, text="", justify="left", padx=10)
        self.result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        # Run the Tkinter event loop
        self.window.mainloop()

    def calculate_cgpa(self):
        # Get inputs from the user
        self.cgpa_input = self.entry_cgpa.get()
        self.cgpa_credit_hours_input = self.entry_credit_hours.get()
        
        # Validation check for CGPA (CGPA must be between 0 and 4)
        try:
            self.cgpa = float(self.cgpa_input)
            if not (self.cgpa>=0 and self.cgpa <= 4):
                messagebox.showerror("Invalid Input", "CGPA must be between 0 and 4.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid CGPA value between 0 and 4.")
            return

        # Validation check for cgpa_credit_hours (must be positive)
        try:
            self.cgpa_credit_hours = int(self.cgpa_credit_hours_input)
            if self.cgpa_credit_hours <= 0:
                raise ValueError("Credit hours must be a positive integer.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for credit hours.")
            return
        
        # Initialize variables to track total quality points and credit hours
        self.total_gpa_quality_pts = 0
        self.total_gpa_credit_hours = 0
        
        # Process each subject input
        for i in range(num_subjects):
            self.grade = grade_inputs[i].get()
            self.credit_hours = credit_hours_inputs[i].get()
            
            # Validate grade selection
            if not self.grade:
                messagebox.showerror("Invalid Input", f"Please select a grade for subject {i + 1}.")
                return
            
            try:
                self.credit_hours = float(self.credit_hours)
                if self.credit_hours <= 0:
                    messagebox.showerror("Invalid Input", f"Credit hours for subject {i + 1} must be positive.")
                    return
            except ValueError:
                messagebox.showerror("Invalid Input", f"Please enter a valid positive number for credit hours of subject {i + 1}.")
                return
            
            # Determine the grade point based on the grade entered
            grade_points = {
                'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0,
                'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'F': 0.0
            }
            
            if self.grade in grade_points:
                self.quality_pt = grade_points[self.grade] * self.credit_hours
            else:
                messagebox.showerror("Invalid Input", f"Invalid grade for subject {i + 1}.")
                return
            
            self.total_gpa_quality_pts += self.quality_pt      # Calculate quality points in this semester (GPA)
            self.total_gpa_credit_hours += self.credit_hours

            self.cgpa_calculated = (self.cgpa * self.cgpa_credit_hours + self.total_gpa_quality_pts) / (self.cgpa_credit_hours + self.total_gpa_credit_hours)  
        
        # Show results
        # result_text = f"Total quality points this semester: {total_gpa_quality_pts:.4f}\n"
        result_text = f"Total credit hours this semester: {self.total_gpa_credit_hours:.2f}\n"
        result_text += f"GPA: {self.total_gpa_quality_pts / self.total_gpa_credit_hours:.4f}\n"
        result_text += f"Total credit hours earned: {self.cgpa_credit_hours + self.total_gpa_credit_hours}\n"
        result_text += f"CGPA: {self.cgpa_calculated:.4f}"

        self.result_label.config(text = result_text)

    def create_subject_inputs(self):
        global num_subjects, grade_inputs, credit_hours_inputs
        num_subjects = self.entry_num_subjects.get()
        
        try:
            num_subjects = int(num_subjects)
            if num_subjects > 17:
                messagebox.showerror("Invalid Input", "Maximium number of subjects is 17.")
                return
            if num_subjects <= 0:
                messagebox.showerror("Invalid Input", "Number of subjects must be a positive integer.")
                return
                
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of subjects.")
            return
        
        # Clear previous input fields if any
        for widget in self.frame_subject_inputs.winfo_children():   # Clear subject input
            widget.destroy()

        grade_inputs = []
        credit_hours_inputs = []

        for i in range(num_subjects):
            tk.Label(self.frame_subject_inputs, text=f"Enter grade for subject {i + 1}:").grid(row=i, column=0, padx=10, pady=5)
            grade_input = ttk.Combobox(self.frame_subject_inputs, values=["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "F"], state="readonly")
            grade_input.grid(row=i, column=1, padx=10, pady=5)
            grade_inputs.append(grade_input)

            tk.Label(self.frame_subject_inputs, text=f"Enter credit hours for subject {i + 1}:").grid(row=i, column=2, padx=10, pady=5)
            credit_hours_input = tk.Entry(self.frame_subject_inputs)
            credit_hours_input.grid(row=i, column=3, padx=10, pady=5)
            credit_hours_inputs.append(credit_hours_input)