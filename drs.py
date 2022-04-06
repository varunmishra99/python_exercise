import tkinter
import cv2   #pip install opencv-python
import PIL.Image, PIL.ImageTk #pip install pillow
from functools import partial
import threading
import imutils
import time

#width and height of the screen
SET_WIDTH = 600
SET_HEIGHT = 400
 
stream =cv2.VideoCapture("clip.mp4")
flag =True
def play(speed):
    global flag
    print(f"You click play. speed is {speed}")
    
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(220, 25, fill ="white" , font="Times 20 bold", text = "DECISION PENDING")
    flag  = not flag
    


def pending(decision):
    # Display decision pending image 
    frame = cv2.cvtColor(cv2.imread("decision.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width =SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # wait for 1 second
    time.sleep(1)
    # display varun image
    frame = cv2.cvtColor(cv2.imread("spo.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width =SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    # wait for 1.5 sec
    time.sleep(0.5)
    # display out/notout image 
    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width =SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

window = tkinter.Tk()
window.title("Varun's Third Umpire Drs")
cv_image = cv2.cvtColor(cv2.imread("intro.jpeg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH,height=SET_HEIGHT)
pic = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image))
image_on_canvas = canvas.create_image(0,0, ancho=tkinter.NW, image=pic)
canvas.pack()

#Buttons
btn = tkinter.Button(window, text="<<<< PRevious frame (fast)",width=50, command=partial(play,-20))
btn.pack()

btn = tkinter.Button(window, text="<< PRevious frame (slow)",width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text=" Next frame (slow)>>",width=50, command=partial(play,1))
btn.pack()

btn = tkinter.Button(window, text=" Next frame (fast)>>>>",width=50, command=partial(play,20))
btn.pack()

btn = tkinter.Button(window, text=" Give OUT",width=50, command=out)
btn.pack()

btn = tkinter.Button(window, text=" Give Not Out",width=50, command=not_out)
btn.pack()

window.mainloop()