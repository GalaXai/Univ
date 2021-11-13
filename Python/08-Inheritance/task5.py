class Music():
    def __init__(self,artist,track_title,album,year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return "Performer: "+self.artist+"\nSong: "+self.track_title+"\nAlbum: "+self.album+"\nYear: "+str(self.year)

if __name__ == '__main__':
    song0 = Music("Ed Sheeran","Hearts Don't Break Around Here","Divide",2017)
    print(song0)