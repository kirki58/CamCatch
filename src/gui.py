import tkinter as tk
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Live Camera Feed")
        self.grayLabel = tk.Label(self.root)
        self.grayLabel.pack()
        self.invLabel = tk.Label(self.root)
        self.invLabel.pack()
        self.running = True
        self.root.bind('<q>', lambda event: self.on_close())
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.running = False
        self.root.quit()
        self.root.destroy()
        
    def put_gray(self, gray):
        grayImage = Image.fromarray(gray)
        grayPhoto = ImageTk.PhotoImage(grayImage)
        self.grayLabel.configure(image=grayPhoto)
        self.grayLabel.image = grayPhoto

    def put_inv(self, inv):
        invImage = Image.fromarray(inv)
        invPhoto = ImageTk.PhotoImage(invImage)
        self.invLabel.configure(image=invPhoto)
        self.invLabel.image = invPhoto
    
    def update(self):
        self.root.update_idletasks()
        self.root.update()
