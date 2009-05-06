import os
import random
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
	def get(self, url):
		if url == 'random-city':
			NUM_CITIES = 3;
			index = random.randint(0, NUM_CITIES - 1)
			if index == 0:
				self.redirect('http://www.icelandair.is/destinations/flights/item13097/flug-til-barcelona/?utm_source=mbl.is&utm_medium=banner&utm_term=Barcelona&utm_content=Randcom%2BCity&utm_campaign=Borgarherfer%C3%B0')
			elif index == 1:
				self.redirect('http://www.icelandair.is/destinations/flights/item13108/flug-til-new-york/?utm_source=mbl.is&utm_medium=banner&utm_term=New%2BYork&utm_content=Randcom%2BCity&utm_campaign=Borgarherfer%C3%B0') 
			else:
				self.redirect('http://www.icelandair.is/destinations/flights/item14172/flug-til-manchester/?utm_source=mbl.is&utm_medium=banner&utm_term=Manchester&utm_content=Randcom%2BCity&utm_campaign=Borgarherfer%C3%B0') 
		if url == 'german-cities':
			NUM_CITIES = 4;
			index = random.randint(0, NUM_CITIES - 1)
			if index == 0:
				self.redirect('http://www.icelandair.is/destinations/flights/item13096/flug-til-berlinar/?utm_source=thyskalandsferdir.travel&utm_medium=banner&utm_term=Berlin&utm_campaign=Fer%C3%B0am%C3%A1lar%C3%A1%C3%B0%2B%C3%9E%C3%BDskalands')
			if index == 1:
				self.redirect('http://www.icelandair.is/destinations/flights/item218155/?utm_source=thyskalandsferdir.travel&utm_medium=banner&utm_term=D%C3%BCsseldorf&utm_campaign=Fer%C3%B0am%C3%A1lar%C3%A1%C3%B0%2B%C3%9E%C3%BDskalands')
			if index == 2:
				self.redirect('http://www.icelandair.is/destinations/flights/item13093/flug-til-frankfurt/?utm_source=thyskalandsferdir.travel&utm_medium=banner&utm_term=Frankfurt&utm_campaign=Fer%C3%B0am%C3%A1lar%C3%A1%C3%B0%2B%C3%9E%C3%BDskalands')
			if index == 3:
				self.redirect('http://www.icelandair.is/destinations/flights/item13095/flug-til-munchen/?utm_source=thyskalandsferdir.travel&utm_medium=banner&utm_term=M%C3%BCnchen&utm_campaign=Fer%C3%B0am%C3%A1lar%C3%A1%C3%B0%2B%C3%9E%C3%BDskalands')
		elif url == '':
			self.redirect('http://www.icelandair.is/offers-and-bookings/brochure/?utm_source=visir.is&utm_medium=banner&utm_term=M%C3%ADn%2BBorg%20Fer%C3%B0abla%C3%B0&utm_campaign=Borgarherfer%C3%B0')
		else:
			self.response.set_status(404, 'Sorry, no one here by that name.  Try next door.')
	

application = webapp.WSGIApplication([
	('/(.*)', MainPage)],debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()