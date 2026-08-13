students =[]

def show_menu():
    print("============== Student Management System ==============")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("========================================================")

def add_student():
    student_id = int(input("Student ID: ").strip())

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists")
            return

    student = {}

    student["id"] = student_id
    student["name"] = input("Student Name: ").strip()
    student["department"] = input("Student Department: ").strip()
    student["gpa"] = float(input("Student GPA: ").strip())

    students.append(student)

    print("Student Add Successfully")

def view_students():
    if not students:
        print("No Students Found")
        return

    print("\n============== Students ==============")
    for student in students:
        print("----------------------------")
        print("ID", student["id"])
        print("Name", student["name"])
        print("Department", student["department"])
        print("GPA", student["gpa"])

def search_student():
    if not students:
        print("No Students Found")
        return

    students.sort(key=lambda student: student["id"])
    
    student_id = int(input("Enter Student ID: ").strip())

    left = 0
    right = len(students) - 1

    while left <= right:
        middle = (left + right) // 2

        if students[middle]["id"] == student_id :
            student = students[middle]

            print("\nStudent Found")
            print("ID", student["id"])
            print("Name", student["name"])
            print("Department", student["department"])
            print("GPA", student["gpa"])
            print("----------------------------")

            return
        
        elif students[middle]["id"] < student_id:
            left = middle + 1
        else:    
            right = middle - 1

    print("Student Not Found") 

def update_student():
    if not students:
        print("No Students Found")
        return
    
    student_id = int(input("Enter Student ID: ").strip())

    for student in students:
        if student["id"] == student_id:

            student["id"] = int(input("New Student ID: ").strip())
            student["name"] = input("New Student Name: ").strip()
            student["department"] = input("New Student Department: ").strip()
            student["gpa"] = float(input("New Student GPA: ").strip())

            print("Student updated Successfully")

            return
        
    print("Student Not Found")

def delete_student():
    if not students:
        print("No Students Found")
        return
        
    student_id = int(input("Enter Student ID: ").strip())
    
    for student in students:
        if student["id"] == student_id:

            students.remove(student)

            print("Student deleted Successfully")

            return
    
    print("Student Not Found")


def main():
    while True:
        show_menu()

        choice = input("Enter Your Choice: ").strip()

        match choice:
            case "1":
                add_student()
            case "2":
                view_students()
            case "3":
                search_student()
            case "4":
                update_student()
            case "5":
                delete_student()
            case "6":
                print("Exit")
                break
            case "_":                                  
                print("Invalid Choice")
                   
main()