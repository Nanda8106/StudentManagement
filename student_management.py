class StudentManagement:

    def __init__(self):
        # we will store students details in a list
        self.students = []

    # writing functionality for adding student
    def add_student(self, name, age, course):
        self.students.append({"name":name, "age":age, "course": course})
        # return str(f"{name} details added")
        return "nothing"
