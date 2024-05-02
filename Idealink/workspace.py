import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def workspace_window(workspace_path):
    # Create new Tkinter window

    def change_color():
        # fg is foreground, bg is background
        root.config(bg="black")
        textbox_listbox_bg = "dark gray"
        textbox_listbox_fg = "white"
        button_bg = "gray20"
        button_fg = "white"

        # Configss
        text_box.config(bg=textbox_listbox_bg, fg=textbox_listbox_fg)
        listbox.config(bg=textbox_listbox_bg, fg=textbox_listbox_fg)
        new_button.config(bg=button_bg, fg=button_fg)
        delete_button.config(bg=button_bg, fg=button_fg)
        save_button.config(bg=button_bg, fg=button_fg)

    root = tk.Tk()
    root.title(os.path.basename(workspace_path))
 
    #window Position
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 800
    window_height = 720
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


    # Change Window Icon (the one at top left of app)
    icon = "Images/window_icon.ico"  # Provide the path to your icon file
    root.iconbitmap(icon)

    def assistance():
        messagebox.showinfo("Tutorial", "Welcome to Idealink!\n"
                                "On the left side shows the list of all your notes. Double click them to open\n"
                                "Click [New] to create a new note! \n"
                                "Click [Delete] to delete currently open note (BECAREFUL, CANNOT BE UNDONE!)\n"
                                "Click [Save] to save your current work!")

    # Menu Bar
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Tutorial", command=assistance)
    file_menu.add_command(label="Switch Theme", command=change_color)

    # Attach file_menu to menu_bar
    menu_bar.add_cascade(label="More", menu=file_menu)

    # Configure menu_bar in root window
    root.config(menu=menu_bar)

    # Configure resizing behavior
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

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
    text_box.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

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
    def new_file():
        # Function to handle OK button click in the custom dialog
        def ok():
            nonlocal file_name_entry
            # Get the inputted file name
            file_name = file_name_entry.get()
            if file_name:
                # Close the dialog window
                dialog_window.destroy()
                # Create the new .md file with the inputted name
                file_path = os.path.join(workspace_path, file_name + ".md")
                with open(file_path, 'w') as file:
                    file.write("")
                # Update listbox and md_files list
                md_files.append(file_name + ".md")
                listbox.insert(tk.END, file_name + ".md")

        # Function to handle Cancel button click in the custom dialog
        def cancel():
            dialog_window.destroy()

        # Create the custom dialog window
        dialog_window = tk.Toplevel()
        dialog_window.title("Enter File Name")

        # Label and Entry for file name input
        file_name_label = tk.Label(dialog_window, text="Enter file name:")
        file_name_label.pack()
        file_name_entry = tk.Entry(dialog_window)
        file_name_entry.pack()

        # OK button
        ok_button = tk.Button(dialog_window, text="OK", command=ok)
        ok_button.pack(side="left", padx=5)

        # Cancel button
        cancel_button = tk.Button(dialog_window, text="Cancel", command=cancel)
        cancel_button.pack(side="right", padx=5)

        # Center the dialog window
        dialog_window.geometry("+%d+%d" % (root.winfo_rootx() + 50, root.winfo_rooty() + 50))


    new_button = tk.Button(root, text="New", command=new_file, width=15)
    new_button.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 5))

    # Delete button
    def delete_md():
        selected_index = listbox.curselection()
        if selected_index:
            response = messagebox.askyesno("Delete File", "Are you sure you want to delete this file?")
            if response:
                selected_file = md_files[selected_index[0]]
                os.remove(os.path.join(workspace_path, selected_file))
                md_files.remove(selected_file)
                listbox.delete(selected_index)

    delete_button = tk.Button(root, text="Delete", command=delete_md, width=15)
    delete_button.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 5))

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

    def open_md(event):
        selected_file = listbox.get(tk.ACTIVE)
        if selected_file:
            response = messagebox.askyesno("Open File", "Are you sure you want to open?\nMake sure to save your current work!")
            if response:
                with open(os.path.join(workspace_path, selected_file), 'r') as file:
                    text_box.delete(1.0, tk.END)
                    text_box.insert(tk.END, file.read())
                currently_open.delete(1.0, tk.END)
                currently_open.insert(tk.END, f"Currently Editing: {selected_file}")

    listbox.bind("<Double-Button-1>", open_md)

    def ignore_click(event):
        return "break"

    currently_open = tk.Text(root, height=1)
    currently_open.grid(row=2, column=1, sticky="w", padx=10, pady=(0, 5))
    currently_open.bind("<Button-1>", ignore_click)


    root.mainloop()
