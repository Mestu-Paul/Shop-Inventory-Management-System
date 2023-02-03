import tkinter as tk
v = {'1':2,'2':2}
if '5' in v.keys:
    print('yes')
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
