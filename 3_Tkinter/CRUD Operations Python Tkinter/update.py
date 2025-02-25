from tkinter import messagebox 
import sqlite3

def Update(name, id):
  try:
    conn = sqlite3.connect("mydatabase.db")
    c = conn.cursor()
    
    # Statement to Update a Row
    c.execute("UPDATE mytable SET myname=? WHERE id=?", (name, id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data Updated Successfully")
  except sqlite3.Error as e:
    messagebox.showinfo("Error", e)
  finally:
    conn.close()