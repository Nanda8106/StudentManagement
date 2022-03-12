from student_management import StudentManagement
import unittest


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManagement()

    # this is not a test case, it is a function to set data
    def set_data(self):
        name = "nanda"
        age = 20
        course = "computers"
        self.manager.add_student(name, age, course)
        self.assertEqual(len(self.manager.students), 1)

    # writing test case for adding_Students
    def test_add_student(self):
        self.set_data()
        name = "kishore"
        age = 20
        course = "Mechanical"
        output = self.manager.add_student(name, age, course)
        expected_output = str(f"{name} details added")
        # expected_output = str(f"")
        self.assertEqual(expected_output, output)

    # this test case belongs to Yahya Mirza
    def test_view(self):
        self.set_data()
        data = self.manager.students[0]
        name = data["name"]
        age = data["age"]
        course = data["course"]
        output = self.manager.view_details(name)
        expected_output = str(f"Student details of {name} are age={age}, course={course}")
        # expected_output = str(f"")
        self.assertEqual(expected_output, output)

    # This test belongs to Muhammad Usman
    def test_update_student(self):
        self.set_data()
        data = self.manager.students[0]
        name = data["name"]
        age = data["age"]
        course = data["course"]
        output = self.manager.update_student(name, age, course)
        expected_output = str(f"{name} details updated")
        # expected_output = str(f"")
        self.assertEqual(expected_output, output)

