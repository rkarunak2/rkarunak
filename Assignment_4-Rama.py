# ASSIGNMENT 4 - Wednesday, September 25th (session cancelled due to weather)
# 1. Use a dictionary to store information about a fictional person. Store their first name, last name, age, 
#     and the city in which they live. You should have keys such as first_name, last_name, age, and city. 
#     Print each piece of information stored in your dictionary.
fictional_person = {'first_name': 'Dubuku', 'last_name' : 'Damaru', 'age':'105', 'city' : 'Hell city'}
print(f"{fictional_person['first_name']},{fictional_person['last_name']},{fictional_person['age']}, {fictional_person['city']}")

# 2. Make two new dictionaries representing different people, and store all three dictionaries in a list 
#     called people. Loop through your list of people. As you loop through the list, print everything you 
#     know about each person.

fictional_person_1 = {'first_name': 'Dubuku', 'last_name' : 'Damaru', 'age':'105', 'city' : 'Hell city'}
print(f"{fictional_person['first_name']},{fictional_person['last_name']},{fictional_person['age']}, {fictional_person['city']}")

fictional_person_2 = {'first_name': 'Dub', 'last_name' : 'Dam', 'age':'5', 'city' : 'Heaven city'}
print(f"{fictional_person['first_name']},{fictional_person['last_name']},{fictional_person['age']}, {fictional_person['city']}")

fictional_person_3 = {'first_name': 'buku', 'last_name' : 'maru', 'age':'35', 'city' : 'Earth city'}
print(f"{fictional_person['first_name']},{fictional_person['last_name']},{fictional_person['age']}, {fictional_person['city']}")

people = [fictional_person_1, fictional_person_2, fictional_person_3]

for thing in people:
    print(thing)
