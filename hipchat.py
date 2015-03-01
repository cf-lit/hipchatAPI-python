#!/usr/bin/env python
#
# hipchat API
###

import json
import urllib2
import pprint

class Hipchat:

	hipchat_url = "https://api.hipchat.com/v2/"
	hipchat_header = {'content-type':'application/json'}

	def __init__(self, hipchat_token):
		#
		# Set the Hipchat token and test
		self.hipchat_token = hipchat_token


	#
	# Users
	## 
	
	#
	# list users
	##
	def list_users(self):
		#
		# Data to send to hipchat
		data = json.dumps({'start-index': 0, 'max-results': 100, 'include-guests': false, 'include-deleted': false})
		#
		# Build the request
		request = urllib2.Request(self.hipchat_url+"?auth_token="+self.hipchat_token, data, self.hipchat_header)
		#
		# send the request and return the resulting json
		result = urllib2.urlopen(request)
		return result.read()
		

#
# Testing
conf = json.load(open('hipchat_conf.json'))

test = Hipchat(conf['hipchat_token'])
result = test.list_users

pprint.pprint(result)


