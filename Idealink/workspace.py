import os
import tkinter as tk
from tkinter import filedialog, messagebox

def workspace_window(workspace_path):
    # Create new Tkinter window
    root = tk.Tk()
    root.title(os.path.basename(workspace_path))
    root.geometry("800x720")

    # List files in workspace directory
    files = os.listdir(workspace_path)

    # Filter .md files
    md_files = [file for file in files if file.endswith('.md')]

    # Create a frame to hold the Listbox and text box
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Display list of .md files in a Listbox
    listbox = tk.Listbox(frame, width=30, height=40)
    for file in md_files:
        listbox.insert(tk.END, file)
    listbox.pack(side="left", fill="both", expand=True)

    # Configure scrollbar for Listbox
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=listbox.yview)
    scrollbar.pack(side="right", fill="y")
    listbox.config(yscrollcommand=scrollbar.set)

    # Text box
    text_box = tk.Text(root, width=70, height=40)
    text_box.grid(row=0, column=1, padx=10, pady=10)

    # Function to handle opening .md file
    def open_md(event):
        selected_file = listbox.get(tk.ACTIVE)
        if selected_file:
            response = messagebox.askyesno("Open File", "Are you sure you want to open?\nMake sure to save your current work!")
            if response:
                with open(os.path.join(workspace_path, selected_file), 'r') as file:
                    text_box.delete(1.0, tk.END)
                    text_box.insert(tk.END, file.read())

    listbox.bind("<Double-Button-1>", open_md)

    # New button
    def new_md():
        file_name = filedialog.asksaveasfilename(initialdir=workspace_path, title="New .md File", defaultextension=".md", filetypes=[("Markdown Files", "*.md")])
        if file_name:
            with open(file_name, 'w') as file:
                file.write("")
            md_files.append(os.path.basename(file_name))
            listbox.insert(tk.END, os.path.basename(file_name))

    new_button = tk.Button(root, text="New", command=new_md, width=15)
    new_button.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 5))

    # Save button
    def save_md():
        selected_file = listbox.get(tk.ACTIVE)
        if selected_file:
            response = messagebox.askyesno("Save File", "Are you sure you want to save?")
            if response:
                with open(os.path.join(workspace_path, selected_file), 'w') as file:
                    file.write(text_box.get("1.0", tk.END))

    save_button = tk.Button(root, text="Save", command=save_md, width=15)
    save_button.grid(row=1, column=1, sticky="ew", padx=10, pady=(0, 5))

    root.mainloop()
