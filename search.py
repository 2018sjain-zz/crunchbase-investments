import numpy as np

def copy(array):
	copy = []
	for each in array:
		copy.append(each)
	return copy

def search():
	print("If no specification, enter 'na'")
	sector = input("Sector: ")
	location = input("Location: ")
	if sector == 'na':
		sector = None
	if location == 'na':
		location = None
	return [sector, location]

def facts(person):
	title = str(person.get_title())
	location = str(person.get_location())
	if location == "":
		location = str(person.get_organization().get_location())
	categories = person.get_categories()
	name = str(person.get_name())
	organization = str(person.get_organization().get_name())
	return [name, title, organization, location, categories]



people = np.load('people.npy')

for person in people:
	name = str(person.get_name())
	organization = person.get_organization()
	organization_name = str(organization.get_name())
	location = str(person.get_location())
	if location == "":
		location = str(organization.get_location())

	# print(organization_name + ": " + name + " - " + location)

temp = copy(people)
result = []
# request = search()
request = ['California', 'Health Care', 'VP Engineering']
for person in temp:
	info = facts(person)
	for item in request:
		if item == None:
			continue
		if item in info or item in info[-1]:
			result.append(person)

result = set([x for x in result if result.count(x) > len(request) - 1])

for each in result:
	print(facts(each))