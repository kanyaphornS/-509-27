def calculate_grade():
    try:
        score = int(input("กรุณากรอกคะแนน (จำนวนเต็ม): "))
        
        if score >= 80:
            print("เกรดของคุณคือ A")
        elif score >= 70:
            print("เกรดของคุณคือ B")
        elif score >= 60:
            print("เกรดของคุณคือ C")
        elif score >= 50:
            print("เกรดของคุณคือ D")
        else:
            print("เกรดของคุณคือ F")
    
    except ValueError:
        print("กรุณากรอกคะแนนเป็นจำนวนเต็มที่ถูกต้อง")

calculate_grade()
