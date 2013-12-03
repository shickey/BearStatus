#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#

# this is some template "hello world" code

import webapp2

# import the date module
from datetime import date

# imports jinja2 and sets it up
import jinja2
import os

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

# hardcode in the current block
current_block = '7'

class MainHandler(webapp2.RequestHandler):
    def get(self):
      
        # determine the current week day
        today = date.today()
        current_weekday = today.isoweekday()
        # one thing I'm not sure about is whether the above code needs to go in the request handler (calculated at very page load)
        
        # write variables to template
        template_values = {
            'block': current_block,
        }

        template = jinja_environment.get_template('frontendproto.html')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
