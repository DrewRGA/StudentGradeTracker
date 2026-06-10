menu = True
class_roster = []

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}.")

    def update_grade(self, new_grade):
        self.grade = new_grade

def add_student():
    name = str(input("Enter their name: "))
    for student in class_roster:
            if student.name == name:
                print(f"{student.name} is already in the class.\n")
                return

    age = int(input("Enter their age: "))
    grade = int(input("Enter their current grade average: "))
    new_student = Student(name, age, grade)
    class_roster.append(new_student)
    print("\n")

def view_student():
    if not class_roster:
        print("There are no students in the class.")
    else:
        for student in class_roster:
            student.display()

    print("\n")

def search_students():
    if not class_roster:
        print("There are no students in the class.\n")
        return

    user_search = str(input("Please type the name of the student you would like to search: \n")).lower()

    for student in class_roster:
            if student.name == user_search:
                print(f"{student.name} is doing well. Their grade is: {student.grade}% \n")
                return

    print("That student does not exist.")
    return

def grade_average():
    if not class_roster:
        print("There are no students in the class. Average cannot be computed.\n")
        return

    average = 0.0

    for student in class_roster:
        average = average + student.grade

    average = average / len(class_roster)

    print(f"The class has a grade average of: {average}\n")

def remove_student():
    if not class_roster:
        print("There is nobody to remove from the class.\n")
        return

    user_name = str(input("Who would you like to remove? ")).lower()

    for student in class_roster:
        if user_name == student.name:
            class_roster.remove(student)
            print(f"{user_name} has been removed from the class.\n")
            return

    print(f"{user_name}, could not be removed as they are not in the class roster. \n")

def update_grade():
    if not class_roster:
        print("There are no students in the class. No grades can be updated.\n")
        return

    user_name = (input("Which Student needs their grade updated? ")).lower()
    user_grade = int(input("What is their new grade? "))

    for student in class_roster:
        if user_name == student.name:
            student.update_grade(user_grade)
            print(f"{student.name}'s grade has been updated.\n")
            return

    print(f"Please double check the class roster, {user_name} in not is the class. \n")

def save_students():
    with open("students.txt", "w") as file:
        for student in class_roster:
            file.write(f"{student.name},{student.age},{student.grade}\n")

def load_students():
    class_roster.clear()
    with open("students.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")  # Creates into a list of strings
            load = Student(str(line[0]),int(line[1]),int(line[2]))
            class_roster.append(load)

def sort_alpha():
    if not class_roster:
        print("There are no students in the class to sort.\n")
        return

    class_roster.sort(key=lambda student: student.name)
    print("The class is now sorted by name.\n")

def sort_grade():
    if not class_roster:
        print("There are no students in the class to sort.\n")
        return

    class_roster.sort(key=lambda student: student.grade)
    print("The class is now sorted by grade.\n")

def highest_grade():
    if not class_roster:
        print("There are no students in the class.\n")
        return

    temp_grade = 0
    temp_name = ""

    for student in class_roster:
        if student.grade > temp_grade:
            temp_grade = student.grade
            temp_name = student.name
    print(f"{temp_name} has the highest grade of {temp_grade}%\n")

def lowest_grade():
    if not class_roster:
        print("There are no students in the class to sort.\n")
        return

    temp_grade = 100
    temp_name = ""

    for student in class_roster:
        if student.grade < temp_grade:
            temp_grade = student.grade
            temp_name = student.name
    print(f"{temp_name} has the lowest grade of {temp_grade}%\n")

load_students()
while menu is True:
    print(
        "1. Add Student",
        "2. View Students",
        "3. Search Student",
        "4. Calculate Average Grade",
        "5. Update Student Grade",
        "6. Remove Student",
        "7. Sort Students Alphabetically",
        "8. Sort Students by Grade",
        "9. View Highest Grade",
        "10. View Lowest Grade",
        "11. Exit",
        sep="\n"
    )
    print()

    selection = int(input("Please enter 1 - 11 to pick an option: "))
    print()

    if selection == 1:
        add_student()

    elif selection == 2:
        view_student()

    elif selection == 3:
        search_students()

    elif selection == 4:
        grade_average()

    elif selection == 5:
        update_grade()

    elif selection == 6:
        remove_student()

    elif selection == 7:
        sort_alpha()

    elif selection == 8:
        sort_grade()

    elif selection == 9:
        highest_grade()

    elif selection == 10:
        lowest_grade()

    else:
        save_students()
        print("Saving...\n")
        print("Goodbye.")
        menu = False