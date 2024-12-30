import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class GUI:
    comboboxOptions = ["Off", "Erosion", "Opening"]

    def __init__(self, title = "Live Camera Feed", width = 640, height = 480):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.bind('<q>', lambda event: self.on_close())
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.geometry(f"{width}x{height}")

        self.running = True

        self.grayLabel = tk.Label(self.root)
        self.grayLabel.grid(row = 0, column = 0)

        self.invLabel = tk.Label(self.root)
        self.invLabel.grid(row = 0, column = 1)

        self.centerOfMassLabel = tk.Label(self.root, text="Center of Mass: ", font=("Helvetica", 16))
        self.centerOfMassLabel.grid(row = 0, column = 2, padx=20, pady=20)

        self.drawCenterOfMass = False
        self.centerOfMassCheckButtonLabel = tk.Checkbutton(self.root, text="Draw Center of Mass", command= lambda: self.on_checkbox_change("drawCenterOfMass"))
        self.centerOfMassCheckButtonLabel.grid(row = 1, column = 2, padx=10, pady=35)

        self.thresholdValue = 45

        self.thresholdSelector = tk.Scale(self.root, from_=0, to=255, orient=tk.HORIZONTAL, label="Threshold", command= lambda value : self.on_scale_change(value, "thresholdValue") , length=255, resolution=1)
        self.thresholdSelector.set(self.thresholdValue)
        self.thresholdSelector.grid(row = 1, column = 0, padx=10, pady=35, columnspan=2)

        self.iterationsValue = 0
        self.iterationsSelector = tk.Scale(self.root, from_=0, to=10, orient=tk.HORIZONTAL, label="Iterations", length=255, resolution=1, command= lambda value : self.on_scale_change(value, "iterationsValue"))
        self.iterationsSelector.set(self.iterationsValue)

        self.kernelSizeValue = 2
        self.kernelSizeSelector = tk.Scale(self.root, from_=2, to=15, orient=tk.HORIZONTAL, label="Kernel Size", length=255, resolution=1, command = lambda value : self.on_scale_change(value, "kernelSizeValue"))
        self.kernelSizeSelector.set(self.kernelSizeValue)

        self.iterationsSelector.grid(row = 2, column = 0, padx=10, pady=35)
        self.kernelSizeSelector.grid(row = 2, column = 1, padx=10, pady=35)

        self.combobox = ttk.Combobox(self.root, values=self.comboboxOptions)
        self.combobox.set(self.comboboxOptions[0])
        self.combobox.grid(row = 2, column = 2, padx=10, pady=35)

        self.minAreaValue = 100
        self.minAreaInput = tk.Entry(self.root, validate="key", validatecommand = (self.root.register(lambda value : self.validate_entry(value, "minAreaValue")), '%P'))
        self.minAreaInput.insert(0, self.minAreaValue)
        self.minAreaInput.grid(row = 3, column = 1, padx=10, pady=35)

        self.applyContourFiltering = False
        self.contourCheckButtonLabel = tk.Checkbutton(self.root, text="Apply Contour Filtering", command=lambda: self.on_checkbox_change("applyContourFiltering"))
        self.contourCheckButtonLabel.grid(row = 3, column = 2, padx=10, pady=35)
    

    def on_checkbox_change(self, attribute_name):
        current_value = getattr(self, attribute_name)
        setattr(self, attribute_name, not current_value)
    
    def on_scale_change(self, value, attribute_name):
        dtype = type(getattr(self, attribute_name))
        setattr(self, attribute_name, dtype(value))

    def validate_entry(self, value, attribute_name):
        dtype = type(getattr(self, attribute_name))
        try:
            setattr(self, attribute_name, dtype(value))
            return True
        except ValueError:
            return False

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