import numpy as np
import simpleaudio as sa
import tkinter as tk
from functools import partial


class SoundGenerator:
    def __init__(self, win):
        self.freq = 440
        self.duration = 3

        #frequency
        self.freq_lbl = tk.Label(win, text = 'Frequency')
        self.freq_lbl.place(x=10, y=50)
        self.inc_btn = tk.Button(win, text="+10", fg = 'black', command= self.inc_freq)
        self.inc_btn.place(x=215,y=48)
        self.dec_btn = tk.Button(win, text="-10", fg = 'black', command= self.dec_freq)
        self.dec_btn.place(x=250,y=48)
        self.freq_text = tk.Entry(win, text = "frequency", bd =3)
        self.freq_text.place(x=75,y=50)
        self.freq_text.insert(0,"440")

        #duration
        self.dur_lbl = tk.Label(win, text = 'Duration')
        self.dur_lbl.place(x=10, y=100)
        self.inc_btn_dur = tk.Button(win, text="+1  ", fg = 'black', command= self.inc_dur)
        self.inc_btn_dur.place(x=215,y=98)
        self.dec_btn_dur = tk.Button(win, text="-1  ", fg = 'black', command= self.dec_dur)
        self.dec_btn_dur.place(x=250,y=98)
        self.dur_text = tk.Entry(win, text = "duration", bd =3)
        self.dur_text.place(x=75,y=100)
        self.dur_text.insert(0,"3")

        #play
        self.play_btn = tk.Button(win, text="play", fg = 'red', command= self.play_sound)
        self.play_btn.place(x=250, y=150)

    def set_text(self, text):
        self.freq_text.delete(0, tk.END)
        self.freq_text.insert(0,text)

    def set_text_dur(self, text):
        self.dur_text.delete(0, tk.END)
        self.dur_text.insert(0,text)

    def play_sound(self):
        self.freq = int(self.freq_text.get())
        frequency = self.freq  
        fs = 44100  # 44100 samples per second
        self.duration = int(self.dur_text.get())
        seconds = self.duration 

        # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
        t = np.linspace(0, seconds, seconds * fs, False)

        # Generate a 440 Hz sine wave
        note = np.sin(frequency * t * 2 * np.pi)

        # Ensure that highest value is in 16-bit range
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        # Convert to 16-bit data
        audio = audio.astype(np.int16)

        # Start playback
        play_obj = sa.play_buffer(audio, 1, 2, fs)

        # Wait for playback to finish before exiting
        play_obj.wait_done()

    def inc_freq(self):
        self.freq = int(self.freq_text.get())
        self.freq += 10
        self.set_text(self.freq)
    def dec_freq(self):
        self.freq = int(self.freq_text.get())
        if self.freq > 0:
            self.freq -=10
            self.set_text(self.freq)

    def inc_dur(self):
        self.duration = int(self.dur_text.get())
        self.duration += 1
        self.set_text_dur(self.duration)
    def dec_dur(self):
        self.freq = int(self.dur_text.get())
        if self.duration > 0:
            self.duration -=1
            self.set_text_dur(self.duration)


#GUI
window = tk.Tk()
sg =SoundGenerator(window)

window.title("Sound Generator")
window.geometry("300x200+10+20")
window.mainloop()


