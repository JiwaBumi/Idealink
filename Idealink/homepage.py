# homepage.py
import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk
import os
from workspace import workspace_window

def new_workspace():
    # Open file explorer to select directory
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        # Prompt user for workspace name
        workspace_name = tk.simpledialog.askstring("New Workspace", "Enter workspace name:")
        if workspace_name:
            # Create folder with input name in selected directory
            new_workspace_path = os.path.join(selected_directory, workspace_name)
            os.makedirs(new_workspace_path, exist_ok=True)
            workspace_window(new_workspace_path)


def load_workspace():
    # Open file explorer to select directory
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        workspace_window(selected_directory)

root = tk.Tk()
root.title("IDEALINK")
root.geometry("720x720")

# Load background image
background_image = Image.open("Images/background.jpg")
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load app icon
app_icon_img = Image.open("Images/main-logo.png").resize((350, 330))
app_icon = ImageTk.PhotoImage(app_icon_img)
app_icon_label = tk.Label(root, image=app_icon)
app_icon_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

# Buttons
new_workspace_btn = tk.Button(root, text="New Workspace", command=new_workspace, width=20, height=2)
new_workspace_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

load_workspace_btn = tk.Button(root, text="Load Workspace", command=load_workspace, width=20, height=2)
load_workspace_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Load gear icon
gear_icon_img = Image.open("Images/settings-icon.png").resize((30, 30))
gear_icon = ImageTk.PhotoImage(gear_icon_img)
gear_icon_btn = tk.Button(root, image=gear_icon, command=None, width=50, height=50)
gear_icon_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()
