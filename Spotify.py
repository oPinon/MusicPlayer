from Songs import *

import urllib2, json

SpotifyAPIURL = "https://api.spotify.com/v1/"

# @returns : an object from the URL of a JSON file
def FetchURL( url ) :
	return json.load( urllib2.urlopen(url) )

def SpotifySearch( query, type="track", limit = 1 ) :
	url = SpotifyAPIURL +  "search?type=" + type + "&query=" + query + "&;limit" + str(limit)
	return FetchURL( url )

def Artist_getSpotifyID( self ) :

	if self.spotifyID == None :
		matches = SpotifySearch( self.name, "artist" )
		self.spotifyID = matches["artists"]["items"][0]["id"]
	return self.spotifyID
Artist.getSpotifyID = Artist_getSpotifyID

def Artist_getSongs( self, number=32 ) :

	url = SpotifyAPIURL + "artists/" + self.getSpotifyID() + "/top-tracks?country=US"
	rep = FetchURL( url )
	songs = []
	for track in rep["tracks"] :
		song = Song()
		song.name = track["name"]
		song.spotifyID = track["id"]
		song.artist = self
		songs.append( song )
	return songs
Artist.getSongs = Artist_getSongs

def Artist_getSimilarArtists( self ) :

	url = SpotifyAPIURL + "artists/" + self.getSpotifyID() + "/related-artists"
	results = FetchURL( url )["artists"]
	artists = []
	for artistInfo in results :
		artist = Artist( artistInfo["name"] )
		artist.spotifyID = artistInfo["id"]
		artists.append( artist )
	return artists
Artist.getSimilarArtists = Artist_getSimilarArtists

def Song_getMp3URL( self ) :

	if self.mp3Url == None :
		url = SpotifyAPIURL + "tracks/" + self.getSpotifyID()
		spotifyInfo = FetchURL( url )
		self.mp3Url = spotifyInfo["preview_url"]
	return self.mp3Url
Song.getMp3URL = Song_getMp3URL
