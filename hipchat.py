#!/usr/bin/env python
#
# hipchat API
###

import json
import pycurl
import pprint
from StringIO import StringIO

class Hipchat:

	hipchat_url = "https://api.hipchat.com/v2/"
	hipchat_header = ["content-type:", "application/json"]

	def __init__(self, hipchat_token):
		#
		# Set the Hipchat token and test
		self.hipchat_token = hipchat_token

	def get(self, url):
                buffer = StringIO()
                c = pycurl.Curl()
                c.setopt(c.URL, url)
                c.setopt(c.HTTPHEADER, self.hipchat_header)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                c.close()
                return buffer.getvalue()

	def post(self, url, post_data):
                buffer = StringIO()
                c = pycurl.Curl()
                c.setopt(c.URL, url)
                c.setopt(c.HTTPHEADER, self.hipchat_header)
                c.setopt(c.POSTFIELDS, post_data)
                c.perform()
                c.close()
                return buffer.getvalue()
		
	def delete(self, url):
                buffer = StringIO()
                c = pycurl.Curl()
                c.setopt(c.URL, url)
                c.setopt(c.HTTPHEADER, self.hipchat_header)
                c.setopt(c.CUSTOMREQUEST, 'delete')
                c.perform()
                c.close()
                return buffer.getvalue()
		


	def send_to_hip(self, url, data="", method='get'):
		return

	#
	# User Methods
	################### 
	
	#
	# Get users
	# https://www.hipchat.com/docs/apiv2/method/get_all_users
	##
	def get_all_users(self):
		url = self.hipchat_url+"user?auth_token="+self.hipchat_token
		return self.get(url)

	#
	# Create User
	# https://www.hipchat.com/docs/apiv2/method/create_user
	##
	def create_user(self, name, email, password, title="", mention_name="", is_group_admin=False, timezone='UTC'):
		post_data = json.dumps({'name': name, 'password': password, 'email': email, 'title': title, 'mention_name': mention_name, 'is_group_admin': is_group_admin, 'timezone': timezone})
		url = self.hipchat_url+"user?auth_token="+self.hipchat_token
		return self.post(url, post_data)	
	
	#
	# Delete User
	# https://www.hipchat.com/docs/apiv2/method/delete_user
	##
	def delete_user(self, id_or_email):
		url = self.hipchat_url+"user/"+id_or_email+"?auth_token="+self.hipchat_token
                return self.delete(url)


#
# Testing
conf = json.load(open('hipchat_conf.json'))

test = Hipchat(conf['hipchat_token'])

print  json.dumps(test.create_user("Joe Blogs", "joblogs@yahoo.co.uk", "Ugs673jdjke"), indent=4, sort_keys=True)

print json.dumps(json.loads(test.get_all_users()), indent=4, sort_keys=True)

print  json.dumps(test.delete_user("1878931"), indent=4, sort_keys=True)

print json.dumps(json.loads(test.get_all_users()), indent=4, sort_keys=True)

