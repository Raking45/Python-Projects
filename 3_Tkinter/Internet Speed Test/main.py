from tkinter import * 
from tkinter.ttk import Progressbar 
import speedtest 
import time 

# Animate Speed Function
def animate_speed(speed_value, progress_bar, scaling_factor, step=0):
  max_value = speed_value * scaling_factor
  if step <= 0.9 * max_value:
    progress_bar["value"] = step
    root.update_idletasks()
    root.after(10, animate_speed, speed_value, progress_bar, scaling_factor, step+1)
    
# Check Speed Function
def check_speed():
  st = speedtest.Speedtest()
  
  download_speed = st.download() / 1000000
  upload_speed = st.upload() / 1000000
  ping = st.results.ping
  
  download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
  upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
  ping_label.config(text=f"Ping: {ping:.2f} ms")
  
  download_progress["value"] = 0
  upload_progress["value"] = 0
  ping_progress["value"] = 0
  
  root.update_idletasks() # Refresh GUI Before Animation
  
  animate_speed(download_speed, download_progress, 5)
  animate_speed(upload_speed, upload_progress, 3)
  animate_speed(ping, ping_progress, 2)
  
# GUI
root = Tk()
root.title("Internet Speed Check")
root.config(bg="#1e90ff")
root.geometry("600x600")
root.resizable(False, False)

label1 = Label(root, text="Internet Speed Check", font=("Arial", 24, "bold"), bg="#1e90ff", fg="black").pack()

download_label = Label(root, font=("Arial", 18), bg="#1e90ff", fg="white")
download_label.pack(pady=10)
download_progress = Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
download_progress.pack(pady=10)

upload_label = Label(root, font=("Arial", 18), bg="#1e90ff", fg="white")
upload_label.pack(pady=10)
upload_progress = Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
upload_progress.pack(pady=10)

ping_label = Label(root, font=("Arial", 18), bg="#1e90ff", fg="white")
ping_label.pack(pady=10)
ping_progress = Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
ping_progress.pack(pady=10)

# Check Speed & Refresh Buttons
button = Button(root, text="Check Speed", font=("Arial", 16, "bold"), bg="green", fg="white", command=check_speed)
button.pack(pady=20, expand=True)

root.mainloop()