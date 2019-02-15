# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python27_app]
#!/usr/bin/python
# -*- coding: utf-8 -*-


import logging

from flask import Flask

# [START imports]
import requests
from bs4 import BeautifulSoup
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()
# [END imports]

app = Flask(__name__)


@app.route('/')
def index():
    # [START requests_get]
    #urls
		target_url = 'https://townwork.net/joSrchRsltList/?ac=041&slc=0113&suc=01&svos=SCP01030101Salary0113'
		townwork_url = 'https://townwork.net'

		res = requests.get(target_url)

		soup = BeautifulSoup(res.text, "html5lib")

		job_url_list = []

		for a in soup.find_all('a', class_ = 'job-lst-main-box-inner'):
			job_url_list.append(townwork_url + a.get('href'))

		return job_url_list[0]
    # [END requests_get]


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
# [END app]

