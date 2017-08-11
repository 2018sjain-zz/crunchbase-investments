import requests
import json

class Person:
	global user_key 
	user_key = '' #input crunchbase API key
	def __init__(self, permalink, organization):
		self.permalink = permalink
		self.name, self.location, self.title = self.self_populate()
		self.organization = organization

	def get_permalink(self):
		return self.permalink

	def set_permalink(self, permalink):
		self.permalink = permalink

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def get_title(self):
		return self.title

	def set_title(self, title):
		self.title = title

	def self_populate(self):
		data_person = requests.get("https://api.crunchbase.com/v3/people/" + self.permalink + "?user_key=" + user_key).json()
		name = ""
		try:	
			first_name = data_person['data']['properties']['first_name']
			last_name = data_person['data']['properties']['last_name']
			name = first_name + last_name
		except (KeyError, TypeError) as e:
			pass
		location = ""
		try:
			location = data_person['data']['relationships']["primary_location"]['item']['properties']['region']
		except (KeyError, TypeError) as e:
			pass
		title = ""
		try:
			title = data_person['data']['relationships']["primary_affiliation"]['item']['properties']['title']
		except KeyError as e:
			pass
		return name, location, title