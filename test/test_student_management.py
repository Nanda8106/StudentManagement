from student_management import StudentManagement
import unittest


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManagement()

    def set_data(self):
        name = "nanda"
        age = 20
        course = "computers"
        self.manager.add_student(name, age, course)
        self.assertEqual(len(self.manager.students), 1)

    def test_add_student(self):
        self.set_data()
        name = "kishore"
        age = 20
        course = "mechanical"
        output = self.manager.add_student(name, age, course)
        expected_output = str(f"{name} details added")
        self.assertEqual(expected_output, output)

    def test_view_details(self):
        self.set_data()
        data = self.manager.students[0]
        name = data["name"]
        output = self.manager.view_details(name)
        expected_output = str(f"Student details of {name} are age=20, course = computers")
        self.assertEqual(expected_output, output)

    def test_update_student(self):
        self.set_data()
        data = self.manager.students[0]
        name = data["name"]
        age = data["age"]
        course = data["course"]
        output = self.manager.update_student(name, age, course)
        expected_output = str(f"{name} details updated")
        self.assertEqual(expected_output, output)

    def test_delete_student(self):
        self.set_data()
        data = self.manager.students[0]
        name = data["name"]
        output = self.manager.delete_student(name)
        expected_output = str(f"{name} details deleted")
        self.assertEqual(expected_output, output)
