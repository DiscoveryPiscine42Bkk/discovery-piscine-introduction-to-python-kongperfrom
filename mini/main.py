tasks = []

while True:
    print("\n1. เพิ่ม\n2. แสดง\n3. ลบ\n4. สรุป\n5. ออก")
    c = input("เลือก: ")
    if c == '1':
        tasks.append({"name": input("ชื่องาน: "), "cat": input("ประเภท: ")})
    elif c == '2':
        [print(f"{i+1}. {t['name']} ({t['cat']})") for i, t in enumerate(tasks)] if tasks else print("❌ ไม่มีงาน")
    elif c == '3':
        [print(f"{i+1}. {t['name']}") for i, t in enumerate(tasks)]
        try: tasks.pop(int(input("ลบหมายเลข: "))-1)
        except: print("❌ ผิดพลาด")
    elif c == '4':
        if not tasks: print("❌ ไม่มีงาน")
        else:
            s = {}
            for t in tasks: s[t['cat']] = s.get(t['cat'], 0) + 1
            [print(f"{k}: {v}") for k, v in s.items()]
    elif c == '5':
        break
    else:
        print("❌ เลือก 1-5")