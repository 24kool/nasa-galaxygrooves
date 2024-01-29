#import sounddevice as sd
class Note:
    def __init__(self, duration, frequency, volume):
        topHertz=1500-(int)(200)#(ra)
        bottomHertez=200+(int)(-12)#(dec)
        self.duration = duration/50  # in seconds
        self.frequency = (int)(((topHertz-bottomHertez)*(frequency/100) )+bottomHertez) # in Hz
        # print(self.frequency)
        self.volume = volume  # 0 to 1
        if(self.duration>1):
            self.duration==1
        elif (self.duration<0.1):
            self.duration=0.1
        if(self.frequency>1200):
            self.frequency=1200
        elif(self.frequency<100):
            self.frequency=100
# Initialize audio parameters
sample_rate = 44100  # Sample rate in Hz
#sd.default.samplerate = sample_rate





