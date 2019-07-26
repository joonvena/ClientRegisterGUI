import tkinter as tk
import tkinter.ttk as ttk

class RoomList(ttk.Treeview):
    def __init__(self, master):
        ttk.Treeview.__init__(self, master)
        self["columns"]=("NAME", "ADDRESS", "PHONE")
		
        self.column("#0", width=0, minwidth=0, stretch=tk.YES)
        self.column("NAME", width=50, minwidth=100, stretch=tk.YES)
        self.column("ADDRESS", width=50, minwidth=50, stretch=tk.YES)
        self.column("PHONE", width=50, minwidth=50, stretch=tk.YES)
		
        self.heading("#0", text="ID", anchor=tk.W)
        self.heading("NAME", text="NAME", anchor=tk.W)
        self.heading("ADDRESS", text="ADDRESS", anchor=tk.W)
        self.heading("PHONE", text="PHONE", anchor=tk.W)
        self.bind_events()
		
		
    def bind_events(self):
        self.bind("<Double-Button-1>", self.deleteClient)
		
    def deleteClient(self, event=None):
        for i in self.selection():
            name = self.item(i)['text']
            self.delete(i)