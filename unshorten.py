#!/usr/bin/env python3

import requests
import re, os
from urllib.parse import urlparse

def main(url):
	if urlparse(url).scheme == '':
		url = 'http://{}'.format(url)
	try:
		shorturl = re.findall('http[s]?://ezl.ink/[a-zA-Z0-9]+', str(url))[0]
		if shorturl:
			try:
				r = requests.get(shorturl, allow_redirects = True)
				print(os.environ['NICKNAME'] + ', LongURL: ' + r.url)
			except:
				print(os.environ['NICKNAME'] + ', ' + shorturl + ' doesn\'t exist in http://ezl.ink database, move on moron.')
				return
	except IndexError:
		print(os.environ['NICKNAME'] + ', that is no http://ezl.ink shortened url. Puddi\'s cousin. XD.')

if __name__ == '__main__':
	import sys
	try:
		main(sys.argv[1])
	except IndexError as e:
		#fricking no args
		print(os.environ['NICKNAME'] + ', give me a URL to shorten. Twart XD.')
