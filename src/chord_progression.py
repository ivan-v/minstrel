from random import choice

from chord import Chord_Type_to_Pitches, Starting_Pitch, Chord

def grow_minor_chord_progression(*progression):
    if progression:
        root = progression[0][0]
    else:
        return [['i', choice(['suss', 'm'])]]
    if root[0] == 'i' and root[1] in ['suss', 'm']:
        options = [['bVII', ['9']],
                   ['V',    ['7', 'b9', 'suss']],
                   ['iv',   ['m6', 'm7', 'm9']],
                   ['bIII', ['aug']], 
                   ['ii',   ['dim']],
                   ['vii',  ['dim/2']],
                   ['i',    ['m/b3']],
                   ['bII',  ['M']]]
    elif root[0] == 'ii' and root[1] in ['dim']:
        options = [['bVI',  ['6', 'M7']],
                   ['iv',   ['m/b6', 'm6/b6', 'm7/b6', 'm6', 'm7', 'm9']],
                   ['i',    ['m/b3']],
                   ['bII',  ['M']]]
    elif root[0] == 'vii' and root[1] in ['dim/2']:
        options = [['bVI',  ['6', 'M7']],
                   ['iv',   ['m/b6', 'm6/b6', 'm7/b6', 'm6', 'm7', 'm9']],
                   ['i',    ['m/b3']],
                   ['bII',  ['M/4']]]
    elif root[0] == 'i' and root[1] in ['m/b3']:
        options = [['bII',  ['M']],
                   ['iv',   ['m', 'm6', 'm7', 'm9']]]
    elif (root[0] == 'iv' and root[1] in ['m7']) \
      or (root[0] == 'bII' and root[1] in ['M']):
        options = [['ii',   ['dim']],
                   ['vii',  ['dim/2']],
                   ['I',    ['7', 'b9']],
                   ['iii',  ['dim7']],
                   ['bIII', ['aug']],
                   ['i',    ['m/b3']],
                   ['bVI',  ['6', 'M7']],
                   ['iv',   ['m/b6', 'm6/b6', 'm7/b6']]]
    elif root[0] == 'V' and root[1] in ['7', 'b9', 'suss']:
        options = [['iv',   ['m', 'm6', 'm7', 'm9']],
                   ['bII',  ['M']],
                   ['ii',   ['dim']],
                   ['vii',  ['dim/2']],
                   ['II',   ['7', 'b9']],
                  ['#iv',  ['dim7']]]
    elif root[0] == 'II' and root[1] in ['7', 'b9']:
        options = [['vi',   ['7b5']]]
    elif root[0] == 'bVII' and root[1] in ['9']:
        options = [['bVI',  ['M']]]
    elif root[0] == 'I' and root[1] in ['7', 'b9']:
        options = [['V',   ['dim7', 'm7b5']]]
    elif (root[0] == 'bIII' and root[1] in ['aug']) \
      or (root[0] == 'i' and root[1] in ['m/b3']):
        options = [['bii',  ['dim']],
                   ['vii',  ['dim/2']]]
    elif (root[0] == 'bVI' and root[1] in ['6', 'M7']) \
      or (root[0] == 'iv' and root[1] in ['m/b6', 'm6/b6', 'm7/b6', 'm6', 'm7', 'm9']):
        options = [['bIII', ['7', '9', 'b9']],
                   ['V',    ['m7b5']]]
    elif root[0] == 'bIII' and root[1] in ['7', '9', 'b9']:
        options = [['bvii', ['m7b5']]]
    else:
        return False
    selected = choice(options)
    return [[selected[0], choice(selected[1])]] + progression[0]


def grow_major_chord_progression(*progression):
  if progression:
      root = progression[0][0]
  else:
      return [['I', choice(['6', 'M7', 'M9', 'suss'])]]

  function_weights = {
    "I": {"Happy": 1, "Sad": 0, "Angry": .05, "Excited": .5, "Fear": 0},
    "ii": {"Happy": 1, "Sad": 0, "Angry": .05, "Excited": .5, "Fear": 0},
    "iii":  {"Happy": 1, "Sad": 0, "Angry": .05, "Excited": .5, "Fear": 0},
    "VI": {"Happy": 1, "Sad": 0, "Angry": .05, "Excited": .5, "Fear": 0},
    "V": {"Happy": 1, "Sad": 0, "Angry": .05, "Excited": .5, "Fear": 0},
    "VI": {"Happy": 1, "Sad": 0, "Angry": .05, "Excited": .5, "Fear": 0},
    "VII": {"Happy": 1, "Sad": 0, "Angry": .05, "Excited": .5, "Fear": 0},
  }

  if root[0] == 'I' and root[1] in ['6', 'M7', 'M9', 'suss']:
      options = [['V',   ['7', '9', '11', '13', 'suss']], 
                 ['IV',  ['6', 'M7', 'm6', 'm']], 
                 ['iii', ['m7']], 
                 ['ii',  ['m7', 'm9']], 
                 ['bII', ['7']], 
                 ['IV',  ['m7']], 
                 ['bVII',['9']]]
  elif root[0] == 'V' and root[1] in ['7', '9', '11', '13', 'suss']:
      options = [['IV',  ['6', 'M7', 'm6', 'm']], 
                 ['ii',  ['m7', 'm9']], 
                 ['II',  ['7', '9', 'b9']],
                 ['#IV', ['m7b5']],
                 ['I',   ['M/5']]]
  elif root[0] == 'ii':
      options = [['IV',  ['6', 'M7', 'm6', 'm']],
                 ['vi',  ['m7', 'm9']],
                 ['VI',  ['7', '9', 'b9']],
                 ['#I',  ['dim7']],
                 ['I',   ['dim/b3']],
                 ['I',   ['M/3']]]
  elif root[0] == 'iii':
      options = [['ii',  ['m7', 'm9']],
                 ['V',   ['7', '9', '11', '13', 'suss']],
                 ['VII', ['7', '9', 'b9']],
                 ['#II', ['dim7']]]
  elif root[0] == 'IV' and root[1] in ['6', 'M7', 'm6', 'm']:
      options = [['iii', ['m7']], 
                 ['vi',  ['m7', 'm9']],
                 ['I',   ['7', '9', 'b9']],
                 ['III', ['m7b5']]]
  elif root[0] == 'vi':
      options = [['V',   ['7', '9', '11', '13', 'suss']], 
                 ['iii', ['m7']], 
                 ['III', ['7', '9', 'b9']],
                 ['#V',  ['dim7']]]
  elif root[0] == 'bII' or (root[0] == 'IV' and root[1] == 'm7'):
      options = [['ii',  ['m7', 'm9']]]
  elif root[0] == 'bVII':
      options = [['bVI', ['M']]]
  elif root[0] == 'I' and root[1] == 'M/3':
      options = [['IV',  ['6', 'M7', 'm6', 'm']]]
  elif root[0] == 'II':
      options = [['I',   ['m6']],
                 ['V',   ['M/2']],
                 ['VI',  ['m7b5/b3']]] # the hardest one to process
  elif root[0] == 'V' and root[1] == 'M/2':
      options = [['I',   ['m6']]]
  elif root[0] == 'I' and root[1] == '/5':
      options = [['bVI', ['7']],
                 ['bVII',['9']],
                 ['#IV', ['m7b5']]]
  elif root[0] == 'VI' and root[1] in ['7', '9', 'b9']:
      options = [['III', ['m7b5']]]
  elif root[0] == 'I' and root[1] in ['7', '9', 'b9']:
      options = [['V',   ['m7']]]
  elif root[0] == 'VII':
      options = [['#IV', ['m7b5']]]
  elif root[0] == 'III' and root[1] in ['7', '9', 'b9']:
      options = [['VII', ['m7b5']]]
  else:
      return False

  selected = choice(options)
  return [[selected[0], choice(selected[1])]] + progression[0]


def generate_chord_progression(applied_key, length, *is_minor):
    growth = grow_minor_chord_progression() if is_minor else grow_major_chord_progression()
    progression = []
    # TODO: guarantee the length (currently can be shorter)
    while growth and len(progression) < length:
        progression = growth
        # print('growth:', growth, 'progression:', progression)
        # print(type(growth), type(len(progression)))
        growth = grow_minor_chord_progression(progression) if is_minor else grow_major_chord_progression(progression)
    return [chord for chord in roman_progression_to_chords(applied_key, progression)]


def roman_numeral_to_note(applied_key, roman_numeral):
    # print(applied_key) for some reason switching key?
    if roman_numeral[0] == 'b':
        modifier = -1
        roman_numeral = roman_numeral[1:]
    elif roman_numeral[0] == '#':
        modifier = 1
        roman_numeral = roman_numeral[1:]
    else:
        modifier = 0
    r_n = roman_numeral.lower()
    if r_n == "i":
        return applied_key.tones[0] + modifier + Starting_Pitch[applied_key.root]
    elif r_n == "ii":
        return applied_key.tones[1] + modifier + Starting_Pitch[applied_key.root]
    elif r_n == "iii":
        return applied_key.tones[2] + modifier + Starting_Pitch[applied_key.root]
    elif r_n == "iv":
        return applied_key.tones[3] + modifier + Starting_Pitch[applied_key.root]
    elif r_n == "v":
        return applied_key.tones[4] + modifier + Starting_Pitch[applied_key.root]
    elif r_n == "vi":
        return applied_key.tones[5] + modifier + Starting_Pitch[applied_key.root]
    elif r_n == "vii":
        return applied_key.tones[6] + modifier + Starting_Pitch[applied_key.root]
    else:
        raise ValueError("Numeral not found in applied_key:", roman_numeral)


def roman_progression_to_chords(applied_key, roman_progression):
    result = []
    for chord in roman_progression:
        root_note = next(key for key, value in Starting_Pitch.items() 
            if value == roman_numeral_to_note(applied_key, chord[0]))
        operating_bit = '' if len(chord[1].split('/')) < 2 else chord[1].split('/')[1]
        result.append(Chord(root=root_note, type=chord[1].split('/')[0], operating_bit=operating_bit))
    return result


# Example usage:
# from applied_key import Applied_Key
# applied_key = Applied_Key("C", "Aeolian")
# [print(chord.root, chord.type) for chord in generate_chord_progression(applied_key, 5, 'minor')]

