import pytube

pytube.YouTube(input()).streams.get_audio_only().download()
