from __future__ import annotations
from typing import Optional
from dataclasses import dataclass
from copy import deepcopy
import turtle
import random
import math
from enum import Enum


class Infinity():
    def __init__(self):
        self.value = 'infinity'

    def __add__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __sub__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __mul__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __truediv__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __lt__(self, other) -> bool:
        '''
        less than method definition
        '''
        if type(other) != int and type(other) != float and type(other) != Infinity:
            raise ValueError("must compare infinity to numbers only")

        return False

    def __eq__(self, other) -> bool:
        '''
        equal than method definition
        '''
        if type(other) != int and type(other) != float and type(other) != Infinity:
            raise ValueError("must compare infinity to numbers only")

        if type(other) == Infinity:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        '''
        greater than method definition
        '''
        if type(other) != int and type(other) != float and type(other) != Infinity:
            raise ValueError("must compare infinity to numbers only")

        if type(other) == Infinity:
            return False
        else:
            return True

    def __str__(self) -> str:
        return '<Infinity bitches>'

LASER_BEAM_THICKNESS = 0.05

@dataclass
class Coordinate:
    x: int | float
    y: int | float
    z: Optional[int | float] = None
    d: Optional[int] = None

    def __eq__(self, other: Coordinate) -> bool:
        '''
        defines equality between coordinates
        '''
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        z = "" if self.z is None else f"Z{self.z}"
        return f"(X{self.x}Y{self.y}{z})"

    def __getitem__(self, index) -> float:
        '''
        Enable slicing of coordinate objects
        '''
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Only X, Y, Z values available")

    def __len__(self) -> int:
        '''
        return whether it's x,y or x,y,z
        '''
        if self.z is None:
            return 2
        else:
            return 3

    @classmethod
    def get_min_max(cls, coordinates_list: list[Coordinate]) -> tuple[Coordinate, Coordinate]:
        '''
        finds the Min, Max of X and Y coordinates from input list of coordinates

        :param coordinates: list of coordinates [(x, y), ..]
        :return: ((x_min, y_min), (x_max, y_max))
        '''

        x_min, y_min = coordinates_list[0].x, coordinates_list[0].y
        x_max, y_max = x_min, y_min

        for coordinate in coordinates_list:

            new_x, new_y = coordinate.x, coordinate.y

            if new_x < x_min:
                x_min = new_x

            elif new_x > x_max:
                x_max = new_x

            if new_y < y_min:
                y_min = new_y

            elif new_y > y_max:
                y_max = new_y

        return Coordinate(x_min, y_min), Coordinate(x_max, y_max)

    @classmethod
    def generate_semicircle_coordinates(cls, coordinate1: Coordinate, coordinate2: Coordinate, resolution: int =100) -> list[Coordinate]:
        '''
        :param coordinate1: The coordinate the list of semicircle coordinates start from
        :param coordinate2: The coordinate the list of semicircle coordinates ends at
        :param resolution: The number of coordinates in the list of semicircle coordinates

        :return: list of coordinates that if joined with straight makes a pseudo semicircle
        '''
        ### Step 1: Get circle equation attributes
        # a and b are the x and y offset value from circle center respectively
        # They are also the midpoints between coord1 and coord2
        a = round((coordinate1.x + coordinate2.x) / 2, 3)
        b = round((coordinate1.y + coordinate2.y) / 2, 3)

        # r is the radius of circle
        # It's also the half length form coordinate1 to coordinate2
        r = round( (math.sqrt( (coordinate2.x - coordinate1.x)**2 + (coordinate2.y - coordinate1.y)**2 ) / 2) , 3)

        ### Step 2: Get linear equation of the line that passes through the circle diameter, aka the 2 coordinates
        # Get the linear equation of the diameter coordinates
        if coordinate2.x == coordinate1.x:
            gradient = Infinity()
            y_intercept = None

            # Get the linear equation of the inverse of the diameter linear equation
            inverse_gradient= 0.0
            inverse_y_intercept = b

            raise ValueError("NOT IMPLEMENTED YET")

        elif coordinate2.y == coordinate1.y:
            gradient = 0.0
            y_intercept = a ### NOT SURE

            # Get the linear equation of the inverse of the diameter linear equation
            inverse_gradient = Infinity()
            inverse_y_intercept = None

            raise ValueError("NOT IMPLEMENTED YET")

        else:
            gradient = (coordinate2.y - coordinate1.y) / (coordinate2.x - coordinate1.x)
            y_intercept = coordinate1.y - gradient*coordinate1.x

            # Get the linear equation of the inverse of the diameter linear equation
            inverse_gradient = round(-1/gradient, 3)
            inverse_y_intercept = b - inverse_gradient*a

            ### Step 3: Getting linear equation of tangent to the circle at the maximum
            # This is done by solving simultaneous equation of circle and the inverse linear equation
            # This is done to get the coordinates of the maximum and minimum points on the circle relative to our coordinates
            # The following equations I completely derived on my own on the iPad
            a_q = 1 + inverse_gradient**2
            b_q = -2*a + 2*inverse_gradient*inverse_y_intercept - 2*b*inverse_gradient
            c_q = inverse_y_intercept**2 - 2*b*inverse_y_intercept + b**2 - r**2 + a**2

            # Now I have the quadratic equation 
            # a_q * x**2 + b_q * x + c_q = 0
            # Solving quadratic equation using quadratic formula
            x1 = round((-b_q + math.sqrt(b_q**2 - 4*a_q*c_q)) / (2*a_q), 3)
            x2 = round((-b_q - math.sqrt(b_q**2 - 4*a_q*c_q)) / (2*a_q), 3)

            # Getting values of y by substituting in inverse linear equation
            y1 = inverse_gradient*x1 + inverse_y_intercept
            y2 = inverse_gradient*x2 + inverse_y_intercept


            # Getting linear equation of maximum point and saving it in a variable, (ignoring minimum point)
            maximum_point_coordinate = Coordinate(x1, y1)
            print(maximum_point_coordinate, 'lksjdflksjdkfj')
            maximum_line_gradient = gradient
            maximum_line_y_intercept = y1 - maximum_line_gradient*x1

            ### Step 4: Getting the list of y_intercepts of linear equations that intersects the circle
            y_intercept_range = maximum_line_y_intercept - y_intercept  #TODO: Adapt this for gradient=Infinity()
            num_iterations = resolution/2 - 1
            increment = y_intercept_range / num_iterations
            y_intercept_list = []  #NOTE: It is meant to not include the last coordinate, the maximum_line coordinate, (x1, y1)
            increment_sum = increment
            for _ in range(round(num_iterations)):
                y_intercept_list.append(y_intercept + increment_sum)
                increment_sum += increment

            ### Step 5: Getting the intersection between circle equation and all the intersection linear equations
            # from the diameter to the maximum line.
            semicircle_coords_from_right = []
            semicircle_coords_from_left = []
            for current_y_intercept in y_intercept_list:
                a_q = 1 + gradient**2
                b_q = -2*a + 2*gradient*current_y_intercept - 2*b*gradient
                c_q = current_y_intercept**2 - 2*b*current_y_intercept + b**2 - r**2 + a**2

                x1 = round((-b_q + math.sqrt(b_q**2 - 4*a_q*c_q)) / (2*a_q), 6)
                y1 = inverse_gradient*x1 + inverse_y_intercept
                semicircle_coords_from_right.append(Coordinate(x1, y1))

                x2 = round((-b_q - math.sqrt(b_q**2 - 4*a_q*c_q)) / (2*a_q), 6)
                y2 = inverse_gradient*x2 + inverse_y_intercept
                semicircle_coords_from_left.append(Coordinate(x2, y2))

            ### Step 6: Get the final ordered list of coordinates
            ordered_semicircle_coords = []
            ordered_semicircle_coords.extend(semicircle_coords_from_right)
            # ordered_semicircle_coords.append(maximum_point_coordinate)
            ordered_semicircle_coords.extend(semicircle_coords_from_left)

            return ordered_semicircle_coords

@dataclass
class Edge:
    start: Coordinate 
    end: Coordinate
    thickness: float

    @property
    def delta_x(self) -> float:
        '''
        :return delta x
        '''
        return self.end.x - self.start.x

    @property
    def delta_y(self) -> float:
        '''
        :return delta y
        '''
        return self.end.y - self.start.y
    
    @property
    def gradient(self) -> float:
        '''
        Assumes the edge as a linear equation
        m = (y2-y1)/(x2-x1)

        :returns: gradient of the edge
        '''
        try:
            return round(self.delta_y / self.delta_x, 3)
        except ZeroDivisionError:
            return Infinity() 

    @property
    def y_intercept(self) -> float:
        '''
        Assumes the edge as linear equation
        y=mx+c
        c=y-mx
        taking y as y1 and x as x1 

        :return: y intercept of the edge
        '''
        return self.start.y - self.gradient*self.start.x

    def anticlockwise_successors(self, edge_list) -> list[Edge]:
        '''
        :returns: a list of the right most edge to the left most edge relative to self
        '''
        ### Step 1: Put inverted OG edge into the edge list
        inverted_og = self.reversed()
        include_inverted_og = True
        if inverted_og not in edge_list:
            include_inverted_og = False
            edge_list.append(inverted_og)

        ### Step 2: Get all edges in there correct Quadrant
        quadrants = [[], [], [], []]
        for edge in edge_list:

            if edge.delta_x >= 0 and edge.delta_y >= 0:
                quadrants[0].append(edge)

            elif edge.delta_x > 0 and edge.delta_y < 0:
                quadrants[3].append(edge)

            elif edge.delta_x < 0 and edge.delta_y > 0:
                quadrants[1].append(edge)

            elif edge.delta_x <= 0 and edge.delta_y <= 0:
                quadrants[2].append(edge)

            else:
                raise ValueError("WTF?!??!")

        ### Step 3: Get each Quadrant list in order
        sorted_quadrants = [[], [], [], []]
        for ind, quadrant in enumerate(quadrants):
            sorted_quadrants[ind] = sorted(quadrant, key= lambda x: x.gradient)

        ### Step 4: Split the list with the inverted OG into 'prelist' and 'post list'
        if inverted_og.delta_x >= 0 and inverted_og.delta_y >= 0:
            og_index = sorted_quadrants[0].index(inverted_og)

            pre_list = sorted_quadrants[0][:og_index]
            post_list = sorted_quadrants[0][og_index+1:]

            quadrant_order = [1, 2, 3]

        elif inverted_og.delta_x > 0 and inverted_og.delta_y < 0:
            og_index = sorted_quadrants[3].index(inverted_og)

            pre_list = sorted_quadrants[3][:og_index]
            post_list = sorted_quadrants[3][og_index+1:]

            quadrant_order = [0, 1, 2]

        elif inverted_og.delta_x < 0 and inverted_og.delta_y > 0:
            og_index = sorted_quadrants[1].index(inverted_og)

            pre_list = sorted_quadrants[1][:og_index]
            post_list = sorted_quadrants[1][og_index+1:]

            quadrant_order = [2, 3, 0]

        elif inverted_og.delta_x <= 0 and inverted_og.delta_y <= 0:
            og_index = sorted_quadrants[2].index(inverted_og)

            pre_list = sorted_quadrants[2][:og_index]
            post_list = sorted_quadrants[2][og_index+1:]

            quadrant_order = [3, 0, 1]

        if include_inverted_og:
            pre_list.append(inverted_og)


        ### Step 5: Creating the final list :)
        final_list = []

        final_list.extend(post_list)
        final_list.extend(sorted_quadrants[quadrant_order[0]])
        final_list.extend(sorted_quadrants[quadrant_order[1]])
        final_list.extend(sorted_quadrants[quadrant_order[2]])
        final_list.extend(pre_list)

        debug = False
        if debug:
            print()
            print(edge_list, 'initial edge_list', len(edge_list), 'edges')
            print()
            print(quadrants[0], 'Q1')
            print(quadrants[1], 'Q2')
            print(quadrants[2], 'Q3')
            print(quadrants[3], 'Q4')
            print()
            print(post_list, 'post list')
            print(sorted_quadrants[quadrant_order[0]], f'quadrant{quadrant_order[0]}')
            print(sorted_quadrants[quadrant_order[1]], f'quadrant{quadrant_order[1]}')
            print(sorted_quadrants[quadrant_order[2]], f'quadrant{quadrant_order[2]}')
            print()



        return final_list

    def reversed(self) -> Edge:
        '''
        return the reversed Edge
        '''
        return Edge(self.end, self.start, self.thickness)

    @classmethod
    def visualize_edges(cls, edges: list[Edge], hide_turtle=True, speed=0, offset=20, line_width=3, multiplier=8, terminate=False) -> None:
        '''
        visualizes the sequence of edges in a list 
        '''
        skk = turtle.Turtle()
        turtle.width(line_width)
        turtle.speed(speed)
        if hide_turtle:
            turtle.hideturtle()
        else:
            turtle.showturtle()

        colors = ['black', 'red', 'blue', 'light blue', 'green', 'brown', 'dark green', 'orange', 'gray', 'indigo']
        color = random.choice(colors)
        while color in Graph.used_colors:
            color = random.choice(colors)

        turtle.pencolor(color)

        turtle.up()

        turtle.setpos((edges[0].start.x - offset) * multiplier, (edges[0].start.y - offset) * multiplier)
        for edge in edges:
            turtle.down()
            turtle.setpos((edge.start.x - offset) * multiplier, (edge.start.y - offset) * multiplier)
            turtle.setpos((edge.end.x - offset) * multiplier, (edge.end.y - offset) * multiplier)
            turtle.up()

        Graph.used_colors.add(color)
        if len(Graph.used_colors) == len(colors):
            print('\n\n!!!!!!!!!! COLORS RESET !!!!!!!!!!!!!!!!!\n\n')
            Graph.used_colors = set()

        if terminate:
            turtle.done()

    def intersection(self, other: Edge) -> Coordinate:
        '''
        :param self: the first edge 
        :param other: the second edge 

        returns the coordinate of intersection between self and other
        '''
        if type(self.gradient) != Infinity() and type(other) != Infinity():
            if (prev_gradient - gradient) != 0:
                x = round((y_intercept - prev_y_intercept) / (prev_gradient - gradient), 3)
                y = round(gradient * x + y_intercept, 3)
                return Coordinate(x, y)
            else:
                return None

        elif type(self.gradient) == Infinity() and type(other) != Infinity():
            x = self.start.x
            y = round(other.gradient*x + other.y_intercept, 3)
            return Coordinate(x, y)

        elif type(self.gradient) != Infinity() and type(other) == Infinity():
            x = other.start.x
            y = round(self.gradient*x + self.y_intercept, 3)
            return Coordinate(x, y)

        elif type(self.gradient) == Infinity() and type(other) == Infinity():
            # it's either infinite intersections if same line or no intersection if different lines
            return None

    def is_same_direction(self, other: Edge) -> bool:
        '''
        :param self: edge1
        :param other: edge2

        :returns: whether the two edges are on point to the same direction or not
        '''
        if self.gradient != other.gradient:
            return False

        if self.gradient != Infinity():
            return (self.delta_x > 0 and other.delta_x > 0) or (self.delta_x < 0 and other.delta_x < 0)

        else:
            return (self.delta_y > 0 and other.delta_y > 0) or (self.delta_y < 0 and other.delta_y < 0)
            
    def __eq__(self, other) -> bool:
        '''
        Equality Definition
        '''
        return (self.start == other.start and self.end == other.end and self.thickness == other.thickness)

    def __hash__(self):
        '''
        hashing the Edge object
        '''
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        '''
        string representation of the edge
        '''
        return f"{self.start} -> {self.end} : thickness{self.thickness}"


class Graph:
    '''
    Graph Data structure
    
    It is made out of vertices (Coordinates) 
    and Edges which represents connections between vertices

    #NOTE: each connection is made out of TWO edges assigned to each vertix
        one edge assigned to vertix1 which is 1->2
        second edge assigned to vertix2 which is 2->1

    The Underlying Datastructures:
    1- Dictionary of key vertices(Coordinate) and value list of Edges GOING OUT from the vertex key

    '''
    # class variables
    used_colors = set()
    DEBUG_APPLY_OFFSET = True

    def __init__(self, vertices: list[Coordinate] = []):

        # Dictionary to relate each vertices to its edges
        self.vertex_edge: dict[Coordinate: list[Edge]] = {vertex: [] for vertex in vertices}
        # Dictionary to relate each vertices to the vertices it is attached to in the other end
        self.vertex_vertices: dict[Coordinate: list[Coordinate]] = {vertex: [] for vertex in vertices}

    @property
    def vertex_count(self) -> int:
        '''
        return number of vertices in this graph
        '''
        return len(self.vertex_edge)

    @property
    def edge_count(self) -> int:
        '''
        return number of edges in this graph
        '''
        return sum(len(edges) for edges in self.vertex_edge.values())

    def add_vertex(self, vertex: Coordinate) -> None:
        '''
        adds the new vertex to the underlying data structures of the graph

        :param vertex: the new vertex to be added to our graph
        '''
        if vertex not in self.vertex_edge:
            self.vertex_edge[vertex] = []
            self.vertex_vertices[vertex] = []

    def add_edge(self, edge: Edge) -> None:
        '''
        adds the new edge to the underlying data structures of the graph

        :param edge: the new edge to be added to the graph
        '''
        # checking if it's an edge
        if abs(edge.delta_x) == 0 and abs(edge.delta_y) == 0:
            raise ValueError("not an edge, it's a point")

        # Adding only if it's not there, ensure not duplicates
        if edge not in self.vertex_edge[edge.start]:
            self.vertex_edge[edge.start].append(edge)
        if edge.reversed() not in self.vertex_edge[edge.end]:
            self.vertex_edge[edge.end].append(edge.reversed())

        if edge.end not in self.vertex_vertices[edge.start]:
            self.vertex_vertices[edge.start].append(edge.end)
        if edge.start not in self.vertex_vertices[edge.end]:
            self.vertex_vertices[edge.end].append(edge.start)

    @property
    def ordered_edges(self) -> list[Edge]:
        '''
        DP algorithm to order edges,
        #NOTE: HIGHLY DEPENDENT ON 'Edge.anticlockwise_successors()'

        :return: an ordered list of how to traverse the trace in a continual manner
        '''
        ordered_edges = []

        visited = set()
        next_edge = list(self.vertex_edge.values())[0][0]
        while len(visited) < self.edge_count:

            # print()
            # print(next_edge, 'start')
            ordered_edges.append(next_edge)
            
            next_v = next_edge.end

            if len(self.vertex_edge[next_v]) == 1:
                # dead end must return
                next_edge = self.vertex_edge[next_v][0]
                visited.add(next_edge)
                # print(next_edge, 'DEADEND')

            else:
                successors = next_edge.anticlockwise_successors(self.vertex_edge[next_v])
                # print(successors, 'successors')
                for edge in successors:
                    # print('potential edge', edge, edge not in visited, edge.reversed() != next_edge)
                    if edge not in visited and edge.reversed() != next_edge:
                        # print('yes')
                        next_edge = edge
                        visited.add(next_edge)
                        break

                    else:
                        pass
                        # print('no')
                else:
                    ### This is now an non-tree graph.
                    ### Backtracking !!!

                    Edge.visualize_edges(ordered_edges, speed=1, terminate=True)
                    raise ValueError("Backtracking not implemented yet!!")
                
        # Edge.visualize_edges(ordered_edges, speed=1)
        return ordered_edges

    def __contains__(self, vertex: Coordinate) -> bool:
        '''
        checks if given vertex is already added to the graph or not

        :param vertex: vertex to check if it's in the graph or not
        :return: whether given vertex is in the graph or not
        '''
        return vertex in list(self.vertex_vertices.keys())

    def visualize(self, hide_turtle=True, offset=20, speed = 0, line_width=3, multiplier=8, terminate=False) -> None:
        '''
        Uses Python Turtle graphs to draw the graph
        '''
        skk = turtle.Turtle()
        turtle.width(line_width)
        turtle.speed(speed)
        if hide_turtle:
            turtle.hideturtle()
        else:
            turtle.showturtle()

        colors = ['black', 'red', 'blue', 'light blue', 'green', 'brown', 'dark green', 'orange', 'gray', 'indigo']
        color = random.choice(colors)
        while color in Graph.used_colors:
            color = random.choice(colors)

        turtle.pencolor(color)

        turtle.up()

        for edges in self.vertex_edge.values():
            turtle.setpos((edges[0].start.x - offset) * multiplier, (edges[0].start.y - offset) * multiplier)
            for edge in edges:
                turtle.down()
                turtle.setpos((edge.start.x - offset) * multiplier, (edge.start.y - offset) * multiplier)
                turtle.setpos((edge.end.x - offset) * multiplier, (edge.end.y - offset) * multiplier)
                turtle.up()

        Graph.used_colors.add(color)
        if len(Graph.used_colors) == len(colors):
            print('\n\n!!!!!!!!!! COLORS RESET !!!!!!!!!!!!!!!!!\n\n')
            Graph.used_colors = set()

        if terminate:
            turtle.done()

    @classmethod
    def visualize_graphs(cls, graph_list: list[Graph]) -> None:
        '''
        calls self.visualize for a bunch of graphs
        
        :param graph_list: list of graphs to visualize
        '''
        for graph in graph_list[:-1]:
            graph.visualize()
        graph_list[-1].visualize(terminate=True)

    def __str__(self) -> str:
        '''
        string representation of the graph
        '''
        desc = ""
        for vertex, vertices in self.vertex_vertices.items():
            desc += f"{vertex} -> {[str(vertex) for vertex in vertices]}\n"  # could of just written vertices as it is 
                                                                            # I want str() not repr()
        desc += '\n'

        return desc

    def seperate(self) -> list[Graph]:
        '''
        Uses a DP algorithm to seperate one big graph into list of graphs which contain one continious trace

        :return: list of continious trace graph
        '''
        seperated_graphs = []

        visited = set()
        # print(self)
        
        for vertex in list(self.vertex_edge.keys()):

            if vertex not in visited:
                # print(vertex, 'added new')
                new_graph = Graph([vertex])
                visited.add(vertex)

                for other_vertex in self.vertex_vertices[vertex]:
                    # print(other_vertex, 'added form vertex_vertices')
                    new_graph.add_vertex(other_vertex)
                    visited.add(other_vertex)

                for edge in self.vertex_edge[vertex]:
                    # print(edge, 'added from vertex_edge')
                    new_graph.add_edge(edge)

                seperated_graphs.append(new_graph)
                # print()

            else:
                # finding the graph that has this vertex
                found = False
                graphs_ind_to_join = []  # if a vertex is found in more than one graph, then join
                for ind, graph in enumerate(seperated_graphs):
                    if vertex in graph:
                        graphs_ind_to_join.append(ind)
                        found = True

                if found == False:
                    raise ValueError("HOW THE HELL??!?!")

                # print(vertex, 'found at graph of ind', graphs_ind_to_join)

                # Create new joined graph from many graphs with same vertex
                if len(graphs_ind_to_join) > 1:
                    # found more than one graph with same vertex, creating joined graph
                    joined_graph = Graph()
                    for graph_ind in graphs_ind_to_join:
                        joined_graph = Graph.join(joined_graph, seperated_graphs[graph_ind])

                    # print(f'Joining graphs of inds: {graphs_ind_to_join}')

                    # Remove the seperate graphs with same vertex and put the newly created joined graph
                    new_seperated_graphs = [joined_graph]
                    wanted_ind = 0
                    for ind, graph in enumerate(seperated_graphs):
                        if ind not in graphs_ind_to_join:
                            new_seperated_graphs.append(graph)

                    seperated_graphs = deepcopy(new_seperated_graphs)

                else:
                    wanted_ind = graphs_ind_to_join[0]

                for other_vertex2 in self.vertex_vertices[vertex]:
                    # print(other_vertex2, 'added form vertex_vertices')
                    visited.add(other_vertex2)
                    seperated_graphs[wanted_ind].add_vertex(other_vertex2)

                for edge in self.vertex_edge[vertex]:
                    # print(edge, 'added from vertex_edge')
                    seperated_graphs[wanted_ind].add_edge(edge)
                # print()
        
        # Removing duplicate edges
        #TODO
        # for graph_ind, graph in enumerate(seperated_graphs):
        #     for vertex in graph.vertex_edge:
        #         seperated_graphs[graph_ind].vertex_edge[vertex] = list(set(graph.vertex_edge[vertex]))


        return seperated_graphs

    def apply_offsets(self, extra_offset=0, terminate_after=False) -> Graph:
        '''
        The graph to execute .apply_offsets() to is a graph of continious lines of ZERO thickness,
        This function will create a new graph from the old one with the thickness applied :)

        :return: Graph with thickness applied. The edges are of thickness 0
        '''
        print('NEW CALL!!!!!!!!!!')
        new_graph = Graph()

        ordered_edges = self.ordered_edges

        ### PRE-ITERATION: get y=mx+c of edge of ind=-1
        # Getting gradient and y_intercept of last edge in cycle
        last_edge = ordered_edges[-1]
        gradient = last_edge.gradient
        abs_offset = round(last_edge.thickness/2 + extra_offset, 3)
        if last_edge.gradient != Infinity():
            alpha = round(math.atan(last_edge.gradient), 3)
            theta = round(math.pi/2 - alpha, 3)
            y_offset = round(abs_offset / math.sin(theta), 3)

            if last_edge.delta_x > 0:
                prev_y_intercept = round(last_edge.y_intercept - y_offset, 3)

            elif last_edge.delta_x < 0:
                prev_y_intercept = round(last_edge.y_intercept + y_offset, 3)

        else:
            if last_edge.delta_y > 0:
                vertical_line_offset_x = last_edge.start.x - abs_offset

            elif last_edge.delta_y < 0:
                vertical_line_offset_x = last_edge.start.x + abs_offset

        prev_gradient = gradient

        ordered_edges.append(ordered_edges[0])  # to force it to do one more iteration at the end
        for ind, edge in enumerate(ordered_edges):

            ### 1- Getting the linear equation of the offseted line
            # The Gradient is ofcoarse the same as the gradient of the original line since they're parallel
            # to get the y-intercept however I devised the following algorithm :)
            gradient = edge.gradient
            abs_offset = round(edge.thickness/2 + extra_offset, 3)

            if gradient != Infinity():
                alpha = round(math.atan(edge.gradient), 3)
                theta = round(math.pi/2 - alpha, 3)
                y_offset = round(abs_offset / math.sin(theta), 3)

                if edge.delta_x > 0:
                    y_intercept = round(edge.y_intercept - y_offset, 3)

                elif edge.delta_x < 0:
                    y_intercept = round(edge.y_intercept + y_offset, 3)

            else:
                if edge.delta_y > 0:
                    vertical_line_offset_x = edge.start.x + abs_offset

                elif edge.delta_y < 0:
                    vertical_line_offset_x = edge.start.x - abs_offset

            # offseted line equation is now 
            # y = gradient * x + y_intercept    :)

            ### Parrallel opposite direction edges are essentially deadends, point of return
            # They are dealt with differently in the else statement
            if ind == 0:
                # This is because the last item in the list is the first one as I just added it before the main loop
                same_dir_ind = ind - 1  
            else:
                same_dir_ind = ind
            if not(gradient == prev_gradient and not edge.is_same_direction(ordered_edges[same_dir_ind-1])):

                ### 2- Getting intersection between previous edge and current edge to get 'current_vertex'
                # Solving simultaneous equations :)
                if gradient == Infinity() and prev_gradient != Infinity():
                    x = round(vertical_line_offset_x, 3)
                    y = round(prev_gradient * x + prev_y_intercept, 3)

                elif prev_gradient == Infinity() and gradient != Infinity():
                    if ordered_edges[same_dir_ind-1].delta_y > 0:
                        x = edge.start.x + abs_offset 
                    else:
                        x = edge.start.x - abs_offset 

                    y = round(gradient * x + y_intercept, 3)

                elif prev_gradient == Infinity() and gradient == Infinity():
                    if edge.delta_y > 0:
                        x = edge.start.x + abs_offset 
                    else:
                        x = edge.start.x - abs_offset 

                    y = edge.start.y

                elif prev_gradient == 0 and gradient == 0:
                    x = edge.start.x

                    if edge.delta_x > 0:
                        y = edge.start.y - abs_offset 
                    else:
                        y = edge.start.y + abs_offset

                elif prev_gradient == gradient:
                    if ind != 0:
                        x = current_edge.end.x
                        y = current_edge.end.y
                    else:
                        raise ValueError('This case is not implemented yet')
                        pass #TODO:

                else:  # both gradient different and not infinity and not 0
                    print('herkljsodifjlkwjefkjspdoiajf;lkwejpobinqapoiwejf;lkajspeoifjqpaoiwj')
                    x = round((y_intercept - prev_y_intercept) / (prev_gradient - gradient), 3)
                    y = round(gradient * x + y_intercept, 3)


                # Adding the vertex to the graph
                current_vertex = Coordinate(x, y)
                new_graph.add_vertex(current_vertex)

                ### 3- Creating and adding a new edge between previous vertex and current vertex
                if ind != 0:  # ONLY FOR ITERATIONS OF INDEX>1
                    current_edge = Edge(prev_vertex, current_vertex, LASER_BEAM_THICKNESS)
                    new_graph.add_edge(current_edge)

                if Graph.DEBUG_APPLY_OFFSET:
                    print(f'Current edge index: {ind}')
                    print(f'Current edge : {edge}')
                    print()

                    if ind != 0:
                        print(f'Previous offseted Vertex: {prev_vertex}')
                    else:
                        print(f'No prev offseted vertex for first iterations')
                    if prev_gradient != Infinity():
                        print(f'Previous offseted edge linear equations:\ny = {prev_gradient}*x + {prev_y_intercept}')
                    else:
                        print(f'prev_gradient = {prev_gradient}')
                    print()

                    print(f'Current offseted Vertex: {current_vertex}')
                    if gradient != Infinity():
                        print(f'Current offseted edge linear equations: y = {gradient}*x + {y_intercept}')
                    else:
                        print(f'gradient = {gradient}')
                    print()

                    if ind != 0:
                        print(f'Newly Created Edge: {current_edge}')
                    else:
                        print(f'No edge to be created for first iteration')
                    print()

                    print()

                ### Setting variables for next iteration
                if gradient != Infinity():
                    prev_y_intercept = y_intercept
                prev_gradient = gradient
                prev_vertex = current_vertex

            else:  
                # lines are parallel and must join them with semi-circle

                #NOTE: This is a TEMPORARY SOLUTION, will connect them with a straight 
                # line for now, should connect them with semi-circle

                if gradient == Infinity():
                    ### 2&3- Create and add the two connecting vertices of the deadend to the graph
                    # Find intersection b/w:
                    # current offseted edge and inverse line
                    # previous offseted edge and inverse line
                    if edge.delta_y > 0:
                        x1 = edge.start.x - abs_offset 
                        x2 = edge.start.x + abs_offset
                    else:
                        x1 = edge.start.x + abs_offset 
                        x2 = edge.start.x - abs_offset

                    y1 = edge.start.y
                    y2 = y1

                elif gradient == 0:
                    ### 2&3- Create and add the two connecting vertices of the deadend to the graph
                    # Find intersection b/w:
                    # current offseted edge and inverse line
                    # previous offseted edge and inverse line
                    x1 = edge.start.x
                    x2 = x1

                    if edge.delta_x > 0:
                        y1 = edge.start.y + abs_offset 
                        y2 = edge.start.y - abs_offset
                    else:
                        y1 = edge.start.y - abs_offset
                        y2 = edge.start.y + abs_offset

                else:
                    ### 2- Getting invserse linear equation (for next step)
                    inverse_gradient = round((-1)/gradient, 3)
                    inverse_y_intercept = round(edge.start.y - inverse_gradient*edge.start.x, 3)

                    ### 3- Create and add the two connecting vertices of the deadend to the graph
                    # Find intersection b/w:
                    # current offseted edge and inverse line
                    # previous offseted edge and inverse line
                    x1 = round((inverse_y_intercept - prev_y_intercept) / (prev_gradient - inverse_gradient), 3)
                    y1 = round(inverse_gradient*x1 + inverse_y_intercept, 3)

                    x2 = round((inverse_y_intercept - y_intercept) / (gradient - inverse_gradient), 3)
                    y2 = round(inverse_gradient*x2 + inverse_y_intercept, 3)

                vertex1 = Coordinate(x1, y1)
                new_graph.add_vertex(vertex1)


                vertex2 = Coordinate(x2, y2)

                semicircle_vertices =  Coordinate.generate_semicircle_coordinates(vertex1, vertex2)
                print(vertex1)
                print(vertex2)
                print()

                for semicircle_vertex in semicircle_vertices:
                    new_graph.add_vertex(semicircle_vertex)

                new_graph.add_vertex(vertex2)

                ### 4- Adding the new edges to the graph
                # b/w:
                # previous vertex and V1
                # V1 and V2
                if ind != 0:
                    edge1 = Edge(prev_vertex, vertex1, LASER_BEAM_THICKNESS)
                    new_graph.add_edge(edge1)

                prev_semicircle_vertex = semicircle_vertices[0]
                for ind, semicircle_vertex in enumerate(semicircle_vertices[1:]):
                    print(ind)
                    print(prev_semicircle_vertex)
                    print(semicircle_vertex)
                    print()
                    new_graph.add_edge(Edge(prev_semicircle_vertex, semicircle_vertex, LASER_BEAM_THICKNESS))
                    prev_semicircle_vertex = semicircle_vertex

                edge2 = Edge(vertex1, vertex2, LASER_BEAM_THICKNESS)
                new_graph.add_edge(edge2)

                if Graph.DEBUG_APPLY_OFFSET:
                    print('PARALLEL EDGE DETECTED!!!')
                    print(f'm=infinity -> {gradient==Infinity()}, m=0 -> {gradient == 0}')
                    print()

                    print(f'Current edge index: {ind}')
                    print(f'Current edge : {edge}')
                    print()

                    if ind != 0:
                        print(f'Previous offseted Vertex: {prev_vertex}')
                    else:
                        print(f'No prev offseted vertex for first iterations')
                    if gradient != Infinity():
                        print(f'Previous offseted edge linear equations:\ny = {prev_gradient}*x + {prev_y_intercept}')
                    print()

                    if gradient != Infinity() and gradient != 0:
                        print(f'Inverse linear equation:\ny = {inverse_gradient}*x + {inverse_y_intercept}')
                    else:
                        print(f'prev_gradient = gradient = {gradient} = {prev_gradient}')
                    print()

                    if gradient != Infinity():
                        print(f'Current offseted edge linear equations: y = {gradient}*x + {y_intercept}')
                    print()

                    print(f'vertex1: {vertex1}')
                    print(f'vertex2: {vertex2}')
                    if ind != 0:
                        print(f'edge1 (prev to inverse): {edge1}')
                    else:
                        print('No edge1 for first iteration')
                    print(f'edge2 (inverse to current): {edge2}')
                    print()

                    print()
               
                ### 5- Setting previous variable for next iteration
                prev_vertex = vertex2
                prev_gradient = gradient
                if gradient != Infinity():
                    prev_y_intercept = y_intercept

        Edge.visualize_edges(self.ordered_edges, hide_turtle=False, offset=25, multiplier=15, speed=3)
        new_graph.visualize(speed=3, line_width=1, offset=25, multiplier = 15, terminate=terminate_after)
        return new_graph

    def to_coordinate(self) -> list[Coordinate]:
        '''

        '''
        return []

    def remove_tiny_edges(self) -> None:
        '''
        Removes the stupid small infuriating edges that mess up with everything
        Affects self Graph
        '''
        pass #TODO:

    def resolve_conflicts(self) -> list[Graph]:
        '''
        after applying offset to graph
        '''
        return []

    @classmethod
    def join(cls, *graphs: Graph) -> Graph:
        '''
        joins the input graphs

        :graphs: undefined number of graphs
        :return: one graph joined from the all the graphs given from *graphs attribute
        '''
        # Type Checking
        if len(set([type(graph) for graph in graphs])) != 1:
            raise ValueError("All Arguments MUST be of type Graph")

        joined_graph = Graph()
        for graph in graphs:
            joined_graph.vertex_vertices.update(graph.vertex_vertices)
            joined_graph.vertex_edge.update(graph.vertex_edge)

        return joined_graph



        
#TODO: the ultimate goal is have list of trace variables of datatype graph, each has is a continious trace
# i edited the __str__ func of Graph to display the funcs I defined as single_dir_...
#       I have a graph that has all the vertices(it's a Coordinate) pointing to one or more vertices 
#       without pointing back (as the original functions does)
# I have traces ready in this 'traces' variables
# The ONLY thing left is the order. now they are not ordered, meaning- it's like
                                            # coord2 -> coord1
                                            # coord4 -> coord3
                                            # coord1 -> NOTHING
                                            # coord3 -> coord2
                                    # but i have to order it
                                            # coord4 -> coord3
                                            # coord3 -> coord2
                                            # coord2 -> coord1
                                            # coord1 -> NOTHING

# after that i can easily extract each trace by finding the coord that points to nothing:
        # I know that this is the start of a new trace and the end of a previous trace 

# next up is to return the proper coordinate list for each trace with two important features:
    # 1- offset the coordinates two times with the wanted thickness
    # 2- find holes and incorporate them in the trace somehow ;)


