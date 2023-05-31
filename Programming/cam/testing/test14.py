
    @staticmethod
    def get_rec_passing_vertices(intersection: Intersection, edge: Edge, vertices: list[Coordinate]) -> tuple[set, set]:
        '''
        return the passing edges
        '''
        gradient_test_passed = set()
        range_test_passed = set()
        e_gradient = edge.gradient
        e_y_intercept = edge.y_intercept
        e_start = edge.start
        e_end = edge.end  # not used
        if e_gradient == Infinity(): 
            if intersection.comppad_coord.x < e_start.x:
                for vertex in vertices:
                    if (vertex.y < e_end.y and vertex.y > e_start.y) or (vertex.y > e_end.y and vertex.y < e_start.y):  # edge start and end coordinates testing
                        range_test_passed.add(vertex)

                    if vertex.x > e_start.x:  # continious line testing
                        gradient_test_passed.add(vertex)

            elif intersection.comppad_coord.x > e_start.x:
                for vertex in vertices:
                    if (vertex.y < e_end.y and vertex.y > e_start.y) or (vertex.y > e_end.y and vertex.y < e_start.y):  # edge start and end coordinates testing
                        range_test_passed.add(vertex)

                    if vertex.x < e_start.x:
                        gradient_test_passed.add(vertex)

            else:
                for vertex in vertices:
                    if (vertex.y < e_end.y and vertex.y > e_start.y) or (vertex.y > e_end.y and vertex.y < e_start.y):  # edge start and end coordinates testing
                        range_test_passed.add(vertices)

        elif e_gradient == 0: 
            if intersection.comppad_coord.y < e_start.y:
                for vertex in vertices:
                    if (vertex.x < e_end.x and vertex.x > e_start.x) or (vertex.x > e_end.x and vertex.x < e_start.x):  # edge start and end coordinates testing
                        range_test_passed.add(vertex)

                    if vertex.y > e_start.y:
                        gradient_test_passed.add(vertex)

            elif intersection.comppad_coord.y > e_start.y:
                for vertex in vertices:
                    if (vertex.x < e_end.x and vertex.x > e_start.x) or (vertex.x > e_end.x and vertex.x < e_start.x):  # edge start and end coordinates testing
                        range_test_passed.add(vertex)

                    if vertex.y < e_start.y:
                        gradient_test_passed.add(vertex)

            else:  # can't decide will let the inter2 decide so will add all of them
                for vertex in vertices:
                    if (vertex.x < e_end.x and vertex.x > e_start.x) or (vertex.x > e_end.x and vertex.x < e_start.x):  # edge start and end coordinates testing
                        range_test_passed.add(vertex)

        else:
            inter_comppad_y = e_gradient*intersection.comppad_coord.x + e_y_intercept
            if intersection.comppad_coord.y < inter_comppad_y:

                for vertex in vertices:
                    if vertex.within_edge(Edge(e_start, e_end, None), intersection.comppad_block.thickness):
                        range_test_passed.add(vertex)

                    inter_vertex_y = e_gradient*vertex.x + e_y_intercept
                    if vertex.y > inter_vertex_y:
                        gradient_test_passed.add(vertex)

            elif intersection.comppad_coord.y > inter_comppad_y:

                for vertex in vertices:
                    if vertex.within_edge(Edge(e_start, e_end, None), intersection.comppad_block.thickness):
                        range_test_passed.add(vertex)

                    inter_vertex_y = e_gradient*vertex.x + e_y_intercept
                    if vertex.y < inter_vertex_y:
                        gradient_test_passed.add(vertex)


            else:  # inter_edge is exactly on comppad_coord, so can't decide will let the inter2 decide so will add all of them
                for vertex in vertices:
                    if vertex.within_edge(Edge(e_start, e_end, None)):
                        range_test_passed.add(vertex)

        return (gradient_test_passed, range_test_passed)



def generate_comppad_nodes_rectangle()
### in the 'generate_comppad_nodes_rectangle()'
        # Getting vertices that are outside intersection edge 1
        grad_passed1, range_passed1 = Intersection.get_rec_passing_vertices(intersection, intersection.inter1_edge, vertices)

        # Getting vertices that is outside intersection edge 2
        grad_passed2, range_passed2 = Intersection.get_rec_passing_vertices(intersection, intersection.inter2_edge, vertices)

        passed_vertices = set()
        ### Now that we have which rec vertex passed which gradient and range tests, we can decide which vertex pass
        for vertex in vertices:
            print('\n\n\n', vertex)

            ### vertices that pass both gradient and range test are definitly IN
            if (vertex in grad_passed1 and vertex in range_passed1) or (vertex in grad_passed2 and vertex in range_passed2):
                passed_vertices.add(vertex)

            ### vertices that are out of range in both inter1 and inter2 edges 
            ### AND are in the other side of the inter_edges relative to the comppad_coord
            ### should be alowed too ;)
            # getting the small angle between the two inter_edges
            # angle = round(intersection.inter2_edge.angle_between(intersection.inter1_edge.reversed()))  #TODO: this should be executed once outside of this loop
            edge1 = intersection.inter1_edge.reversed()
            edge2 = Edge(nodes_tobe_removed.vertex, nodes_tobe_removed.parent.vertex, None)
            angle = round(edge1.angle_between(edge2))
            print(angle)

            if angle != 0 and angle != 180 and angle != 360:  # 0 or 180 or 360 couldn't be inverted, doesn't matter where the comppad_coord is
                ### Determining whether the angle measured is in the same side as the comppad_coord, 
                # if so then we must get the other angle (360-angle) 
                # if intersection.inter1_edge.end == intersection.inter2_edge.start:
                edges = [intersection.inter1_edge, intersection.inter2_edge]

                # else:
                #     # a intersection between two inter_edges that are not connected only happens in deadends!
                #     # which has angle 0 or 360 so it must never have passed
                #     # could be two very skewed edges
                #     raise ValueError("OH SHIT!!! NEVER ENCOUNTERED THIS BEFORE")

                comppad_side = intersection.comppad_coord.get_side_open_polygon(intersection.pre_inter1_node, intersection.pre_inter2_node.parent)
                print('comppad_side', comppad_side)
                angle_side = Edge(intersection.inter1_edge.start, intersection.inter2_edge.end, None).midpoint.get_side_open_polygon(intersection.pre_inter1_node.parent, intersection.pre_inter2_node.parent)
                print('angle_side', angle_side)

                if comppad_side == angle_side:
                    angle = 360 - angle

            #TODO: must do (360-angle) according to comppad_coord relative to the 2 inter_edges
            if angle > 180 or angle == 0:
                if (vertex not in range_passed1 and vertex not in range_passed2):
                    passed_vertices.add(vertex)

        print(passed_vertices)
        print('\n\n\n')



