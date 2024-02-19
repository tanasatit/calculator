from math import *
import tkinter as tk
from tkinter import ttk


class Calculator_UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ans = None
        self.title("Calculator")
        self.num = None
        self.op = None
        self.value = tk.StringVar()
        self.init_component()
        self.value.set('')
        self.history = []

    def init_component(self):
        display = tk.Label(self, textvariable=self.value, fg='yellow', bg='black', anchor=tk.E, font=("Arial", 18),
                           height=4)
        display.pack(side=tk.TOP, fill=tk.BOTH)
        frame_num = self.numeric_keys()
        frame_num.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        frame_op = self.operator_keys()
        frame_op.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def numeric_keys(self) -> tk.Frame:
        """Create a frame containing buttons for the numeric keys."""
        self.keys = list('789456123 0.')
        option = {'sticky': tk.NSEW, 'padx': 3, 'pady': 3}
        frame1 = tk.Frame()
        for i, key in enumerate(self.keys):
            row = i // 3
            column = i % 3
            (tk.Button(frame1, text=key, command=lambda x=str(key): self.show_display(x))
             .grid(row=row, column=column, **option))
            frame1.grid_rowconfigure(row, weight=1)
            frame1.grid_columnconfigure(column, weight=1)
        return frame1

    def operator_keys(self) -> tk.Frame:
        o2 = "( CLR ) DEL ^ mod / sqrt * log10 - HTR + ="
        self.oper_pad = o2.split()
        option = {'sticky': tk.NSEW, 'padx': 3, 'pady': 3}
        frame2 = tk.Frame()
        for i, key in enumerate(self.oper_pad):
            row = i // 2
            column = i % 2
            (tk.Button(frame2, text=key, command=lambda x=str(key): self.show_display(x), fg='red')
             .grid(row=row, column=column, **option))
            frame2.grid_rowconfigure(row, weight=1)
            frame2.grid_columnconfigure(column, weight=1)
        return frame2

    def show_display(self, key):
        value = self.value.get()
        if key == '=':
            try:
                self.ans = eval(value)
                self.history.append(f"{value} = {self.ans}")
                self.value.set(self.ans)
            except:
                self.value.set('error')

        elif key == 'DEL':
            if value[-5:] == 'sqrt(':
                self.value.set(value[:-5])
            elif value[-6:] == 'log10(':
                self.value.set(value[:-6])
            else:
                self.value.set((self.value.get())[:-1])
        elif key == 'CLR':
            self.value.set('')
        elif key == 'HTR':
            self.show_history()
        elif key == 'mod':
            self.value.set(value + '%')
        elif key == 'sqrt':
            if value == '':
                self.value.set(value + 'sqrt(')
            elif value[-1] in self.keys:
                self.value.set('sqrt(' + value)
            else:
                self.value.set(value + 'sqrt(')
        elif key == 'log10':
            if value == '':
                self.value.set(value + 'log10(')
            elif value[-1] in self.keys:
                self.value.set('log10(' + value)
            else:
                self.value.set(value + 'log10(')
        elif key == '^':
            self.value.set(value + '**')
        else:
            self.value.set(value + key)

    def show_history(self):
        history_window = tk.Toplevel(self)
        history_window.title("History")
        history_text = tk.Text(history_window, height=20, width=40)
        history_text.pack()
        for entry in self.history:
            history_text.insert(tk.END, entry + "\n")
            history_text.tag_add('clickable', '1.0', 'end')
            history_text.tag_bind('clickable', '<Button-1>', self.update_history)
        history_text.configure(state="disabled")

    def update_history(self, event):
        text = event.widget
        index = text.index(tk.CURRENT)
        click = text.get(index + 'linestart', index + 'lineend')
        expression = click.split('=')[0].strip()
        self.value.set(expression)

    def run(self):
        self.mainloop()



