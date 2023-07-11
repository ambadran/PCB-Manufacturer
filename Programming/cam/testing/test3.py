
num = 1.000001

print(round(num, 2))

def get_max_decimal_place(value: float) -> int:
    '''
    finds out how much decimal places does the number has

    :param value: the value to be tested for how much decimal places
    :returns: the number of decimal places of parameter value
    '''
    num_dec_places = 0
    while round(value, num_dec_places) != value:
        num_dec_places += 1

    return num_dec_places

print(get_max_decimal_place(num))


def increment_current_decimal_point(value: float, current_decimal_points: int, max_dec_places: int) -> float:
    '''
    increment the argument value in the wanted current_decimal_points decimal value

    :param value: value to be incremented
    :param current_decimal_points: which decimal place to increment the value
    :return: incremented value in the wanted decimal place
    '''
    num_to_increment = 10**-current_decimal_points
    return_value = round(value+num_to_increment, max_dec_places)
    return return_value


print(increment_current_decimal_point(num, 4, 8))



    found = False
    do = True
    if do:
        while not found:
            print('\n\n\nfirst loop')
            while num_ys >= num_ys_min_value and not found:
                print('\n\nsecond loop')
                while overlapping_distance <= OD_max_value:
                    print('\nthird loop')

                    # Equation to find overlapping_distance according to given inputs, mainly the num_ys
                    overlapping_distance_unrounded = (tip_thickness+num_ys*tip_thickness-y_length) / (num_ys + 2)
                    overlapping_distance = round(overlapping_distance_unrounded, 2)
                    print(num_ys, overlapping_distance, overlapping_distance_unrounded, 'current iteration')

                    # If wanted number of decimal places achieved, Goal Found :)
                    print(get_max_decimal_place(overlapping_distance), current_decimal_points, 'goal test')
                    if get_max_decimal_place(overlapping_distance) <= current_decimal_points:
                        found = True
                        break

                    overlapping_distance = increment_current_decimal_point(overlapping_distance, current_decimal_points)
                    print(overlapping_distance, '; incremented OD')


                num_ys -= 1
                overlapping_distance = OD_min_value

            current_decimal_points += 1
            num_ys = num_ys_max_value

            if current_decimal_points > 3:
                break
            if current_decimal_points >= dec_point_max_value:
                raise ValueError('too much decimal points')








