from tkinter import *
import tkinter.messagebox as tkMessageBox
from PIL import ImageTk, Image
from pygame import mixer
import time
import pyttsx3

# Create object
root = Tk()
# Adjust size
root.geometry("1200x780")
root.config(bg="#000000")
root.title('Calculator')
root.resizable(0, 0)

###################Starting with functions ####################
###############################################################
# 'btn_click' function : 
# input any no or expression
def btn_click_0(item):
    # Load the sound file
    sound_file = "sound\\0.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_1(item):
    # Load the sound file
    sound_file = "sound\\1.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_click_2(item):
    # Load the sound file
    sound_file = "sound\\2.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_3(item):
    # Load the sound file
    sound_file = "sound\\3.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_4(item):
    # Load the sound file
    sound_file = "sound\\4.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_click_5(item):
    # Load the sound file
    sound_file = "sound\\5.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_click_6(item):
    # Load the sound file
    sound_file = "sound\\6.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_7(item):
    # Load the sound file
    sound_file = "sound\\7.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_click_8(item):
    # Load the sound file
    sound_file = "sound\\8.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_9(item):
    # Load the sound file
    sound_file = "sound\\9.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_dot(item):
    # Load the sound file
    sound_file = "sound\\dot.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_add(item):
    # Load the sound file
    sound_file = "sound\\addition.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_substract(item):
    # Load the sound file
    sound_file = "sound\\substraction.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_multiply(item):
    # Load the sound file
    sound_file = "sound\\multiplication.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
def btn_click_divide(item):
    # Load the sound file
    sound_file = "sound\\division.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression
    expression = expression + str(item)
    input_text.set(expression)
###############################################################
# 'bt_clear' function : clear the input field

def btn_clear():
    # Load the sound file
    sound_file = "sound\\clear.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global expression 
    expression = "" 
    input_text.set("")
 
###############################################################
# 'bt_equal':calculates the expression present in input field
def btn_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
    engine.say(f"The result is {result}")
    engine.runAndWait()
    
def enable_operations():
    # Enable all operations on the Tkinter window
    root.attributes('-disabled', False)
    return
    
################################################################
# 'StringVar()' :It is used to get the instance of input field
expression = ""
input_text = StringVar()
 
    
###############################################################
########### creating the frames of main screnn#################
TopFrame = Frame(root, width=1200, height=83,bg="#CDC0B0")
TopFrame.pack(side=TOP)
Bottom = Frame(root, width=1200, height=697)
Bottom.pack(side=BOTTOM)
Middle = Frame(Bottom, width=1200, height=615,bg="#FF6A6A")
Middle.pack(side=TOP)
Bottom1 = Frame(Bottom, width=1200, height=82,bg="#FF6A6A")
Bottom1.pack(side=BOTTOM)


MidLeft = Frame(Middle, width=300, height=625,bg="#FF6A6A")
MidLeft.pack(side=LEFT)
MidRight = Frame(Middle, width=900, height=625)
MidRight.pack(side=RIGHT)

Calculator = Frame(MidRight, width=600, height=630,bg="#FF6A6A")
Calculator.pack(side=LEFT)
Rest = Frame(MidRight, width=300, height=656,bg="#FF6A6A")
Rest.pack(side=RIGHT)

####################################################################
def shift():
    x1,y1,x2,y2 = canvas.bbox("liicter")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("liicter",x1,y1)
    else:
        canvas.move("liicter", -2, 0)
    canvas.after(800//fps,shift)
####################################################################
canvas=Canvas(TopFrame,bg="#FF6A6A",highlightbackground="#FF6A6A", highlightthickness=1)
canvas.pack(fill=BOTH, expand = True)
text_var="\t\t\t\t\t\t\t\t  A GUI based Simple Calculator using Python. Developed By Mr. Ayan Singha"
text=canvas.create_text(0,-2000,text=text_var,font=('Comic Sans MS',40,'bold'),fill='white',tags=("liicter"))
x1,y1,x2,y2 = canvas.bbox("liicter")
width = 1200
height = 83
canvas['width']=width
canvas['height']=height
fps=60    #Change the fps to make the animation faster/slower
shift()
####################################################################
####################################################################



####################################################################

Screen = Frame(Calculator, width=614, height=151, bg="#C1FFC1",  highlightbackground="#1A1A1A", highlightthickness=20)
Screen.pack(side=TOP)


operators = Frame(Calculator, width=612, height=50, bg="#1A1A1A",)
operators.pack()

Buttons = Frame(Calculator, width=615, height=430,highlightbackground="#1A1A1A", highlightthickness=15)
Buttons.pack()

input_field = Entry(Screen, font = ('arial', 30, 'bold'), textvariable = input_text,  width = 26, bg = "#C1FFC1", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 46)
#####################################################################
OpRight = Frame(operators, width=315, height=50,bg="#1A1A1A")
OpRight.pack(side=RIGHT)

OpLeft = Frame(operators, width=300, height=50,bg="#1A1A1A")
OpLeft.pack(side=LEFT)

#####################################################################
OpRightL = Frame(OpRight , width=150, height=50,bg="#1A1A1A")
OpRightL.pack(side=RIGHT,fill = 'both', expand = True,
           padx = 25, pady = 0)

OpRightR = Frame(OpRight , width=150, height=50,bg="#1A1A1A")
OpRightR.pack(side=LEFT,fill = 'both', expand = True,
           padx = 25, pady = 0)



#####################################################################

OpLeftL = Frame(OpLeft, width=150, height=50,bg="#1A1A1A")
OpLeftL.pack(side=LEFT,fill = 'both', expand = True,
           padx = 22, pady =0)

OpLeftR = Frame(OpLeft, width=150, height=50,bg="#1A1A1A")
OpLeftR.pack(side=RIGHT,fill = 'both', expand = True,
           padx = 23, pady =0)


#####################################################################
Top = Frame(Buttons, width=600, height=300)
Top.pack(side=TOP)

Bottom = Frame(Buttons, width=600, height=350,bg="#1A1A1A",  padx = 0, pady =1)
Bottom.pack(side=BOTTOM)

#####################################################################
LeftTop = Frame(Top, width=300, height=300,bg="#1A1A1A")
LeftTop.pack(side=LEFT)

RightTop = Frame(Top, width=300, height=300,bg="#1A1A1A")
RightTop.pack(side=RIGHT)

#####################################################################

LeftBottom = Frame(Bottom, width=300, height=300,bg="#1A1A1A")
LeftBottom.pack(side=LEFT)

RightBottom = Frame(Bottom, width=300, height=300,bg="#1A1A1A")
RightBottom.pack(side=RIGHT)

#####################################################################






#####################################################################
LeftTopL = Frame(LeftTop, width=150, height=300,bg="#1A1A1A")
LeftTopL.pack(side=LEFT)

LeftTopR = Frame(LeftTop, width=150, height=300,bg="#1A1A1A")
LeftTopR.pack(side=RIGHT)

#####################################################################

RightTopT = Frame(RightTop, width=300, height=150,bg="#1A1A1A")
RightTopT.pack(side=TOP)

RightTopB = Frame(RightTop, width=300, height=150,bg="#1A1A1A")
RightTopB.pack(side=BOTTOM, fill = 'both', expand = True,
           padx = 20, pady = 20)


#####################################################################

LeftBottomT = Frame(LeftBottom, width=300, height=150,bg="#1A1A1A")
LeftBottomT.pack(side=TOP)

LeftBottomB = Frame(LeftBottom, width=300, height=150,bg="#1A1A1A")
LeftBottomB.pack(side=BOTTOM,  fill = 'both', expand = True,
           padx = 12, pady = 20)

#####################################################################

RightBottomL = Frame(RightBottom, width=150, height=300,bg="#1A1A1A")
RightBottomL.pack(side=LEFT)

RightBottomR = Frame(RightBottom, width=150, height=300,bg="#1A1A1A")
RightBottomR.pack(side=RIGHT, fill = 'both', expand = True,
           padx = 20, pady = 20)

#####################################################################



#####################################################################
LeftTopLT = Frame(LeftTopL, width=100, height=50,bg="#1A1A1A")
LeftTopLT.pack(side=TOP, fill = 'both', expand = True,
           padx = 20, pady = 20)


LeftTopLB = Frame(LeftTopL, width=100, height=50,bg="#1A1A1A")
LeftTopLB.pack(side=BOTTOM, fill = 'both', expand = True,
           padx = 20, pady = 20)

#####################################################################

LeftTopRT = Frame(LeftTopR, width=100, height=50,bg="#1A1A1A")
LeftTopRT.pack(side=TOP, fill = 'both', expand = True,
           padx = 20, pady = 20)

LeftTopRB = Frame(LeftTopR, width=100, height=50,bg="#1A1A1A")
LeftTopRB.pack(side=TOP, fill = 'both', expand = True,
           padx = 20, pady = 20)

#####################################################################

RightTopTR = Frame(RightTopT, width=100, height=50,bg="#1A1A1A")
RightTopTR.pack(side=RIGHT, fill = 'both', expand = True,
           padx = 20, pady = 20)

RightTopTL = Frame(RightTopT, width=100, height=50,bg="#1A1A1A")
RightTopTL.pack(side=LEFT, fill = 'both', expand = True,
           padx = 20, pady = 20)



#####################################################################

LeftBottomTR = Frame(LeftBottomT, width=100, height=50,bg="#1A1A1A")
LeftBottomTR.pack(side=RIGHT, fill = 'both', expand = True,
           padx = 20, pady = 20)

LeftBottomTL = Frame(LeftBottomT, width=100, height=50,bg="#1A1A1A")
LeftBottomTL.pack(side=LEFT, fill = 'both', expand = True,
           padx = 20, pady = 20)



#####################################################################

RightBottomLT = Frame(RightBottomL, width=100, height=50, bg="#1A1A1A")
RightBottomLT.pack(side=TOP, fill = 'both', expand = True,
           padx = 20, pady = 20)

RightBottomLB = Frame(RightBottomL, width=100, height=50,bg="#1A1A1A")
RightBottomLB.pack(side=BOTTOM, fill = 'both', expand = True,
           padx = 12, pady = 20)


#####################################################################
#########Store Image fils into variable##############################

no0 = ImageTk.PhotoImage(Image.open("Button\\0.png").resize((250,50)))
no1 = ImageTk.PhotoImage(Image.open("Button\\1.png").resize((100,50)))
no2 = ImageTk.PhotoImage(Image.open("Button\\2.png").resize((100,50)))
no3 = ImageTk.PhotoImage(Image.open("Button\\3.png").resize((100,50)))
no4 = ImageTk.PhotoImage(Image.open("Button\\4.png").resize((100,50)))
no5 = ImageTk.PhotoImage(Image.open("Button\\5.png").resize((100,50)))
no6 = ImageTk.PhotoImage(Image.open("Button\\6.png").resize((100,50)))
no7 = ImageTk.PhotoImage(Image.open("Button\\7.png").resize((100,50)))
no8 = ImageTk.PhotoImage(Image.open("Button\\8.png").resize((100,50)))
no9 = ImageTk.PhotoImage(Image.open("Button\\9.png").resize((100,50)))
no9 = ImageTk.PhotoImage(Image.open("Button\\9.png").resize((100,50)))
dot = ImageTk.PhotoImage(Image.open("Button\\dot.png").resize((100,50)))
add = ImageTk.PhotoImage(Image.open("Button\\add.png").resize((100,50)))
substract = ImageTk.PhotoImage(Image.open("Button\\substract.png").resize((100,50)))
multiply = ImageTk.PhotoImage(Image.open("Button\\multiply.png").resize((100,50)))
divide = ImageTk.PhotoImage(Image.open("Button\\divide.png").resize((100,50)))
equal = ImageTk.PhotoImage(Image.open("Button\\equal.png").resize((100,150)))
clear = ImageTk.PhotoImage(Image.open("Button\\clear.png").resize((240,50)))

#################################################################################
###################Creating buttons##############################################
btn_0 = Button(LeftBottomB, image = no0,bg="#1A1A1A", command = lambda: btn_click_0(0))
btn_0.pack()

btn_1 = Button(RightBottomLT , image = no1, bg="#1A1A1A", command = lambda: btn_click_1(1))
btn_1.pack()

btn_2 = Button(LeftBottomTR, image = no2,bg="#1A1A1A", command = lambda: btn_click_2(2))
btn_2.pack()

btn_3 = Button(LeftBottomTL, image = no3,bg="#1A1A1A", command = lambda: btn_click_3(3))
btn_3.pack()

btn_4 = Button(LeftTopRB, image = no4,bg="#1A1A1A", command = lambda: btn_click_4(4))
btn_4.pack()

btn_5 = Button(LeftTopLB , image = no5,bg="#1A1A1A", command = lambda: btn_click_5(5))
btn_5.pack()

btn_6 = Button(RightTopTR, image = no6,bg="#1A1A1A", command = lambda: btn_click_6(6))
btn_6.pack()

btn_7 = Button(RightTopTL  , image = no7,bg="#1A1A1A", command = lambda: btn_click_7(7))
btn_7.pack()


btn_8 = Button(LeftTopRT  , image = no8,bg="#1A1A1A", command = lambda: btn_click_8(8))
btn_8.pack()

btn_9 = Button(LeftTopLT, image = no9,bg="#1A1A1A", command = lambda: btn_click_9(9))
btn_9.pack()

btn_dot = Button(RightBottomLB, image = dot,bg="#1A1A1A",  command = lambda: btn_click_dot("."))
btn_dot.pack()

btn_add = Button(OpRightR, image = add,bg="#1A1A1A", command = lambda: btn_click_add("+"))
btn_add.pack()

btn_substract = Button(OpLeftR, image = substract,bg="#1A1A1A", command = lambda: btn_click_substract("-"))
btn_substract.pack()

btn_multiply = Button(OpRightL, image = multiply,bg="#1A1A1A", command = lambda: btn_click_multiply("*"))
btn_multiply.pack()

btn_divide = Button(OpLeftL, image = divide,bg="#1A1A1A",command = lambda: btn_click_divide("/"))
btn_divide.pack()

btn_equalto = Button(RightBottomR, image = equal,bg="#1A1A1A", command = lambda: btn_equal())
btn_equalto.pack()

btn_clearScreen = Button(RightTopB, image = clear,bg="#1A1A1A",command = lambda: btn_clear())
btn_clearScreen.pack()

# Initialize text-to-speech engine
engine = pyttsx3.init()

#################################################################################
###################Calling the main function########################################

root.mainloop()



