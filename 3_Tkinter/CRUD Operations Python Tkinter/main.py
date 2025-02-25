from tkinter import *
import random 
import string

top = Tk()
top.title("Python CRUD Operations")
top.geometry("600x400")

# Create Function
def CreateOperation():
  from create import InsertData
  
  top1 = Tk()
  top1.geometry("360x200")
  top1.title("Create Operation")
  
  letters = string.ascii_lowercase
  random_id = "".join(random.choice(letters) for i in range(8))
  
  name = StringVar(top1)
  ID = StringVar(top1)
  ID.set(random_id)
  
  Label(top1, text="Name").grid(row=0, column=0, padx=20, pady=20, sticky="w")
  Entry(top1, textvariable=name).grid(row=0, column=1, padx=20)
  Label(top1, text="ID (Auto Generated)").grid(row=1, padx=20, column=0, sticky="w")
  Entry(top1, textvariable=ID, state="disabled").grid(row=1, column=1)
  
  Button(top1, text="Create", fg="white", bg="slategray", width=12, font=("Arial", 16), command=lambda: InsertData(name.get(), random_id)).grid(row=2, column=0, columnspan=2, pady=20)
  
  top1.mainloop()
  
Button(top, text="Create", bg="slategray", fg="white", width=12, font=("Arial", 16), command=lambda: CreateOperation()).grid(row=0, column=0, padx=25, pady=30)

# Read Function
def ReadOperation():
  from read import Read 
  
  top2 = Tk()
  top2.geometry("250x200")
  top2.title("Read Operation")
  
  Label(top2, text="Name").grid(row=0, column=0, padx=30, sticky="w")
  Label(top2, text="  |   ").grid(row=0, column=1)
  Label(top2, text="ID").grid(row=0, column=2, padx=20, sticky="w")
  Label(top2, text="------"*7).grid(row=1, column=0, padx=20, columnspan=5)
  
  data = Read()
  for i in range(len(data)):
    Label(top2, text=data[i][0]).grid(row=2+i, column=0, padx=20, sticky="w")
    Label(top2, text="  |   ").grid(row=2+i, column=1)
    Label(top2, text=data[i][1]).grid(row=2+i, column=2, sticky="w")
    
  top2.mainloop()
  
Button(top, text="Read", bg="slategray", fg="white", width=12, font=("Arial", 16), command=lambda: ReadOperation()).grid(row=0, column=1)

# Update Function
def UpdateOperation():
  from read import Read 
  from update import Update 
  
  top3 = Tk()
  top3.geometry("250x200")
  top3.title("Update Operation")
  
  data = Read()
  id_list = []
  for i in data:
    id_list.append(i[1])
    
  e = StringVar(top3)
  e.set("Select ID")
  OptionMenu(top3, e, *id_list).pack(pady=15)
  
  name = StringVar(top3)
  name.set("New Name")
  Entry(top3, textvariable=name).pack(pady=15)
  
  def MyUpdate():
    Update(name.get(), e.get())
    top3.destroy()
  Button(top3, text="Update", command=lambda: MyUpdate(), bg="slategray", fg="white", font=("Arial", 16)).pack(pady=15)
  
  top3.mainloop()
  
Button(top, text="Update", bg="slategray", fg="white", width=12, font=("Arial", 16), command=lambda: UpdateOperation()).grid(row=1, column=0, pady=20)

# Delete Function
def DeleteOperation():
  from read import Read 
  from delete import Delete 
  
  top4 = Tk()
  top4.geometry("250x200")
  top4.title("Delete Operation")
  
  data = Read()
  id_list = []
  for i in data:
    id_list.append(i[1])
    
  e = StringVar(top4)
  e.set("Select ID")
  OptionMenu(top4, e, *id_list).pack()
  
  def MyDelete():
    Delete(e.get())
    top4.destroy()
  Button(top4, text="Delete", bg="slategray", fg="white", width=12, font=("Arial", 16), command=lambda: MyDelete()).pack(pady=20)
  
  top4.mainloop()
  
Button(top, text="Delete", bg="slategray", fg="white", width=12, font=("Arial", 16), command=lambda: DeleteOperation()).grid(row=1, column=1)

top.mainloop()