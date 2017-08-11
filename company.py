import requests
import json
from person import Person

class Company:
	global user_key 
	user_key = '' #input crunchbase API key
	def __init__(self, name, permalink, fund):
		self.name = name
		self.permalink = permalink
		self.fund = fund
		self.categories, self.location = self.self_populate()
		self.type = "COMPANY"
		self.team = self.gen_team()

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_permalink(self):
		return self.permalink

	def set_permalink(self, permalink):
		self.permalink = permalink

	def get_fund(self):
		return self.fund

	def set_fund(self, fund):
		self.fund = fund

	def get_categories(self):
		return self.categories

	def set_categories(self, categories):
		self.categories = categories

	def get_location(self):
		return self.location

	def set_location(self, location):
		self.location = location

	def get_type(self):
		return self.type

	def set_type(self, types):
		self.type = types

	def get_team(self):
		return self.team

	def set_team(self, team):
		self.team = team

	def self_populate(self):
		location = ""
		data_loc = requests.get("https://api.crunchbase.com/v3/organizations/" + self.permalink + "/headquarters?user_key=" + user_key).json()
		try:	
			location = data_loc['data']['items'][0]['properties']['region']
		except IndexError as e:
			pass

		data_cat = requests.get("https://api.crunchbase.com/v3/organizations/" + self.permalink + "/categories?user_key=" + user_key).json()
		categories = []
		temp_cat = data_cat['data']['items']
		for item in temp_cat:
			categories.append(item['properties']['name'])

		return categories, location

	def gen_team(self):
		data_team = requests.get("https://api.crunchbase.com/v3/organizations/" + self.permalink + "/current_team?user_key=" + user_key).json()
		team = []
		temp_team = data_team['data']['items']
		for item in temp_team:
			permalink = item['relationships']['person']['properties']['permalink']
			team.append(Person(permalink, self))
		return team
