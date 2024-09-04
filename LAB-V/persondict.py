person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Part 1: Check if the person dictionary has 'skills' key, if so print the middle skill
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print("Middle skill in the skills list:", person['skills'][middle_index])
# Part 2: Check if the person has 'Python' skill and print out the result
if 'skills' in person and 'Python' in person['skills']:
    print("The person has 'Python' skill.")
# Part 3: Determine the developer type based on skills
if person['skills'] == ['JavaScript', 'React']:
    print("He is a front end developer")
elif all(skill in person['skills'] for skill in ['Node', 'Python', 'MongoDB']):
    print("He is a backend developer")
elif all(skill in person['skills'] for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer")
else:
    print("Unknown title")
# Part 4: Print the marital status and country if conditions are met
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")