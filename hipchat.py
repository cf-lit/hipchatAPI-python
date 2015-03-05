#!/usr/bin/env python
#
# hipchat API
###

import json
import pycurl
import pprint
from StringIO import StringIO
import urllib2

class Hipchat:

	hipchat_url = "https://api.hipchat.com/v2/"
	hipchat_header = {'content-type': 'application/json'}

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
	
		#buffer = StringIO()
		#post_data = {'': 'value'}
		#c = pycurl.Curl()
		#c.setopt(c.URL, self.hipchat_url+"user/?auth_token="+self.hipchat_token)
		#c.setopt(c.HTTPHEADER, self.hipchat_header)
		#c.setopt(c.WRITEDATA, buffer)
		#c.perform()
		#c.close()
		#return buffer.getvalue()
		
		data = json.dumps({'start-index': 0, 'max-results': 100, 'include-guests': 0, 'include-deleted': 0})
		#request = urllib2.Request(self.hipchat_url+"user?auth_token="+self.hipchat_token, data, self.hipchat_header)
		request = urllib2.Request(self.hipchat_url+"room?auth_token="+self.hipchat_token)
		print self.hipchat_url+"room?auth_token="+self.hipchat_token
		return urllib2.urlopen(request)
		

#
# Testing
conf = json.load(open('hipchat_conf.json'))

test = Hipchat(conf['hipchat_token'])
res = test.list_users()

print res.read()

