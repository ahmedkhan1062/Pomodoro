import time
import tkinter
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import font

#colour codes for UI colour pallete
light = "#FFBB5C"
medium = "#FF9B50"
dark = "#E25E3E"
very_dark = "#C63D2F"

#positions of for where checkmarks will be placed on UI
tickposition = [(80,320),(110,320),(140,320),(170,320)]

#List of checkmark objecs
ticks = []

#Counter to tell how many repetitions have passed
count = 0

#Program state boolean
running = False

#Create UI window
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=75, pady=50, bg=light)


#--------------BUTTON PRESS METHODS--------------#


#Method to reset UI and timer when Reset button is clicked
def reset_press():
    global running
    running= False
    canvas.itemconfig(timer, text="00:00")
    canvas.itemconfig(heading, text = "Timer", fill = dark)
    clearTicks()

#Functionality for when start button is clicked
def start_press():
    global count
    count = 0
    global running
    running = True
    while running == True:
        count+=1
        if running == True:
            canvas.itemconfig(heading, text = "Work", fill = very_dark)
            window.attributes("-topmost",True)
            window.attributes("-topmost",False)
        else:
            continue
        countdown(1500) #1500
        
        if running == True:
            canvas.itemconfig(heading, text = "Break", fill = dark)
            window.attributes("-topmost",True)
            window.attributes("-topmost",False)
            placeTicks(count)
            window.update()
        else:
            continue
        if count == 4:
            countdown(1200)
            count = 0
            reset_press()
            window.attributes("-topmost",True)
            window.attributes("-topmost",False)
        else: 
            countdown(300)


#--------------COUNTDOWN FUNCTIONALITY-------------#


#Method to create count down functionality
def countdown(seconds):
    global running
    global count
    while seconds and running:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        
        canvas.itemconfig(timer, text=timeformat)
        window.update()
        time.sleep(1)
        seconds -= 1


#--------------UI HELPER METHODS--------------#


#Method to add checkmarks to UI
def placeTicks(tally):
    clearTicks()
    if tally == 0:
        return
    else:
        for i in range(tally):
            pos = tickposition[i]
            new_tick = canvas.create_image(pos[0],pos[1],image = tickmark)
            ticks.append(new_tick)

#Method to clear checkmarks from UI
def clearTicks():
    for tick in ticks:
        canvas.delete(tick)

#--------------UI DESIGN--------------#

#Create background tomato image
img = PhotoImage(file=r"\Users\Alienware 15\Documents\Udemy Projects\Project 12 - Pomodoro\tomato.png")
canvas = Canvas(width = 250, height=340,highlightthickness=0, bg = light)
canvas.create_image(125,172,image = img)

#Create checkmark image for when the work completes
tickmark =PhotoImage(file=r"\Users\Alienware 15\Documents\Udemy Projects\Project 12 - Pomodoro\checkmark_small.png")

#Create start button
btn_start = tkinter.Button(command = start_press, text="Start", fg= "white", bg = medium, width= 4,height = 0, font=font.Font(family="Inter UI", size=12, weight="bold"), highlightthickness=4, relief= "flat")
btn_start.place(x=0, y=320)

#Create reset button
btn_reset = tkinter.Button(command=reset_press, text="Reset", fg= "white", bg = medium, width= 4,height = 0, font=font.Font(family="Inter UI", size=12, weight="bold"), highlightthickness=4, relief= "flat")
btn_reset.place(x=195, y=320)

#Create big topmost heading
heading = canvas.create_text(128,18, text ="Timer", fill= dark, font=font.Font(family="Inter UI", size=35))

#Create timer display
timer = canvas.create_text(128,195, text ="00:00", fill= "white", font=font.Font(family="Inter UI", size=25))

canvas.pack()

window.mainloop()