
balance = 10000 #ยอดเงินคงเหลือในบัญชี
money = 5000    #จำนวนเงินฝากหรือถอน


#ฟังก์ชันฝากเงิน
def deposit_money(balance, money):
    if money <= 0:
        print("จำนวนเงินฝากต้องมากกว่า 0")
        return balance
    balance += money
    print(f"คุณได้ฝากเงิน {money} บาท เข้าบัญชีของคุณแล้ว")
    print(f"ยอดเงินคงเหลือในบัญชีของคุณคือ {balance} บาท")
    return balance

#ฟังก์ชันถอนเงิน
def withdraw_money(balance, money):
    if money <= 0:
        print("จำนวนเงินถอนต้องมากกว่า 0")
        return balance
    if money > balance:
        print("ยอดเงินในบัญชีไม่เพียงพอ")
        return balance
    balance -= money    
    print(f"คุณได้ถอนเงิน {money} บาท จากบัญชีของคุณแล้ว")
    print(f"ยอดเงินคงเหลือในบัญชีของคุณคือ {balance} บาท")
    return balance

withdraw_money(balance, money)

