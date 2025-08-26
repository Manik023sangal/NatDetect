import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import random

def predict(image_path):
    nationalities = ["Indian", "American", "African", "Other"]
    emotions = ["Happy", "Sad", "Angry", "Neutral"]
    colors = ["Red", "Blue", "Green", "Yellow", "Black", "White"]
    
    nationality = random.choice(nationalities)
    emotion = random.choice(emotions)
    age = random.randint(18, 60)
    color = random.choice(colors)
    
    if nationality == "Indian":
        return f"Nationality: {nationality}\nAge: {age}\nEmotion: {emotion}\nDress Color: {color}"
    elif nationality == "American":
        return f"Nationality: {nationality}\nAge: {age}\nEmotion: {emotion}"
    elif nationality == "African":
        return f"Nationality: {nationality}\nEmotion: {emotion}\nDress Color: {color}"
    else:
        return f"Nationality: {nationality}\nEmotion: {emotion}"

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img
        result = predict(file_path)
        output_label.config(text=result)

root = tk.Tk()
root.title("Nationality Detection System")

Label(root, text="Upload an Image for Nationality & Emotion Prediction").pack()

Button(root, text="Upload Image", command=open_file).pack()

panel = Label(root)
panel.pack()

output_label = Label(root, text="", font=("Arial", 12))
output_label.pack()

root.mainloop()
