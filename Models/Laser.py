from Track import Track

class Laser:
    def __init__(self):
        self.timestamps = []
        self.positions = []
        self.track:Track = Track.LEFTLASER
    
    def addSection(self, timestamp, position):
        self.timestamps.append(timestamp)
        self.positions.append(position)
        
    def setTrack(self, track: Track):
        if track == Track.LEFTLASER or track == Track.RIGHTLASER:
            self.track = track
        else:
            print("Laser.setSide: Invalid side, defaulting to left laser")
            self.track = Track.LEFTLASER
        
    
    def getTrack(self):
        return self.track
    
    def getLaserData(self):
        return self.timestamps, self.positions # todo
    