import chord

def test_chord_c_major_b5():
    test_chord = chord.Chord(root='C', type='M', operating_bit='b5')
    assert test_chord.root == 'C'
    assert test_chord.type == 'M'
    assert test_chord.operating_bit == 'b5'
    assert test_chord.aps == [[12, 16, 19, 6], [24, 28, 31, 18], 
                              [36, 40, 43, 30], [48, 52, 55, 42], 
                              [60, 64, 67, 54], [72, 76, 79, 66], 
                              [84, 88, 91, 78], [96, 100, 103, 90]]