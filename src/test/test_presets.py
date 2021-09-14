from random import seed

import presets

from test_emotions import example_emotions_obj
from test_characters import example_characters_obj

def test_presets_seed():
	example_time = 300 # 300 seconds
	presets_obj_1 = presets.Presets(example_emotions_obj, example_characters_obj, 300)
	assert presets_obj_1.seed is not None

	presets_obj_2 = presets.Presets(example_emotions_obj, example_characters_obj, 300, seed=12345678)
	assert presets_obj_2.seed == 12345678	


example_presets_obj = presets.Presets(example_emotions_obj, example_characters_obj, 300)