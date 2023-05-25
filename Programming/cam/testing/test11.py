        if (intersection.inter1_edge.gradient == intersection.inter2_edge.gradient) and not intersection.inter1_edge.is_same_direction(intersection.inter2_edge):  # aka deadend

            trace_gradient = intersection.inter1_edge.gradient
            if trace_gradient == Infinity():
                for vertex in vertices:
                    if (vertex.x < intersection.inter1_edge.start.x) != (vertex.x > intersection.inter2_edge.start.x):
                        wanted_vertices.append(vertex)

            elif trace_gradient == 0:
                for vertex in vertices:
                    if (vertex.y < intersection.inter1_edge.start.y) != (vertex.y > intersection.inter2_edge.start.y):
                        wanted_vertices.append(vertex)

            else:
                for vertex in vertices:
                    rec_y = vertex.y
                    inter1_edge_y = intersection.inter1_edge.gradient*vertex.x + intersection.inter1_edge.y_intercept
                    inter2_edge_y = intersection.inter2_edge.gradient*vertex.x + intersection.inter2_edge.y_intercept

                    if (rec_y < inter1_edge_y) != (rec_y > inter2_edge_y):
                        wanted_vertices.append(vertex)

        else:
            pass #TODO: CONTINUE DEVELOPMENT HERERERE 25/5


