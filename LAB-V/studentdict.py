student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'Java'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}
# Part 1: Get the length of the student dictionary
print("Length of student dictionary:", len(student))
# Part 2: Get the value of skills and check the data type
skills_value = student['skills']
print("Skills value:", skills_value)
print("Data type of skills:", type(skills_value))
# Part 3: Modify the skills values by adding one or two skills
student['skills'].append('C++')
student['skills'].append('JavaScript')
print("Updated skills in student dictionary:", student['skills'])
# Part 4: Get the dictionary keys as a list
keys_list = list(student.keys())
print("Keys in student dictionary:", keys_list)
# Part 5: Get the dictionary values as a list
values_list = list(student.values())
print("Values in student dictionary:", values_list)
# Part 6: Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student dictionary as a list of tuples:", student_items)
# Part 7: Delete one of the items in the dictionary
student.pop('marital_status')
print("Updated student dictionary after deleting 'marital_status':", student)
# Part 8: Delete the student dictionary
del student
print("Student dictionary has been deleted.")