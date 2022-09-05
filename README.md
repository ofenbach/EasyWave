# EasyWave
Easy to use wave file editor for python with effects like reverb, chorus, compression etc.  

# Usage  
```python
from wavefile import WaveFile

track = WaveFile("test.wav")                    # open wave file test.wav
track.add_reverb(0.3)                           # reverb with room size 30%
track.compress(threshold_db=-12, ratio=3)       # compress audio with threshold -12dB and ratio 3
track.add_chorus()                              # add chorus effect
track.gain(-5)                                  # reduce gain by -5dB
track.phaser()                                  # add phaser effect
track.save("mixed.wav")                         # export file to a new file
```
