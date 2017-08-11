import requests
import json
from company import Company
from person import Person

class VC:
	global user_key 
	user_key = '' #input crunchbase API key
	def __init__(self, name):
		self.name = name
		self.permalink, self.categories, self.location = self.self_populate()
		self.investments = self.gen_investments()
		self.type = 'FUND'
		self.team = self.gen_team()

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_permalink(self):
		return self.permalink

	def set_permalink(self, permalink):
		self.permalink = permalink

	def get_location(self):
		return self.location

	def set_location(self, location):
		self.location = location

	def get_categories(self):
		return self.categories

	def set_categories(self, categories):
		self.categories = categories

	def get_type(self):
		return self.type

	def set_type(self, type):
		return self.type

	def get_investments(self):
		return self.investments

	def add_investment(self, company):
		self.investments.append(company)

	def set_investments(self, companies):
		self.investments = companies

	def get_team(self):
		return self.team

	def set_team(self, team):
		self.team = team

	def add_team(self, person):
		self.team.append(person)

	def self_populate(self):
		data_per = requests.get('https://api.crunchbase.com/v3/organizations?name=' + self.name + '&user_key=' + user_key).json()
		permalink = data_per['data']['items'][0]['properties']['permalink']

		data_loc = requests.get("https://api.crunchbase.com/v3/organizations/" + permalink + "/headquarters?user_key=" + user_key).json()
		location = location = data_loc['data']['items'][0]['properties']['region']

		data_cat = requests.get("https://api.crunchbase.com/v3/organizations/" + permalink + "/categories?user_key=" + user_key).json()
		categories = []
		temp_cat = data_cat['data']['items']
		for item in temp_cat:
			categories.append(item['properties']['name'])

		return permalink, categories, location

	def gen_investments(self):
		data_inv = requests.get('https://api.crunchbase.com/v3/organizations/' + self.permalink +  "/investments?user_key=" + user_key).json()
		holder = data_inv['data']['items']
		companies = []
		temp_inv = []
		for company in holder:
			permalink = company['relationships']['funding_round']['relationships']['funded_organization']['properties']['permalink']
			if permalink in temp_inv:
				continue
			temp_inv.append(permalink)
			name = company['relationships']['funding_round']['relationships']['funded_organization']['properties']['name']
			investment = Company(name, permalink, self)
			companies.append(investment)
		return companies

	def gen_team(self):
		data_team = requests.get("https://api.crunchbase.com/v3/organizations/" + self.permalink + "/current_team?user_key=" + user_key).json()
		team = []
		temp_team = data_team['data']['items']
		for item in temp_team:
			# title = item['properties']['title']
			permalink = item['relationships']['person']['properties']['permalink']
			team.append(Person(permalink, self))
		return team