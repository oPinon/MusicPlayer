import urllib2, json

SpotifyAPIURL = "https://api.spotify.com/v1/"

# @returns : an object from the URL of a JSON file
def FetchURL( url ) :
	return json.load( urllib2.urlopen(url) )

def SpotifySearch( query, type="track", limit = 1 ) :
	url = SpotifyAPIURL +  "search?type=" + type + "&query=" + query + "&;limit" + str(limit)
	return FetchURL( url )

class Artist:

	name = None
	spotifyID = None

	def __init__( self, name=None ) :
		self.name = name

	def __str__(self):
		return str(self.__class__) + " : " + str(self.__dict__)

	# @returns : a String ID
	def getSpotifyID(self) :

		if self.spotifyID == None :
			matches = SpotifySearch( self.name, "artist" )
			self.spotifyID = matches["artists"]["items"][0]["id"]
		return self.spotifyID

	# @returns : a list of Songs
	def getSongs( self, number=32 ) :

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

	# @returns : a list of similar artists
	def getSimilarArtists( self ) :

		url = SpotifyAPIURL + "artists/" + self.getSpotifyID() + "/related-artists"
		results = FetchURL( url )["artists"]
		artists = []
		for artistInfo in results :
			artist = Artist( artistInfo["name"] )
			artist.spotifyID = artistInfo["id"]
			artists.append( artist )
		return artists


class Song:

	name = None
	artist = None

	spotifyID = None
	mp3Url = None

	def __str__(self):
		return str(self.__class__) + " : " + str(self.__dict__)

	def getSpotifyID(self) :

		if self.spotifyID != None :
			return self.spotifyID
		return self.spotifyID

	def getMp3URL(self) :

		if self.mp3Url == None :
			url = SpotifyAPIURL + "tracks/" + self.getSpotifyID()
			spotifyInfo = FetchURL( url )
			self.mp3Url = spotifyInfo["preview_url"]
		return self.mp3Url
