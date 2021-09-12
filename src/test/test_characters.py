import characters

def test_characters():
    characters_obj = characters.Characters({'a': [(0, 10), (13, 20)], 'b': [(4, 6), (15, 25)]}) 
    assert characters_obj.appearances == {'a': [(0, 10), (13, 20)], 'b': [(4, 6), (15, 25)]}

example_characters_obj = characters.Characters({'a': [(0, 10), (13, 20)], 'b': [(4, 6), (15, 25)]})