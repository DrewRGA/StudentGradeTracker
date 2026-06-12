from student import Student

def save_students(class_roster):
    with open("students.txt", "w") as file:
        for student in class_roster:
            file.write(f"{student.name},{student.age},{student.grade}\n")

def load_students(class_roster):
    class_roster.clear()
    with open("students.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")  # Creates into a list of strings
            load = Student(str(line[0]),int(line[1]),int(line[2]))
            class_roster.append(load)