import subprocess

# plays a given mp3 file
# WARNING : currently requires FFmpeg (https://www.ffmpeg.org/) !!
def PlayTrack( mp3Url, silent=True ) :

	subprocess.call([
		"ffplay",
		mp3Url,
		"-autoexit",
		"-showmode", "rdft",
		"-x", "256",
		"-y", "256",
		"-loglevel", ("quiet" if silent else "info")
		] )
