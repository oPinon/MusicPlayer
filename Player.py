import subprocess

# plays a given mp3 file
# WARNING : currently requires FFmpeg (https://www.ffmpeg.org/) !!
# @retuns : what percentage (in [0;1]) of the track was played ?
def PlayTrack( mp3Url, silent=True ) :

	log = subprocess.Popen([
		"ffplay",
		mp3Url,
		"-autoexit",
		"-showmode", "rdft",
		"-x", "256",
		"-y", "256",
		"-loglevel", ("quiet" if False else "info")
		],
		stderr=subprocess.PIPE
		).communicate()[1]

	# getting the full duration of the song
	durationTag = "Duration:"
	durationTagPos = log.find( durationTag )
	durationStart = durationTagPos + len(durationTag)
	durationStr = log[ durationStart : durationStart + log[durationStart:].find( ',' ) ]
	t = durationStr.split( ':' )
	duration = float( t[2] ) + 60 * ( float(t[1]) + 60 * float(t[0]) )

	# getting the time that was actually played
	played = log.split("\r")[-2].split( ' ' )
	played = [ p for p in played if len(p) > 0 ]
	played = float( played[0] )

	return played / duration
