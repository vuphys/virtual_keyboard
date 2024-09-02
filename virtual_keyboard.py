import tkinter as tk

class VirtualKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Keyboard")

        self.entry = tk.Entry(root, width=50, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=15)

        # Define the keys to be included in the virtual keyboard
        self.keys = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['Clear', 'Backspace', 'Delete', 'Quit']
        ]

        self.create_keyboard()

    def create_keyboard(self):
        row_val = 1
        for row in self.keys:
            col_val = 0
            for key in row:
                button = tk.Button(self.root, text=key, width=5, height=2, font=('Arial', 16),
                                   command=lambda k=key: self.on_key_press(k))
                button.grid(row=row_val, column=col_val)
                col_val += 1
            row_val += 1

    def on_key_press(self, key):
        if key == 'Clear':
            self.entry.delete(0, tk.END)  # Clear the entry field
        elif key == 'Backspace':
            current_text = self.entry.get()
            self.entry.delete(len(current_text) - 1, tk.END)  # Delete the last character
        elif key == 'Delete':
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)  # Clear the entry field
        elif key == 'Quit':
            self.root.quit()  # Exit the application
        elif key == '=':
            try:
                # Safely evaluate the expression in the entry
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualKeyboard(root)
    root.mainloop()