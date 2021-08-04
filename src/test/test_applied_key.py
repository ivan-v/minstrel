import applied_key

def test_applied_key_c_major():
    c_major = applied_key.Applied_Key('C', 'Ionian')
    assert c_major.name == 'C Ionian'
    assert c_major.root == 'C'
    assert applied_key.Starting_Pitch[c_major.root] == 60
    assert c_major.tones == (0, 2, 4, 5, 7, 9, 11)
    assert c_major.aps == [12, 14, 16, 17, 19, 21, 23, 24, 26,
                           28, 29, 31, 33, 35, 36, 38, 40, 41, 
                           43, 45, 47, 48, 50, 52, 53, 55, 57, 
                           59, 60, 62, 64, 65, 67, 69, 71, 72, 
                           74, 76, 77, 79, 81, 83, 84, 86, 88, 
                           89, 91, 93, 95, 96, 98, 100, 101, 103, 105, 107]


def test_applied_key_fs_minor():
    fs_minor = applied_key.Applied_Key('Fs', 'Aeolian')
    assert fs_minor.name == 'Fs Aeolian'
    assert fs_minor.root == 'Fs'
    assert applied_key.Starting_Pitch[fs_minor.root] == 66
    assert fs_minor.tones == (0, 2, 3, 5, 7, 8, 10)
    assert fs_minor.aps == [18, 20, 21, 23, 25, 26, 28, 30, 32, 
                            33, 35, 37, 38, 40, 42, 44, 45, 47, 
                            49, 50, 52, 54, 56, 57, 59, 61, 62, 
                            64, 66, 68, 69, 71, 73, 74, 76, 78, 
                            80, 81, 83, 85, 86, 88, 90, 92, 93, 
                            95, 97, 98, 100, 102, 104, 105, 107, 109, 110, 112]

