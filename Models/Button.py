from Track import Track

class Button:
    def __init__(self):
        self.timestamp = ""
        self.length = 0     # 0 means chip
        self.track = Track.L
        
    def setTrack(self, track: Track):
        if track == Track.LEFTLASER or track == Track.RIGHTLASER:
            print("Button.setTrack: Invalid track, defaulting to L")
            self.track = Track.L
        else:
            self.track = track

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp
    
    def setLength(self, length):
        self.length = length
    
    def getButtonData(self):
        return self.timestamp, self.length, self.track # todo