import requests
import json
import numpy as np
from vc import VC

PCD_input = ["Citi Ventures"] #input fund names as strings
organizations = []

for item in PCD_input:
	organizations.append(VC(item))

for item in organizations:
	investments = item.get_investments()
	for each in investments:
		print(item.get_name() + ": " + each.get_permalink() + " - " + each.get_type())

np.save('data', organizations)