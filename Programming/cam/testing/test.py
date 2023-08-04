from __future__ import annotations


def check_rec_coords_order(ordered_rec_coords: list, rec_vertices: list[Coordinate, Coordinate, Coordinate, Coordinate]) -> bool:
    '''
    checks the rectangle coord whether they are indeed in order or form a weird shape not a rectangle
    '''
    rec_vertices.extend(rec_vertices)  # to ensure if we start from the last index we go back to first
    first_element_ind = rec_vertices.index(ordered_rec_coords[0])  # it always finds the first occurance so must work
    for increment, coord in enumerate(ordered_rec_coords):
        if coord != rec_vertices[first_element_ind+increment]:
            return False

    return True


rec_vertices = [1, 2, 3, 4]

tests = [[3, 4, 1, 2], [4, 1, 2, 3], [2, 3, 4, 1], [1, 2, 3, 4], [4, 3, 2, 1], [4, 2, 3, 4], [1, 1, 2, 3], [2, 1, 3, 4]]

for test in tests:
    print(check_rec_coords_order(test, rec_vertices))
