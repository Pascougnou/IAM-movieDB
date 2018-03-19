import json
import requests

from django.shortcuts import render

import constants
from constants import TMDB_API_URL_v3, GET_MOVIE_REQUEST, TMDB_ADD_API_REQUEST, TMDB_API_KEY_v3

# https://api.themoviedb.org/3/movie/film_ID?api_key=XXXX
def get_response(url, request, id, api, key):
	url_full = url + request + id + api + key
	print("get_response")
	print(url_full)
	return requests.get(url=url_full).json() 
		
def startPage(request, token):
	def __init__(self, arg):
		super(utils, self).__init__()
		self.arg = arg
		self.utils = utils()
	if token == '':
		# if no token
		token = '264644'
			
	get_movie = get_response( 
		TMDB_API_URL_v3, 
		GET_MOVIE_REQUEST, 
		token, 
		TMDB_ADD_API_REQUEST, 
		TMDB_API_KEY_v3  )

	print("startPage")
	print (get_movie)
	
	return render(request, 'startPage/startPage.html', {
		'result': 'lolilol', 
		'get_response': get_movie, 
	})

def errorPage(request):
	def __init__(self, arg):
		super(utils, self).__init__()
		self.arg = arg
		self.utils = utils()

	print("errorPage")
	print(request)
	
	return render(request, 'errorPage/errorPage.html', {
		})