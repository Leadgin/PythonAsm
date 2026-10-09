from tkinter import *
from tkinter import messagebox
import csv
import os

class PomodoroTimer:
    def __init__(self):
        self.window = Tk()
        self.window.title("Pomodoro Timer")
        self.window.geometry("1200x400")

        # boolean to swicth timer selection's status
        self.is_timer = True

        # dictionary for each session + times
        self.sessions = self.load_sessions_from_csv() # to save sessions (dictionary) key and values in csv file

        # session's time
        self.sessionTimes = []

        # temporary session name
        self.current_sessionName = None

        # session names (default) 
        self.used_sessions = set()
        self.sessionCounter = 1

        # Initialize current index for tracking the timer
        self.currentIndex = 0

        # Flag to check if time is selected
        self.timeSelected = False  # Start with False

        self.session_frames = {}  # Store references to session frames

        #call functions to display
        self.displaySessions()
        self.displaySelectTimer()
        self.update_frames()
        
        self.window.mainloop()

    def displaySessions(self):
        self.session_frame = Frame(self.window, bg="#F1FDFF")
        self.session_frame.pack(side=LEFT, fill=Y) 

        # Add a frame above the canvas
        self.top_frame = Frame(self.session_frame, bg="#FAEEB1", height=50)
        self.top_frame.pack(side=TOP, fill=X)

        self.SessionLabel = Label(self.top_frame, text = "Pomodoro Timers", font=("Trebuchet MS", 23, "bold"), bg="#FAEEB1", fg="#57441E")
        self.SessionLabel.pack(anchor=W, padx=3)

        # Add a frame below the canvas
        self.canvas_frame = Frame(self.session_frame, bg="#F1FDFF")  # Create a new frame to contain the canvas and scrollbar
        self.canvas_frame.pack(side=LEFT, fill=Y)

        # Create a canvas
        self.canvas = Canvas(self.canvas_frame, bg="#F1FDFF")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a scrollbar
        scrollbar = Scrollbar(self.session_frame, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Create an internal frame inside the canvas
        self.canvaFrame = Frame(self.canvas, bg="#F1FDFF")
        self.canvas.create_window((0, 0), window=self.canvaFrame, anchor="nw")

        # Bind the canvas to update the scroll region when resized
        self.canvaFrame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    def displaySelectTimer(self):               
        self.selectTimer = Frame(self.window)
        self.selectTimer.pack(side=TOP, fill=X)

        self.inputEntryLabel = Label(self.selectTimer, text="Enter Pomodoro Timer Session Name (not more than 18 characters):", font=("Trebuchet MS", 10))
        self.inputEntryLabel.grid(row=0, column=1, pady=20, sticky=W, columnspan= 3)

        # input for session name
        self.inputEntry = Entry(self.selectTimer, width=60)
        self.inputEntry.insert(0, f"Session#{self.sessionCounter}")  # default session name
        self.inputEntry.grid(row=1, column=1, columnspan= 2)

        self.spaceaaaa = Label(self.selectTimer, text="           ")
        self.spaceaaaa.grid(row=2, column=0, pady=10, padx=20, columnspan= 3)

        # labeling depending on type of time selecting
        self.inputLabel = Label(self.selectTimer, text="Select FOCUS timer 1 in minutes:", font=("Trebuchet MS", 10, "bold"))
        self.inputLabel.grid(row=3, column=1, columnspan= 2)

        # scale to select time
        self.userTime = Scale(self.selectTimer, from_=1, to=60, orient=HORIZONTAL, length=380)
        self.userTime.grid(row=4, column=1, columnspan=2)

        # button to go to the next time selection
        self.nextButton = Button(self.selectTimer, text="Next", width=9, command=self.nextSelection)
        self.nextButton.grid(row=5, column=2, pady=15, sticky=E)

        # button to go to previous time selection
        self.backButton = Button(self.selectTimer, text="Back", width=9, command=self.previousSelection)
        self.backButton.grid(row=5, column=1, pady=15, sticky=W)

        # button to proceed select time
        self.selectButton = Button(self.selectTimer, text="Select Time", width=11, command=self.appendtime)
        self.selectButton.grid(row=5, column=3, pady=10, padx=10, sticky=W)

        self.spaceaaa = Label(self.selectTimer, text="           ")
        self.spaceaaa.grid(row=6, column=0, padx=5)

        # button to save the session into the dictionary
        self.saveButton = Button(self.selectTimer, text="Save Pomodoro Timer", width=20, command=self.appenddict)
        self.saveButton.grid(row=6, column=3, pady =5, sticky=W)


        # button to create a new session 
        self.resetButton = Button(self.selectTimer, text="New Pomodoro Timer", width=20,command=self.newSession)
        self.resetButton.grid(row=6, column=0, sticky=W, padx = 20)

        # button to run timer
        #self.proceedButton = Button(self.selectTimer, text="Run Time", width=8, command=self.runTimer)
        #self.proceedButton.grid(row=4, column=4, pady=10, padx=10)

    def newSession(self):
        # Ask for confirmation before resetting the selection
        confirm_reset = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset the current Pomodoro timer session selection? Remember to save the Pomodoro timer session if there's any chances made.")
        
        if confirm_reset:
            messagebox.showinfo("New Session", "Current Pomodoro timer session selection reset. Create a new Pomodoro timer session!")
            self.resetTimerEntry()  # Reset the selection

    def appendtime(self):
        # add or update the time for the current index
        time_value = self.userTime.get()

        # if the index already exists in the list, update it
        if self.currentIndex < len(self.sessionTimes):
            self.sessionTimes[self.currentIndex] = time_value
            messagebox.showinfo("Time Selection", "Time selected!")
        else:
            # If it's a new entry, add it
            self.sessionTimes.append(time_value)
            messagebox.showinfo("Time Selection", "Time selected!")

        # Mark the time as selected
        self.timeSelected = True  # Time has been selected now

    def nextSelection(self):
        # Check if the user has selected a valid time (greater than 0)
        if not self.timeSelected or self.userTime.get() == 0:
            messagebox.showerror("Error", "Please select a time before proceeding.")
            return  # Exit early if time is not selected or invalid

        # Save the current time if not already saved
        if self.currentIndex >= len(self.sessionTimes):
            self.sessionTimes.append(self.userTime.get())
        else:
            self.sessionTimes[self.currentIndex] = self.userTime.get()  # Update existing time

        # Move to the next index
        self.currentIndex += 1

        # If editing a previously saved timer, load its value into the scale
        if self.currentIndex < len(self.sessionTimes):
            self.userTime.set(self.sessionTimes[self.currentIndex])
            self.timeSelected = True  # Mark time as selected if it exists
        else:
            # Otherwise, reset the scale for a new timer
            self.userTime.set(1)
            self.timeSelected = False  # New index, time not selected yet

        # Update the label depending on the type of timer
        if self.currentIndex % 2 == 0:
            self.inputLabel.config(text=f"Select FOCUS timer {self.currentIndex // 2 + 1} in minutes:", font=("Trebuchet MS", 10, "bold"))
        else:
            self.inputLabel.config(text=f"Select REST timer {(self.currentIndex // 2) + 1} in minutes:" , font=("Trebuchet MS", 10, "bold"))

        print("Session Times:", self.sessionTimes)

    def previousSelection(self):
        # Move to the previous index if possible
        if self.currentIndex > 0:
            self.currentIndex -= 1

        # Load the previous timer value into the scale
        self.userTime.set(self.sessionTimes[self.currentIndex])
        self.timeSelected = True  # Set the flag to True since a value exists for this index

        # Update the label depending on the type of timer
        if self.currentIndex % 2 == 0:
            self.inputLabel.config(text=f"Select FOCUS timer {self.currentIndex // 2 + 1} in minutes:", font=("Trebuchet MS", 10, "bold"))
        else:
            self.inputLabel.config(text=f"Select REST timer {(self.currentIndex // 2) + 1} in minutes:", font=("Trebuchet MS", 10, "bold"))

    def appenddict(self):
        # Ensure at least one time is selected
        if not self.sessionTimes:
            messagebox.showerror("Error", "Please select at least one time before saving the session.")
            return

        # Get the session name
        sessionName = self.inputEntry.get()

        if len(sessionName) > 18:
            messagebox.showerror("Error", "Timer session name can't be more than 18 characters!")
            return  # Exit early if the name exceeds 30 characters

        if self.current_sessionName is None:
            # New session
            if sessionName in self.sessions:
                messagebox.showerror("Error", "Pomodoro timer session name already exists! Please choose a different name.")
            else:
                self.sessions[sessionName] = self.sessionTimes[:]
                self.current_sessionName = sessionName
                messagebox.showinfo("Session", "New Pomodoro timer session created! Press 'New Pomodoro Timer' to create a new timer, or stay and edit this timer!")
        else:
            # Editing an existing session
            if sessionName == self.current_sessionName:
                # Update session times
                self.sessions[sessionName] = self.sessionTimes[:]
            elif sessionName in self.sessions:
                messagebox.showerror("Error", "Pomodoro timer session name already exists! Please choose a different name.")
            else:
                # Rename session and update
                self.sessions[sessionName] = self.sessions.pop(self.current_sessionName)
                self.sessions[sessionName] = self.sessionTimes[:]
                self.current_sessionName = sessionName
                messagebox.showinfo("Session", "Pomodoro timer session updated!")

        # Save sessions to CSV after update
        self.save_sessions_to_csv()

        # Update session counter for default naming
        if sessionName.startswith("Session#"):
            sessionNumber = int(sessionName.split("#")[1])
            if sessionNumber >= self.sessionCounter:
                self.sessionCounter = sessionNumber + 1

        self.update_frames()

    # function to load the key and values (session name and times) from csv file
    def load_sessions_from_csv(self):
        filename = 'sessions.csv'
        sessions = {}

        # Check if the CSV file exists and is not empty
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)

                try:
                    next(reader)  # Skip the header row
                except StopIteration:
                    return sessions  # If file only has a header, return empty sessions

                for row in reader:
                    if row:  # Avoid processing empty rows
                        session_name, session_times_str = row
                        session_times = list(map(int, session_times_str.split(',')))

                        sessions[session_name] = session_times

        return sessions

    # function to save session name and times (keys and values) after saving a session (appenddict function)
    def save_sessions_to_csv(self):
        filename = 'sessions.csv'

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write header
            writer.writerow(['Session Name', 'Session Times'])

            # Write each session name and its associated times
            for session_name, times in self.sessions.items():
                # Convert the list of times to a string format that can be stored (e.g., comma-separated values)
                session_times_str = ','.join(map(str, times))
                writer.writerow([session_name, session_times_str])

    def runTimer(self, sessionName=None):
        if sessionName not in self.sessions:
            messagebox.showerror("Error", f"Session '{sessionName}' does not exist!")
            return

        self.sessionTime = self.sessions[sessionName]

        # New pop-up window for the timer
        self.timer_window = Toplevel(self.window)
        self.timer_window.title("Timer Window")
        self.timer_window.geometry("450x360")
        self.timer_window.config(bg = "#F1FBFD")

        # label to display type of timer running
        self.timerLabel = Label(self.timer_window, text="Running Focus timer 1", font=("Trebuchet MS", 17, "bold"),  pady=13, bg = "#F1FBFD", fg="#243A46")
        self.timerLabel.pack()

        # timer label
        self.pTimer = Label(self.timer_window, text="00:00", font=("Arial", 100), bg="#F1FBFD", pady = 3)
        self.pTimer.pack()

        # pause button
        self.pauseButton = Button(self.timer_window, text="Pause", height = 1, width=11, bg="white", font=("Trebuchet MS", 16), command=self.pauseTimer, )
        self.pauseButton.pack()
        self.pause = False

        self.current_timer_index = 0
        #convert min to sec to run timer
        self.total_seconds = self.sessionTime[self.current_timer_index] * 60
        self.update_timer()

    def update_timer(self):
        if self.total_seconds >= 0:
            if not self.pause:  #if pause button is not pressed/unpressed
                mins, secs = divmod(self.total_seconds, 60)
                self.pTimer.config(text=f"{mins:02d}:{secs:02d}")
                self.timer_window.update()
                self.total_seconds -= 1
            self.timer_window.after(1000, self.update_timer)
        else:
            self.current_timer_index += 1

            # Update the label based on the timer type (focus/rest)
            if self.current_timer_index < len(self.sessionTime):
                self.timess = self.current_timer_index  # Assuming timess tracks segment count
                if self.timess % 2 == 0:
                    self.timerLabel.config(text=f"Running Focus timer {self.timess // 2 + 1}", font=("Trebuchet MS", 17, "bold"), pady = 13)
                else:
                    self.timerLabel.config(
                        self.timerLabel.config(text=f"Running Rest timer {(self.timess // 2) + 1}", font=("Trebuchet MS", 17, "bold"), pady = 13)
                    )

                # Start the next timer segment
                self.total_seconds = self.sessionTime[self.current_timer_index] * 60
                self.update_timer()
            else:
                Label(self.timer_window, text="Pomodoro Timer Session ended!", font=("Trebuchet MS", 15, "italic"), pady = 30, bg="#F1FBFD", fg="#013048").pack()

    # function to reset every thing    
    def resetTimerEntry(self):
        self.timeSelected = False
        self.update_frames()
        self.currentIndex = 0
        self.current_sessionName = None
        self.inputEntry.delete(0, END) #empty data in the entry widget
        self.inputEntry.insert(0, f"Session#{self.sessionCounter}")
        self.sessionTimes.clear()  # Clear the current session times for a new session
        self.timess=[]
        self.is_timer = True
        self.inputLabel.config(text="Select FOCUS timer 1 in minutes:")

    def pauseTimer(self):
        #switch pause status
        self.pause = not self.pause

    # Function to add a new frame for each session in the sessions dictionary
    def add_frame(self, key, value, y_position):
        # Create a frame for each session inside the canvas, no fixed width
        frame = Frame(self.canvas, bg="#D7E6EE", padx=20, pady=10, width=500)
        
        # Store the frame in the session_frames dictionary
        self.session_frames[key] = frame

        # Session name label in the dark blue frame
        session_label = Label(frame, text=f"{key}", bg="#D7E6EE", font=("Trebuchet MS", 17, "bold"), width=20, anchor="w")
        session_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)  # Align left with grid

        # Focus and Rest time labels,
        row = 1  # Start from the second row
        for i in range(0, len(value), 2):  # Assuming value contains pairs [focus, rest]
            focus_label = f"Focus Timer {(i//2) + 1}: {value[i]} min"
            focus_label_widget = Label(frame, text=focus_label, bg="#D7E6EE", font=("Trebuchet MS", 12))
            focus_label_widget.grid(row=row, column=0, sticky="w", padx=5)  #left alignment

            # Display Rest time only if it exists
            if i + 1 < len(value) and value[i + 1]:
                rest_label = f"Rest Timer   {(i//2) + 1}: {value[i + 1]} min"
                rest_label_widget = Label(frame, text=rest_label, bg="#D7E6EE", font=("Trebuchet MS", 12))
                rest_label_widget.grid(row=row + 1, column=0, sticky="w", padx=5)  # Align left with grid
                row += 1  # Increase row count for next label
            row += 1  # Move to the next row for the next set of labels

        # frame for buttons
        button_frame = Frame(frame, bg="#D7E6EE")  
        button_frame.grid(row=row, column=0, sticky="w", pady=10)

        # Run button
        Button(button_frame, text="Run", bg="white", height=2, command=lambda: self.runTimer(key), width=11).pack(side="left", padx=5, pady=5)

        # Delete button
        Button(button_frame, text="Delete", bg="white", height=2, command=lambda: self.delete_session(key), width=11).pack(side="right", padx=5)

        # Add the frame to the canvas at the specified y_position, anchor left side of canvas
        self.canvas.create_window((30, y_position), window=frame, anchor="nw")

        # Update the y_position for the next frame
        frame.update_idletasks()  # Ensure the frame's height is calculated
        y_position += frame.winfo_reqheight() + 20  # Add padding between frames

        return y_position


    def delete_session(self, sessionName):
        # Check if the session exists in the dictionary
        if sessionName not in self.sessions:
            messagebox.showerror("Error", f"Session '{sessionName}' does not exist!")
            return

        # Ask for confirmation to delete the session
        confirm_delete = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the session '{sessionName}'?")

        if confirm_delete:
            # Remove the session from the dictionary
            del self.sessions[sessionName]

            # Destroy the frame associated with this session
            if sessionName in self.session_frames:
                self.session_frames[sessionName].destroy()  # removes the frame from the canvas
                del self.session_frames[sessionName]  # remove from dictionary

            # Save sessions to CSV after deletion (remove session name and times in database)
            self.save_sessions_to_csv()

            # Clear the canvas and redraw frames
            self.clear_canvas()
            self.update_frames()  # Redraw frames with updated session data (undisplay deleted ones)

    def clear_canvas(self):
        # Clear all the items from the canvas
        self.canvas.delete("all")

    # Function to update the session frame with all entries in the sessions dictionary
    def update_frames(self):
        # Start from the top of the canvas
        y_position = 20  # Start from the top

        # Loop through the sessions and add frames
        for session_name, session_times in self.sessions.items():
            y_position = self.add_frame(session_name, session_times, y_position)

        self.canvas.configure(scrollregion=self.canvas.bbox("all")) #reactivate scrollbar