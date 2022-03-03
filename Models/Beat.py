class Beat:
    def __init__(self):
        self.timestamp = ""
        self.numerator = 4
        self.denominator = 4
        
    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
    
    def set_beat(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator