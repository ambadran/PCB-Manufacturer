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

    def __lt__(self, other) -> bool:
        '''
        less than method definition
        '''
        if type(other) != int and type(other) != float:
            raise ValueError("must compare infinity to numbers only")

        return False

    def __eq__(self, other) -> bool:
        '''
        equal than method definition
        '''
        if type(other) != int and type(other) != float:
            raise ValueError("must compare infinity to numbers only")

        return False

    def __gt__(self, other) -> bool:
        '''
        greater than method definition
        '''
        if type(other) != int and type(other) != float:
            raise ValueError("must compare infinity to numbers only")

        return True


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
            return self.delta_y / self.delta_x
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
        edge_list.append(inverted_og)

        ### Step 2: Get all edges in there correct Quadrant
        quadrants = [[], [], [], []]
        for edge in edge_list:

            if edge.delta_x > 0:
                if edge.delta_y > 0:
                    quadrants[0].append(edge)

                elif edge.delta_y < 0:
                    quadrants[3].append(edge)

            elif edge.delta_x < 0:
                if edge.delta_y > 0:
                    quadrants[1].append(edge)

                elif edge.delta_y < 0:
                    quadrants[2].append(edge)

        ### Step 3: Get each Quadrant list in order
        for ind, quadrant in enumerate(quadrants):
            quadrants[ind] = sorted(quadrant, key= lambda x: x.gradient)

        ### Step 4: Split the list with the inverted OG into 'prelist' and 'post list'
        if inverted_og.delta_x > 0:
            if edge.delta_y > 0:
                pre_list = quadrants[0][:quadrants[0].index(inverted_og)]
                post_list = quadrants[0][quadrants[0].index(inverted_og)+1:]
                quadrant_order = [1, 2, 3]

            elif edge.delta_y < 0:
                pre_list = quadrants[3][:quadrants[3].index(inverted_og)]
                post_list = quadrants[3][quadrants[3].index(inverted_og)+1:]
                quadrant_order = [0, 1, 2]

        elif edge.delta_x < 0:
            if edge.delta_y > 0:
                pre_list = quadrants[1][:quadrants[1].index(inverted_og)]
                post_list = quadrants[1][quadrants[1].index(inverted_og)+1:]
                quadrant_order = [2, 3, 0]

            elif edge.delta_y < 0:
                pre_list = quadrants[2][:quadrants[2].index(inverted_og)]
                post_list = quadrants[2][quadrants[2].index(inverted_og)+1:]
                quadrant_order = [3, 0, 1]

        ### Step 5: Creating the final list :)
        final_list = []

        final_list.extend(post_list)
        final_list.extend(quadrants[0])
        final_list.extend(quadrants[1])
        final_list.extend(quadrants[2])
        final_list.extend(pre_list)

        return final_list

    def reversed(self) -> Edge:
        '''
        return the reversed Edge
        '''
        return Edge(self.end, self.start, self.thickness)

    @classmethod
    def visualize_edges(cls, edges: list[Edge], speed=0, offset=20, line_width=3, multiplier=8, terminate=False) -> None:
        '''
        visualizes the sequence of edges in a list 
        '''
        skk = turtle.Turtle()
        turtle.width(line_width)
        turtle.speed(speed)
        # turtle.hideturtle()

        colors = ['black', 'red', 'blue', 'light blue', 'green', 'brown', 'yellow', 'orange', 'gray', 'indigo']
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

        :return: an ordered list of how to traverse the trace in a continual manner
        '''
        ordered_edges = []

        visited = set()
        next_edge = list(self.vertex_edge.values())[0][0]
        while len(visited) < self.edge_count:

            print()
            print(next_edge, 'start')
            ordered_edges.append(next_edge)
            
            next_v = next_edge.end

            if len(self.vertex_edge[next_v]) == 1:
                # dead end must return
                next_edge = self.vertex_edge[next_v][0]
                visited.add(next_edge)
                print(next_edge, 'DEADEND')

            else:
                successors = next_edge.anticlockwise_successors(self.vertex_edge[next_v])
                print(successors, 'successors')
                for edge in successors:
                    print('potential edge', edge, edge not in visited, edge.reversed() != next_edge)
                    if edge not in visited and edge.reversed() != next_edge:
                        print('yes')
                        next_edge = edge
                        visited.add(next_edge)
                        break

                    else:
                        print('no')
                else:
                    ### This is now an non-tree graph.
                    ### Backtracking !!!

                    ### THE FOLLOWING CODE IS ONLY TEMPORARY WORKAROUND!!
                    # This code doesn't deal with real internal edges of a non-tree graph
                    # it just ignore very tiny edges that looks like internal edge
                    # in the future I should detect it with the backtracking algorithm and ignore it too.
                    # print(len(visited), self.edge_count)
                    # internal_edges = []
                    # for edge_list in self.vertex_edge.values():
                    #     for edge in edge_list:
                    #         if edge not in visited:
                    #             internal_edges.append(edge)

                    # for edge in internal_edges:
                    #     if edge.delta_x <= 0.05 and edge.delta_y <= 0.05:
                    #         continue
                    #     else:
                    #         # Found a large edge not accounted for, This is definetly an internal edge. MUST deal with!
                    #         break
                    # else:
                    #     # All captured edges are less then 0.05 in x and y so they're tiny wrong edges by user
                    #     break

                    Edge.visualize_edges(ordered_edges, speed=1, terminate=True)
                    raise ValueError("No backtracking implemented!!")
                

        Edge.visualize_edges(ordered_edges, speed=1, terminate=True)
        return ordered_edges

    def __contains__(self, vertex: Coordinate) -> bool:
        '''
        checks if given vertex is already added to the graph or not

        :param vertex: vertex to check if it's in the graph or not
        :return: whether given vertex is in the graph or not
        '''
        return vertex in list(self.vertex_vertices.keys())

    def visualize(self, line_width=3, multiplier=8, terminate=False) -> None:
        '''
        Uses Python Turtle graphs to draw the graph
        '''
        skk = turtle.Turtle()
        turtle.width(line_width)
        turtle.speed(0)
        turtle.hideturtle()

        colors = ['black', 'red', 'blue', 'light blue', 'green', 'brown', 'yellow', 'orange', 'gray', 'indigo']
        color = random.choice(colors)
        while color in Graph.used_colors:
            color = random.choice(colors)

        turtle.pencolor(color)

        turtle.up()

        for edges in self.vertex_edge.values():
            turtle.setpos(edges[0].start.x*multiplier, edges[0].start.y*multiplier)
            for edge in edges:
                turtle.down()
                turtle.setpos(edge.start.x*multiplier, edge.start.y*multiplier)
                turtle.setpos(edge.end.x*multiplier, edge.end.y*multiplier)
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

    def apply_offsets(self) -> Graph:
        '''
        The graph to execute .apply_offsets() to is a graph of continious lines of ZERO thickness,
        This function will create a new graph from the old one with the thickness applied :)

        :return: Graph with thickness applied. The edges are of thickness 0
        '''
        new_graph = Graph()

        for vertex, edges in self.vertex_edge.items():

            for edge in edges:

                ### Getting the linear equation of the offseted line
                # The Gradient is ofcoarse the same as the gradient of the original line since they're parallel
                # to get the y-intercept however I devised the following algorithm :)
                gradient = edge.gradient

                alpha = math.atan(edge.gradient)
                theta = math.pi/2 - alpha

                abs_offset = edge.thickness/2
                
                y_offset = abs_offset / math.sin(theta)

                y_intercept = self.y_intercept - y_offset  #NOTE: I could add/sub, it doesn't matter it just MUST be same for all

                # offseted line equation is now 
                # y = gradient * x + y_intercept    :)

                ### Now we must get the start and end coordinates
                # which is the intersection between the line after and the line before
                x = (y_intercept - prev_y_intercept) / (prev_gradient - gradient)
                y = gradient * x + y_intercept


                ### Setting variables for next iteration
                prev_y_intercept = y_intercept
                prev_gradient = gradient

        return new_graph

    def to_coordinate(self) -> list[Coordinate]:
        '''

        '''
        return []

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


