from student_management import StudentManagement
import unittest


class TestIntegrationStudentManagement(unittest.TestCase):

    def test_integration_add_view_details(self):
        obj1 = StudentManagement()
        name = "kishore"
        age = 20
        course = "Mechanical"
        output = obj1.view_details(obj1.add_student(name, age, course))
        expected_output = [name, age, course]
        self.assertEqual(expected_output, output)

    def test_integration_add_delete_details(self):
        obj1 = StudentManagement()
        name = "kishore"
        age = 20
        course = "Mechanical"
        output = obj1.delete_student(obj1.add_student(name, age, course))
        expected_output = name
        self.assertEqual(expected_output, output)


