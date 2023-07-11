
@staticmethod
def get_slop_y_coords_after_rotate_90(vertex: Coordinate, e_start: Coordinate, e_end: Coordinate) -> Tuple[Coordinate, Coordinate, Coordinate]:
    '''
    Rotating e_end to be 90 degrees from +ve x axis, 
    then rotating vertex and e_start to perserve the Orientation
    This is to enable us to compare y values to ensure the inter_edge affect the correct vertices
    within its area of authority

    PLEASE REFER TO IPAD NOTES TO UNDERSTAND WHAT'S happening, pg-85

    '''
    # Get current angle of e_end
    s_e = Edge(e_start, e_end, None)
    s_v = Edge(e_start, vertex, None)
    h1 = s_e.absolute_length
    h2 = s_v.absolute_length
    beta = s_e.angle_from_x_axis
    alpha = s_v.angle_from_x_axis

    print(alpha, 'alpha')
    print(beta, 'beta')

    theta = 90 - beta
    print(theta, 'angle to move')

    r_vertex = vertex.rotate(theta, absolute_value=False)
    print(r_vertex, 'rec vertex rotated')

    # new rotated vertices to compare
    start_y = e_start.y
    end_y = start_y + h1
    vertex_y = r_vertex.y

    return start_y, end_y, vertex_y



def rotate(self, angle: float, absolute_value=True) -> Coordinate:
    '''
    returns the new coordinate of the point after  getting it to wanted angle from origin
    '''

    temp_e = Edge(Coordinate(0, 0), self, None)
    hypotenuse = temp_e.absolute_length
    new_angle = angle

    if not absolute_value:
        current_angle = round(atan(temp_e.gradient), 5)
        new_angle = current_angle + angle

    return Coordinate(round(hypotenuse*cos(new_angle), 5), round(hypotenuse*sin(new_angle), 5))

################################
        else:
            inter_comppad_y = e_gradient*intersection.comppad_coord.x + e_y_intercept
            if intersection.comppad_coord.y < inter_comppad_y:
                print('\n\n\nhererererer1\n\n\n')

                for vertex in vertices:
                    print('\ncurrent inputs\n', e_start, e_end, vertex, '\n')
                    start_y, end_y, vertex_y = Intersection.get_slop_y_coords_after_rotate_90(vertex, e_start, e_end)
                    print()
                    print(start_y, end_y, vertex_y, 'y_values')
                    if (vertex_y < end_y and vertex_y > start_y) or (vertex_y > end_y and vertex_y < start_y):  # edge start and end coordinates testing
                        inter_vertex_y = e_gradient*vertex.x + e_y_intercept
                        if vertex.y > inter_vertex_y:
                            print(vertex.y, inter_vertex_y, 'passed!')
                            inter_passed_vertices.add(vertex)

                    print('end\n')

            elif intersection.comppad_coord.y > inter_comppad_y:
                print(f'\n\n\nhererere2')

                for vertex in vertices:
                    print('\ncurrent inputs\n', vertex, e_start, e_end, '\n')
                    start_y, end_y, vertex_y = Intersection.get_slop_y_coords_after_rotate_90(vertex, e_start, e_end)
                    print()
                    print(start_y, end_y, vertex_y, 'y_values')
                    if (vertex_y < end_y and vertex_y > start_y) or (vertex_y > end_y and vertex_y < start_y):  # edge start and end coordinates testing
                        inter_vertex_y = e_gradient*vertex.x + e_y_intercept
                        if vertex.y < inter_vertex_y:
                            print(vertex.y, inter_vertex_y, 'passed!')
                            inter_passed_vertices.add(vertex)

                    print('end\n')

            else:  # inter_edge is exactly on comppad_coord, so can't decide will let the inter2 decide so will add all of them
                for vertex in vertices:

                    r_vertex, r_e_start, r_e_end = Intersection.rotate_vertices_90(vertex, e_start, e_end)
                    if (r_vertex.y < r_e_end.y and r_vertex.y > r_e_start.y) or (r_vertex.y > r_e_end.y and r_vertex.y < r_e_start.y):  # edge start and end coordinates testing
                        inter_passed_vertices.add(vertex)




