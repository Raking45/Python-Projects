import qrcode 
from tkinter import * 

cp = Tk()
cp.title("QR Code Generator")
cp.geometry("700x250")
cp.config(bg="slategray")

def generate():
  img = qrcode.make(msg.get())
  type(img)
  img.save(f"{save_name.get()}.png")
  Label(cp, text="File Saved", bg="slategray", fg="black", font=("Arial Black", 8)).pack()
  
def show():
  img = qrcode.make(msg.get())
  type(img)
  img.show()
  
frame = Frame(cp, bg="slategray")
frame.pack(expand=True)

# Enter the Text or URL
Label(frame, text="Enter the Text or URL: ", font=("Arial Black", 16), bg="slategray").grid(row=0, column=0, sticky="w")
msg = Entry(frame)
msg.grid(row=0, column=1)

# Enter the File Name
Label(frame, text="Save As: ", font=("Arial Black", 16), bg="slategray").grid(row=1, column=0, sticky="w")
save_name = Entry(frame)
save_name.grid(row=1, column=1)

# Buttons
btn = Button(cp, text="Show QR Code", bd="5", command=show, width=15)
btn.pack()
btn = Button(cp, text="Save QR Code", command=generate, bd="5", width=15)
btn.pack()

cp.mainloop()