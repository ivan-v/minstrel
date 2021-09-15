from math import ceil

def find_point(current_time, absolute_times, values):
    closest_times = find_nearest_values(current_time, absolute_times)
    if ('smaller_val' not in closest_times and 'larger_val' in closest_times) or \
       ('larger_val' not in closest_times and 'smaller_val' in closest_times):
        location = 'larger_val' if 'larger_val' in closest_times else 'smaller_val'
        return values[closest_times[location][0]]
    else:
        coord1 = (closest_times['smaller_val'][1], values[closest_times['smaller_val'][0]])
        coord2 = (closest_times['larger_val'][1], values[closest_times['larger_val'][0]])
        return find_y_at_x(coord1, coord2, current_time)


def find_y_at_x(coord1, coord2, x3):
    return (((coord2[1] - coord1[1]) / (coord2[0] - coord1[0]))*(x3 - coord1[0])) + coord1[1]


def find_nearest_values(value, arr):
    # assumes sorted list 
    prev_val = ''
    smaller_val = ''
    for i, val in enumerate(arr):
        if val < value:
            smaller_val = val
            smaller_i = i
        elif val > value:
            if smaller_val != '':
                return {'smaller_val': (smaller_i, smaller_val), 'larger_val': (i, val)}
            else:
                return {'larger_val': (i, val)}
        prev_val = val
    return {'smaller_val': (len(arr)-1, prev_val)}


def emotions_by_absolute_times(given_emotions, absolute_times):
    return list(zip(*[[given_emotions[emotion][absolute_times.index(current_time)] if current_time in absolute_times 
           else find_point(current_time, absolute_times, given_emotions[emotion]) for current_time in range(ceil(absolute_times[-1]+1))]
        for emotion in given_emotions]))


class Emotions:
    def __init__(self, given_emotions, absolute_times):
        self.old_times = absolute_times
        self.given_emotions = given_emotions
        self.emotions_over_time = emotions_by_absolute_times(given_emotions, absolute_times)

