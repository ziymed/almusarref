import cgi
import time
from random import Random
# -*- coding: utf8 -*-
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
import os
from google.appengine.ext.webapp import template
from mosaref_main import *

class MainPage(webapp.RequestHandler):
  def get(self):
	        template_values = {  
				 'result': 'AA',  
				 }
		path = os.path.join(os.path.dirname(__file__), 'views/main.html')
		self.response.out.write(template.render(path, template_values))

		
  def post(self):			
		word = self.request.get("verb")
		root = self.request.get("root")
		haraka = self.request.get("haraka")
		template_values = {  
				 'result': do_sarf(word,root,haraka),  
				 }
  
		path = os.path.join(os.path.dirname(__file__), 'views/tasrefat.html')
		self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()	
