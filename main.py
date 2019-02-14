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

# [START gae_python37_app]
import sys
sys.path.insert(0, 'libs')

import webapp2
import json
from bs4 import BeautifulSoup
from google.appengine.api import urlfetch
import webencodings
import six
import html5lib
import logging

#Controllers
class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'application/json'

		#urls
		target_url = 'https://townwork.net/joSrchRsltList/?ac=041&slc=0113&suc=01&svos=SCP01030101Salary0113'
        townwork_url = 'https://townwork.net'

        res = urlfetch.fetch(target_url)
        res_data = json.loads(res.content)

        res_html = BeautifulSoup(res_data, "html5lib")

        job_url_list = []

        for a in soup.find_all('a', class_ = 'job-lst-main-box-inner'):
        	job_url_list.append(townwork_url + a.get('href'))



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
