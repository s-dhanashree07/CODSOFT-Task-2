import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        self.display = tk.Entry(master, width=30, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            "(", "0", ")", "/",
            ".", "DEL", "C", "=" 
        ]

        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.handle_click(x)
            btn = tk.Button(master, text=button, width=5, height=2, font=("Arial", 16), command=command)
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def handle_click(self, button):
        if button == "=":
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        elif button == "C": 
            self.display.delete(0, tk.END)
            self.display.delete(0, tk.END)
        elif button == "DEL": 
            self.display.delete(len(self.display.get())-1, tk.END)
        else:
            self.display.insert(tk.END, button)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
