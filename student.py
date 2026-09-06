import json as js
from datetime import datetime

student = {}

# ===== LOAD STUDENT DATA ===== #
try:
    with open("students.json", "r") as file:
        student = js.load(file)

except FileNotFoundError:
    student = {}


# ===== GENERATE STUDENT ID ===== #
if student:
    student_ids = []

    for i in student.keys():
        i = int(i)
        student_ids.append(i)

    student_id = max(student_ids) + 1

else:
    student_id = 100


# ===== MAIN PROGRAM ===== #
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Average Marks")
    print("7. Top Student")
    print("8. Exit")

    try:
        choice = int(input("\nEnter Your Choice: "))

    except ValueError:
        print("Please enter a valid choice.")
        continue


    # ===== ADD STUDENT ===== #
    if choice == 1:

        print("\n===== ADD STUDENT =====")

        # Student Name
        while True:

            student_name = input("Enter Student Name: ")

            if student_name.strip():
                break

            else:
                print("Name cannot be empty.")


        # Student Age
        while True:

            try:
                student_age = int(input("Enter Student Age: "))

                if student_age > 0:
                    break

                else:
                    print("Age must be greater than 0.")

            except ValueError:
                print("Enter a valid age.")


        # Student Course
        while True:

            student_course = input("Enter Student Course: ")

            if student_course.strip():
                break

            else:
                print("Course cannot be empty.")


        # Student Marks
        while True:

            try:
                student_marks = int(input("Enter Student Marks: "))

                if 0 <= student_marks <= 100:
                    break

                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Enter valid marks.")


        # Store Student
        student[str(student_id)] = {

            "student_name": student_name,
            "student_age": student_age,
            "student_course": student_course,
            "student_marks": student_marks,
            "date": datetime.now().strftime("%d-%m-%Y")
        }


        # Save Data
        with open("students.json", "w") as file:
            js.dump(student, file, indent=4)


        print("\nStudent Added Successfully!")
        print("Student ID:", student_id)

        student_id += 1


    # ===== VIEW STUDENTS ===== #
    elif choice == 2:

        print("\n===== VIEW STUDENTS =====")

        print("A. View All Students")
        print("B. View Particular Student")

        view_choice = input("Enter Your Choice: ").upper()


        # ----- ALL STUDENTS ----- #
        if view_choice == "A":

            print("\n===== ALL STUDENTS =====")

            if not student:

                print("No Student Found.")

            else:

                for std_id, std_data in student.items():

                    print("\nStudent ID:", std_id)
                    print("Student Name:", std_data["student_name"])
                    print("Student Age:", std_data["student_age"])
                    print("Student Course:", std_data["student_course"])
                    print("Student Marks:", std_data["student_marks"])
                    print("Date:", std_data["date"])
                    print("----------------------------")


        # ----- PARTICULAR STUDENT ----- #
        elif view_choice == "B":

            print("\n===== PARTICULAR STUDENT =====")

            selected_student = input("Enter Student ID: ")

            if selected_student in student:

                selected_data = student[selected_student]

                print("\nStudent ID:", selected_student)
                print("Student Name:", selected_data["student_name"])
                print("Student Age:", selected_data["student_age"])
                print("Student Course:", selected_data["student_course"])
                print("Student Marks:", selected_data["student_marks"])
                print("Date:", selected_data["date"])
                print("----------------------------")

            else:

                print("Student Not Found.")


        else:

            print("Invalid Choice.")


    # ===== SEARCH STUDENT ===== #
    elif choice == 3:

        print("\n===== SEARCH STUDENT =====")

        search_student = input("Enter Student Name: ").lower()

        found = False

        for std_id, std_data in student.items():

            if std_data["student_name"].lower() == search_student:

                print("\nStudent ID:", std_id)
                print("Student Name:", std_data["student_name"])
                print("Student Age:", std_data["student_age"])
                print("Student Course:", std_data["student_course"])
                print("Student Marks:", std_data["student_marks"])
                print("Date:", std_data["date"])
                print("----------------------------")

                found = True


        if found == False:

            print("No Student Found in this Student Management System.")


    # ===== UPDATE STUDENT ===== #
    elif choice == 4:

        print("\n===== UPDATE STUDENT =====")

        update = input("Enter the Student ID: ")


        if update in student:

            print("\nCurrent Student Details:")
            print(student[update])

            print("\nWhat You Want To Update?")
            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Course")
            print("4. Update Marks")
            print("5. Cancel")


            try:
                update_choice = int(input("Enter Your Choice: "))

            except ValueError:

                print("Please enter a valid choice.")
                continue


            # ----- UPDATE NAME ----- #
            if update_choice == 1:

                new_name = input("Enter New Student Name: ")

                student[update]["student_name"] = new_name

                print("Student Name Updated Successfully!")


            # ----- UPDATE AGE ----- #
            elif update_choice == 2:

                while True:

                    try:

                        new_age = int(input("Enter New Student Age: "))

                        if new_age > 0:
                            break

                        else:
                            print("Age must be greater than 0.")

                    except ValueError:

                        print("Enter a valid age.")


                student[update]["student_age"] = new_age

                print("Student Age Updated Successfully!")


            # ----- UPDATE COURSE ----- #
            elif update_choice == 3:

                new_course = input("Enter New Student Course: ")

                student[update]["student_course"] = new_course

                print("Student Course Updated Successfully!")


            # ----- UPDATE MARKS ----- #
            elif update_choice == 4:

                while True:

                    try:

                        new_marks = int(input("Enter New Student Marks: "))

                        if 0 <= new_marks <= 100:
                            break

                        else:
                            print("Marks must be between 0 and 100.")

                    except ValueError:

                        print("Enter valid marks.")


                student[update]["student_marks"] = new_marks

                print("Student Marks Updated Successfully!")


            # ----- CANCEL ----- #
            elif update_choice == 5:

                print("Student Update Cancelled.")


            else:

                print("Invalid Choice.")


            # Save Updated Data
            with open("students.json", "w") as file:
                js.dump(student, file, indent=4)


        else:

            print("Student Not Found.")


    # ===== DELETE STUDENT ===== #
    elif choice == 5:

        print("\n===== DELETE STUDENT =====")

        delete_id = input("Enter Student ID: ")


        if delete_id in student:

            delete_choice = input(
                "Are you sure you want to delete this student? (YES/NO): "
            ).upper()


            if delete_choice == "YES":

                del student[delete_id]


                with open("students.json", "w") as file:
                    js.dump(student, file, indent=4)


                print("Student Deleted Successfully!")


            elif delete_choice == "NO":

                print("Student Deletion Cancelled.")


            else:

                print("Invalid Choice.")


        else:

            print("Student Not Found.")


    # ===== AVERAGE MARKS ===== #
    elif choice == 6:

        print("\n===== AVERAGE MARKS =====")


        if not student:

            print("No Student Found.")

        else:

            total_marks = 0

            for std_id, std_data in student.items():

                total_marks += std_data["student_marks"]


            average_marks = total_marks / len(student)

            print("Average Marks:", average_marks)


    # ===== TOP STUDENT ===== #
    elif choice == 7:

        print("\n===== TOP STUDENT =====")


        if not student:

            print("No Student Found.")

        else:

            top_student_id = None
            top_marks = -1


            for std_id, std_data in student.items():

                if std_data["student_marks"] > top_marks:

                    top_marks = std_data["student_marks"]
                    top_student_id = std_id


            top_student = student[top_student_id]


            print("Student ID:", top_student_id)
            print("Student Name:", top_student["student_name"])
            print("Student Age:", top_student["student_age"])
            print("Student Course:", top_student["student_course"])
            print("Student Marks:", top_student["student_marks"])
            print("Date:", top_student["date"])


    # ===== EXIT ===== #
    elif choice == 8:

        print("\nThank you for using Student Management System!")
        break


    # ===== INVALID CHOICE ===== #
    else:

        print("Please enter a choice between 1 and 8.")