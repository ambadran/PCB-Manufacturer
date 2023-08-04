

        min_v_inter1 = Edge(intersection.inter1_coord, passed_vertices[0], None).absolute_length
        min_v_1 = passed_vertices[0]
        min_v_inter2 = Edge(intersection.inter2_coord, passed_vertices[0], None).absolute_length
        min_v_2 = passed_vertices[0]
        for vertex in passed_vertices[1:]:
            current_v_inter1 = Edge(intersection.inter1_coord, vertex, None).absolute_length
            current_v_inter2 = Edge(intersection.inter2_coord, vertex, None).absolute_length

            if current_v_inter1 < min_v_inter1:
                min_v_inter1 = current_v_inter1
                min_v_1 = vertex

            if current_v_inter2 < min_v_inter2:
                min_v_inter2 = current_v_inter2
                min_v_2 = vertex

        the_rest = [v for v in passed_vertices if (v != min_v_1 and v != min_v_2)]
        if len(the_rest) == 0:
            middle_vertices = []

        elif len(the_rest) == 1:
            middle_vertices = the_rest

        elif len(the_rest) == 2:
            min_v_inter1_1 = Edge(intersection.inter1_coord, the_rest[0], None).absolute_length
            min_v_inter1_2 = Edge(intersection.inter1_coord, the_rest[1], None).absolute_length

            if min_v_inter1_1 < min_v_inter1_2:
                middle_vertices = [the_rest[0], the_rest[1]]

            else:
                middle_vertices = [the_rest[1], the_rest[0]]

        else:
            raise ValueError("Rectangles now have more than 4 vertices ;;;)")

        ordered_rec_coords = []
        ordered_rec_coords.append(min_v_1)
        ordered_rec_coords.extend(middle_vertices)
        if min_v_1 != min_v_2:  # preventing duplicates
            ordered_rec_coords.append(min_v_2)

        if not Intersection.rec_coords_order_correct(ordered_rec_coords, vertices):
            raise ValueError("incorrect order")


