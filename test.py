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
		self.response.out.write("<form action='/' method='post'><input type='text' name='verb'/><input type='text' name='root'/><input type='text' name='haraka'/><input type='submit'/></form>")

		
  def post(self):			
		word = self.request.get("verb")
		root = self.request.get("root")
		haraka = self.request.get("haraka")
		# template_values = {  
				# 'html_title': do_sarf(word,root,haraka),  
				# 'html_body_text': 'sss',  
				# }
  
		path = os.path.join(os.path.dirname(__file__), 'views/tasrefat.html')
		#self.response.out.write(template.render(path, template_values))
		#self.response.out.write("<html dir='rtl'><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"></head><body>")
		self.response.out.write(do_sarf(word,root,haraka))
		#self.response.out.write("</body></html>")

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()	
