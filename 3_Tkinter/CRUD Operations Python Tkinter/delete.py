import sqlite3 
from tkinter import messagebox 

def Delete(id):
  try:
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    
    # Statement to Delete a Row
    cursor.execute("DELETE FROM mytable WHERE id=?", (id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data Deleted Successfully")
  except sqlite3.Error as e:
    messagebox.showinfo("Error", e)
  finally:
    conn.close()