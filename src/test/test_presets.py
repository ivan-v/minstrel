from random import seed

import presets

from test_emotions import example_emotions_obj
from test_characters import example_characters_obj

def test_presets_seed():
	presets_obj_1 = presets.Presets(example_emotions_obj, example_characters_obj)
	assert presets_obj_1.seed is not None

	presets_obj_2 = presets.Presets(example_emotions_obj, example_characters_obj, seed=12345678)
	assert presets_obj_2.seed == 12345678	
