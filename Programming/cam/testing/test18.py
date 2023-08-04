vertices = [1, 2, 3, 4]

passed_vertices = [1, 4, 3]  # should be 3, 4, 1


rec_coords_extended = vertices
rec_coords_extended.extend(vertices)

for first_coord in passed_vertices:
    ordered_rec_coords = [first_coord]
    first_element_ind = rec_coords_extended.index(first_coord)  # it always finds the first occurance so must work
    print(f"Trying first element: {first_coord}")

    for increment in range(1, len(passed_vertices)):
        next_correct_coord = rec_coords_extended[first_element_ind+increment]
        print(f"Next correct coord: {next_correct_coord}")

        if next_correct_coord in passed_vertices:
            print('next correct coord passed')
            ordered_rec_coords.append(next_correct_coord)

        else:  
            print('next correct coord failed, breaking and trying another first coord...\n')
            # next correct coord not in passed vertices so must try another first coord
            break

        print()

    else:  
        print(f'Successfully found correct sequence!!!!\nOrdered sequence is: {ordered_rec_coords}')
        # all passed_vertices were correctly found in order so stopping the loop and continuing with found ordered_rec_coords
        break

    print('\n')

else:
    raise ValueError(f"Somehow couldn't recreate a correct sequence from passed_vertices {passed_vertices}")

