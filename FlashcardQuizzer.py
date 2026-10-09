import tkinter as tk
from tkinter import messagebox
import random
class FlashcardQuizzer:
    def __init__(self, window):
        window = tk.Tk()
        self.window = window
        self.window.title("Flashcard Quizzer")  # Define the title of the GUI
        self.window.geometry("1200x800")
        
        # Create flashcard storage 
        self.flashcards = {}                    # The dictionary store the keys and valie
        self.questionslist = []                 # The list store the key from the dictionary

        self.question_index = -1                 # To track the index of the current question
        self.score = 0
        self.question_number = 0 
        self.grades = ''
        self.praise= ""
        self.marks= 0 

        # Main Frame
        self.main_frame = tk.Frame(self.window)    #Create first frame name "Main frame " which is used for setting
        self.main_frame.pack(pady=20)              

        # Add Flashcard Section
        # All of it inside the "Main Frame"
        self.question_label = tk.Label(self.main_frame, text="Question:",font=("Trebuchet MS",20,"bold"),fg="black")   #Display the text 'question' and grid it
        self.question_label.grid(row=0, column=0, padx=17, pady=20)           

        self.question_setup = tk.Entry(self.main_frame, width=50,font=("Trebuchet MS",20,"bold"),fg="black")           #Create the entry forms for the user to set the question
        self.question_setup.grid(row=0, column=1, padx=20, pady=20)           

        self.answer_label = tk.Label(self.main_frame, text="Answer:",font=("Trebuchet MS",20,"bold"),fg="black")       #Display the text 'answer' and grid it
        self.answer_label.grid(row=1, column=0, padx=20, pady=20) 

        self.answer_setup = tk.Entry(self.main_frame, width=50,font=("Trebuchet MS",20,"bold"),fg="black")             #Create the entry forms for the user to set the answer
        self.answer_setup.grid(row=1, column=1, padx=20, pady=20)
        
        self.add_flashcard_button = tk.Button(self.main_frame, text="Add Flashcard", width= 14, font=("Trebuchet MS",20,"bold"),fg="black", command=self.add_flashcard)    #create adding button that use the add_flashcard function
        self.add_flashcard_button.grid(row=2, column=1, pady=20)

        # Question Mode Button
        self.quiz_mode_button = tk.Button(self.main_frame, text="Start Answering",width= 14,font=("Trebuchet MS",20,"bold"),fg="black", command=self.quiz_mode)     #create the quiz mode button the enable user to answer the question set up by them self
        self.quiz_mode_button.grid(row=3, column=1, pady=20)

        self.reset_flashcard_button=tk.Button(self.main_frame,text="Reset Flashcard",width= 14,font=("Trebuchet MS",20,"bold"),fg="black",command=self.reset_flashcard)
        self.reset_flashcard_button.grid(row=4, column=1, pady=20)

        # Quiz Section (Initially Hidden)
        #All in mode frame
        self.quiz_frame = tk.Frame(self.window) #create new frame call "quiz frame"
        self.quiz_frame.pack(pady=20)       
        self.quiz_frame.pack_forget()           # Hide the quiz frame at normal condition 

        self.question_display = tk.Label(self.quiz_frame, text="",font=("Trebuchet MS",20,"bold"),fg="black")  #display the question part 
        self.question_display.pack(pady=20)

        self.user_answer_entry = tk.Entry(self.quiz_frame, width=50,font=("Trebuchet MS",20,"bold"),fg="black")                    #create entry form for user to key in the answer 
        self.user_answer_entry.pack(pady=20)

        self.check_answer_button = tk.Button(self.quiz_frame, text="Submit Answer",font=("Trebuchet MS",20,"bold"),fg="black", command=self.check_answer)  #create a button "submit" for user to chekc the answer
        self.check_answer_button.pack(pady=20)

        self.next_question_button = tk.Button(self.quiz_frame, text="Next Question",font=("Trebuchet MS",20,"bold"),fg="black", command=self.next_question)   #create a button "next question" for user to display the next question
        self.next_question_button.pack_forget()

        window.mainloop()

    # function to reset flashcard
    def reset_flashcard(self):
        confirm_reset = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset the current flashcard quizzer maker?") #confirmation message before reseting
        
        if confirm_reset:
            messagebox.showinfo("Flashcard reset", "Flashcards have been reseted!")
            self.remake()

    def add_refresh(self):
        self.question_index = -1                
        self.score = 0
        self.grades = ''
        self.marks= 0 
        self.praise=""

    def remake_refresh(self):
        self.flashcards = {}                    # The dictionary store the keys and valie
        self.questionslist = []                 # The list store the key from the dictionary

        self.question_index = -1                 # To track the index of the current question
        self.score = 0
        self.question_number = 0 
        self.grades = ''
        self.marks= 0 
        self.praise = ""
 

    def add_flashcard(self):            
        question = self.question_setup.get().strip()                            #store the question that key in by the user into the 'question'
        answer = self.answer_setup.get().strip()                                #store the answer that key in by the user into the 'answer'

        if question and answer:
            self.flashcards[question] = answer                                  # add question as a key and the answer as a value into dictionary
            self.questionslist = list(self.flashcards.keys())                   # update all of the key of dictionary into the list
            random.shuffle(self.questionslist)
            self.question_setup.delete(0, tk.END)                               # delete the question entry for user to add a new one
            self.answer_setup.delete(0, tk.END)                                 # delete the answer entry for user to add a new one
            messagebox.showinfo("Success", "Flashcard added successfully!")     #show the info by using message box
            self.question_number+=1
            
            
        else:
            messagebox.showwarning("Input Error", "Please enter both question and answer.")        #show error if the question or answer is not exist

    def quiz_mode(self):         #if the flashcard is exist
        if self.flashcards:
            self.quiz_frame.pack(pady=20)   # Show the quiz frame
            self.main_frame.pack_forget()   # Hide the main frame
            self.next_question()       # Show the first question
        else:
            messagebox.showwarning("No Flashcards", "Please add some flashcards before entering the quiz section.")    #show the message if no existing flashcard

    def next_question(self): # NEXT QUESTION FUNCTION
        if self.flashcards:         # If flashcard exist
            self.question_index += 1         # the index will +1 evrytime user click the button so that the question display will be change base on the index  number

            if self.question_index>= len(self.questionslist):  # Loop back to the beginning
                self.result()

            self.current_question = self.questionslist[self.question_index] #display question base on the index number
            self.question_display.config(text=self.current_question)                
            self.user_answer_entry.delete(0, tk.END)                        #delete the answer before to let user enter the the new one
        else:
            messagebox.showwarning("No Flashcards", "No flashcards available to display!")  #if flashcard not exist, prompt the msg
        self.next_question_button.pack_forget()
        self.check_answer_button.pack(pady=10)

    def check_answer(self):         #Check function 
        self.check_answer_button.pack_forget() #hide the check answer buttons
        if self.current_question:   #if current question exist
            user_answer = self.user_answer_entry.get().strip()      #store the answer that key in by the user
            correct_answer = self.flashcards[self.current_question] #store the answer that set up by the user in the dictionary as 'correct answer'
            self.next_question_button.pack(pady=10)
            if user_answer.lower() == correct_answer.lower():       #if the answer key in by the user is equal to correct answer
                messagebox.showinfo("Correct", "Your answer is correct!")   #print correct
                self.score +=1
            else:
                messagebox.showerror("Incorrect", f"Wrong answer! The correct answer is: {correct_answer}") #if not, print incorrect
        else:
            messagebox.showwarning("No Question", "No question is currently being displayed.")#if no question, display no question
        

    def result(self):
        self.quiz_frame.pack_forget()
        self.result_frame = tk.Frame(self.window)
        self.result_frame.pack(pady=100)
        self.score_label = tk.Label(self.result_frame,text='Congratulation!! You answered {} {}, and you got the result of {}/{}'.format(self.question_number,"questions" if self.question_number>1 else "question",self.score,self.question_number),font=("Trebuchet MS",20,"bold"),fg="black")
        self.score_label.pack(pady=50)
        self.marks=(self.score/self.question_number)*100
        self.grade()
        self.marks_label = tk.Label(self.result_frame,text='Your grade is {}, and marks is {:.0f}%. {}'.format(self.grades, self.marks,self.praise),font=("Trebuchet MS",20,"bold"),fg="black")
        self.marks_label.pack(pady=50)

        self.add_button=tk.Button(self.result_frame,text="Add Flashcard",font=("Trebuchet MS",20,"bold"),fg="black",command=self.add)
        self.add_button.pack(pady=20)
        
        self.remake_button=tk.Button(self.result_frame,text="Remake Flashcard",font=("Trebuchet MS",20,"bold"),fg="black",command=self.reset_flashcard)
        self.remake_button.pack(pady=20)
        

    def grade(self):
        if self.marks >= 90 and self.marks <= 100:
            self.grades = 'A'
            self.praise = "Excellent!"
        elif self.marks >= 70 and self.marks< 90:
            self.grades = 'B'
            self.praise = "Well done!"
        elif self.marks >= 50 and self.marks < 70:
            self.grades = 'C'
            self.praise="Keep it up!"
        elif self.marks >= 40 and self.marks < 50:
            self.grades = 'D'
            self.praise="Do better next time!"
        else :
            self.grades = 'F'
            self.praise ="Study harder!"

    def add(self):
        self.add_refresh()
        self.result_frame.pack_forget()
        self.main_frame.pack(pady=20)

    def remake_confirmation(self):
        confirm_reset = messagebox.askyesno("Confirm Reset", "Are you sure you want to remake the flashcard quizzer?")
        
        if confirm_reset:
            messagebox.showinfo("Flashcard reset", "Flashcard reseted!")
            self.remake()

    def remake(self):
        self.remake_refresh()
        self.result_frame.pack_forget()
        self.main_frame.pack(pady=20)