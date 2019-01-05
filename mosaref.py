#!/usr/bin/python
# -*- coding=utf-8 -*-
from mosaref_main import *
import cgi
import time
from random import Random
# -*- coding: utf8 -*-
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template


class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write("<form action='/mosaref' method='post'><input type='text' name='verb'/><input type='text' name='root'/><input type='text' name='haraka'/><input type='submit'/></form>")

		
  def post(self):			
		#word = self.request.get("verb")
    self.response.out.write("A")
				
application = webapp.WSGIApplication(
                                     [('/mosaref', MainPage)],
                                     debug=True)
																	 
																		 
																		 
def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()	