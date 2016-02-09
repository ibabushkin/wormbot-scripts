#!/usr/bin/env python3

from robobrowser import RoboBrowser
from robobrowser.forms.form import Form
import re
import os
from urllib.parse import urlparse


def main(url):
    # morons are too lazy to type out the URL scheme
    if urlparse(url).scheme == '':  # rfc3987: parse(url, rule='URI')['scheme']
        url = 'http://{}'.format(url)

    # And i wonder if it is a valid URL
    try:
        urlparse(url).netloc.split('.')[1]
    except IndexError:
        print(os.environ['NICKNAME'] +
              ', give me a valid URL to shorten. Louge off you skeleton pile..')
        return

    # lay on the force bro.
    browser = RoboBrowser(history=True)
    browser.open('http://ezl.ink/index.php')
    form = browser.get_form(0)
    assert isinstance(form, Form)

    form["url"] = url

    browser.submit_form(form)
    html = browser.parsed

    shorturl = re.findall('http[s]?://ezl.ink/[a-zA-Z0-9]+', str(html))
    print(os.environ['NICKNAME'] + ', shorturl: ' + shorturl[0])

if __name__ == '__main__':
    import sys
    try:
        main(sys.argv[1])
    except IndexError as e:
        # fricking no args
        print(os.environ['NICKNAME'] + ', give me a URL to shorten. Twart XD.')
