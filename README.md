## Run the program

**Visual Studio code**
1. Download the following files in the same folder:
2. MainMenu.py
3. FlashcardQuizzer.py
4. CGPACalculator.py
5. PomodoroTimer.py
6. Users also need to download the latest version of python extension in the VS Code.
7. Open the folder and run the python file.

**Anaconda Prompt**

1. Download the following files in the same folder:
2. MainMenu.py
3. FlashcardQuizzer.py
4. CGPACalculator.py
5. PomodoroTimer.py
6. Start Anaconda Prompt
7. Enter the right path (forward): cd “folder name”
8. Enter the right path (backward): cd..
9. Enter the command “python MainMenu.py” to execute a script (.py extension)

**Jupyter Notebook**

1. Download the following files in the same folder:
2. MainMenu.py
3. FlashcardQuizzer.py
4. CGPACalculator.py
5. PomodoroTimer.py
6. Click on the search box located at the Windows toolbar.
7. Type "jupyter notebook", and then select "Jupyter Notebook" to launch the application.
8. Click "New", and then select "Python 3 (ipykernel)" to create a new notebook.
9. Enter the command "%run MainMenu.py" to execute the script.



## CGPA & GPA Calculator application
- This is a GPA Calculator application built using Python and Tkinter. It allows users to enter their student information like total credit hours and grades, and then calculates their GPA.
1. Features:
   ```
    - Enter CGPA, total credit hour
    - Enter grades for multiple subjects
    - Validate input data
    - Save and load student information and grades from files
    - Calculate and display GPA, CGPA, current total credit hours and total credit hours
   ```
2. Usage:
   ```
    - Run the `CGPACalculator.py` file.
    - Enter your current CGPA and total credit hours earned.
    - Enter number of subjects, and click "Create Subject Inputs" to enter your grades and credit hours for each subject.
    - Click "Calculate GPA" to see your GPA and CGPA.
    - You can return to the main window or exit the program.
   ```
3. Files:
   ```
    - `CGPACalculator.py`: The main application file.
    ```

## Pomodoro Timer application
- This is a Pomodoro Timer application built using Python and Tkinter. It allows users to select their desired times based on focus timer and rest time to run the Pomodoro Timer
1. Features:
   ```
    - Select times (Focus timers and Rest timers).
    - Enter Pomodoro Timer name.
    - Validate input data and selections.
    - Save and load Pomodoro Timer name and times from file.
    - Display Pomodoro Timers and run Pomodoro timer.
    - Delete Pomodoro Timer desired
   ```
2. Usage:
   ```
    - Run the `PomodoroTimer.py` file.
    - Enter Pomodoro Timer name.
    - Select times of focus timers and rest timers repeatably
    - Click "Save Pomodoro Timer" to save the Pomodoro Timer, and display Pomodoro Timer content list
    - Click "Run" to run the Pomodoro Timer
    - You can return to the main window or exit the program.
   ```
3. Files:
   ```
    - `PomodoroTimer.py`: The main application file.
    - `sessions.csv`: File to save pomodoro timer name and list of times
    ```

## Flashcaard Quizzer application
- This is a Flashcaard Quizzer application built using Python and Tkinter. It allows users create flashcard by entering questions and answers, then answer those questions.
1. Features:
   ```
    - Enter questions and answers to create flashcard.
    - Save the questions and answers.
    - Answer the questions.
    - Validate answers.
    - Display total score.
   ```
2. Usage:
   ```
    - Run the `FlashcardQuizzer.py` file.
    - Enter question and answer.
    - Click "Add FlashCard" to add the question and answer into the flashcard.
    - Click "Start Answering" to answer the questions user entered that is displayed.
    - Click "Submit Answer" to check if the answer is correct or wrong.
    - Click "Next Question" to answer the next question
    - Flashcard quiz ends with displaying total score and mark.
    - You can return to the main window, exit the program, add flashcards or remake flashcards.
   ```
3. Files:
   ```
    - `FlashcardQuizzer.py`: The main application file.
    ```
