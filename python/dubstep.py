def song_decoder(song):
    return " ".join([i.strip() for i in song.split("WUB") if i != ""]).strip()
