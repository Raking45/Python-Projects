import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk

# Global variable to track the saved text for unsaved changes check
saved_text = ""

# New File
def new_file():
    global saved_text
    if text_area.get("1.0", "end-1c") != saved_text:
        result = messagebox.askyesnocancel("Save Changes", "Do you want to save changes to this file?")
        if result:
            save_file()
        elif result is None:
            return
    text_area.delete(1.0, "end")
    saved_text = ""

# Open File
def open_file():
    global saved_text
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, "end")
            text_area.insert("1.0", file.read())
        saved_text = text_area.get("1.0", "end-1c")

# Save File
def save_file():
    global saved_text
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", "end-1c"))
        saved_text = text_area.get("1.0", "end-1c")

# Exit Program
def exit_program():
    if text_area.get("1.0", "end-1c") != saved_text:
        result = messagebox.askyesnocancel("Save Changes", "Do you want to save changes to the file?")
        if result:
            save_file()
        elif result is None:
            return
    root.quit()

# Change font style font size
def change_font():
    font_style = simpledialog.askstring("Font Style", "Enter font style (e.g., Arial, Courier):")
    font_size = simpledialog.askinteger("Font Size", "Enter font size:")
    if font_style and font_size:
        text_area.config(font=(font_style, font_size))

# Search text
def search_text():
    search_term = simpledialog.askstring("Search", "Enter text to search:")
    if search_term:
        text_area.tag_remove("highlight", "1.0", "end")
        start_pos = "1.0"
        while True:
            start_pos = text_area.search(search_term, start_pos, stopindex="end")
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search_term)}c"
            text_area.tag_add("highlight", start_pos, end_pos)
            text_area.tag_configure("highlight", background="yellow")
            start_pos = end_pos

# Autosave
def auto_save():
    save_file()
    root.after(60000, auto_save)  # Auto-save every 60 seconds

# Update line numbers
def update_line_numbers(event=None):
    lines = text_area.get("1.0", "end-1c").splitlines()
    line_numbers = "\n".join(str(i + 1) for i in range(len(lines)))
    line_numbers_text.config(state="normal")
    line_numbers_text.delete("1.0", "end")
    line_numbers_text.insert("1.0", line_numbers)
    line_numbers_text.config(state="disabled")

# Create new tabs
def create_new_tab():
    tab = ttk.Frame(notebook)
    notebook.add(tab, text="Untitled")
    new_text_area = tk.Text(tab, wrap="word", undo=True)
    new_text_area.pack(expand=1, fill="both")
    new_text_area.bind("<KeyRelease>")

# Initialize tkinter window
root = tk.Tk()
root.title("RK Notepad")
root.geometry("800x600")

# Notebook (Tab system)
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# Create a new tab for a new file
create_new_tab()

# Create a text area widget for the Notepad
text_area = tk.Text(notebook, wrap="word", undo=True)
text_area.pack(expand="yes", fill="both")

# Create line numbers text widget
line_numbers_text = tk.Text(root, width=4, padx=5, state="disabled", bg="lightgray")
line_numbers_text.pack(side="left", fill="y")

# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=lambda: text_area.edit_undo())
edit_menu.add_command(label="Redo", command=lambda: text_area.edit_redo())
edit_menu.add_command(label="Search", command=search_text)
edit_menu.add_command(label="Change Font", command=change_font)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Tab menu (for handling tabs)
tab_menu = tk.Menu(menu_bar, tearoff=0)
tab_menu.add_command(label="New Tab", command=create_new_tab)
menu_bar.add_cascade(label="Tabs", menu=tab_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add the menu bar to the window
root.config(menu=menu_bar)

# Bind events for word count and line numbers
text_area.bind("<KeyRelease>")
text_area.bind("<KeyRelease>", update_line_numbers)

# Auto-save feature
root.after(60000, auto_save)  # Auto-save every 60 seconds

# Start the Tkinter event loop
root.mainloop()
