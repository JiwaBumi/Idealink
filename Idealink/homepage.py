import tkinter as tk
from PIL import Image, ImageTk

def new_workspace():
    print("New Workspace button clicked")

def load_workspace():
    print("Load Workspace button clicked")

root = tk.Tk()
root.title("Workspace Manager")
root.geometry("1280x720")

# Load app icon
app_icon_img = Image.open("Images/main-logo.png").resize((100, 100))
app_icon = ImageTk.PhotoImage(app_icon_img)
app_icon_label = tk.Label(root, image=app_icon)
app_icon_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

# Buttons
new_workspace_btn = tk.Button(root, text="New Workspace", command=new_workspace)
new_workspace_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

load_workspace_btn = tk.Button(root, text="Load Workspace", command=load_workspace)
load_workspace_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Load gear icon
gear_icon_img = Image.open("Images/settings-icon.png").resize((30, 30))
gear_icon = ImageTk.PhotoImage(gear_icon_img)
gear_icon_btn = tk.Button(root, image=gear_icon, command=None)
gear_icon_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()
