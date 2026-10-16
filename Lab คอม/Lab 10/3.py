import tkinter as tk
from tkinter import messagebox

class TextAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Text Analyzer")
        self.root.geometry("450x380")
        
        # 1. ช่องรับข้อความหลัก
        tk.Label(root, text="พิมพ์ข้อความ (Text):", font=("Arial", 11)).pack(anchor="w", padx=30, pady=(15, 0))
        self.entry_text = tk.Entry(root, font=("Arial", 12), width=35)
        self.entry_text.pack(padx=30, pady=5)
        
        # 2. ช่องรับตัวอักษรสำหรับค้นหา/นับ
        tk.Label(root, text="ตัวอักษรที่ต้องการนับ (Character):", font=("Arial", 11)).pack(anchor="w", padx=30, pady=(10, 0))
        self.entry_char = tk.Entry(root, font=("Arial", 12), width=10)
        self.entry_char.pack(anchor="w", padx=30, pady=5)
        
        # 3, 4, 5. ปุ่มกดการทำงานต่างๆ
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        
        self.btn_count_char = tk.Button(btn_frame, text="Count Character", font=("Arial", 10), width=15, command=self.count_character)
        self.btn_count_char.grid(row=0, column=0, padx=5, pady=5)
        
        self.btn_count_vowels = tk.Button(btn_frame, text="Count Vowels", font=("Arial", 10), width=15, command=self.count_vowels)
        self.btn_count_vowels.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_palindrome = tk.Button(btn_frame, text="Check Palindrome", font=("Arial", 10), width=32, command=self.check_palindrome)
        self.btn_palindrome.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        # 6. แสดงผลลัพธ์ผ่าน Label
        tk.Label(root, text="ผลลัพธ์ (Result):", font=("Arial", 11, "bold")).pack(anchor="w", padx=30, pady=(10, 0))
        self.label_result = tk.Label(root, text="-", font=("Arial", 12), fg="blue", wraplength=380, justify="left")
        self.label_result.pack(anchor="w", padx=30, pady=5)

    def count_character(self):
        text = self.entry_text.get()
        char = self.entry_char.get()
        
        if not text:
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกข้อความหลักก่อนครับ")
            return
        if len(char) != 1:
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกตัวอักษรสำหรับนับเพียง 1 ตัวอักษร")
            return
            
        # นับจำนวนตัวอักษร (ไม่สนตัวพิมพ์เล็ก/ใหญ่ ใช้ .lower() หรือนับตรงๆ ตามต้องการ)
        count = text.lower().count(char.lower())
        self.label_result.config(text=f"ตัวอักษร '{char}' ปรากฏในข้อความทั้งหมด {count} ครั้ง")

    def count_vowels(self):
        text = self.entry_text.get()
        if not text:
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกข้อความก่อนครับ")
            return
            
        vowels = "aeiouAEIOU"
        count = sum(1 for char in text if char in vowels)
        self.label_result.config(text=f"จำนวนสระ (a, e, i, o, u) ทั้งหมด: {count} ตัว")

    def check_palindrome(self):
        text = self.entry_text.get()
        if not text:
            messagebox.showwarning("แจ้งเตือน", "กรุณากรอกข้อความก่อนครับ")
            return
            
        # กรองเอาเฉพาะตัวอักษรและตัวเลข และแปลงเป็นตัวพิมพ์เล็กเพื่อเทียบความถูกต้อง
        cleaned_text = "".join(ch.lower() for ch in text if ch.isalnum())
        
        if not cleaned_text:
            self.label_result.config(text="ข้อความนี้ไม่สามารถตรวจสอบ Palindrome ได้")
            return
            
        is_pal = cleaned_text == cleaned_text[::-1]
        if is_pal:
            self.label_result.config(text=f"'{text}' เป็น Palindrome (อ่านกลับหลังได้)")
        else:
            self.label_result.config(text=f"'{text}' ไม่เป็น Palindrome")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextAnalyzerApp(root)
    root.mainloop()