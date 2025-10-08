from tkinter import *

# ---------------------------- Other Functions ------------------------------- #


def modify_window():
    """Set up the window title and background color."""
    window.title("The Pomodoro App")
    window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)


# ---------------------------- CONSTANTS ------------------------------- #

# Color constants for the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BACKGROUND_COLOR = "#f7f5dd"

# Font settings for the UI elements
FONT = ("Arial", 35, "bold")
BUTTON_FONT = ("Arial", 8, "normal")

# Time settings for work and break intervals (in minutes) for testing
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1

# Global variables to track the state of the timer and repetitions
repeats = 0
timer = None
mark = ""

# Uncomment the lines below for standard Pomodoro timing
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    """Reset the timer to its initial state."""
    global timer, mark, repeats
    window.after_cancel(timer)  # Stop any active timer
    timer_txt.config(text="TIMER", fg=GREEN, bg=BACKGROUND_COLOR, bd=0, font=FONT)  # Reset timer label
    background_img.itemconfig(text_id, text="00:00")  # Reset displayed time to 00:00
    check_mark.config(text="")  # Clear check marks
    repeats = 0  # Reset the repeat counter


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """Start the Pomodoro timer based on the current state."""
    global repeats
    repeats += 1  # Increment the repeat counter
    work_sec = WORK_MIN * 60  # Convert work minutes to seconds
    short_break_sec = SHORT_BREAK_MIN * 60  # Convert short break minutes to seconds
    long_break_sec = LONG_BREAK_MIN * 60  # Convert long break minutes to seconds

    # Determine the type of timer based on the number of repeats
    if repeats % 2 != 0:
        timer_txt.config(text="Work", fg=GREEN)  # Set label for work session
        counter(work_sec)  # Start work timer
    elif repeats % 8 == 0:
        timer_txt.config(text="Long Break", fg=RED)  # Set label for long break
        counter(long_break_sec)  # Start long break timer
    elif repeats % 2 == 0:
        timer_txt.config(text="Break", fg=PINK)  # Set label for short break
        counter(short_break_sec)  # Start short break timer


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter(count):
    """Countdown timer logic."""
    global timer, repeats, mark
    minutes = count // 60  # Calculate minutes
    seconds = count % 60  # Calculate seconds
    background_img.itemconfig(text_id, text=f"{minutes:02d}:{seconds:02d}")  # Update displayed time

    if count > 0:
        timer = window.after(1000, counter, count - 1)  # Call counter every second
    else:
        work_sessions = repeats // 2  # Calculate number of completed work sessions
        for i in range(work_sessions):
            mark += '✔'  # Add a check mark for each completed work session
        check_mark.config(text=mark)  # Update check marks on the screen
        start_timer()  # Start the next timer


# ---------------------------- UI SETUP ------------------------------- #

# Create the main application window
window = Tk()
modify_window()  # Set up window properties

# Timer label setup
timer_txt = Label(text="TIMER", fg=GREEN, bg=BACKGROUND_COLOR, bd=0, font=FONT)
timer_txt.grid(column=1, row=0)  # Position the timer label

# Canvas setup for the timer image
background_img = Canvas(bg=BACKGROUND_COLOR, width=200, height=223, bd=0)
tomato_img = PhotoImage(file="tomato.png")
background_img.create_image(102, 112, image=tomato_img)  # Add tomato image to canvas
text_id = background_img.create_text(100, 130, text="00:00", fill="white", font=FONT)  # Display time on canvas
background_img.grid(column=1, row=1)  # Position canvas in the window

# Start button setup
start_button = Button()
start_button.config(text="Start", font=BUTTON_FONT, bd=0, command=start_timer)  # Set button properties
start_button.grid(column=0, row=2)  # Position start button

# Label to display check marks for completed sessions
check_mark = Label(fg=GREEN, bg=BACKGROUND_COLOR, bd=0, font=("Arial", 20, "normal"))
check_mark.grid(column=1, row=3)  # Position check mark label

# Reset button setup
reset_button = Button()
reset_button.config(text="Reset", font=BUTTON_FONT, bd=0, bg=BACKGROUND_COLOR, command=reset_timer)  # Set button properties
reset_button.grid(column=2, row=2)  # Position reset button

# Run the main event loop
window.mainloop()