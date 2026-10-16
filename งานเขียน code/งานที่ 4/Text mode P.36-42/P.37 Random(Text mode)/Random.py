import random

# สุ่มจำนวนเต็มตั้งแต่ -5 ถึง 5
x = random.randint(-5, 5)

# แสดงค่าที่สุ่มได้
print("Random number =", x)

# ตรวจสอบว่าจำนวนที่สุ่มได้เป็นบวก ลบ หรือศูนย์
if x > 0:
    print("Positive Number")
elif x < 0:
    print("Negative Number")
else:
    print("Zero")