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

def get_int(message):
    while True:
        try:
            return int(input(message).strip())
        except ValueError:
            print("Please enter a valid number")

def validation_id(message):
    while True:
        student_id = get_int(message)

        if student_id > 0:
            return student_id
        else:
            print("Student ID Must be grater 0")
    
def get_float(message):
    while True:
        try:
            return float(input(message).strip())
        except ValueError:
            print("Please enter a valid number")

def get_gpa():
    while True:
        gpa = get_float("Student GPA: ")       

        if 0 <= gpa <= 4:
            return gpa
        else:
            print("GPA Must be between 0 and 4")     

def add_student():
    student_id = validation_id("Student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists")
            return

    student = {}

    student["id"] = student_id
    student["name"] = input("Student Name: ").strip()
    student["department"] = input("Student Department: ").strip()
    student["gpa"] = get_gpa()

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
    
    student_id = validation_id("Enter Student ID: ")

    left = 0
    right = len(students) - 1

    while left <= right:
        middle = (left + right) // 2

        if students[middle]["id"] == student_id :
            student = students[middle]

            print("\n============== Student Found ==============")
            print("----------------------------")
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
    
    student_id = validation_id("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            new_id = validation_id("New Student ID: ")

            for other_student in students:
                if other_student["id"] == new_id and other_student is not student:
                    print("Student ID already exists")
                    return

            student["id"] = new_id
            student["name"] = input("New Student Name: ").strip()
            student["department"] = input("New Student Department: ").strip()
            student["gpa"] = get_gpa()

            print("Student updated Successfully")

            return
        
    print("Student Not Found")

def delete_student():
    if not students:
        print("No Students Found")
        return
        
    student_id = validation_id("Enter Student ID: ")
    
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
            case _:                                  
                print("Invalid Choice")
                   
main()