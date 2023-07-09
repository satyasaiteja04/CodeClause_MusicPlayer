import os
import pygame
from tkinter import *
from tkinter import filedialog, messagebox
root = Tk()
root.title("Music Player using Python")

pygame.mixer.init()

current_song = StringVar()
current_song.set("No Song")
current_artist = StringVar()
current_artist.set("No Artist")


song_list = []
song_listb = Listbox(root, selectmode=SINGLE, font=("Arial", 12), width=50, height=20)
song_listb.pack(padx=10, pady=10)

def Add_songs():
    songs = filedialog.askopenfilenames(filetypes=[("ALL Files", "*.mp3")])
    for song in songs:
        song_list.append(song)
        song_name = os.path.basename(song)
        song_listb.insert(END, song_name)

def Play_songs():
    selected_song = song_listb.curselection()
    if selected_song:
        song_index = selected_song[0]
        song_path = song_list[song_index]
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        update_track_info(song_path)

def Stop_songs():
    pygame.mixer.music.stop()
    current_song.set("No Song")
    current_artist.set("No Artist")
    

def update_track_info(song_path):
    try:
        tags = pygame.mixer.music.get_tags()
        current_song.set(tags["title"])
        current_artist.set(tags["artist"])
        
    except:
        current_song.set(os.path.basename(song_path))
        current_artist.set("Unknown Artist")
       

def Next_songs():
    selected_song = song_listb.curselection()
    if selected_song:
        current_index = selected_song[0]
        if current_index < len(song_list) - 1:
            song_listb.selection_clear(0, END)
            song_listb.selection_set(current_index + 1)
            song_listb.activate(current_index + 1)
            Play_songs()

def Previous_songs():
    selected_song = song_listb.curselection()
    if selected_song:
        current_index = selected_song[0]
        if current_index > 0:
            song_listb.selection_clear(0, END)
            song_listb.selection_set(current_index - 1)
            song_listb.activate(current_index - 1)
            Play_songs()

button_frame = Frame(root)
button_frame.pack(pady=10)

add_button = Button(button_frame, text="Select Song", command=Add_songs)
add_button.pack(side=LEFT, padx=10)

play_button = Button(button_frame, text="Play", command=Play_songs)
play_button.pack(side=LEFT, padx=10)

stop_button = Button(button_frame, text="pause", command=Stop_songs)
stop_button.pack(side=LEFT, padx=10)

next_button = Button(button_frame, text="Next", command=Next_songs)
next_button.pack(side=LEFT, padx=10)

previous_button = Button(button_frame, text="Previous", command=Previous_songs)
previous_button.pack(side=LEFT, padx=10)

track_info = Frame(root)
track_info.pack(pady=10)

song_label = Label(track_info, textvariable=current_song, font=("Times new roman", 20))
song_label.pack()

artist_label = Label(track_info, textvariable=current_artist, font=("Times new roman", 20))
artist_label.pack()

root.mainloop()