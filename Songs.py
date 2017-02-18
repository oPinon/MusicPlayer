
class Artist:

	name = None
	spotifyID = None

	def __init__( self, name=None ) :
		self.name = name

	def __str__(self):
		return str(self.__class__) + " : " + str(self.__dict__)

	# @returns : a String ID
	def getSpotifyID(self) : raise Exception("Artist.getSongs not implemented")

	# @returns : a list of Songs
	def getSongs( self ) : raise Exception("Artist.getSongs not implemented")

	# @returns : a list of similar artists
	def getSimilarArtists( self ) : raise Exception("Artist.getSimilarArtists not implemented")


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

	def getMp3URL(self) : raise Exception("Artist.getMp3URL not implemented")
