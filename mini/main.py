tasks = []
def add_task():
    global tasks
    print("\n--- เพิ่มงานในฟาร์ม ---")
    name = input("ใส่ชื่องาน: ")
    category = input("ประเภทงาน (เช่น พืช หรือ สัตว์): ")
    tasks.append({"name": name, "category": category})
    print(f"✅ เพิ่มงาน '{name}' ในประเภท '{category}' เรียบร้อยแล้ว")
def show_tasks():
    print("\n--- รายการงานทั้งหมด ---")
    if not tasks:
        print("❌ ยังไม่มีงานในระบบ")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['name']} ({task['category']})")
def delete_task():
    global tasks
    print("\n--- ลบงาน ---")
    show_tasks()
    if not tasks:
        return
    try:
        choice = int(input("เลือกหมายเลขงานที่จะลบ: ")) - 1
        if 0 <= choice < len(tasks):
            removed = tasks.pop(choice)
            print(f"✅ ลบงาน '{removed['name']}' เรียบร้อยแล้ว")
        else:
            print("❌ ไม่พบงานนี้")
    except ValueError:
        print("❌ กรุณาใส่หมายเลขให้ถูกต้อง")
def summarize_tasks():
    print("\n--- สรุปจำนวนงานในแต่ละประเภท ---")
    if not tasks:
        print("❌ ยังไม่มีงานในระบบ")
        return
    summary = {}
    for task in tasks:
        if task['category'] in summary:
            summary[task['category']] += 1
        else:
            summary[task['category']] = 1
    for category, count in summary.items():
        print(f"{category}: {count} งาน")
def main_menu():
    while True:
        print("\n========== เมนูจัดการงานฟาร์ม ==========")
        print("1. เพิ่มงานในฟาร์ม")
        print("2. แสดงรายการงานทั้งหมด")
        print("3. ลบงาน")
        print("4. สรุปจำนวนงานในแต่ละประเภท")
        print("5. ออกจากโปรแกรม")
        print("======================================")
        choice = input("เลือกเมนู (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            summarize_tasks()
        elif choice == '5':
            print("👋 ออกจากโปรแกรมแล้ว")
            break
        else:
            print("❌ กรุณาเลือกเมนูให้ถูกต้อง (1-5)")
if __name__ == "__main__":
    main_menu()
