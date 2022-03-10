class StudentManagement:

    def __init__(self):
        self.students = []

    def add_student(self, name, age, course):
        self.students.append({"name": name, "age":age, "course":course})
        return str(f"{name} details added")

    def update_student(self, name, age, course):
        for index in range(len(self.students)):
            if self.students[index]["name"] == name:
                self.students[index] = {"name": name, "age": age, "course": course}
                return str(f"{name} details updated")
        else:
            return "No data found"

    def delete_student(self, name):
        for index in range(len(self.students)):
            if self.students[index]["name"] == name:
                self.students.pop(index)
                return str(f"{name} details deleted")
        else:
            return "No data found"

    def view_details(self, name):
        for index in range(len(self.students)):
            if self.students[index]["name"] == name:
                age = self.students[index]["age"]
                course = self.students[index]["course"]
                return str(f"Student details of {name} are age={age}, course = {course}")
        else:
            return "No data found"

