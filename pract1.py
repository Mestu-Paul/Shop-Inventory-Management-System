import tkinter as tk

class EntryForm(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entries = []
        for i in range(5):
            entry = tk.Entry(self)
            entry.grid(row=i, column=0)
            entry.bind("<Return>", self.focus_next_widget)
            self.entries.append(entry)

    def focus_next_widget(self, event):
        print(event)
        event.widget.tk_focusNext().focus()

form = EntryForm()
form.mainloop()
