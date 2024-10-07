# reducer.py
import sys

current_district = None
current_income_total = 0
current_count = 0

# อ่านข้อมูลจาก stdin
for line in sys.stdin:
    # ลบช่องว่างด้านหน้าและหลังบรรทัด
    line = line.strip()

    # แยกข้อมูลเป็น district_id และ personal_income โดยใช้แท็บเป็นตัวคั่น
    district_id, personal_income = line.split('\t')

    try:
        # แปลง personal_income เป็นจำนวนเต็ม
        personal_income = int(personal_income)
    except ValueError:
        continue

    # ถ้าเจอ district เดิม ให้รวมรายได้เพิ่มขึ้น
    if current_district == district_id:
        current_income_total += personal_income
        current_count += 1
    else:
        # แสดงผลลัพธ์ของ district ก่อนหน้า
        if current_district:
            # คำนวณค่าเฉลี่ยรายได้
            print "%s\t%s" % (current_district, current_income_total / current_count)

        # รีเซ็ตค่าเมื่อเจอ district ใหม่
        current_district = district_id
        current_income_total = personal_income
        current_count = 1

# แสดงผลลัพธ์ของ district สุดท้าย
if current_district == district_id:
    print "%s\t%s" % (current_district, current_income_total / current_count)
