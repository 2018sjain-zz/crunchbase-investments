import numpy as np

people = []

data = np.load('data.npy')
for vc in data:
	name = vc.get_name()
	team = vc.get_team()
	for person in team:
		people.append(person)
	companies = vc.get_investments()
	for comp in companies:
		name = comp.get_name()
		team = comp.get_team()
		for person in team:
			people.append(person)

np.save('people', people)