import tkinter as tk
from tkinter import messagebox
import pygame

pygame.init()

root = tk.Tk()
root.title("Music Player")
root.geometry('200x300') 

playlist = [
    "song1.mp3",
    "song2.mp3",
    "song3.mp3",
    "song4.mp3",
    "song5.mp3",
]

current_track_index = 0

def play_music():
    global current_track_index
    track = playlist[current_track_index]
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(loops=0)

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    if current_track_index < len(playlist) - 1:
        current_track_index += 1
        stop_music()
        play_music()
    else:
        messagebox.showinfo("End of Playlist", "You have reached end of playlist so playing first song in Playlist")
        current_track_index=0
        play_music()

def previous_track():
    global current_track_index
    if current_track_index > 0 :
        current_track_index -= 1
        stop_music()
        play_music()
    else:
        messagebox.showinfo("Out of Playlist", "You have reached out of playlist so playing last song in Playlist")
        current_track_index=len(playlist) - 1
        play_music()


play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=5)

resume_button = tk.Button(root, text="Resume", command=resume_music)
resume_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=5)

next_button = tk.Button(root, text="Next Song", command=next_track)
next_button.pack(pady=5)

previous_button = tk.Button(root, text="Previous Song", command=previous_track)
previous_button.pack(pady=5)

root.mainloop()