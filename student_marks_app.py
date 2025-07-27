students = {}
while True:
    print("""1. Add Student\n
    2. View Marks\n
    3. Update Marks\n
    4. Delete Student\n
    5. Exit""")
    choice=input("enter your choice:")
    if choice=="1":
        name=input("enter student name:")
        marks=int(input("enter student marks:"))
        students[name]=marks
    elif choice=="2":
        if students=={}:
            print("No students added yet.")
        else:
            for x,y in students.items():
                print(f"{x}:{y}")
    elif choice=="3":
        a=input("Enter student name to update: ")
        if a in students:
            m=int(input("Enter new marks: "))
            students[a]=m
        else:
            print("Student not found.")
    elif choice=="4":
        a=input("Enter student name to delete: ")
        if a in students:
            del students[a]
            print("Student deleted.")
        else:
            print("Student not found.")
