from google.appengine.ext import ndb
import webapp2
import logging
import renderer
import utilities
from anagram import Anagram


class SubAnagram(webapp2.RequestHandler):
    # GET-request
    def get(self):
        logging.debug("GET")
        self.response.headers['Content-Type'] = 'text/html'

        # check whether user is logged in
        if utilities.user_is_logged_in():
            # if myuser object is None --> No user with key found --> new user --> make new user in datastore
            if not utilities.user_exists():
                utilities.add_new_user(utilities.get_user())
                
            renderer.render_subanagram(self, utilities.get_logout_url(self),
                                       self.request.get('name'),
                                       utilities.get_anagrams_of_user(utilities.get_my_user()))

        # if no user is logged in create login url
        else:
            renderer.render_login(self, utilities.get_login_url(self))

