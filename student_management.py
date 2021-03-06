class StudentManagement:

    def __init__(self):
        # we will store students details in a list
        self.students = []

    # writing functionality for adding student
    def add_student(self, name, age, course):
        self.students.append({"name":name, "age":age, "course": course})
        return str(f"{name}")
        # return "nothing"

    # this functionality belongs to yahya mirza
    def view_details(self, name):
        for index in range(len(self.students)):
            if self.students[index]["name"] == name:
                age = self.students[index]["age"]
                course = self.students[index]["course"]
                return [name, age, course]
                # return ""
        else:
            return "No data found"

    # This functionality belongs to Muhammad Usman
    def update_student(self, name, age, course):
        for index in range(len(self.students)):
            if self.students[index]["name"] == name:
                self.students[index] = {"name": name, "age":age, "course": course}
                return str(f"{name}")
                # return ""
        else:

            return "No data found"

    def delete_student(self, name):
        for index in range(len(self.students)):
            if self.students[index]["name"] == name:
                self.students.pop(index)
                return str(f"{name}")
                # return ""
        else:

            return "No data found"
