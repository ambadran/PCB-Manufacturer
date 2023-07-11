        inv_edge_pass_vs = set()
        if intersection.inter1_edge.gradient == intersection.inter2_edge.gradient and intersection.inter1_edge.is_same_direction(intersection.inter2_edge.reversed()):
            print('happennned')
            raise ValueError()
            inverse_edge = Edge(intersection.inter1_edge.end, intersection.inter2_edge.start, None)
            if inverse_edge.gradient == Infinity(): 
                if intersection.comppad_coord.x < (inverse_edge.start.x+ round(intersection.comppad_block.thickness/2, 3)):
                    for vertex in vertices:
                        if vertex.x > inverse_edge.start.x:
                            inv_edge_pass_vs.add(vertex)

                elif intersection.comppad_coord.x > (inverse_edge.start.x + round(intersection.comppad_block.thickness/2, 3)):
                    for vertex in vertices:
                        if vertex.x < inverse_edge.start.x:
                            inv_edge_pass_vs.add(vertex)

                else:
                    inv_edge_pass_vs.update(set(vertices))

            elif inverse_edge.gradient == 0: 
                if intersection.comppad_coord.y < (inverse_edge.start.y + round(intersection.comppad_block.thickness/2, 3)):
                    for vertex in vertices:
                        if vertex.y > inverse_edge.start.y:
                            inv_edge_pass_vs.add(vertex)

                elif intersection.comppad_coord.y > (inverse_edge.start.y + round(intersection.comppad_block.thickness/2, 3)):
                    for vertex in vertices:
                        if vertex.y < inverse_edge.start.y:
                            inv_edge_pass_vs.add(vertex)

                else:  # can't decide will let the inter2 decide so will add all of them
                    inv_edge_pass_vs.update(set(vertices))

            else:
                inter1_comppad_y = inverse_edge.gradient*intersection.comppad_coord.x + inverse_edge.y_intercept + round(intersection.comppad_block.thickness/2, 3)
                if intersection.comppad_coord.y < inter1_comppad_y:
                    print('hererere')
                    for vertex in vertices:
                        inter1_vertex_y = inverse_edge.gradient*vertex.x + inverse_edge.y_intercept
                        if vertex.y > inter1_vertex_y:
                            inv_edge_pass_vs.add(vertex)

                elif intersection.comppad_coord.y > inter1_comppad_y:
                    print('hererererer222222222')
                    print(inverse_edge, 'inverse_edge')
                    print(inter1_comppad_y, 'inter1_comppad_y')
                    for vertex in vertices:
                        inter1_vertex_y = inverse_edge.gradient*vertex.x + inverse_edge.y_intercept
                        if vertex.y < inter1_vertex_y:
                            inv_edge_pass_vs.add(vertex)

                else:  # can't decide will let the inter2 decide so will add all of them
                    inv_edge_pass_vs.update(set(vertices))


