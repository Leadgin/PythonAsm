from tkinter import *
from PomodoroTimer import *
from CGPACalculator import *
from FlashcardQuizzer import *

class MainMenu:
    def __init__(self):
        self.window = Tk()
        self.window.title("Main Menu")
        self.window.config(bg = "#F1FFF9")

        # Use grid for consistent layout
        self.mainMenu_frame = Frame(self.window, bg = "#F1FFF9")
        self.mainMenu_frame.grid(row=0, column=0, padx=80, pady=20)

        self.welcome = Label(self.mainMenu_frame, text="Welcome!", font=("Trebuchet MS", 40, "bold"), bg = "#F1FFF9")
        self.welcome.grid(row=0, column=0, columnspan=2, padx=80, pady=10)

        self.goWhere = Label(self.mainMenu_frame, text="Where would you like to go to?", font=("Trebuchet MS", 30), bg = "#F1FFF9")
        self.goWhere.grid(row=1, column=0, columnspan=2, pady=20)


        # pomodoro frame
        self.pomodoroFrame = Frame(self.mainMenu_frame, bg="#D7EEE7")
        self.pomodoroFrame.grid(row=4, column=0, columnspan=2)

        self.pomodoroLabel = Label(self.pomodoroFrame, text="POMODORO TIMER", bg="#D7EEE7", font=("Trebuchet MS", 20, "bold"))
        self.pomodoroLabel.grid(row=0, column=0, pady=10, padx = 30)

        self.pomodoro = Button(self.pomodoroFrame, text="Go", bg="white", width=9, command=self.gotopomodoro)
        self.pomodoro.grid(row=1, column=0, pady=10)

        # flashcard frame
        self.flashcardFrame = Frame(self.mainMenu_frame, bg="#D7EEE7")
        self.flashcardFrame.grid(row=5, column=0, columnspan=2, pady = 14, padx = 30)

        self.flashcardLabel = Label(self.flashcardFrame, text="FLASHCARD QUIZZER", bg="#D7EEE7", font=("Trebuchet MS", 20, "bold"))
        self.flashcardLabel.grid(row=0, column=0, pady=10, padx = 16)

        self.flashcardButton = Button(self.flashcardFrame, text="Go", bg="white", width=9, command=self.gotoflashcash)
        self.flashcardButton.grid(row=1, column=0, pady=10)

        # cgpa calculator frame
        self.cgpaFrame = Frame(self.mainMenu_frame, bg="#D7EEE7")
        self.cgpaFrame.grid(row=6, column=0, columnspan=2, pady = 10, padx = 30)    

        self.cgpaLabel = Label(self.cgpaFrame, text="CGPA & GPA\nCALCULATOR", bg="#D7EEE7", font=("Trebuchet MS", 20, "bold"))
        self.cgpaLabel.grid(row=0, column=0, padx = 63)

        self.cgpaButton = Button(self.cgpaFrame, text="Go", bg="white", width=9, command=self.gotogpacalculator)
        self.cgpaButton.grid(row=1, column=0, pady=10)

        self.window.mainloop()

    def gotopomodoro(self):
        PomodoroTimer() 

    def gotoflashcash(self):
        FlashcardQuizzer(self.window)

    def gotogpacalculator(self):
        CGPACalculator()
        
MainMenu()
