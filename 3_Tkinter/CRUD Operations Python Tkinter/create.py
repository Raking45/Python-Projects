import sqlite3
from tkinter import messagebox 

def Create():
  conn = sqlite3.connect("mydatabase.db")
  cursor = conn.cursor()
  
  # Statement to Create a Table
  cursor.execute("CREATE TABLE IF NOT EXISTS mytable (myname TEXT, id TEXT PRIMARY KEY)")
  conn.close()
  
def InsertData(name, id):
  Create()
  try:
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    
    # Statement to Insert Data
    cursor.execute("INSERT INTO mytable(myname, id) VALUES (?, ?)", (name, id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data Inserted Successfully")
  except sqlite3.Error as e:
    messagebox.showinfo("Error", e)
  finally:
    conn.close()