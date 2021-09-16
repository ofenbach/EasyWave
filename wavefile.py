from pedalboard import (
    Pedalboard,
    Convolution,
    Compressor,
    Chorus,
    Gain,
    Reverb,
    Limiter,
    LadderFilter,
    Phaser,
)
import soundfile as sf
from pydub import AudioSegment


class WaveFile:


    def __init__(self, filename):
        self.audio, self.sample_rate = sf.read(filename)
        self.filename = filename[:-4] + "_COPY.wav"
        self.board = Pedalboard([
            # Compressor(threshold_db=-10, ratio=2),
            # Gain(gain_db=10),
            # Chorus(),
            # LadderFilter(mode=LadderFilter.Mode.HPF12, cutoff_hz=900),
            # Phaser(),
            # Convolution("./guitar_amp.wav", 1.0),
            # Reverb(room_size=0.25),
        ], sample_rate=self.sample_rate)


    def compress(self, threshold_db=-12, ratio=3):
        """ Compresses your audio."""
        self.board = Pedalboard([], sample_rate=self.sample_rate)               # reset pedal
        self.board.append(Compressor(threshold_db=threshold_db, ratio=ratio))   # add effect
        effected = self.board(self.audio)                                       # apply pedal to wave
        with sf.SoundFile(self.filename, 'w', samplerate=self.sample_rate,channels=len(effected.shape)) as f:
            f.write(effected)


    def add_reverb(self, room_size=0.25):
        """ Adds reverb to wavefile """
        self.board = Pedalboard([], sample_rate=self.sample_rate)       # reset pedal
        self.board.append(Reverb(room_size=room_size))                  # add effect
        effected = self.board(self.audio)                               # apply pedal to wave
        with sf.SoundFile(self.filename, 'w', samplerate=self.sample_rate,channels=len(effected.shape)) as f:
            f.write(effected)


    def add_chorus(self):
        self.board = Pedalboard([], sample_rate=self.sample_rate)       # reset pedal
        self.board.append(Chorus())                                     # add effect
        effected = self.board(self.audio)                               # apply pedal to wave
        with sf.SoundFile(self.filename, 'w', samplerate=self.sample_rate,channels=len(effected.shape)) as f:
            f.write(effected)


    def limiter(self):
        self.board = Pedalboard([], sample_rate=self.sample_rate)       # reset pedal
        self.board.append(Limiter())                                    # add effect
        effected = self.board(self.audio)                               # apply pedal to wave
        with sf.SoundFile(self.filename, 'w', samplerate=self.sample_rate,channels=len(effected.shape)) as f:
            f.write(effected)


    def phaser(self):
        self.board = Pedalboard([], sample_rate=self.sample_rate)       # reset pedal
        self.board.append(Phaser())                                     # add effect
        effected = self.board(self.audio)                               # apply pedal to wave
        with sf.SoundFile(self.filename, 'w', samplerate=self.sample_rate,channels=len(effected.shape)) as f:
            f.write(effected)


    def gain(self, dB):
        self.board = Pedalboard([], sample_rate=self.sample_rate)       # reset pedal
        self.board.append(Gain(gain_db=dB))                             # add effect
        effected = self.board(self.audio)                               # apply pedal to wave
        with sf.SoundFile(self.filename, 'w', samplerate=self.sample_rate,channels=len(effected.shape)) as f:
            f.write(effected)


    def mix(self, file2):
        """ Combines two waves into one
            Mix/Merge will overwrite file """
        sound1 = AudioSegment.from_file(self.filename)
        sound2 = AudioSegment.from_file(file2)
        combined = sound1.overlay(sound2)
        combined.export(self.filename, format='wav')


    def save(self, filename):
        tmp_copy = AudioSegment.from_file(self.filename)
        tmp_copy.export(filename, format="wav")


""" EXAMPLE USAGE:

track = WaveFile("test.wav")                    # open wave file test.wav
track.add_reverb(0.3)                           # reverb with room size 30%
track.compress(threshold_db=-12, ratio=3)       # compress audio with threshold -12dB and ratio 3
track.add_chorus()                              # add chorus effect
track.gain(-5)                                  # reduce gain by -5dB
track.phaser()                                  # add phaser effect
track.save("mixed.wav")                         # export file to a new file

"""
