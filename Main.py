from Songs import *
from Player import *
import Spotify

artist = Artist( "Coldplay" )
artists = [ artist ] + artist.getSimilarArtists()
tracks = []

for artist in artists :
	tracks += artist.getSongs()

import random
random.shuffle( tracks )

for track in tracks :
	print( track )
	PlayTrack( track.getMp3URL() )
