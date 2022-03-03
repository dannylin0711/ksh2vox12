class Timestamp:
    def __init__(self):
        self.subsection = 1
        self.beat = 1
        self.offset = 0
        
    def getVoxTimestamp(self):
        temp = '%3d,%2d,%2d' % (self.subsection, self.beat, self.offset)
        return temp