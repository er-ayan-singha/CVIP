import tkinter as tk
from tkinter import ttk,Label, Button
from PIL import Image, ImageTk
from tkinter import messagebox
from pygame import mixer
import random
import string
import pyperclip
import time



def first_checkbox_click():   
    if uppercase_var.get():        
        image_path = "Image\\Sweety\\yes.png"  # Replace with the path to your PNG image
        background_color = ("#000000")
        image_with_background = set_background(image_path, background_color)
        image_label1.config(image=image_with_background)
        image_label1.image = image_with_background
        first_label.config(text="Obviously... Yes")
        # Load the sound file
        sound_file = "sound\\Sweety\\yes.wav"
        # Replace with the path to your sound file
        mixer.init()
        sound = mixer.Sound(sound_file)
        # Play the sound
        sound.play()
        # Disable all operations on the Tkinter window
        root.attributes('-disabled', True)
        # Wait for the sound to finish
        root.after(int(sound.get_length() * 1000), enable_operations)
    else:
        image_path = "Image\\Sweety\\no.png"  # Replace with the path to your PNG image
        background_color = ("#000000")
        image_with_background = set_background(image_path, background_color)
        image_label1.config(image=image_with_background)
        image_label1.image = image_with_background
        first_label.config(text="Absolutely.. No")
        # Load the sound file
        sound_file = "sound\\Sweety\\no.wav"
        # Replace with the path to your sound file
        mixer.init()
        sound = mixer.Sound(sound_file)
        # Play the sound
        sound.play()
        # Disable all operations on the Tkinter window
        root.attributes('-disabled', True)
        # Wait for the sound to finish
        root.after(int(sound.get_length() * 1000), enable_operations)
    return

def second_checkbox_click():   
    if digits_var.get():        
        image_path = "Image\\Kanchan\\yes.png"  # Replace with the path to your PNG image
        background_color = ("#000000")
        image_with_background = set_background(image_path, background_color)
        image_label2.config(image=image_with_background)
        image_label2.image = image_with_background
        second_label.config(text="Obviously... Yes")
        # Load the sound file
        sound_file = "sound\\Kanchan\\yes.wav"
        # Replace with the path to your sound file
        mixer.init()
        sound = mixer.Sound(sound_file)
        # Play the sound
        sound.play()
        # Disable all operations on the Tkinter window
        root.attributes('-disabled', True)
        # Wait for the sound to finish
        root.after(int(sound.get_length() * 1000), enable_operations)
    else:
        image_path = "Image\\Kanchan\\no.png"  # Replace with the path to your PNG image
        background_color = ("#000000")
        image_with_background = set_background(image_path, background_color)
        image_label2.config(image=image_with_background)
        image_label2.image = image_with_background
        second_label.config(text="Absolutely.. No")
        # Load the sound file
        sound_file = "sound\\Kanchan\\no.wav"
        # Replace with the path to your sound file
        mixer.init()
        sound = mixer.Sound(sound_file)
        # Play the sound
        sound.play()
        # Disable all operations on the Tkinter window
        root.attributes('-disabled', True)
        # Wait for the sound to finish
        root.after(int(sound.get_length() * 1000), enable_operations)
    return

def third_checkbox_click():   
    if special_chars_var.get():        
        image_path = "Image\\Avik\\yes.png"  # Replace with the path to your PNG image
        background_color = ("#000000")
        image_with_background = set_background(image_path, background_color)
        image_label3.config(image=image_with_background)
        image_label3.image = image_with_background
        third_label.config(text="Obviously... Yes")
        # Load the sound file
        sound_file = "sound\\Avik\\yes.wav"
        # Replace with the path to your sound file
        mixer.init()
        sound = mixer.Sound(sound_file)
        # Play the sound
        sound.play()
        # Disable all operations on the Tkinter window
        root.attributes('-disabled', True)
        # Wait for the sound to finish
        root.after(int(sound.get_length() * 1000), enable_operations)
    else:
        image_path = "Image\\Avik\\no.png"  # Replace with the path to your PNG image
        background_color = ("#000000")
        image_with_background = set_background(image_path, background_color)
        image_label3.config(image=image_with_background)
        image_label3.image = image_with_background
        third_label.config(text="Absolutely.. No")
        # Load the sound file
        sound_file = "sound\\Avik\\no.wav"
        # Replace with the path to your sound file
        mixer.init()
        sound = mixer.Sound(sound_file)
        # Play the sound
        sound.play()
        # Disable all operations on the Tkinter window
        root.attributes('-disabled', True)
        # Wait for the sound to finish
        root.after(int(sound.get_length() * 1000), enable_operations)
    return

def display_first_option():
    global uppercase_var  
    uppercase_var = tk.BooleanVar(value=False)
    button.config(command=pass_action)
    # Load the sound file
    global first_label
    first_label = Label(root, font=("Nature Beauty Personal Use", 21),fg="white", bg="black")
    first_label.pack()
    first_label.place(x=70, y=330)
      # Image label
    global image_label1
    image_path = "Image\\Sweety\\normal.png"  # Replace with the path to your PNG image
    background_color = ("#000000")
    image_label1 = Label(root,bg="black")
    image_label1.pack(pady=10)
    image_label1.place(x=50, y=90)
    image_with_background = set_background(image_path, background_color)
    image_label1.config(image=image_with_background)
    image_label1.image = image_with_background
    #time.sleep(3)
    custom_font = ("Nature Beauty Personal Use", 24)
    checkbutton = tk.Checkbutton(root,variable=uppercase_var,text="Uppercase Character",font=custom_font,command=first_checkbox_click)
    checkbutton.pack()
    checkbutton.place(x=10, y=10)
    checkbutton.config(fg="#FF1493", bg="black" ,activeforeground="#FF1493",activebackground="black")
    sound_file = "sound\\Sweety\\normal.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    root.after(10000, display_second_option)
    
def display_second_option():
    global digits_var
    digits_var = tk.BooleanVar(value=False)
    # Load the sound file
    sound_file = "sound\\Kanchan\\normal.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global image_label2
      # Image label
    image_label2 = Label(root,bg="black")
    image_label2.pack(pady=10)
    image_label2.place(x=800, y=90)
    image_path = "Image\\Kanchan\\normal.png"  # Replace with the path to your PNG image
    background_color = ("#000000")
    image_with_background = set_background(image_path, background_color)
    image_label2.config(image=image_with_background)
    image_label2.image = image_with_background
    custom_font = ("Nature Beauty Personal Use", 24)
    checkbutton = tk.Checkbutton(root, text="Numeric  Digits",variable=digits_var,font=custom_font,command=second_checkbox_click)
    checkbutton.pack(pady=20)
    # Set the text color and background color
    checkbutton.place(x=780, y=10)
    checkbutton.config(fg="#EE7600", bg="black" ,activeforeground="#EE7600",activebackground="black")
    global second_label
    second_label = Label(root,font=("Nature Beauty Personal Use", 21),fg="white", bg="black")
    second_label.pack()
    second_label.place(x=790, y=330)
    root.after(10000, display_third_option)  
    

def display_third_option():
    global special_chars_var
    special_chars_var = tk.BooleanVar(value=False)
    # Load the sound file
    sound_file = "sound\\Avik\\normal.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    global image_label3
    image_label3 = Label(root,bg="black")
    image_label3.pack(pady=10)
    image_label3.place(x=50, y=465)
    image_path = "Image\\Avik\\normal.png"  # Replace with the path to your PNG image
    background_color = ("#000000")
    image_with_background = set_background(image_path, background_color)
    image_label3.config(image=image_with_background)
    image_label3.image = image_with_background
    custom_font = ("Nature Beauty Personal Use", 24)
    checkbutton = tk.Checkbutton(root, text="Special Character",variable=special_chars_var,font=custom_font,command=third_checkbox_click)
    checkbutton.pack(pady=20)
    checkbutton.place(x=30, y=385)
    checkbutton.config(fg="#009ACD", bg="black" ,activeforeground="#009ACD",activebackground="black")
    global third_label
    third_label = Label(root, font=("Nature Beauty Personal Use", 21),fg="white", bg="black")
    third_label.pack()
    third_label.place(x=70, y=705)
    root.after(14000, display_fourth_option)
    
def display_fourth_option():
    global length_var
    # Load the sound file
    sound_file = "sound\\Pinaki\\01.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
    #global third_label
    fourth_label = Label(root, text="Select Length",font=("Nature Beauty Personal Use", 24),fg="#ADFF2F", bg="black")
    fourth_label.pack()
    fourth_label.place(x=790, y=385)
    global image_label4
    image_label4 = Label(root,bg="black")
    image_label4.pack(pady=10)
    image_label4.place(x=765, y=465)
    image_path = "Image\\Pinaki\\normal.png"  # Replace with the path to your PNG image
    background_color = ("#000000")
    image_with_background = set_background(image_path, background_color)
    image_label4.config(image=image_with_background)
    image_label4.image = image_with_background
    length_var = tk.IntVar(value=0)
    # Create a ComboBox with values from 1 to 10
    values = list(range(6, 13))
    custom_font = ("Copperplate Gothic Bold", 18)
    combobox = ttk.Combobox(root,width=10, textvariable=length_var, values=values, state='readonly',font=custom_font)
    combobox.set(values[0])
    combobox.pack(pady=20)
    combobox.place(x=810, y=715)
    custom_font1 = ("Nature Beauty Personal Use", 16)
    submit_button = tk.Button(root, text="G e n e r a t e",font=custom_font1,command=_generate_password)
    submit_button.pack(pady=20)
    submit_button.place(x=475, y=685)
    submit_button.config(fg="white", bg="#FF4500" ,activeforeground="#000000",activebackground="#BBFFFF")
 
def _generate_password():    
    length = length_var.get()
    uppercase = uppercase_var.get()
    digits = digits_var.get()
    special_chars = special_chars_var.get()
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if uppercase else ''
    digit_chars = string.digits if digits else ''
    special_chars_set = '!@#$%^&*()_-+=<>?/{}[]|' if special_chars else ''
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars_set
    length = max(length, 4)
    global password
    password = random.sample(all_chars, min(length, len(all_chars)))
    password = ''.join(password)
    pyperclip.copy(password)
    time.sleep(2)
    text_label = Label(root, text="", font=("Eras Bold ITC", 24),fg="white", bg="black")
    text_label.pack(pady=10)
    text_label.place(x=465, y=400)
    text = password
    text_label.config(text=text)
    # Image label
    image_label = Label(root,bg="black")
    image_label.pack(pady=10)
    image_label.place(x=425, y=450)
    image_path = "Image\\liicter\\02.png"  # Replace with the path to your PNG image
    background_color = ("#000000")
    image_with_background = set_background(image_path, background_color)
    image_label.config(image=image_with_background)
    image_label.image = image_with_background
    # Load the sound file
    sound_file = "sound\\Ayan\\congrants.wav"
    # Replace with the path to your sound file
    mixer.init()
    sound = mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Disable all operations on the Tkinter window
    root.attributes('-disabled', True)
    # Wait for the sound to finish
    root.after(int(sound.get_length() * 1000), enable_operations)
        
def set_background(image_path, background_color):
    original = Image.open(image_path)
    new = Image.new("RGBA", original.size, background_color)
    new.paste(original, (0, 0), original)
    return ImageTk.PhotoImage(new)

def pass_action():
    # Perform a different action
    pass    
def enable_operations():
    # Enable all operations on the Tkinter window
    root.attributes('-disabled', False)
    return
    
# Create the main Tkinter window
root = tk.Tk()
root.title("liicter")
root.geometry("1050x770")
root.config(bg="#000000")
# Load the sound file
sound_file = "sound\\Ayan\\intro.wav"
# Replace with the path to your sound file
mixer.init()
sound = mixer.Sound(sound_file)
# Play the sound
sound.play()
# Disable all operations on the Tkinter window
root.attributes('-disabled', True)
# Wait for the sound to finish
root.after(int(sound.get_length() * 1000), enable_operations)
sound_file = "sound\\Ayan\\intro.wav"
# Replace with the path to your sound file
mixer.init()
sound = mixer.Sound(sound_file)
# Play the sound
sound.play()
# Disable all operations on the Tkinter window
root.attributes('-disabled', True)
# Wait for the sound to finish
root.after(int(sound.get_length() * 1000), enable_operations)
# Load PNG image and create PhotoImage object
image_path = "Image\\liicter\\01.png"  # Replace with the path to your PNG image
background_color = ("#000000")
image_with_background = set_background(image_path, background_color)
# Create button with PNG image
button = tk.Button(root, image=image_with_background, command=display_first_option, bd=0, highlightthickness=0,bg="#FF1493")
button.image = image_with_background
button.place(x=450, y=140)
label = Label(root, text=" Random  Password \n Generator", font=("Nature Beauty Personal Use", 24),fg="#FF0000", bg="black")
label.pack()
label.place(x=420, y=10)
# Run the Tkinter event loop
root.mainloop()



