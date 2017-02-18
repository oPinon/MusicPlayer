
NoImpEx = Exception( "Method not implemented : did you import Spotify.py ?" )

class Artist:

	name = None
	spotifyID = None

	def __init__( self, name=None ) :
		self.name = name

	def __str__(self):
		return str(self.__class__) + " : " + str(self.__dict__)

	# @returns : a String ID
	def getSpotifyID(self) : raise NoImpEx

	# @returns : a list of Songs
	def getSongs( self ) : raise NoImpEx

	# @returns : a list of similar artists
	def getSimilarArtists( self ) : raise NoImpEx


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

	def getMp3URL(self) : raise NoImpEx
