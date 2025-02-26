import tkinter as tk 
from tkcalendar import Calendar 

root = tk.Tk()
root.title("Calendar")
root.geometry("600x600")

cal = Calendar(root, selectmode="day", date_pattern="mm-dd-yyyy")
cal.pack(pady=20)

selected_date = tk.Label(root, text="")
selected_date.pack(pady=10)

def update_selected_date():
  selected_date.config(text="Selected Date: " + cal.get_date())
  
cal.bind("<<CalendarSelected>>", lambda event: update_selected_date())

root.mainloop()