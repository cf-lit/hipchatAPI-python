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


	#
	# User Methods
	################### 
	
	#
	# Get users
	# https://www.hipchat.com/docs/apiv2/method/get_all_users
	##
	def get_all_users(self):
		buffer = StringIO()
		c = pycurl.Curl()
		c.setopt(c.URL, self.hipchat_url+"user?auth_token="+self.hipchat_token)
		c.setopt(c.HTTPHEADER, self.hipchat_header)
		c.setopt(c.WRITEDATA, buffer)
		c.perform()
		c.close()
		return buffer.getvalue()

	#
	# Create user
	# https://www.hipchat.com/docs/apiv2/method/create_user
	##
	def create_user(self,
			name,
			title="",
			mention_name="",
			is_group_admin=False,
			timezone='UTC'
			password,
			email ):
		

#
# Testing
conf = json.load(open('hipchat_conf.json'))

test = Hipchat(conf['hipchat_token'])
result = test.list_users()

print json.dumps(json.loads(result), indent=4, sort_keys=True)

