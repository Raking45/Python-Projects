import tkinter as tk 

def main():
  # Create the Main Window
  root = tk.Tk()
  root.title("Tkinter Basic GUI")
  
  # Create a Label
  label_text = "RK Dev Studio"
  label = tk.Label(root, text=label_text)
  label.grid(row=0, column=0)
  
  # Create a Button
  button_text = "Exit"
  button = tk.Button(root, text=button_text, command=root.destroy)
  button.grid(row=1, column=0)
  
  # Start the Application
  root.mainloop()
  
if __name__ == "__main__":
  main()