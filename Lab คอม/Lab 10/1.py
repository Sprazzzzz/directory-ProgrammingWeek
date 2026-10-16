import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")
        self.root.geometry("300x200")
        
        self.count = 0
        
        # แสดงตัวเลข
        self.label_num = tk.Label(root, text="0", font=("Arial", 30))
        self.label_num.pack(pady=20)
        
        # ปุ่มควบคุม
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        
        self.btn_inc = tk.Button(btn_frame, text="Increase", width=8, command=self.increase)
        self.btn_inc.grid(row=0, column=0, padx=5)
        
        self.btn_dec = tk.Button(btn_frame, text="Decrease", width=8, command=self.decrease)
        self.btn_dec.grid(row=0, column=1, padx=5)
        
        self.btn_reset = tk.Button(btn_frame, text="Reset", width=8, command=self.reset)
        self.btn_reset.grid(row=0, column=2, padx=5)
        
    def increase(self):
        self.count += 1
        self.label_num.config(text=str(self.count))
        
    def decrease(self):
        self.count -= 1
        self.label_num.config(text=str(self.count))
        
    def reset(self):
        self.count = 0
        self.label_num.config(text=str(self.count))

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()