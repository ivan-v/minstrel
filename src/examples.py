import characters
import emotions
import presets

example_characters_obj = characters.Characters({'a': [(0, 10), (13, 20)], 'b': [(4, 6), (15, 25)]})

example_emotions_obj = emotions.Emotions(
                     {'Fear': [0.2925117076, 0.2853800474, 0.1521330108, 0.0640701076], 
                      'Sad': [0.204908212, 0.2562443577, 0.2411708104, 0.0852725165], 
                      'Angry': [0.2148454052, 0.3279547604, 0.3169042835, 0.0474158701], 
                      'Happy': [0.0781342094, 0.0468821089, 0.0977227001, 0.2811726655], 
                      'Bored': [0.0577362764, 0.0296855249, 0.0694645185, 0.3424433423], 
                      'Excited': [0.1518641895, 0.0538532007, 0.1226046768, 0.179625498]}, 
                      [0, 2, 4, 6])

example_presets_obj = presets.Presets(example_emotions_obj, example_characters_obj, 300)

print(example_presets_obj.chapters)