def check_credit_card():
    try:
        income = float(input("กรุณากรอกรายได้ต่อเดือนของคุณ (บาท): "))
        
        if income < 15000:
            print("ขออภัย คุณไม่สามารถทำบัตรเครดิตได้")
        elif income < 70000:
            print("คุณสามารถทำบัตรเครดิตประเภท 'บัตรเงิน' ได้")
        elif income < 100000:
            print("คุณสามารถทำบัตรเครดิตประเภท 'บัตรทอง' ได้")
        else:
            print("คุณสามารถทำบัตรเครดิตประเภท 'Platinum' ได้")
    
    except ValueError:
        print("กรุณากรอกตัวเลขที่ถูกต้อง")

check_credit_card()
