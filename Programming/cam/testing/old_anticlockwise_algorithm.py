        ### Sequence to Sort Edges nearst edge anti-clockwise to furthest
        ### Look at iPad for detailed explanation
        # 1- Get ALL edges in one list including the main edge to compare to later
        edge_list = deepcopy(edge_list_param)
        if self in edge_list:
            raise ValueError("OG MUST NOT BE IN EDGE_LIST, it will interfere with same gradient edge selection process")

        # 2- Seperate the edge_list to edge list of 'first priority edges' and 'second priority edges'
        first_priority_edges = []
        second_priority_edges = []
        is_edge_under = lambda edge: (edge.end.y) < (self.gradient*edge.end.x + self.y_intercept)
        is_edge_above = lambda edge: (edge.end.y) > (self.gradient*edge.end.x + self.y_intercept)
        is_on_edge = lambda edge: (edge.end.y) == (self.gradient*edge.end.x + self.y_intercept)
        middle_priority_edge = None
        least_priority_edge = None

        if self.delta_x < 0:

            for edge in edge_list:
                if is_edge_above(edge):
                    first_priority_edges.append(edge)

                elif is_edge_under(edge):
                    second_priority_edges.append(edge)

                elif is_on_edge(edge):
                    if edge.delta_x < 0:
                        middle_priority_edge = edge

                    elif edge.delta_x > 0:
                        least_priority_edge = edge

                    else:
                        raise ValueError("I put this because i am paranoid")

                else:
                    raise ValueError("I put this because i am paranoid")

        elif self.delta_x > 0:

            for edge in edge_list:
                if is_edge_above(edge):
                    second_priority_edges.append(edge)

                elif is_edge_under(edge):
                    first_priority_edges.append(edge)

                elif is_on_edge(edge):
                    if edge.delta_x > 0:
                        middle_priority_edge = edge

                    elif edge.delta_x < 0:
                        least_priority_edge = edge

                    else:
                        raise ValueError("I put this because i am paranoid")

                else:
                    raise ValueError("I put this because i am paranoid")


        elif self.delta_x == 0:
            print("lskdjfplakjsdf;lkjasd;lkfj!!!!!!")

            if self.delta_y < 0:

                for edge in edge_list:
                    if edge.delta_x < 0:
                        first_priority_edges.append(edge)

                    elif edge.delta_x > 0:
                        second_priority_edges.append(edge)

                    elif edge.delta_x == 0:
                        if edge.delta_y < 0:
                            middle_priority_edge = edge

                        elif edge.delta_y > 0:
                            least_priority_edge = edge

                        else:
                            raise ValueError("I put this because i am paranoid")

                    else:
                        raise ValueError("I put this because i am paranoid")

            elif self.delta_y > 0:

                for edge in edge_list:
                    if edge.delta_x > 0:
                        first_priority_edges.append(edge)

                    elif edge.delta_x < 0:
                        second_priority_edges.append(edge)

                    elif edge.delta_x == 0:
                        if edge.delta_y > 0:
                            middle_priority_edge = edge

                        elif edge.delta_y < 0:
                            least_priority_edge = edge

                        else:
                            raise ValueError("I put this because i am paranoid")

                    else:
                        raise ValueError("I put this because i am paranoid")

        else:
            raise ValueError("I put this because i am paranoid")

        # 3- Sort each list in ascending order
        first_priority_edges_ordered = sorted(first_priority_edges, key=lambda x: x.gradient)
        second_priority_edges_ordered = sorted(second_priority_edges, key=lambda x: x.gradient)

        # 4- Finally, Create the Final Correctly orderd list :)
        final_list = []
        final_list.extend(first_priority_edges_ordered)

        if middle_priority_edge:
            final_list.append(middle_priority_edge)

        final_list.extend(second_priority_edges_ordered)

        if least_priority_edge:
            final_list.append(least_priority_edge)

        debug = True
        if debug:
            print()
            print(edge_list, 'initial edge_list', len(edge_list), 'edges')
            print()
            print(first_priority_edges, 'first priority')
            print(middle_priority_edge, 'middle priority edge')
            print(second_priority_edges, 'second priority')
            print(least_priority_edge, 'least priority edge')
            print()
            print(first_priority_edges_ordered, 'orderd first priority')
            print(middle_priority_edge, 'middle priority edge')
            print(second_priority_edges_ordered, 'orderd second priority')
            print(least_priority_edge, 'least priority edge')
            print()

        return final_list


