import tkinter as tk 

class Application(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()
    self.create_widgets()
    
  def create_widgets(self):
    # Create a Frame
    self.frame = tk.Frame(self)
    self.frame.grid(row=0, column=0)
    
    # Create Multiple Widgets within the Frame
    label = tk.Label(self.frame, text="RK Dev Studio")
    label.pack()
    entry = tk.Entry(self.frame)
    entry.pack()
    button = tk.Button(self.frame, text="Exit", command=root.destroy)
    button.pack()
    
# Create the Main Window
root = tk.Tk()
root.title("Multiple Widgets within a Frame")
app = Application(master=root)

# Start the Application
app.mainloop()