import sqlite3 as sql
from tkinter import *
from tkinter import messagebox

try:
    conn = sql.connect('notes.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE notes (data text, notes_title text, notes text)''')

except:
    print("Connection error")

def add__note():
    today = date_entry.get()
    notes_title = notes_title_entry.get()
    notes = notes_entry.get("1.0", END)

    if (len(today) == 0) & (len(notes_title) == 0) & (len(notes) <=1):
        messagebox.showerror(message="Please enter notes as per required!")
    else:
        cur.execute(f"ISERT INTO notes VALUE ({today},{notes_title},{notes})")
        messagebox.showinfo(message="Note Added Successfully")
        conn.commit()

def display_note():
    date = date_entry.get()
    notes_title = notes_title_entry.get()

    if (len(date) <= 0) & (len(notes_title) <= 0):
        sql_statement = "SELECT * FROM notes"

    elif (len(date) <= 0) & (len(notes_title) <= 0):
        sql_statement = f"SELECT * FROM notes where notes_title = {date}"

    else:
        sql_statement = f"SELECT * FROM notes where date = {date} notes_title = {notes_title}"

    cur.execute(sql_statement)

    row = cur.fetchall()

    if len(row) <= 0:
        messagebox.showerror(message = "Could not found")
    else:
        for i in row:
            messagebox.showinfo(message = "Date: " + i[0] + "\nTitle:" + i[1] + "\nNotes:" + i[2])

def delete_note():
    date = date_entry.get()
    notes_title = notes_title_entry.get()
    choice = messagebox.askquestion(message="Do you want to delete all notes?")

    if choice == 'yes':
        sql_statement = "DELETE FROM notes"

    else:
        if (len(date) <=0) & (len(notes_title) <=0):
            messagebox.showerror(message="Invalid Inputs. Enter correct details")
            return
        else:
            sql = f"SELECT * FROM notes WHERE date = {date}  and notes_title = {notes_title}"

            cur.execute(sql)
            messagebox.showinfo(message="Notes Delected")
            conn.commit()
        
def update_note():
    today = date_entry.get()
    notes_title = notes_title_entry.get()
    notes = notes_entry.get("1.0", END)
    if (len(today) <0) & (len(notes_title) <=0) (len(notes) <=1):
        messagebox.showerror(message="Invalid Inputs. Enter correct details")
    else:
        sql_statement = "UPDATE notes SET notes = {notes} WHERE date = {today} and notes_title = {notes_title}"

        cur.execute(sql_statement)
        messagebox.showinfo(message="Note Updated Successfully")
        conn.commit()

root = Tk()
root.geometry("500x300")
root.title("Sticky Notes")

title_lbl = Label(root, text="Sticky Notes").pack()

date_label = Label(root, text="Date:").place(x=10, y=20)
date_entry = Entry(root, width=20)
date_entry.place(x=50, y=20)

notes_title_label = Label(root, text="Notes Title:").place(x=10,y=50)
notes_title_entry = Entry(root, width=30)
notes_title_entry.place(x=80,y=50)

notes_label = Label(root, text="Notes:").place(x=10,y=90)
notes_entry = Entry(root, width=50)
notes_entry.place(x=60, y=90)

button1 = Button(root, text="Add Note", bg='Turquoise', fg='Red', command=add__note).place(x=10, y=190)
button2 = Button(root, text="View Note", bg='Turquoise', fg='Red', command=display_note).place(x=110, y=190)
button3 = Button(root, text="Delete Note", bg='Turquoise', fg='Red', command=delete_note).place(x=210, y=190)
button4 = Button(root, text="Update Note", bg='Turquoise', fg='Red', command=update_note).place(x=310, y=190)

root.mainloop()
conn.close()