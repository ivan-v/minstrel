from random import randint, seed

import emotions

class Presets:

    def __init__(self, emotions_obj, characters_obj, time, **kwargs):
        self.seed = kwargs["seed"] if "seed" in kwargs else randint(10000000, 100000000)
        seed(self.seed)


        self.time = time
        self.emotions = emotions_obj
        self.characters = characters_obj

        # TODO: infer chapter-chunks from ambiance + emotions
        self.chapters = [(i, i+100) for i in range(0, self.time, 100)]
        # temp /\