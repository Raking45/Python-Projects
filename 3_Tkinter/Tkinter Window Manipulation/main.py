import tkinter as tk 

root = tk.Tk()
root.title('RK Dev Studio')
root.geometry('600x800+50+50')
root.resizable(True, True)

window_width = 600
window_height = 800

# Get the Screen Dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the Center Point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the Position of the Window to the Center of the Screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.mainloop()