from random import randint, seed

import emotions

class Presets:

    def __init__(self, emotions_obj, characters_obj, **kwargs):
        self.seed = kwargs["seed"] if "seed" in kwargs else randint(10000000, 100000000)
        seed(self.seed)

