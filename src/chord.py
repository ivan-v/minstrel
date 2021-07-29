Chord_Type_to_Emotions = {
    'M': {"Happy": 1, "Sad": 0, "Angry": 0, "Excited": .5, "Fear": 0},
    'm': {"Happy": 0, "Sad": 1, "Angry": 0, "Excited": 0, "Fear": 0},
    'suss': {"Happy": .7, "Sad": 0, "Angry": .2, "Excited": .4, "Fear": 0},
    'dim': {"Happy": 0, "Sad": .2, "Angry": .8, "Excited": .2, "Fear": .4},
    'aug': {"Happy": 0, "Sad": 0, "Angry": .2, "Excited": .4, "Fear": .4},
    'M7': {"Happy": .9, "Sad": 0, "Angry": 0, "Excited": .5, "Fear": 0},
    'm7': {"Happy": .4, "Sad": .4, "Angry": 0, "Excited": .2, "Fear": 0},
    '7': {"Happy": .4, "Sad": .3, "Angry": .2, "Excited": .3, "Fear": 0},
    'm7b5': {"Happy": .2, "Sad": .6, "Angry": .4, "Excited": .2, "Fear": .1},
    '7b5': {"Happy": .1, "Sad": .4, "Angry": .6, "Excited": .2, "Fear": .6},
    '6': {"Happy": 1, "Sad": 0, "Angry": 0, "Excited": .7, "Fear": 0},
    'm6': {"Happy": .2, "Sad": .2, "Angry": .1, "Excited": .3, "Fear": .2},
    '7#5': {"Happy": .2, "Sad": .4, "Angry": .5, "Excited": .3, "Fear": .3},
    'm+9': {"Happy": .7, "Sad": .5, "Angry": .2, "Excited": .5, "Fear": 0},
    'dim7': {"Happy": 0, "Sad": 0, "Angry": 1, "Excited": .4, "Fear": .4},
    'halfdim7': {"Happy": 0, "Sad": .3, "Angry": .1, "Excited": .2, "Fear": .1},
    'm9': {"Happy": .5, "Sad": .2, "Angry": .1, "Excited": .1, "Fear": 0},
    'Dom.min9': {"Happy": .1, "Sad": .3, "Angry": 0, "Excited": .2, "Fear": .1},
    '9': {"Happy": .6, "Sad": 0, "Angry": .2, "Excited": .5, "Fear": 0},
    'b9': {"Happy": 0, "Sad": .3, "Angry": .1, "Excited": .2, "Fear": .1},
    'M9': {"Happy": 1, "Sad": 1, "Angry": 0, "Excited": 1, "Fear": 0},
    '11': {"Happy": .5, "Sad": 0, "Angry": 0, "Excited": .8, "Fear": 0},
    '7#9': {"Happy": 0, "Sad": .2, "Angry": .7, "Excited": .7, "Fear": .2},
    '7#11': {"Happy": 0, "Sad": .2, "Angry": .4, "Excited": .5, "Fear": .3},
    'm11': {"Happy": .2, "Sad": 0, "Angry": 0, "Excited": .6, "Fear": .1},
    'M7#11': {"Happy": .5, "Sad": .3, "Angry": 0, "Excited": .5, "Fear": .1}, 
    '13': {"Happy": .8, "Sad": 0, "Angry": 0, "Excited": .5, "Fear": 0},
    'M13': {"Happy": .5, "Sad": .2, "Angry": 0, "Excited": .4, "Fear": .1},
    'm13': {"Happy": 0, "Sad": .2, "Angry": 0, "Excited": .2, "Fear": 0},
}

Chord_Type_to_Pitches = {    
    'M': (0, 4, 7),
    'm': (0, 3, 7),
    'suss': (0, 5, 7), 
    'dim': (0, 3, 6), 
    'aug': (0, 4, 8), 
    'M7': (0, 4, 7, 11), 
    'm7': (0, 3, 7, 10), 
    '7': (0, 4, 7, 10), 
    'm7b5': (0, 3, 6, 10),
    '7b5': (0, 4, 6, 10), 
    '6': (0, 4, 7, 9),
    'm6': (0, 3, 7, 9),
    '7#5': (0, 4, 8, 10),
    'm+9': (0, 3, 7, 14), 
    'dim7': (0, 3, 6, 9), 
    'halfdim7': (0, 3, 6, 10), 
    'm9': (0, 3, 7, 10, 14), 
    'Dom.min9': (0, 4, 7, 10, 11),
    '9': (0, 4, 7, 10, 14), 
    'b9': (0, 4, 7, 10, 13), 
    'M9': (0, 4, 7, 11, 14), 
    '11': (0, 7, 10, 14, 17), 
    '7#9': (0, 4, 7, 10, 15), 
    '7#11': (0, 4, 7, 10, 18), 
    'm11': (0, 3, 7, 10, 14, 17), 
    'M7#11': (0, 4, 7, 11, 14, 18), 
    '13': (0, 4, 7, 10, 14, 21), 
    'M13': (0, 4, 7, 11, 14, 21), 
    'm13': (0, 3, 7, 10, 14, 17, 21),
}

Starting_Pitch = {
    "C":  60,
    "Cs": 61,
    "Db": 61,
    "D":  62,
    "Ds": 63,
    "Eb": 63,
    "E":  64,
    "Fb": 64,
    "Es": 65,
    "F":  65,
    "Fs": 66,
    "Gb": 66,
    "G":  67,
    "Gs": 68,
    "Ab": 68,
    "A":  69,
    "As": 70,
    "Bb": 70,
    "B":  71,
    "Cb": 71,
    "Bs": 60,
}


def get_undertone(is_minor, operating_bit):
    tones = (0, 2, 3, 5, 7, 8, 10) if is_minor else (0, 2, 4, 5, 7, 9, 11)
    if len(operating_bit) > 1:
        if operating_bit[0] == 'b':
            modifier = -1
        elif operating_bit[0] == '#':
            modifier = 1
        else:
            modifier = 0
        return tones[int(operating_bit[1]) - 1] + modifier - 12
    else:
        return tones[int(operating_bit) - 1] - 12



class Chord:

    def __init__(self, **kwargs):
        # In the format ("name='F', type='13'")
        # operating_bit is an optional tone under the root
        if 'root' in kwargs:
            self.root = kwargs['root']
            self.type = kwargs['type'] if 'type' in kwargs else 'm' if self.root.islower() else 'M'
            self.operating_bit = kwargs['operating_bit'] if 'operating_bit' in kwargs else ''
            if self.operating_bit != '':
              undertone = get_undertone('m' in self.type, self.operating_bit)
              self.aps = [[pitch + octave*12 + Starting_Pitch[self.root] for pitch in Chord_Type_to_Pitches[self.type]] + [undertone + octave*12 + Starting_Pitch[self.root]] for octave in range(-4, 4)]
            else:
              self.aps = [[pitch + octave*12 + Starting_Pitch[self.root] for pitch in Chord_Type_to_Pitches[self.type]] for octave in range(-4, 4)]
            self.pitches = kwargs['pitches'] if 'pitches' in kwargs else self.aps[4]
        else:
            raise ValueError("Chord has not root")

    def invert(self, inversion):
        self.pitches = [self.pitches[i] + 12 for i in range(inversion)] + self.pitches[inversion:]
        return self

# print(Chord(root='C', type='M', operating_bit='b5').aps)

