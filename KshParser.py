from Models.BPM import BPM
from Models.Button import Button
from Models.Laser import Laser

class KshParser:
    def __init__(self):
        self.bpms:BPM = []
        self.left_lasers:Laser = []
        self.leftfx:Button = []
        self.bta:Button = []
        self.btb:Button = []
        self.btc:Button = []
        self.btd:Button = []
        self.rightfx:Button = []
        self.right_lasers:Laser = []
        
    def parse(self, filename):
        f = open(filename, "r")
        kshLines = f.readlines()