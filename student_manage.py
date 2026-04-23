students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        student = {"roll": roll, "name": name, "marks": marks}
        students.append(student)

        print("Student Added!")
        
    elif choice == 2:
        if students:
            for s in students:
                print(s)
        else:
            print("No records found")

    elif choice == 3:
        r = int(input("Enter Roll No to search: "))

        found = False
        for s in students:
            if s["roll"] == r:
                print("Found:", s)
                found = True
                break

        if not found:
            print("Student not found")


    elif choice == 4:
        r = int(input("Enter Roll No to update: "))

        found = False
        for s in students:
            if s["roll"] == r:
                print("Current Data:", s)

                s["name"] = input("Enter new name: ")
                s["marks"] = int(input("Enter new marks: "))

                print("Student Updated!")
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == 5:
        r = int(input("Enter Roll No to delete: "))

        found = False
        for s in students:
            if s["roll"] == r:
                students.remove(s)
                print("Student Deleted!")
                found = True
                break

        if not found:
            print("Student not found")

    elif choice == 6:
        break

    else:
        print("Invalid choice")