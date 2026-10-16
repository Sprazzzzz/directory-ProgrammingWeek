# =========================================
# โปรแกรมระบบแคชเชียร์ด้วย OOP
# =========================================


# =========================================
# Product
# =========================================

class Product:

    def __init__(self, name, product_type, price, stock):
        self.name = name
        self.product_type = product_type
        self.price = price
        self.stock = stock

    def show_info(self):
        print(
            f"{self.name} | "
            f"ประเภท: {self.product_type} | "
            f"ราคา: {self.price:.2f} บาท | "
            f"สต็อก: {self.stock} ชิ้น"
        )

    def check_stock(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        self.stock -= amount


# =========================================
# Sale
# =========================================

class Sale:

    def __init__(self, product, amount):
        self.product = product
        self.amount = amount
        self.total = product.price * amount

    def show_sale(self):
        print(
            f"{self.product.name} | "
            f"{self.amount} ชิ้น | "
            f"ชิ้นละ {self.product.price:.2f} บาท | "
            f"รวม {self.total:.2f} บาท"
        )


# =========================================
# Cart
# =========================================

class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, sale):
        self.items.append(sale)

    def get_total(self):

        total = 0

        for sale in self.items:
            total += sale.total

        return total

    def show_cart(self):

        print("\n===== ตะกร้าสินค้า =====")

        if len(self.items) == 0:
            print("ตะกร้าว่าง")
            return

        for sale in self.items:
            sale.show_sale()

        print("-------------------------")

        print(
            f"ยอดรวม: "
            f"{self.get_total():.2f} บาท"
        )


# =========================================
# Discount
# =========================================

class Discount:

    @staticmethod
    def percent(total, percent):

        return total * percent / 100

    @staticmethod
    def fixed(total, amount):

        if amount > total:
            return total

        return amount


# =========================================
# Payment
# =========================================

class Payment:

    # -------------------------------
    # เงินสด
    # -------------------------------

    @staticmethod
    def cash(total):

        paid = float(
            input("ลูกค้าจ่ายเงิน: ")
        )

        if paid < total:

            print("จำนวนเงินไม่เพียงพอ")

            return False

        change = paid - total

        print(
            f"เงินทอน: "
            f"{change:.2f} บาท"
        )

        return True


    # -------------------------------
    # บัตรเครดิต / เดบิต
    # -------------------------------

    @staticmethod
    def card(total):

        print(
            f"ยอดที่ต้องชำระ: "
            f"{total:.2f} บาท"
        )

        print("ชำระด้วยบัตรสำเร็จ")

        return True


    # -------------------------------
    # QR Code
    # -------------------------------

    @staticmethod
    def qr(total):

        print(
            f"ยอดที่ต้องชำระ: "
            f"{total:.2f} บาท"
        )

        print("ชำระด้วย QR Code สำเร็จ")

        return True


# =========================================
# Cashier
# =========================================

class Cashier:

    def __init__(self):

        self.products = []

        self.summary = []

        self.cart = Cart()


    # =====================================
    # เพิ่มสินค้า
    # =====================================

    def add_product(self):

        name = input(
            "ชื่อสินค้า (พิมพ์ stop เพื่อจบ): "
        )

        if name.lower() == "stop":
            return False

        product_type = input(
            "ประเภทสินค้า: "
        )

        price = float(
            input("ราคาสินค้า: ")
        )

        stock = int(
            input("จำนวนสินค้าในสต็อก: ")
        )

        product = Product(
            name,
            product_type,
            price,
            stock
        )

        self.products.append(product)

        print("เพิ่มสินค้าเรียบร้อย")

        return True


    # =====================================
    # แสดงสินค้า
    # =====================================

    def show_products(self):

        print("\n===== รายการสินค้า =====")

        for i, product in enumerate(self.products):

            if product.stock > 0:

                print(f"{i + 1}. ", end="")

                product.show_info()


    # =====================================
    # ค้นหาสินค้า
    # =====================================

    def find_product(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                return product

        return None


    # =====================================
    # ตรวจสอบว่ามีสินค้าเหลือหรือไม่
    # =====================================

    def has_stock(self):

        for product in self.products:

            if product.stock > 0:

                return True

        return False


    # =====================================
    # เพิ่มสินค้าเข้า Cart
    # =====================================

    def sell_product(self):

        self.show_products()

        name = input(
            "\nเลือกสินค้า: "
        )

        product = self.find_product(name)

        if product is None:

            print("ไม่พบสินค้านี้ในระบบ")

            return


        amount = int(
            input("จำนวนที่ต้องการซื้อ: ")
        )


        if amount <= 0:

            print(
                "จำนวนสินค้าต้องมากกว่า 0"
            )

            return


        if not product.check_stock(amount):

            print(
                "สินค้าในสต็อกไม่เพียงพอ"
            )

            return


        # สร้าง Sale

        sale = Sale(
            product,
            amount
        )


        # เพิ่ม Sale ลง Cart

        self.cart.add_item(sale)


        print(
            "\nเพิ่มสินค้าลงตะกร้าเรียบร้อย"
        )


        # แสดง Cart

        self.cart.show_cart()


    # =====================================
    # Checkout
    # =====================================

    def checkout(self):

        if len(self.cart.items) == 0:

            print(
                "\nตะกร้าว่าง "
                "ไม่สามารถ Checkout ได้"
            )

            return


        print("\n================================")
        print("           CHECKOUT")
        print("================================")


        # แสดง Cart

        self.cart.show_cart()


        # ===============================
        # คำนวณยอด
        # ===============================

        total = self.cart.get_total()

        print(
            f"\nยอดรวมก่อนลด: "
            f"{total:.2f} บาท"
        )


        # ===============================
        # ส่วนลด
        # ===============================

        discount_percent = float(
            input("ส่วนลด (%): ")
        )


        if discount_percent < 0:

            discount_percent = 0


        if discount_percent > 100:

            discount_percent = 100


        discount = Discount.percent(
            total,
            discount_percent
        )


        final_total = total - discount


        print(
            f"ส่วนลด: "
            f"{discount:.2f} บาท"
        )


        print(
            f"ยอดที่ต้องจ่าย: "
            f"{final_total:.2f} บาท"
        )


        # ===============================
        # วิธีชำระเงิน
        # ===============================

        print("\n===== วิธีการชำระเงิน =====")

        print("1. เงินสด")
        print("2. บัตรเครดิต/เดบิต")
        print("3. QR Code")


        payment_method = input(
            "เลือกวิธีชำระเงิน: "
        )


        payment_success = False


        # ===============================
        # เงินสด
        # ===============================

        if payment_method == "1":

            payment_success = Payment.cash(
                final_total
            )


        # ===============================
        # บัตร
        # ===============================

        elif payment_method == "2":

            payment_success = Payment.card(
                final_total
            )


        # ===============================
        # QR
        # ===============================

        elif payment_method == "3":

            payment_success = Payment.qr(
                final_total
            )


        # ===============================
        # วิธีไม่ถูกต้อง
        # ===============================

        else:

            print(
                "เลือกวิธีชำระเงินไม่ถูกต้อง"
            )

            return


        # ===============================
        # ตรวจสอบการชำระเงิน
        # ===============================

        if not payment_success:

            return


        # ===============================
        # ลด Stock
        # ===============================

        for sale in self.cart.items:

            sale.product.reduce_stock(
                sale.amount
            )


            # เพิ่มลง Summary

            self.summary.append(sale)


        # ===============================
        # ล้าง Cart
        # ===============================

        self.cart.items = []


        print("\nชำระเงินสำเร็จ")

        print("ขอบคุณที่ใช้บริการ")


    # =====================================
    # Summary
    # =====================================

    def show_summary(self):

        print(
            "\n========== สรุปการขาย =========="
        )


        if len(self.summary) == 0:

            print("ยังไม่มีรายการขาย")

            return


        grand_total = 0


        for sale in self.summary:

            sale.show_sale()

            grand_total += sale.total


        print("--------------------------------")


        print(
            f"ยอดขายรวมทั้งหมด: "
            f"{grand_total:.2f} บาท"
        )


# =========================================
# Main Program
# =========================================

cashier = Cashier()


print("================================")
print("        ระบบแคชเชียร์")
print("================================")


# =========================================
# เพิ่มข้อมูลสินค้า
# =========================================

while True:

    print("\n--- เพิ่มข้อมูลสินค้า ---")

    if not cashier.add_product():

        break


print(
    "\nบันทึกข้อมูลสินค้าเรียบร้อยแล้ว"
)


# =========================================
# เลือกซื้อสินค้า
# =========================================

while cashier.has_stock():

    cashier.sell_product()


    choice = input(
        "\nต้องการเลือกสินค้าเพิ่มหรือไม่ (y/n): "
    )


    if choice.lower() != "y":

        break


# =========================================
# Checkout
# =========================================

cashier.checkout()


# =========================================
# แสดง Summary
# =========================================

cashier.show_summary()


print(
    "\nจบการทำงานของโปรแกรม"
)