]
        break_prev_iter = False
        find_second_intersection = False
        # Step 1: Identify intersection 1
        for edges_ind, edges in enumerate(list(self.vertex_edge.values())):
            for edge_ind, edge in enumerate(edges):
                for block in blocks:
                    for coordinate in block.coordinates:

                        intersections = Coordinate.point_edge_intersection(edge, coordinate, block)
                        if intersections:
                            if intersections[0] in [inter_data[-1] for inter_data in intersection_data]:
                                # make sure this intersection is not the second intersection of a previous set of intersections
                                break_prev_iter = True
                                break

                            # Step 2: Identify intersection 2
                            if not find_second_intersection:
                                if len(intersections) == 2:
                                    # second intersectio on the same line
                                    intersection1 = intersections[0]
                                    intersection2 = intersections[1]

                                    intersection_data.append([edges_ind, edge_ind, edges_ind, edge_ind, coordinate, 
                                        block.thickness, block.thickness2, block.shape_type, intersection1, intersection2])

                                    break_prev_iter = True
                                    break

                                elif len(intersections) == 1:
                                    intersection1 = intersections[0]

                                    # Must find the second intersection
                                    if edges_ind == len(self.vertex_edge):
                                        edges_ind = -1
                                    if edge_ind == len(self.vertex_edge[edges_ind]):
                                        edge_ind = -1
                                    for edges_ind2, edges2 in enumerate(list(self.vertex_edge.values())[edges_ind+1:]):
                                        for edge_ind2, edge2 in enumerate(edges[edge_ind+1:]):
                                            intersections = Coordinate.point_edge_intersection(edge2, coordinate, block)
                                            if intersections:
                                                if len(intersections) == 1:
                                                    edges_ind2 += edges_ind+1
                                                    edge_ind2 += edge_ind+1
                                                    intersection_data.append([edges_ind, edge_ind, edges_ind2, edge_ind2,
                                                        coordinate, block.shape_type, block.thickness, block.thickness2,
                                                        intersection1, intersection2])
                                                    
                                                    break_prev_iter = True
                                                    break

                                                else:
                                                    raise ValueError('second intersection not in same edge MUST ONLY have one number of intersections!!!')
                                        if break_prev_iter:
                                            break
                                else:
                                    raise ValueError('>2 intersection ?!?!??!?!')

                    if break_prev_iter:
                        break_prev_iter = False
                        break

        print(intersection_data)

