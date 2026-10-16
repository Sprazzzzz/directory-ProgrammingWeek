import tkinter as tk
from tkinter import messagebox

class TempConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Celsius to Fahrenheit Converter")
        self.root.geometry("320x220")
        
        # ป้ายบอกช่องกรอก
        self.label_instruction = tk.Label(root, text="กรอกอุณหภูมิ (°C):", font=("Arial", 12))
        self.label_instruction.pack(pady=10)
        
        # ช่องรับข้อมูล (Entry)
        self.entry_celsius = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry_celsius.pack(pady=5)
        
        # ปุ่ม Convert
        self.btn_convert = tk.Button(root, text="Convert", font=("Arial", 11), width=10, command=self.convert)
        self.btn_convert.pack(pady=10)
        
        # แสดงผลลัพธ์ (Label)
        self.label_result = tk.Label(root, text="ผลลัพธ์: - °F", font=("Arial", 14, "bold"))
        self.label_result.pack(pady=10)
        
    def convert(self):
        celsius_str = self.entry_celsius.get()
        try:
            # แปลงค่าที่รับเข้ามาเป็นตัวเลขทศนิยม
            celsius = float(celsius_str)
            # คำนวณเป็นฟาเรนไฮต์
            fahrenheit = (celsius * 9/5) + 32
            self.label_result.config(text=f"ผลลัพธ์: {fahrenheit:.2f} °F")
        except ValueError:
            # จัดการกรณีผู้ใช้กรอกไม่ใช่ตัวเลข
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TempConverterApp(root)
    root.mainloop()