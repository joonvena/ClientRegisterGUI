import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from roomlist import RoomList
import mysql.connector

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.inputfield_value = StringVar()
        self.config(bg="#e83e8c", height=700, width=1000)
        self.title("Reservation System")
        self.canvas = tk.Frame(self, bg="red")
        self.entry = tk.Frame(self, bg="blue")
        self.list = tk.Frame(self, bg="green")
        self.entry.place(relx=0.0, rely=0.0, relwidth=0.3, relheight=0.05)
        self.canvas.place(relx=0.0, rely=0.05, relwidth=0.3, relheight=0.95)
        self.list.place(relx=0.3, rely=0.0, relwidth=0.7, relheight=1)
        self.searchbox = Entry(self.entry, textvariable=self.inputfield_value, bg="#c5e2e8", borderwidth=0, relief=FLAT)
        self.searchbox.insert(0, "Last name of the person")
        self.searchbox.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)
        self.room_list = Listbox(self.canvas) 
        self.room_list.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)
        self.listentries = RoomList(self.list)
        self.listentries.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.bind_events()
		
        self.config = {
           'user': 'root',
           'password': '',
		   'host': '127.0.0.1',
		   'database': 'test',
		   'raise_on_warnings': True
		}
        

    def bind_events(self, event=None):
        self.searchbox.bind("<Return>", self.search)

    def search(self, event):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM clients WHERE last_name LIKE %s", ('%'+self.inputfield_value.get()+'%',))
        print(self.inputfield_value.get())
        self.listentries.delete(*self.listentries.get_children())
        for (client_id, first_name, last_name, address, phone) in cursor:
            self.listentries.insert('', "end", text=client_id, values=(first_name + " " + last_name, address, phone))
        cursor.close()
        cnx.close()

		
		
if __name__ == '__main__':
    mw = MainWindow()
    mw.mainloop()