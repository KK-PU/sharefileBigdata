# mapper.py
import sys

# อ่านข้อมูลจาก input
for line in sys.stdin:
    # ลบช่องว่างด้านหน้าและหลังบรรทัด
    line = line.strip()
    
    # แยกข้อมูลตามเครื่องหมายจุลภาค
    person_id, district_id, personal_income = line.split(',')

    # ส่งออก district_id และ personal_income (ใช้แท็บเป็นตัวคั่น)
    print "%s\t%s" % (district_id, personal_income)
