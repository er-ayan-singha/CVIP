import os
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import pyaudio
import wave
import datetime
from pydub import AudioSegment
import pygame  # Add this line
from pygame import mixer
from tkinter import PhotoImage, Label, Canvas, StringVar
from PIL import ImageTk, Image
from time import strftime, localtime

class AudioRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Sweety")
        self.frames = []
        self.is_recording = False
        self.is_playing = False
        self.is_paused = False
        self.auto_open_folder_var = tk.BooleanVar(value=True)
        mixer.init()
        self.mixer = mixer
        self.canvas2 = tk.Canvas(root, width=240, height=170)
        self.canvas2.pack()
        self.canvas2.place(x=360, y=250)
        bg2 = self.canvas2.create_image(0, 0, image=show, anchor=tk.NW)       
        self.canvas1 = tk.Canvas(root, width=240, height=170)
        self.canvas1.pack()
        self.canvas1.place(x=360, y=70)
        bg1 = self.canvas1.create_image(0, 0, image=player, anchor=tk.NW)
        self.canvas = tk.Canvas(root, width=210, height=350, bd=0)
        self.canvas.pack()
        self.canvas.place(x=875, y=70)
        bg = self.canvas.create_image(0, 0, image=sub_bg_image, anchor=tk.NW)
        pause_button = self.canvas1.create_image(28, 143, image=pause)
        self.canvas1.tag_bind(pause_button, "<Button-1>", self.pause_resume_audio)
        stop_button = self.canvas1.create_image(212, 143, image=stop)
        self.canvas1.tag_bind(stop_button, "<Button-1>", self.stop_playback)
        check = self.canvas.create_image(105, 55, image=check_button)
        self.music_emoji = tk.Label(self.canvas1, text="\U0001F3B5 \U0001F3B5 \U0001F3B5",font=('Ananda Black Personal Use', 15, 'bold'))
        self.music_emoji.pack(anchor='n')
        self.music_emoji.place(x=62,y=123)
        self.music_emoji.config(fg="#EE7600", bg="black")
        self.record_button = tk.Button(self.canvas, text="Record", font=("Eras Bold ITC", 13), image=bt1_image, compound="top", command=self.toggle_recording, bd=0)
        self.record_button.pack(pady=10)
        self.record_button.place(x=70, y=90)       
        self.open_folder_button = tk.Button(self.canvas, image=open_file, compound="top", command=self.open_output_folder, bd=0)
        self.open_folder_button.pack(pady=10)
        self.open_folder_button.place(x=83, y=285)       
        self.mp3 = tk.Button(self.canvas, image=mp3, compound="top", command=self.convert_to_mp3, bd=0)
        self.mp3.pack(pady=10)
        self.mp3.place(x=20, y=276)       
        self.exit = tk.Button(self.canvas, image=exit_s, compound="top", command=self.close_window, bd=0)
        self.exit.pack(pady=10)
        self.exit.place(x=135, y=276)
        self.current_recording_index = 0
        self.auto_open_folder_checkbox = tk.Checkbutton(root, text="Auto  Open  Folder", variable=self.auto_open_folder_var, font=("Nature Beauty Personal Use", 11))
        self.auto_open_folder_checkbox.pack(pady=10)
        self.auto_open_folder_checkbox.config(fg="black", bg="#dddddd", activeforeground="black", activebackground="#dddddd")
        self.auto_open_folder_checkbox.place(x=900, y=110)
        
        self.name_entry = tk.Entry(root, width=26,bd=0)
        self.name_entry.insert(0, "Name")
        self.name_entry.pack(pady=10)
        self.name_entry.place(x=900, y=318)
        
        self.playing_label = tk.Label(self.canvas1, text="", font=("Bookman Old Style", 10))
        self.playing_label.config(background="#74747c", foreground="white")
        self.playing_label.pack(pady=10)
        self.playing_label.place(x=5, y=55)
        
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.fs = 44100
        self.load_recordings()

    def close_window(self):
        root.destroy()
        
    def toggle_recording(self):
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.is_recording = True
        self.record_button.config(text="Stop")
        self.frames = []
        self.p = pyaudio.PyAudio()
        stream = self.p.open(format=self.sample_format, channels=self.channels, rate=self.fs, frames_per_buffer=self.chunk, input=True)
        print("Recording...")
        while self.is_recording:
            data = stream.read(self.chunk)
            self.frames.append(data)
            self.root.update()
        stream.stop_stream()
        stream.close()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.config(text="Record")
        self.p.terminate()
        self.save_audio()
        if self.auto_open_folder_var.get():
            self.open_output_folder()
        self.load_recordings()

    def save_audio(self):
        folder_path = self.create_date_specific_folder()
        file_name = f"{self.name_entry.get()}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        file_path = os.path.join(folder_path, file_name)
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print(f"Audio saved: {file_path}")

    def create_date_specific_folder(self):
        folder_path = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y%m%d'))
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path

    def open_output_folder(self):
        folder_path = self.create_date_specific_folder()
        os.system(f'explorer "{folder_path}"')

    def load_recordings(self):
        folder_path = self.create_date_specific_folder()
        recordings = [f for f in os.listdir(folder_path) if f.endswith(".wav")]
        recordings = recordings[-8:]
        for i, recording in enumerate(recordings):
            img = self.set_background()
            button = tk.Button(self.canvas2, image=img, compound=tk.TOP, command=lambda rec=recording: self.play_selected_audio(selected_recording=rec), bd=0)
            button.image = img
            row = i // 4
            col = i % 4
            x = 24 + col * 55
            y = 33 + row * 75
            self.canvas2.create_window(x, y, anchor=tk.NW, window=button)
        self.canvas2.update()
        
    def play_selected_audio(self, event=None, selected_recording=None):
        if selected_recording:
            folder_path = self.create_date_specific_folder()
            file_path = os.path.join(folder_path, selected_recording)
            try:
                if self.is_paused:
                    self.mixer.music.unpause()
                    self.is_paused = False
                    print("Resuming playback.")
                else:
                    self.mixer.music.stop()
                    self.mixer.music.load(file_path)
                    self.mixer.music.play()
                    self.is_playing = True
                    self.update_playing_label(selected_recording)
                    print(f"Playing audio: {file_path}")
            except pygame.error as e:
                messagebox.showerror("File Not Found", f"Error: {e}\nAudio file not found: {file_path}")
        else:
            print("No audio file selected.")

    def update_playing_label(self, recording_name):
        # Show only the file name without "Currently Playing"
        self.playing_label.config(text=f"{recording_name}")
    def pause_resume_audio(self, event=None):
        if self.is_playing:
            if not self.is_paused:
                self.mixer.music.pause()
                self.is_paused = True
                print("Pausing playback.")
            else:
                self.mixer.music.unpause()
                self.is_paused = False
                print("Resuming playback.")
        else:
            print("No audio is currently playing.")
            
    def stop_playback(self, event=None):
        if self.is_playing:
            self.mixer.music.stop()
            self.is_playing = False
            self.is_paused = False
            self.update_playing_label("")
        else:
            print("No audio is currently playing.")
            
    def update_playing_label(self, recording_name):
        self.playing_label.config(text=f"{recording_name}")
        
    def set_background(self):
        original = Image.open(file_icon_path)
        new = Image.new("RGBA", original.size, file_background_color)
        new.paste(original, (0, 0), original)
        return ImageTk.PhotoImage(new)
    def convert_to_mp3(self):
        file_paths = filedialog.askopenfilenames(
            title="Select Audio Files",
            filetypes=[("WAV files", "*.wav"), ("All files", "*.*")],
            initialdir=self.create_date_specific_folder()
        )
        if file_paths:
            mp3_folder_name = datetime.datetime.now().strftime('%Y%m%d_mp3')
            mp3_folder_path = os.path.join(os.getcwd(), mp3_folder_name)
            if not os.path.exists(mp3_folder_path):
                os.makedirs(mp3_folder_path)
            for wav_file_path in file_paths:
                recording_name = os.path.splitext(os.path.basename(wav_file_path))[0]
                mp3_file_name = f"{recording_name}.mp3"
                mp3_file_path = os.path.join(mp3_folder_path, mp3_file_name)
                sound = AudioSegment.from_wav(wav_file_path)
                sound.export(mp3_file_path, format="mp3")
                print(f"Audio converted to MP3: {mp3_file_path}")
            if self.auto_open_folder_var.get():
                os.system(f'explorer "{mp3_folder_path}"')
        else:
            print("No files selected for conversion.")
def time():
    time_string = strftime('%I:%M:%S %p')
    day_string = strftime('%A', localtime())
    date_string = strftime('%B %d', localtime())
    time_label.config(text=time_string)
    day_label.config(text=day_string)
    date_label.config(text=date_string)
    root.after(1000, time)
    
# Entry point for the script.
if __name__ == "__main__":
    root = tk.Tk()
    bg_image = ImageTk.PhotoImage(Image.open("Image\\main.png").resize((1000, 600)))
    bt1_image = ImageTk.PhotoImage(Image.open("Image\\mic.png").resize((73, 130)))
    image_width = 800
    root.geometry("1200x600")
    background_label = Label(root, image=bg_image)
    background_label.place(x=110, y=0, relwidth=1, relheight=1)
    sub_bg_image = ImageTk.PhotoImage(Image.open("Image\\sub.png").resize((210, 350)))
    check_button = ImageTk.PhotoImage(Image.open("Image\\check.png"))
    pause = ImageTk.PhotoImage(Image.open("Image\\pause.png"))
    stop = ImageTk.PhotoImage(Image.open("Image\\stop.png"))
    file = ImageTk.PhotoImage(Image.open("Image\\file.png"))
    open_file = ImageTk.PhotoImage(Image.open("Image\\open.png"))
    exit_s = ImageTk.PhotoImage(Image.open("Image\\exit.png"))
    mp3 = ImageTk.PhotoImage(Image.open("Image\\mp3.png"))
    player = ImageTk.PhotoImage(Image.open("Image\\player.png").resize((240, 170)))
    show = ImageTk.PhotoImage(Image.open("Image\\show.jpg").resize((240, 170)))
    file_icon_path = "Image\\file.png"
    file_background_color = ("#fff3db")
    root.resizable(0, 0)
    app = AudioRecorder(root)
    
    time_label = tk.Label(root, font=('Eras Bold ITC', 30, 'bold'))
    time_label.pack(anchor='center')
    time_label.place(x=600,y=330)
    
    date_label = tk.Label(root, font=('Comic Sans MS', 20, 'bold'))
    date_label.pack(anchor='s')
    date_label.place(x=650,y=380)
    
    day_label = tk.Label(root, font=('Ananda Black Personal Use', 20, 'bold'))
    day_label.pack(anchor='n')
    day_label.place(x=680,y=280)
    music="\U0001F3B5"
    smile_emoji = "\U0001F604 \U0001F604 \U0001F604 \U0001F604 \U0001F604 \U0001F604 \U0001F604"
    smile_label = tk.Label(root, text=smile_emoji, font=("Arial", 23))
    smile_label.pack(anchor='n')
    smile_label.place(x=600,y=230)
    app_name = tk.Label(root, text="Voice \nRecorder", font=("Flicker", 50))
    app_name.pack(anchor='n')
    app_name.place(x=640,y=70)
    time()
    root.mainloop()
    root.mainloop()


