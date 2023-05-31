from __future__ import annotations
from typing import Optional, Deque
from dataclasses import dataclass
from copy import deepcopy
import turtle
import random
import math
from enum import Enum
from heapq import heappush, heappop

def sin(angle):
    return math.sin(math.radians(angle))

def cos(angle):
    return math.cos(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def asin(value):
    return math.degrees(math.asin(value))

def acos(value):
    return math.degrees(math.acos(value))

def atan(value):
    return math.degrees(math.atan(value))

LASER_BEAM_THICKNESS = 0.05

class Stack:
    """
    singly linkedlist with LIFO settings
    """ 
    def __init__(self):
        self._container = []

    def push(self, value):
        self._container.append(value)

    def pop(self):
        return self._container.pop()

    @property
    def empty(self):
        return not self._container

    def __repr__(self):
        return repr(self._container)

class Queue:
    """
    singly linkedlist with FIFO settings
    """
    def __init__(self):
        self._container = Deque()

    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def __repr__(self):
        return repr(self._container)

@dataclass
class Intersection:
    comppad_coord: Coordinate  # the center of the component pad coordinate
    comppad_block: Block  # what block does the component pad belong to
    inter1_coord: Coordinate  # the first intersection coordinate between the trace edges and the component pad edges
    inter2_coord: Coordinate  # the second intersection coordinate between the trace edges and the component pad edges
    inter1_edge: Edge  # the edge at which the first intersection coordinate lies
    inter2_edge: Edge  # the edge at which the second intersection coordinate lies
    pre_inter1_node: Node  # the node at inter1_edge.start
    pre_inter2_node: Node  # the node at inter2_edge.start
    stupid_corner_case_flag: bool = False  # fuck the stupid corner case

    @staticmethod
    def generate_comppad_nodes_rectangle(intersection: Intersection, trace_nodes: Node, resolution: int) -> Node:
        '''
        generates the coordinates of the rectangle component pad 

        :param intersection: Intersection object to determine all the variables needed to generate the coordinates
        :param resolution: how many points per mm
        :return: Node object representing the HEAD of the linkedlist of the coordinates of the component pad
        '''
        ### Step 1: Get intersection between the edge and all the four lines of the square
        # Getting the Coordinates of the square
        block = intersection.comppad_block
        v1 = Coordinate(round(intersection.comppad_coord.x - block.thickness/2, 5), round(intersection.comppad_coord.y + block.thickness2/2, 5))
        v2 = Coordinate(round(intersection.comppad_coord.x + block.thickness/2, 5), round(intersection.comppad_coord.y + block.thickness2/2, 5))
        v3 = Coordinate(round(intersection.comppad_coord.x - block.thickness/2, 5), round(intersection.comppad_coord.y - block.thickness2/2, 5))
        v4 = Coordinate(round(intersection.comppad_coord.x + block.thickness/2, 5), round(intersection.comppad_coord.y - block.thickness2/2, 5))
        vertices = [v1, v2, v3, v4]
        e1 = Edge(v1, v2, None)
        e2 = Edge(v1, v3, None)
        e3 = Edge(v2, v4, None)
        e4 = Edge(v3, v4, None)
        edges = [e1, e2, e3, e4]

        ### STEP 1: Getting the vertices of the rectangle comppad that will be 
        ### displayed in the pcb (not the ones inbetween the trace)
        passed_vertices = []
        for vertex in vertices:
            if not vertex.inside_polygon(trace_nodes):
                passed_vertices.append(vertex)

        ### STEP 2: ORDERING THE VERTICES
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
        if len(the_rest) == 1:
            middle_vertices = the_rest

        elif len(the_rest) == 2:
            min_v_inter1_1 = Edge(intersection.inter1_coord, the_rest[0], None).absolute_length
            min_v_inter1_2 = Edge(intersection.inter1_coord, the_rest[1], None).absolute_length

            if min_v_inter1_1 < min_v_inter1_2:
                middle_vertices = [the_rest[0], the_rest[1]]

            else:
                middle_vertices = [the_rest[1], the_rest[0]]

        else:
            middle_vertices = []

        ordered_rec_coords = []
        ordered_rec_coords.append(min_v_1)
        ordered_rec_coords.extend(middle_vertices)
        ordered_rec_coords.append(min_v_2)

        # coords are reversed to create the linkedlist 
        ordered_rec_coords.reverse()
        return Node.from_list(ordered_rec_coords)

    @staticmethod
    def generate_comppad_nodes_circle(intersection: Intersection, resolution: int) -> Node:
        '''
        generates the coordinates of the circle component pad or oval with equal x and y (aka a circle)

        :param intersection: Intersection object to determine all the variables needed to generate the coordinates
        :param resolution: how many points per mm
        :return: Node object representing the HEAD of the linkedlist of the coordinates of the component pad
        '''
        ### Determining Orientation
        # orientation is determined by looking at inter1_edge.end or inter2_edge.start 
        #        (should be the same thing before intersection is processed and it's not a deadend)
        # and the comppad_coord

        delta_x = intersection.comppad_coord.x - intersection.inter1_edge.end.x
        delta_y = intersection.comppad_coord.y - intersection.inter1_edge.end.y
        # delta_x = intersection.inter1_edge.delta_x
        # delta_y = intersection.inter1_edge.delta_y

        if delta_x > 0:
            orientation = True
        elif delta_x < 0:
            orientation = False
        elif delta_x == 0:
            if delta_y > 0:
                orientation = True
            elif delta_y < 0:
                orientation = False

        if intersection.inter1_edge.end == intersection.inter2_edge.start or delta_x == 0:  #TODO I don't think adding 'or delta_x==0' solved the main problem, trace ind -3 doesn't get one of the comppads correctly
            orientation = not orientation

        coordinate1 = intersection.inter1_coord
        coordinate2 = intersection.inter2_coord

        if not(resolution // 2 != resolution /2):
            raise ValueError('resolution argument MUST be ODD number, \nas there will be pairs of coordinates PLUS the final single coordinate which will always result in an odd number. \nRefer to iPad notes to understand more')

        ### Step 1: Get circle equation attributes
        # a and b are the x and y offset value from circle center respectively
        # They are also the midpoints between coord1 and coord2
        a = intersection.comppad_coord.x
        b = intersection.comppad_coord.y

        # r is the radius of circle
        r = round(intersection.comppad_block.thickness/2 , 5)

        if coordinate2.x == coordinate1.x:  # Gradient = infinity  # trace itself is m=0
        # if intersection.inter1_edge.gradient == 0:
            ### Step 2: Get linear equation of the line that passes through the circle diameter, aka the 2 coordinates
            # Getting equation of a vertical line
            x = coordinate1.x
            # y = y  # the independent variable of a vertical line is y

            ### Step 3: Getting linear equation of tangent to the circle at the maximum
            if orientation:
                x_max = intersection.comppad_coord.x + r
            else:
                x_max = intersection.comppad_coord.x - r
            y = b
            max_coord = Coordinate(x_max, b)

            ### Step 4: Getting the list of x values of vertical line equations that intersects the circle
            x_range = x_max - x
            num_iterations = int((resolution-1)/2)
            increment = round(x_range / (num_iterations + 1), 5)
            x_values = []
            for iter_ind in range(1, num_iterations+1):
                x_values.append(x + iter_ind*increment)

            ### Step 5: Getting the intersection between circle equation and all the intersection linear equations
            arc_coords_positive = []
            arc_coords_negative = []
            for current_x_value in x_values:
                y1 = round(b + math.sqrt(round(r**2 - (current_x_value - a)**2, 6)), 5)
                arc_coords_positive.append(Coordinate(round(current_x_value, 6), y1))

                y2 = round(b - math.sqrt(round(r**2 - (current_x_value - a)**2, 6)), 5)
                if y1 != y2: # to eleminate max point
                    arc_coords_negative.append(Coordinate(round(current_x_value, 6), y2))

        elif coordinate2.y == coordinate1.y:  # Gradient = 0.0, trace itself is m=infinity
        # elif intersection.inter1_edge.gradient == Infinity():
            ### Step 2: Get linear equation of the line that passes through the circle diameter, aka the 2 coordinates
            # Getting equation of a horizontal line
            # x = x  # the independent variable of a horizontal line is x
            y = coordinate1.y

            ### Step 3: Getting linear equation of tangent to the circle at the maximum and max coord
            x = a
            if orientation:
                y_max = intersection.comppad_coord.y + r
            else:
                y_max = intersection.comppad_coord.y - r
            max_coord = Coordinate(a, y_max)

            ### Step 4: Getting the list of y_intercepts of linear equations that intersects the circle
            y_range = y_max - y
            num_iterations = int((resolution-1)/2)
            increment = round(y_range / (num_iterations + 1), 5)
            y_values = []
            for iter_ind in range(1, num_iterations+1):
                y_values.append(y + iter_ind*increment)

            ### Step 5: Getting the intersection between circle equation and all the intersection linear equations
            arc_coords_positive = []
            arc_coords_negative = []
            for current_y_value in y_values:
                x1 = round(a + math.sqrt(round(r**2 - (current_y_value - b)**2, 6)), 5)
                arc_coords_positive.append(Coordinate(x1, round(current_y_value, 6)))

                x2 = round(a - math.sqrt(round(r**2 - (current_y_value - b)**2, 6)), 5)
                if x1 != x2: # to eleminate max point
                    arc_coords_negative.append(Coordinate(x2, round(current_y_value, 6)))

        else:
            ### Step 2: Get linear equation of the line that passes through the circle diameter, aka the 2 coordinates
            # Get the linear equation of the diameter coordinates
            gradient = (coordinate2.y - coordinate1.y) / (coordinate2.x - coordinate1.x)
            y_intercept = coordinate1.y - gradient*coordinate1.x

            # Get the linear equation of the inverse of the diameter linear equation
            inverse_gradient = -1/gradient
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
            x1 = round((-b_q + math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)
            x2 = round((-b_q - math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)

            # Getting values of y by substituting in inverse linear equation
            y1 = inverse_gradient*x1 + inverse_y_intercept
            y2 = inverse_gradient*x2 + inverse_y_intercept

            # Choosing the correct maximum point, according to orientation argument
            if  orientation:
                max_coord = Coordinate(x1, y1)
            else:
                max_coord = Coordinate(x2, y2)


            # Getting linear equation of correct maximum point and saving it in a variable, (ignoring minimum point)
            # tangent line of the comppad circle touching the maximum point from the parallel line passing through the 2 interseciton coords
            maximum_line_gradient = gradient
            maximum_line_y_intercept = max_coord.y - maximum_line_gradient*max_coord.x

            ### Step 4: Getting the list of y_intercepts of linear equations that intersects the circle
            y_intercept_range = maximum_line_y_intercept - y_intercept
            num_iterations = int((resolution-1)/2)
            increment = round(y_intercept_range / (num_iterations + 1), 5)
            y_intercept_list = [] 
            for iter_ind in range(1, num_iterations+1):
                y_intercept_list.append(y_intercept + iter_ind*increment)

            ### Step 5: Getting the intersection between circle equation and all the intersection linear equations
            # from the diameter to the maximum line.
            arc_coords_positive = []
            arc_coords_negative = []
            for current_y_intercept in y_intercept_list:
                a_q = 1 + gradient**2
                b_q = -2*a + 2*gradient*current_y_intercept - 2*b*gradient
                c_q = current_y_intercept**2 - 2*b*current_y_intercept + b**2 - r**2 + a**2

                if b_q**2 - 4*a_q*c_q > 0:  # >0 means maximum point isn't there (it's at ==0)
                    x1 = round((-b_q + math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)
                    y1 = round(gradient*x1 + current_y_intercept, 5)
                    arc_coords_positive.append(Coordinate(x1, y1))

                    x2 = round((-b_q - math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)
                    y2 = round(gradient*x2 + current_y_intercept, 5)
                    arc_coords_negative.append(Coordinate(x2, y2))
                else:
                    raise ValueError("SHITTT")
                    # print('SHITTTT')

        ### Step 6: Get the final ordered list of coordinates
        # PLEASE refer to iPad. The combination are truly ENORMOUS and was difficult to derive ;)
        ordered_arc_coords = []

        # creating tmp edges from intersection coord to first point of -ve and to +ve
        test_e1 = Edge(intersection.inter1_coord, arc_coords_positive[0], None)
        test_e2 = Edge(intersection.inter1_coord, arc_coords_negative[0], None)
        
        # deciding who goes first according to who is nearer
        if test_e1.absolute_length == test_e2.absolute_length:
            raise ValueError("HOWWWWWWWWWWW, THIS IS IMPOSSIBLE!!! I CAN'T IMAGINE THIS !!!!!!!!")
        leading_list = arc_coords_positive if test_e1.absolute_length < test_e2.absolute_length else arc_coords_negative
        trailing_list = arc_coords_positive if test_e1.absolute_length > test_e2.absolute_length else arc_coords_negative

        # creating the final properly ordered list of coordinates
        ordered_arc_coords.extend(leading_list)
        ordered_arc_coords.append(max_coord)
        ordered_arc_coords.extend(reversed(trailing_list))

        # coords are reversed to create the linkedlist 
        ordered_arc_coords.reverse()
        return Node.from_list(ordered_arc_coords)

    @staticmethod
    def generate_comppad_nodes_oval(intersection: Intersection, resolution: int) -> Node:
        '''
        generates the coordinates of the oval component pad 

        :param intersection: Intersection object to determine all the variables needed to generate the coordinates
        :param resolution: how many points per mm
        :return: Node object representing the HEAD of the linkedlist of the coordinates of the component pad
        '''
        pass

    @staticmethod
    def generate_comppad_nodes(intersection: Intersection, trace_nodes: Node, resolution: int=15) -> Node:
        '''
        generates the coordinates of the component pad in the form of a linkedlist

        :param intersection: Intersection object to determine all the variables needed to generate the coordinates
        :param resolution: how many points per mm
        :return: Node object representing the HEAD of the linkedlist of the coordinates of the component pad
        '''
        if type(resolution) != int:
            raise ValueError("resolution must be of type int")

        if intersection.comppad_block.shape_type == ShapeType.Circle or (intersection.comppad_block.shape_type == ShapeType.Oval  and intersection.comppad_block.thickness == intersection.comppad_block.thickness2):
            return Intersection.generate_comppad_nodes_circle(intersection, resolution)

        elif intersection.comppad_block.shape_type == ShapeType.Rectangle:
            return Intersection.generate_comppad_nodes_rectangle(intersection, trace_nodes, resolution)

        elif intersection.comppad_block.shape_type == ShapeType.Oval:
            return Intersection.generate_comppad_nodes_oval(intersection, resolution)


class Node:
    def __init__(self, vertex: Coordinate, parent: Optional[Node]):
        self.vertex = vertex
        self.parent = parent

    @classmethod
    def from_list(cls, coordinate_list: list[Coordinate]):
        '''
        creates self
        '''
        next_node = Node(coordinate_list[0], None)  # the last node, doens't have any head
        for coordinate in coordinate_list[1:]:
            next_node = Node(coordinate, next_node)

        return next_node

    def to_list(self) -> list[Coordinate]:
        '''
        converts the linkedlist to a normal list of coordinates
        '''
        next_node = self
        vertex_list = []
        while next_node.parent != None and next_node.parent != self:
            vertex_list.append(next_node.vertex)
            next_node = next_node.parent

        vertex_list.append(next_node.vertex)

        return vertex_list

    def to_edge_list(self) -> list[Edge]:
        '''
        converts nodes to list of edges
        '''
        coordinates = self.to_list()
        pre_coord = coordinates[0]
        edges = []
        for coordinate in coordinates[1:]:
            edges.append(Edge(pre_coord, coordinate, None))
            pre_coord = coordinate

        if self.does_loop:
            edges.append(Edge(pre_coord, coordinates[0], None))

        return edges

    def extend(self, other_node: Node) -> None:
        '''
        just like list.extend() it extends the current linkedlist with other linkedlist
        finds the last node, the node with parent none (or head for looping linkedlists) 
        then attaches the other_node node to it and joins the loop or not depending on 
        original state

        :param other_node: the node to make parent of the last node in the current linkedlist
        :return: the new head Node of the extended linkedlist
        '''
        # next_node = self
        # while next_node.parent != None and next_node.parent != self:
        #     next_node = next_node.parent

        # .last_node == None
        if self.last_node.parent == None:
            # just join
            self.last_node.parent = other_node

        else:
            self.last_node.parent = other_node

            # must join the last node with the first node to make the loop
            self.make_it_loop()

    # def __eq__(self, other_node) -> bool:
    #     '''
    #     equality operator ==

    #     Must be same variable, doesn't care if same vertex or even same vertex with same parents but initiated seperatly
    #     '''
    #     return self == other_node  

    def __contains__(self, other_node) -> bool:
        '''
        in operator
        '''
        next_node = self
        while next_node.parent != None and next_node.parent != self:
            if next_node == other_node:
                return True
            next_node = next_node.parent

        return next_node == other_node

    @property
    def does_loop(self) -> bool:
        '''
        return if it loops
        '''
        next_node = self
        while next_node.parent != None and next_node.parent != self:
            next_node = next_node.parent

        return next_node.parent == self

    def make_it_loop(self) -> None: 
        '''
        converts a non looping linkedlist to a looping linkedlist
        '''
        temp_node = self.last_node
        # print(repr(temp_node), 'pre')
        while temp_node.vertex == self.vertex:
            temp_node = self.child(temp_node)
            # print(repr(temp_node), 'in')
        # print(repr(temp_node), 'out')

        temp_node.parent = self
  
    @classmethod
    def reversed(cls, node: Node) -> Node:
        '''
        reverses the argument node
        '''
        new_node = Node(node.vertex, None)
        next_node = node.parent
        while next_node.parent != None and next_node.parent != node:
            new_node = Node(next_node.vertex, new_node)

            next_node = next_node.parent

        new_node = Node(next_node.vertex, new_node)

        if next_node.parent == node:
            next_node = next_node.parent
            new_node = Node(next_node.vertex, new_node)

        if node.does_loop:
            new_node.make_it_loop()

        # print(new_node, 'reversed\n')

        return new_node

    @property
    def pre_last_node(self) -> Node:
        '''
        returns last node in the linkedlist
        '''
        next_node = self
        while next_node.parent != None and next_node.parent != self:
            pre_node = next_node
            next_node = next_node.parent

        return pre_node

    @property
    def last_node(self) -> Node:
        '''
        returns last node in the linkedlist
        '''
        next_node = self
        while next_node.parent != None and next_node.parent != self:
            next_node = next_node.parent

        return next_node

    def child(self, parent_node: Node) -> Node:
        '''
        return child of node, the previous node
        '''
        if self.does_loop:
            pre_node = self.last_node

        elif self.last_node.vertex == self.vertex:
            # print('lsjdflkajsd;flkjasd;lkfja;sldkfj')
            pre_node = self.pre_last_node

        else:
            pre_node = None

        next_node = self
        while next_node.parent != None and next_node.parent != self:

            if next_node.vertex == parent_node.vertex:
                return pre_node

            pre_node = next_node
            next_node = next_node.parent
            
        if next_node.vertex == parent_node.vertex:
            return pre_node
        else:
            raise ValueError('parent_node given is not in self node parents')

    @property
    def single_line_trace_with_comppad_at_ends_only(self) -> bool:
        '''
        :returns: whether this trace is a single line trace or not
        '''
        next_node = self
        real_edge_count = 0
        while next_node.parent != None and next_node.parent != self:

            current_edge = Edge(next_node.vertex, next_node.parent.vertex, None)

            if current_edge.absolute_length <= Graph.CURVE_THRESHOLD_LENGTH:
               pass  # ignore

            else:
                real_edge_count += 1
            
            next_node = next_node.parent  # ignore

        # last edge if available (if it's a loop)
        if next_node.parent == self:
            current_edge = Edge(next_node.vertex, next_node.parent.vertex, None)

            if current_edge.absolute_length <= Graph.CURVE_THRESHOLD_LENGTH:
               pass  # ignore

            else:
                real_edge_count += 1

        return real_edge_count == 2

    @property
    def node_count(self) -> int:
        '''
        return the number of nodes in this linkedlist, starting with the head node to the last node
        '''
        next_node = self
        count = 1
        while next_node.parent != None and next_node.parent != self:
            count += 1
            next_node = next_node.parent

        if next_node.parent == self:
            count += 1
            
        return count

    def visualize(self, hide_turtle=True, speed=0, x_offset=20, y_offset=20, line_width=1.5, multiplier=8, terminate=False) -> None:
        '''
        visualizes the linked list
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

        next_node = self
        turtle.setpos((next_node.vertex.x - x_offset) * multiplier, (next_node.vertex.y - y_offset) * multiplier)
        turtle.down()
        while next_node.parent != None and next_node.parent != self:
            turtle.setpos((next_node.vertex.x - x_offset) * multiplier, (next_node.vertex.y - y_offset) * multiplier)
            next_node = next_node.parent

        turtle.setpos((next_node.vertex.x - x_offset) * multiplier, (next_node.vertex.y - y_offset) * multiplier)
        if next_node.parent == self:
            next_node = next_node.parent
            turtle.setpos((next_node.vertex.x - x_offset) * multiplier, (next_node.vertex.y - y_offset) * multiplier)

        Graph.used_colors.add(color)
        if len(Graph.used_colors) == len(colors):
            print('\n\n!!!!!!!!!! COLORS RESET !!!!!!!!!!!!!!!!!\n\n')
            Graph.used_colors = set()

        if terminate:
            turtle.done()

    def round_all(self, accuracy: int):
        '''
        rounds all vertices to {accuracy} number of decimal places
        '''
        coordinate_list = self.to_list()
        for ind, coord in enumerate(coordinate_list):
            coordinate_list[ind] = round(coord, accuracy)

        self = Node.from_list(coordinate_list)

    def find(self, wanted_vertex: Coordinate, enable_error=True) -> Optional[Node]:
        '''
        binary search through the self node and it's parent if it contains the wanted vertex

        :param vertex: the vertex to search for
        :return: the Node with the wanted vertex or None if not found
        '''
        if type(wanted_vertex) != Coordinate:
            raise ValueError('Node Objects only carry a Coordinate objects with attribute name .vertex')
        
        next_node = self
        while next_node.parent != None and next_node.parent != self:

            if next_node.vertex == wanted_vertex: 
                return next_node

            next_node = next_node.parent

        if enable_error:
            raise ValueError("Didn't find wanted vertex in given linkedlist")
        else:
            return None

    def get_intersections_data(self, blocks: list[block]) -> list[Intersection]:
        '''
        :return: list of Intersection objects        
        '''
        prev_vertex = self.vertex
        prev_node = self
        next_node = self.parent  # start iteration from second node
        intersections_data = []
        found_first = False

        # There is one stupid corner case where the first edge has the second intersection of a component pad ;)
        print('\nSTUPID CORNER CASE DETECTIN AND DEALING WITH CODE\n')
        done_intersections = []
        current_edge = Edge(prev_vertex, next_node.vertex, None)  
        print('stupid corner case: first edge', current_edge)
        for block in blocks:
            for coordinate in block.coordinates:

                # Must refresh it every loop because code here sometimes changes current_edge in false alarm situations
                current_edge = Edge(prev_vertex, next_node.vertex, None)  
                intersections = Coordinate.point_edge_intersection(current_edge, coordinate, block)
                if intersections != None:

                    if len(intersections) == 2:
                        pass  # will deal with it in the normal loop

                    elif len(intersections) == 1:
                        print('POSSIBLE stupid corner case: found one intersection, could be a second intersection!')
                        print()

                        # found a single component pad intersection in the very first edge, first node to second node
                        # finding out if this is the first intersection of a component pad or the second
                        # if it's the first intersection of a component pad then ignore else it's a problem ;)
                        first_or_second_inter= intersections[0]
                        edge_at_inter1or2 = current_edge
                        coordinate_to_find_inter1or2 = coordinate  # coordinate of center of componentpad
                        pre_inter1or2_node = prev_node
                        block_to_find_inter1or2 = block  # block of found componentpad

                        # Reversing the Node to test the previous nodes if this intersection has a pair previously
                        reversed_nodes = Node.reversed(prev_node)
                        prev_vertex_t = reversed_nodes.vertex
                        prev_node_t = reversed_nodes
                        next_node_t = reversed_nodes.parent

                        # Looking for the very next previous edge that has greater length than the average edge length
                        # So as to account for if the intersection found is moving away from a deadend trace
                        while next_node_t.parent != None and next_node_t.parent != reversed_nodes:

                            current_edge = Edge(prev_vertex_t, next_node_t.vertex, None)
                            if current_edge.absolute_length <= Graph.CURVE_THRESHOLD_LENGTH:
                                prev_vertex_t = next_node_t.vertex
                                prev_node_t = next_node_t
                                next_node_t = next_node_t.parent

                            else:
                                break

                        current_edge = current_edge.reversed()

                        print(f'stupid corner case: test previous edge {current_edge} if it has another intersection of the same componentpad\n')
                        intersections = Coordinate.point_edge_intersection(current_edge, coordinate_to_find_inter1or2, block_to_find_inter1or2)

                        if intersections == None:
                            print("False alarm, No second intersection of same component pad in previous edge, No stupid corner case\n")

                        else:
                            if len(intersections) == 1:
                                # pre_inter1_node = prev_node_t
                                # pre_inter1_node = prev_node_t.last_node
                                pre_inter1_node_deep_copy = Node.reversed(prev_node_t).pre_last_node
                                pre_inter1_node = self.find(pre_inter1_node_deep_copy.vertex).parent

                                found_intersection = Intersection(coordinate_to_find_inter1or2, 
                                    block_to_find_inter1or2, intersections[0], first_or_second_inter, 
                                    current_edge, edge_at_inter1or2, 
                                    pre_inter1_node, pre_inter1or2_node, True)

                                #IMP: Corner Case for trace of one single line, the algorithm detects two stupid_corner_case 
                                # Must detect which one is the real one, keep it and the other ignore it
                                # stupid_corner_case must have the very first edge of the trace pointing away from the componentpad behind it
                                if self.single_line_trace_with_comppad_at_ends_only and not edge_at_inter1or2.pointing_away_from_coord(coordinate_to_find_inter1or2):

                                        # False alarm it's not the stupid_corner_case it's the other componentpad >:)
                                        print("False alarm, it's the second false stupid_corner_case for a single line trace >:)")
                                        continue

                                else:
                                    print("Stupid corner case: found second intersection of an edge, stupid corner case DETECTED\n")
                                    intersections_data.append(found_intersection)

                                    # So we don't process it again in first iteration
                                    done_intersections.append([edge_at_inter1or2, coordinate_to_find_inter1or2])
                                    # So we don't process it again in last iteration, this is especially important if it's a deadend stupid corner case
                                    done_intersections.append([current_edge, coordinate_to_find_inter1or2])

                            elif len(intersections) == 2:
                                raise ValueError('THIS IS NOT POSSIBLE!!!!!!!')

        # Main Routine
        print('\nStarting Main Routine....\n')
        while next_node.parent != None and next_node.parent != self:

            # current working edge
            current_edge = Edge(prev_vertex, next_node.vertex, None)
            print()
            print(current_edge, 'current edge to be examined')

            # testing to see if it intersects with any component pad what so ever
            if not found_first:
                for block in blocks:
                    for coordinate in block.coordinates:
                        intersections = Coordinate.point_edge_intersection(current_edge, coordinate, block)


                        if intersections != None:

                            if [current_edge, coordinate] in done_intersections:
                                print('skipping processed intersection!')
                                continue

                            if not found_first:
                                if len(intersections) == 2:
                                    print('found 2 intersections in one edge')
                                    intersections_data.append(Intersection(coordinate, block, intersections[0], intersections[1], 
                                        current_edge, current_edge, prev_node, prev_node))

                                elif len(intersections) == 1:

                                    print('found first intersection of an edge')
                                    found_first = True
                                    first_intersection = intersections[0]
                                    edge_at_inter1 = current_edge
                                    coordinate_to_find_inter2 = coordinate  # coordinate of center of componentpad
                                    pre_inter1_node = prev_node
                                    block_to_find_inter2 = block  # block of found componentpad


            else:
                intersections = Coordinate.point_edge_intersection(current_edge, coordinate_to_find_inter2, block_to_find_inter2)

                if intersections != None:
                    if len(intersections) == 1:
                        print('found second intersection of an edge')
                        intersections_data.append(Intersection(coordinate_to_find_inter2, 
                            block_to_find_inter2, first_intersection, 
                            intersections[0], edge_at_inter1, current_edge,
                            pre_inter1_node, prev_node))

                        found_first = False
                        # so that when searching for the same edge on the next iteration, 
                        # we don't detect the same intersection and maybe detect new ones or just move on
                        done_intersections.append([current_edge, coordinate_to_find_inter2])
                        continue

                    elif len(intersections) == 2:
                        raise ValueError('THIS IS NOT POSSIBLE!!!!!!!')


            prev_vertex = next_node.vertex
            prev_node = next_node
            next_node = next_node.parent

        # Pre-Final iteration, the node which points to the node which has parent None or self
        print("\nPre-Last Iteration:\n")
        current_edge = Edge(prev_vertex, next_node.vertex, None)
        print()
        print(current_edge, 'current edge to be examined')

        # testing to see if it intersects with any component pad what so ever
        if not found_first:
            for block in blocks:
                for coordinate in block.coordinates:
                    intersections = Coordinate.point_edge_intersection(current_edge, coordinate, block)


                    if intersections != None:

                        if [current_edge, coordinate] in done_intersections:
                            print('skipping processed intersection!')
                            continue

                        if not found_first:
                            if len(intersections) == 2:
                                print('found 2 intersections in one edge')
                                intersections_data.append(Intersection(coordinate, block, intersections[0], intersections[1], 
                                    current_edge, current_edge, prev_node, prev_node))

                            elif len(intersections) == 1:

                                print('found first intersection of an edge')
                                found_first = True
                                first_intersection = intersections[0]
                                edge_at_inter1 = current_edge
                                coordinate_to_find_inter2 = coordinate  # coordinate of center of componentpad
                                pre_inter1_node = prev_node
                                block_to_find_inter2 = block  # block of found componentpad


        else:
            intersections = Coordinate.point_edge_intersection(current_edge, coordinate_to_find_inter2, block_to_find_inter2)

            if intersections != None:
                if len(intersections) == 1:
                    print('found second intersection of an edge in Pre-last iteration')
                    intersections_data.append(Intersection(coordinate_to_find_inter2, 
                        block_to_find_inter2, first_intersection, 
                        intersections[0], edge_at_inter1, current_edge,
                        pre_inter1_node, prev_node))

                    found_first = False

                    # this is the last iteration i don't think i need to do this but i won't remove anyway
                    done_intersections.append([current_edge, coordinate_to_find_inter2])

                    # Instead of the continue statement, which in Main Routine, checks for first intersections for same node
                    for block in blocks:
                        for coordinate in block.coordinates:
                            intersections = Coordinate.point_edge_intersection(current_edge, coordinate, block)


                            if intersections != None:

                                if [current_edge, coordinate] in done_intersections:
                                    print('skipping processed intersection!')
                                    continue

                                if not found_first:
                                    if len(intersections) == 2:
                                        print('found 2 intersections in one edge')
                                        intersections_data.append(Intersection(coordinate, block, intersections[0], intersections[1], 
                                            current_edge, current_edge, prev_node, prev_node))

                                    elif len(intersections) == 1:

                                        print('found first intersection of an edge')
                                        found_first = True
                                        first_intersection = intersections[0]
                                        edge_at_inter1 = current_edge
                                        coordinate_to_find_inter2 = coordinate  # coordinate of center of componentpad
                                        pre_inter1_node = prev_node
                                        block_to_find_inter2 = block  # block of found componentpad

                elif len(intersections) == 2:
                    raise ValueError('THIS IS NOT POSSIBLE!!!!!!!')

        # Checking if there will be a final iteration
        prev_vertex = next_node.vertex
        prev_node = next_node
        next_node = next_node.parent

        if next_node == self:
            # Final Iteration !!!
            print("\nLast Iteration:\n")
            current_edge = Edge(prev_vertex, next_node.vertex, None)
            print()
            print(current_edge, 'current edge to be examined')

            # testing to see if it intersects with any component pad what so ever
            if not found_first:
                for block in blocks:
                    for coordinate in block.coordinates:
                        intersections = Coordinate.point_edge_intersection(current_edge, coordinate, block)


                        if intersections != None:

                            if [current_edge, coordinate] in done_intersections:
                                print('skipping processed intersection!')

                                # instead of the continue statement
                                print("\nLoop Finished, Intersection data extracted!\n\n")
                                return intersections_data

                            if not found_first:
                                if len(intersections) == 2:
                                    print('found 2 intersections in one edge')
                                    intersections_data.append(Intersection(coordinate, block, intersections[0], intersections[1], 
                                        current_edge, current_edge, prev_node, prev_node))

                                elif len(intersections) == 1:
                                    pass  # This is stupid_corner_case from the other side :)


            else:
                intersections = Coordinate.point_edge_intersection(current_edge, coordinate_to_find_inter2, block_to_find_inter2)

                if intersections != None:
                    if len(intersections) == 1:
                        print('found second intersection of an edge in Pre-last iteration')
                        intersections_data.append(Intersection(coordinate_to_find_inter2, 
                            block_to_find_inter2, first_intersection, 
                            intersections[0], edge_at_inter1, current_edge,
                            pre_inter1_node, prev_node))

                        found_first = False

                        # this is the last iteration i don't think i need to do this but i won't remove anyway
                        done_intersections.append([current_edge, coordinate_to_find_inter2])

                        # Instead of the continue statement, which in Main Routine, checks for first intersections for same node
                        for block in blocks:
                            for coordinate in block.coordinates:
                                intersections = Coordinate.point_edge_intersection(current_edge, coordinate, block)


                                if intersections != None:

                                    if [current_edge, coordinate] in done_intersections:
                                        print('skipping processed intersection!')

                                        # instead of the continue statement
                                        print("\nLoop Finished, Intersection data extracted!\n\n")
                                        return intersections_data

                                    if not found_first:
                                        if len(intersections) == 2:
                                            print('found 2 intersections in one edge')
                                            intersections_data.append(Intersection(coordinate, block, intersections[0], intersections[1], 
                                                current_edge, current_edge, prev_node, prev_node))

                                        elif len(intersections) == 1:
                                            pass  # This is stupid_corner_case from the other side :)
                                           
                    elif len(intersections) == 2:
                        raise ValueError('THIS IS NOT POSSIBLE!!!!!!!')

        print("\nLoop Finished, Intersection data extracted!\n\n")

        return intersections_data

    def add_comppad(self, blocks: list[Block], terminate_after=False) -> Node:
        '''
        :param blocks: list of ComponentPad Block objects

        '''
        print('NEW CALLLL!!!!!!\n')

        ### Step 1: Find all the intersection data between all the traces and all the component pads :)
        trace_nodes = deepcopy(self)

        print(self, 'before extracting intersection data')
        intersections_data = self.get_intersections_data(blocks)
        print(self, 'after extracting intersection data, MUST BE THE SAME AS BEFORE INTERSECTION DATA EXTRACTOR ALGORITHM RAN')

        # if not self.test_all_parents_values(temp_self):
        #     return ValueError('Node.get_intersections_data() ulters the linkedlist, THIS IS HIGHLY UNACCEPTABLE!')

        if self.single_line_trace_with_comppad_at_ends_only and len(intersections_data) != 2:
            raise ValueError(f"WHAT THE FUCK?!??!?!?!??!!!!!???!!!!!!!\n{self}")

        if [intersection.stupid_corner_case_flag for intersection in intersections_data].count(True) > 1:
            raise ValueError("Somehow the intersecion data extraction algorithm detected more than one stupid_corner_case ;(")

        ### Step 2: remove all old vertices in between intersections and add new component pad vertices
        print()
        stupid_corner_case_flag = False
        single_line_trace_with_comppad_at_ends_only_flag = self.single_line_trace_with_comppad_at_ends_only
        for intersection in intersections_data:

            print('CURRENT INTERSECTION DATA TO EXECUTE:\n')
            print(intersection, '\n')

            if intersection.stupid_corner_case_flag:
                ### Pre-Step for stupid corner case
                print('Pre-Step for stupid corner case: changed vertex value of headnode to intersection.inter2_coord:')
                print(f"from {self.vertex} to {intersection.inter2_coord}\n")
                self.vertex = intersection.inter2_coord

            ### Step 1:
            print(f"Step 1: change parent of node pre_inter1_node: <{repr(self.child(intersection.pre_inter1_node.parent))}> to: <{repr(Node(intersection.inter1_coord, None))}>")

            self.child(intersection.pre_inter1_node.parent).parent = Node(intersection.inter1_coord, None)
            print(self, '\n')

            ### Step 2:
            self.extend(Intersection.generate_comppad_nodes(intersection, trace_nodes))
            print("Step 2: fill in the componentpad nodes\n", f"{self}\n")

            ### Step 3:
            print(f"Step 3: extending the current linkedlist with a node of inter2_coord: {intersection.inter2_coord}")
            self.extend(Node(intersection.inter2_coord, None))
            print(self, '\n')

            if intersection.stupid_corner_case_flag:
                ### Post Step for stupid corner case
                print('Post-Step for stupid corner case: Joining the linkedlist')
                self.pre_last_node.parent = self  # I don't use normal .make_it_loop() because the last node is already added in step 3
                stupid_corner_case_flag = False

            else:

                if single_line_trace_with_comppad_at_ends_only_flag:
                    print("single_line_trace_with_comppad_at_ends_only Corner Case Step 4: ")
                    #TODO: write explanation
                    self.extend(intersection.pre_inter2_node.parent)

                else:
                    ### Step 4:
                    print(f"Step 4: extending the current linkedlist with a node of value intersection.inter2_edge.end: {intersection.inter2_edge.end}")
                    print(f"and parent intersection.pre_inter2_node.parent: {repr(intersection.pre_inter2_node.parent)}")
                    self.extend(Node(intersection.inter2_edge.end, intersection.pre_inter2_node.parent))
            print(self, '\n')

            print()

        print('Number of intersections_data: ', len(intersections_data))
        print()

        self.visualize(multiplier=15, x_offset=27, speed=5, terminate=terminate_after)

    def __repr__(self) -> str:
        '''
        repr representation
        '''
        try:
            return f"{self.vertex}, Parent: {self.parent.vertex}"
        except AttributeError:
            return f"{self.vertex}, Parent: None"

    def __str__(self) -> str:
        '''
        string representation of the linkedlist made of nodes
        '''

        string_representation = ""

        next_node = self
        while next_node.parent != None and next_node.parent != self:
            string_representation += f"{next_node.vertex}, "
            next_node = next_node.parent

        string_representation += f"{next_node.vertex}, "

        if next_node.parent == self:
            string_representation += f"{next_node.parent.vertex}, ... (loops)"

        else:
            string_representation += f"{next_node.parent}"  # aka None

        return string_representation


class ShapeType(Enum):
    Circle = 'C'
    Rectangle = 'R'
    Oval = 'O'


class Infinity():
    def __init__(self):
        self.value = 'infinity'

    def __add__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __radd__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __sub__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __rsub__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __mul__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __rmul__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __truediv__(self, other) -> Infinity:
        '''
        add magic method to divide addition
        '''
        return Infinity()

    def __rtruediv__(self, other) -> Infinity:
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

    def __round__(self, value: int) -> Infinity:
        '''
        inifinity is rounded to infinity
        '''
        return Infinity()

    def __str__(self) -> str:
        return '<Infinity bitches>'


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

    def __round__(self, accuracy: int) -> None:
        '''
        Rounds x, y and z values to 'accuracy' decimal place
        '''
        self.x = round(self.x, accuracy)
        self.y = round(self.y, accuracy)
        if self.z:
            self.z = round(self.z, accuracy)

    def inside_polygon(self, nodes: Node) -> bool:
        '''
        return whether or not this coordinate resides inside the argument closed polygon

        if even number of intersections -> outside -> False
        else: -> inside -> True
        '''
        intersections = 0

        edges = nodes.to_edge_list()
        for edge in edges:
            if edge.gradient == 0:
                continue

            elif edge.gradient == Infinity():
                # gradient test will definitly pass
                # range test is the deciding factor
                # x axis
                if self.x < edge.start.x:
                    # y axis
                    if (self.y < edge.start.y and self.y > edge.end.y) or (self.y > edge.start.y and self.y < edge.end.y):
                        intersections += 1

            else:
                # x coord test
                x_line = round((self.y - edge.y_intercept) / edge.gradient, 5)
                if self.x < x_line:
                    # y axis
                    if (self.y < edge.start.y and self.y > edge.end.y) or (self.y > edge.start.y and self.y < edge.end.y):
                        intersections += 1

        return intersections%2 == 1

    @property
    def origin(self) -> Coordinate:
        '''
        returns the origin coordinate
        '''
        return Coordinate(0, 0)

    def within_edge(self, edge: Edge, thickness: float) -> bool:
        '''
        #NOTE: Please Refer to iPad Notes pg86
        Angle SVE must be acute for the vertex to be in between an edge range
        :return: boolean value
        '''
        a = edge.absolute_length
        b = Edge(edge.end, self, None).absolute_length
        c = Edge(edge.start, self, None).absolute_length
        B = round(acos( ( a**2 + c**2 - b**2 )/( 2*a*c ) ), 5)
        C = round(acos( ( a**2 + b**2 - c**2 )/( 2*a*b ) ), 5)

        return (B <= 90 and C <= 90)

    def get_side_open_polygon(self, pre_inter1_node, post_inter2_node) -> bool:
        '''
        return whether the given coordinate is to the right or the left of the node
        >0 intersection means it's on left, return True
        0 intersection means it's on the right, return False
        as rays goes from left to right
        '''
        # the ray is y=self.y, a horizontal line
        edges = pre_inter1_node.to_list()
        edges = edges[:edges.index(post_inter2_node.vertex)]

        intersections = 0
        for edge in edges:
            if edge.gradient == 0:
                continue

            elif edge.gradient == Infinity():
                # gradient test will definitly pass
                # range test is the deciding factor
                # x axis
                if self.x < edge.start.x:
                    # y axis
                    if (self.y < edge.start.y and self.y > edge.end.y) or (self.y > edge.start.y and self.y < edge.end.y):
                        intersections += 1

            else:
                # x coord test
                x_line = round((self.y - edge.y_intercept) / edge.gradient, 5)
                if self.x < x_line:
                    # y axis
                    if (self.y < edge.start.y and self.y > edge.end.y) or (self.y > edge.start.y and self.y < edge.end.y):
                        intersections += 1

        return intersections%2 == 0

    @classmethod
    def get_min_max(cls, coordinates_list: list[Coordinate]) -> tuple[Coordinate, Coordinate]:
        '''
        finds the Min, Max of X and Y coordinates from input list of coordinates

        :param coordinates: list of coordinates [(x, y), ..]
        :return: ((x_min, y_min), (x_max, y_max))
        '''

        if len(coordinates_list) == 0:
            raise ValueError('An empty list is passed')

        if len(set([type(i) for i in coordinates_list])) != 1:
            raise ValueError('All values in coordinates_list argument must be of type Coordinate')

        if type(coordinates_list[0]) != Coordinate:
            raise ValueError('All values in coordinates_list argument must be of type Coordinate')

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
    def generate_semicircle_coordinates(cls, coordinate1: Coordinate, coordinate2: Coordinate, 
            delta_x: float, delta_y: float, resolution: int =21) -> list[Coordinate]:
        '''
        :param coordinate1: The coordinate the list of semicircle coordinates start from
        :param coordinate2: The coordinate the list of semicircle coordinates ends at
        :param orientation: the orientation of the semicircle
        :param resolution: The number of coordinates in the list of semicircle coordinates

        :return: list of coordinates that if joined with straight makes a pseudo semicircle
        '''
        if type(resolution) != int:
            raise ValueError("resolution must be of type int")
        if not(resolution // 2 != resolution /2):
            raise ValueError('resolution argument MUST be ODD number, \nas there will be pairs of coordinates PLUS the final single coordinate which will always result in an odd number. \nRefer to iPad notes to understand more')

        if delta_x > 0:
            orientation = False
        elif delta_x < 0:
            orientation = True
        elif delta_x == 0:
            if delta_y > 0:
                orientation = False
            elif delta_y < 0:
                orientation = True

        ### Step 1: Get circle equation attributes
        # a and b are the x and y offset value from circle center respectively
        # They are also the midpoints between coord1 and coord2
        a = round((coordinate1.x + coordinate2.x) / 2, 3)
        b = round((coordinate1.y + coordinate2.y) / 2, 3)

        # r is the radius of circle
        # It's also the half length form coordinate1 to coordinate2
        r = round( (math.sqrt( (coordinate2.x - coordinate1.x)**2 + (coordinate2.y - coordinate1.y)**2 ) / 2) , 3)

        if coordinate2.x == coordinate1.x:  # Gradient = infinity
            ### Step 2: Get linear equation of the line that passes through the circle diameter, aka the 2 coordinates
            # Getting equation of a vertical line
            x = coordinate1.x
            # y = y  # the independent variable of a vertical line is y

            ### Step 3: Getting linear equation of tangent to the circle at the maximum
            if orientation:
                x_max = x + r
            else:
                x_max = x - r
            y = b
            max_coord = Coordinate(x_max, b)

            ### Step 4: Getting the list of x values of vertical line equations that intersects the circle
            x_range = x_max - x
            num_iterations = int((resolution-1)/2)
            increment = round(x_range / (num_iterations + 1), 5)
            x_values = []
            for iter_ind in range(1, num_iterations+1):
                x_values.append(x + iter_ind*increment)

            ### Step 5: Getting the intersection between circle equation and all the intersection linear equations
            semicircle_coords_positive = []
            semicircle_coords_negative = []
            for current_x_value in x_values:
                y1 = round(b + math.sqrt(round(r**2 - (current_x_value - a)**2, 6)), 5)
                semicircle_coords_positive.append(Coordinate(round(current_x_value, 6), y1))

                y2 = round(b - math.sqrt(round(r**2 - (current_x_value - a)**2, 6)), 5)
                if y1 != y2: # to eleminate max point
                    semicircle_coords_negative.append(Coordinate(round(current_x_value, 6), y2))

        elif coordinate2.y == coordinate1.y:  # Gradient = 0.0
            ### Step 2: Get linear equation of the line that passes through the circle diameter, aka the 2 coordinates
            # Getting equation of a horizontal line
            # x = x  # the independent variable of a horizontal line is x
            y = coordinate1.y

            ### Step 3: Getting linear equation of tangent to the circle at the maximum and max coord
            x = a
            if orientation:
                y_max = y + r
            else:
                y_max = y - r
            max_coord = Coordinate(a, y_max)

            ### Step 4: Getting the list of y_intercepts of linear equations that intersects the circle
            y_range = y_max - y
            num_iterations = int((resolution-1)/2)
            increment = round(y_range / (num_iterations + 1), 5)
            y_values = []
            for iter_ind in range(1, num_iterations+1):
                y_values.append(y + iter_ind*increment)

            ### Step 5: Getting the intersection between circle equation and all the intersection linear equations
            semicircle_coords_positive = []
            semicircle_coords_negative = []
            for current_y_value in y_values:
                x1 = round(a + math.sqrt(round(r**2 - (current_y_value - b)**2, 6)), 5)
                semicircle_coords_positive.append(Coordinate(x1, round(current_y_value, 6)))

                x2 = round(a - math.sqrt(round(r**2 - (current_y_value - b)**2, 6)), 5)
                if x1 != x2: # to eleminate max point
                    semicircle_coords_negative.append(Coordinate(x2, round(current_y_value, 6)))

        else:
            ### Step 2: Get linear equation of the line that passes through the circle diameter, aka the 2 coordinates
            # Get the linear equation of the diameter coordinates
            gradient = (coordinate2.y - coordinate1.y) / (coordinate2.x - coordinate1.x)
            y_intercept = coordinate1.y - gradient*coordinate1.x

            # Get the linear equation of the inverse of the diameter linear equation
            inverse_gradient = -1/gradient
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
            x1 = round((-b_q + math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)
            x2 = round((-b_q - math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)

            # Getting values of y by substituting in inverse linear equation
            y1 = inverse_gradient*x1 + inverse_y_intercept
            y2 = inverse_gradient*x2 + inverse_y_intercept

            # Choosing the correct maximum point, according to orientation argument
            if orientation:
                max_coord = Coordinate(x1, y1)
            else:
                max_coord = Coordinate(x2, y2)


            # Getting linear equation of correct maximum point and saving it in a variable, (ignoring minimum point)
            maximum_line_gradient = gradient
            maximum_line_y_intercept = max_coord.y - maximum_line_gradient*max_coord.x

            ### Step 4: Getting the list of y_intercepts of linear equations that intersects the circle
            y_intercept_range = maximum_line_y_intercept - y_intercept
            num_iterations = int((resolution-1)/2)
            increment = round(y_intercept_range / (num_iterations + 1), 5)
            y_intercept_list = [] 
            for iter_ind in range(1, num_iterations+1):
                y_intercept_list.append(y_intercept + iter_ind*increment)

            ### Step 5: Getting the intersection between circle equation and all the intersection linear equations
            # from the diameter to the maximum line.
            semicircle_coords_positive = []
            semicircle_coords_negative = []
            for current_y_intercept in y_intercept_list:
                a_q = 1 + gradient**2
                b_q = -2*a + 2*gradient*current_y_intercept - 2*b*gradient
                c_q = current_y_intercept**2 - 2*b*current_y_intercept + b**2 - r**2 + a**2

                if b_q**2 - 4*a_q*c_q > 0: 
                    x1 = round((-b_q + math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)
                    y1 = round(gradient*x1 + current_y_intercept, 6)
                    semicircle_coords_positive.append(Coordinate(x1, y1))

                    x2 = round((-b_q - math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)
                    y2 = round(gradient*x2 + current_y_intercept, 6)
                    semicircle_coords_negative.append(Coordinate(x2, y2))
                else:
                    raise ValueError("SHITTT")
                    # print('SHITTTT')

        ### Step 6: Get the final ordered list of coordinates
        # PLEASE refer to iPad. The combination are truly ENORMOUS and was difficult to derive ;)
        ordered_semicircle_coords = []
        if delta_x > 0:
            if coordinate2.y > coordinate1.y:
                if delta_y > 0:
                    ordered_semicircle_coords.extend(semicircle_coords_positive)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_negative))

                elif delta_y < 0:
                    ordered_semicircle_coords.extend(semicircle_coords_negative)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_positive))

                elif delta_y == 0:
                    ordered_semicircle_coords.extend(semicircle_coords_negative)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_positive))

            elif coordinate1.y > coordinate2.y:
                if delta_y > 0:
                    ordered_semicircle_coords.extend(semicircle_coords_negative)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_positive))

                elif delta_y < 0:
                    ordered_semicircle_coords.extend(semicircle_coords_positive)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_negative))

                elif delta_y == 0:
                    ordered_semicircle_coords.extend(semicircle_coords_positive)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_negative))

            else:
                raise ValueError('NOT FUCKING POSSIBLE (acoording to my calculations ;) )')

        elif delta_x < 0:
            if coordinate2.y > coordinate1.y:
                if delta_y > 0:
                    ordered_semicircle_coords.extend(semicircle_coords_negative)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_positive))

                elif delta_y < 0:
                    ordered_semicircle_coords.extend(semicircle_coords_positive)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_negative))
 
                elif delta_y == 0:
                    ordered_semicircle_coords.extend(semicircle_coords_negative)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_positive))

            elif coordinate1.y > coordinate2.y:
                if delta_y > 0:
                    ordered_semicircle_coords.extend(semicircle_coords_positive)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_negative))

                elif delta_y < 0:
                    ordered_semicircle_coords.extend(semicircle_coords_negative)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_positive))

                elif delta_y == 0:
                    ordered_semicircle_coords.extend(semicircle_coords_positive)
                    ordered_semicircle_coords.append(max_coord)
                    ordered_semicircle_coords.extend(reversed(semicircle_coords_negative))

            else:
                raise ValueError('NOT FUCKING POSSIBLE (acoording to my calculations ;) )')

        elif delta_x == 0:
            if coordinate1.x > coordinate2.x:
                ordered_semicircle_coords.extend(semicircle_coords_positive)
                ordered_semicircle_coords.append(max_coord)
                ordered_semicircle_coords.extend(reversed(semicircle_coords_negative))

            elif coordinate2.x > coordinate1.x:
                ordered_semicircle_coords.extend(semicircle_coords_negative)
                ordered_semicircle_coords.append(max_coord)
                ordered_semicircle_coords.extend(reversed(semicircle_coords_positive))

            else:
                raise ValueError('NOT FUCKING POSSIBLE (acoording to my calculations ;) )')


        return ordered_semicircle_coords

    @classmethod
    def test_generate_semicircle(cls):
        '''
        test points:

        v1 = Coordinate(27.172, 30.953)
        v2 = Coordinate(26.608, 31.517)

        v1 = Coordinate(50.367, 28.848)
        v2 = Coordinate(49.803, 29.412)

        v1 = Coordinate(8.827, 31.518)
        v2 = Coordinate(9.393, 30.952)

        v1 = Coordinate(20.828, 31.517)
        v2 = Coordinate(21.392, 30.953)

        v1 = Coordinate(50.358, 15.824)
        v2 = Coordinate(49.558, 15.824)
        '''
        # Data set to test the generate_semicircle_coordinates()
        # According to my calculations there is only 16 possible cases
        #NOTE: PLEASE REFER TO iPad notes to understand the 14 possible cases
        # The following data set is in order of how I indexed the cases in the iPad
        data = [(Coordinate(1, 2), Coordinate(3, 2), 0, 3, 11),  # 1&3
                (Coordinate(3, 2), Coordinate(1, 2), 0, -3, 11),  # 2&4

                (Coordinate(2, 3), Coordinate(2, 1), 5, 0, 11),  # 5
                (Coordinate(2, 1), Coordinate(2, 3), 5, 0, 11),  # 6
                (Coordinate(2, 1), Coordinate(2, 3), -5, 0, 11),  # 7
                (Coordinate(2, 3), Coordinate(2, 1), -5, 0, 11),  # 8

                (Coordinate(3, 1), Coordinate(1, 3), -5, -3, 11),  # 9
                (Coordinate(1, 3), Coordinate(3, 1), -5, -3, 11),  # 10
                (Coordinate(3, 1), Coordinate(1, 3), 5, 3, 11),  # 11
                (Coordinate(1, 3), Coordinate(3, 1), 5, 3, 11),  # 12

                (Coordinate(1, 1), Coordinate(3, 3), 5, -3, 11),  # 13
                (Coordinate(3, 3), Coordinate(1, 1), 5, -3, 11),  # 14
                (Coordinate(1, 1), Coordinate(3, 3), -5, 3, 11),  # 15
                (Coordinate(3, 3), Coordinate(1, 1), -5, 3, 11)]  # 16
                
        # data = [data[1]]

        for datum_ind, datum in enumerate(data):
            vertex1, vertex2, delta_x, delta_y, resolution = datum
            print("Semicircle Coords !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(vertex1)
            print(vertex2)
            new_graph = Graph()
            new_graph.add_vertex(vertex1)

            semicircle_vertices =  Coordinate.generate_semicircle_coordinates(vertex1, vertex2, delta_x, delta_y, resolution)
            for semicircle_vertex in semicircle_vertices:
                new_graph.add_vertex(semicircle_vertex)

            new_graph.add_vertex(vertex2)

            prev_semicircle_vertex = vertex1
            for ind, semicircle_vertex in enumerate(semicircle_vertices):
                print('Point number = ', ind)
                print(prev_semicircle_vertex, '->', semicircle_vertex)
                new_graph.add_edge(Edge(prev_semicircle_vertex, semicircle_vertex, LASER_BEAM_THICKNESS))
                prev_semicircle_vertex = semicircle_vertex

            print('Point number = ', ind+1)
            print(prev_semicircle_vertex, '->', vertex2)
            edge2 = Edge(prev_semicircle_vertex, vertex2, LASER_BEAM_THICKNESS)
            new_graph.add_edge(edge2)


            print()

            if (datum_ind+1) != len(data):
                new_graph.visualize(x_offset=2, y_offset=2, multiplier=200, terminate=False, speed=0)

        print(f"Vertex Count: {new_graph.vertex_count}, Should be: {len(semicircle_vertices)+2}")
        print(f"Edge Count: {new_graph.edge_count}, should be: {(len(semicircle_vertices)+2)*2 - 2}")

        new_graph.visualize(x_offset=2, y_offset=2, multiplier=200, terminate=True, speed=0)

        raise ValueError('END')

    @classmethod
    def point_edge_intersection(cls, edge: Edge, coordinate: Coordinate, block: Block) -> Optional[list[Coordinate]]:
        '''
        Finds the intersection between edges of a graph (offseted traces) and the componentPad (offseted)
        :param edge: edge on the graph to intersect the component pad
        :param coordinate: center of the componentpad that if offset applied might intersect the edge
        :param block: The Block datatype object in which this ComponentPad Coordinate belong to

        :return: None if no intersection, 1 coordinate of the single intersection found or 2 coordinates if 2 intersections found
        '''
        intersections = []
        if block.shape_type == ShapeType.Circle or (block.shape_type == ShapeType.Oval and block.thickness == block.thickness2):

            a = coordinate.x
            b = coordinate.y
            r = round(block.thickness/2, 5)

            if edge.gradient == Infinity():
                # Getting equation of a vertical line
                x = edge.start.x

                # Getting min and maximum
                if edge.start.y > edge.end.y:
                    y_min = edge.end.y
                    y_max = edge.start.y
                else:
                    y_min = edge.start.y
                    y_max = edge.end.y

                # Getting intersection with vertical line
                if (r**2 - (x-a)**2) >= 0:
                    # Solutions Present
                    y1 = round(b - math.sqrt(round(r**2 - (x - a)**2, 6)), 5)
                    y2 = round(b + math.sqrt(round(r**2 - (x - a)**2, 6)), 5)
                    
                    # Within edge check
                    if y1 <= y_max and y1 >= y_min:
                        print(edge, coordinate, 'm inf 1')
                        print(x, y1)
                        print()
                        intersections.append(Coordinate(x, y1))

                    # Within edge check and repeated root check
                    if y2 <= y_max and y2 >= y_min and y1 != y2:
                        print(edge, coordinate, 'm inf 2')
                        print(x, y2)
                        print()
                        intersections.append(Coordinate(x, y2))

                else:
                    # No intersection what so ever
                    return None

            elif edge.gradient == 0:

                # Getting equation of a horizontal line
                y = edge.start.y

                # Getting min and maximum
                if edge.start.x > edge.end.x:
                    x_min = edge.end.x
                    x_max = edge.start.x
                else:
                    x_min = edge.start.x
                    x_max = edge.end.x

                # Getting intersection with vertical line
                if (r**2 - (y-b)**2) >= 0:
                    # Solutions Present
                    x1 = round(a - math.sqrt(round(r**2 - (y - b)**2, 6)), 5)
                    x2 = round(a + math.sqrt(round(r**2 - (y - b)**2, 6)), 5)
                    
                    # Within Edge check
                    if x1 <= x_max and x1 >= x_min:
                        print(edge, coordinate, 'm0 1')
                        print(x1, y)
                        print()
                        intersections.append(Coordinate(x1, y))

                    # Within Edge check and same root check
                    if x2 <= x_max and x2 >= x_min and x1 != x2:
                        print(edge, coordinate, 'm0 2')
                        print(x2, y)
                        print()
                        intersections.append(Coordinate(x2, y))

                else:
                    # No intersection what so ever
                    return None

            else:

                # edge linear equation is given by getter attributes .gradient and .y_intercept
                gradient = edge.gradient
                y_intercept = edge.y_intercept

                # Getting min and maximum
                if edge.start.y > edge.end.y:
                    y_min = edge.end.y
                    y_max = edge.start.y
                else:
                    y_min = edge.start.y
                    y_max = edge.end.y

                # Getting intersection with line, solving simultaneous equation between circle and edge linear equation 
                a_q = 1 + gradient**2
                b_q = -2*a + 2*gradient*y_intercept - 2*b*gradient
                c_q = y_intercept**2 - 2*b*y_intercept + b**2 - r**2 + a**2
                if round(b_q**2 - 4*a_q*c_q, 5) >= 0:
                    # Solving quadratic equation using quadratic formula
                    x1 = round((-b_q + math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)
                    x2 = round((-b_q - math.sqrt(round(b_q**2 - 4*a_q*c_q, 5))) / (2*a_q), 5)

                    # Getting values of y by substituting in inverse linear equation
                    y1 = round(gradient*x1 + y_intercept, 5)
                    y2 = round(gradient*x2 + y_intercept, 5)

                    # Within edge check
                    if y1 <= y_max and y1 >= y_min:
                        print(edge, coordinate, 'else 1')
                        print(x1, y1)
                        print()
                        intersections.append(Coordinate(x1, y1))

                    # Within edge check and repeated root check
                    if y2 <= y_max and y2 >= y_min and y1 != y2:
                        print(edge, coordinate, 'else 2')
                        print(x2, y2)
                        print()
                        intersections.append(Coordinate(x2, y2))

                else:
                    return None

        elif block.shape_type == ShapeType.Rectangle:
            # Refrence iPad Notes for more details
            # Getting the Coordinates of the square
            v1 = Coordinate(coordinate.x - round(block.thickness/2, 5), coordinate.y + round(block.thickness2/2, 5))
            v2 = Coordinate(coordinate.x + round(block.thickness/2, 5), coordinate.y + round(block.thickness2/2, 5))
            v3 = Coordinate(coordinate.x - round(block.thickness/2, 5), coordinate.y - round(block.thickness2/2, 5))
            v4 = Coordinate(coordinate.x + round(block.thickness/2, 5), coordinate.y - round(block.thickness2/2, 5))
            e1 = Edge(v1, v2, None)
            e2 = Edge(v1, v3, None)
            e3 = Edge(v2, v4, None)
            e4 = Edge(v3, v4, None)

            ### Step 1: Get intersection between the edge and all the four lines of the square
            x_values = []
            y_values = []
            intersected_edges = []
            if edge.gradient != e1.gradient:
                intersected_edges.append(e1)
                y_values.append(v1.y)  # or v2.y
                if edge.gradient != Infinity():
                    x_values.append(round((y_values[-1] - edge.y_intercept)/edge.gradient, 5))
                else:
                    x_values.append(edge.start.x)  # or edge.end.x

            if edge.gradient != e2.gradient:
                intersected_edges.append(e2)
                x_values.append(v1.x)  # or v3.x
                if edge.gradient != 0:
                    y_values.append(edge.gradient*x_values[-1] + edge.y_intercept)
                else:
                    y_values.append(edge.start.y)  # or edge.end.y

            if edge.gradient != e3.gradient:
                intersected_edges.append(e3)
                x_values.append(v2.x) # or v4.x
                if edge.gradient != 0:
                    y_values.append(edge.gradient*x_values[-1] + edge.y_intercept)
                else:
                    y_values.append(edge.start.y)  # or edge.end.y

            if edge.gradient != e4.gradient:
                intersected_edges.append(e4)
                y_values.append(v3.y)  # or v4.y
                if edge.gradient != Infinity():
                    x_values.append(round((y_values[-1] - edge.y_intercept)/edge.gradient, 5))
                else:
                    x_values.append(edge.start.x)  # or edge.end.x

            ### Step 2: testing if intersection is within edge and square edge
            # Getting min and maximum
            if edge.start.x > edge.end.x:
                x_min = edge.end.x
                x_max = edge.start.x
            else:
                x_min = edge.start.x
                x_max = edge.end.x

            if edge.start.y > edge.end.y:
                y_min = edge.end.y
                y_max = edge.start.y
            else:
                y_min = edge.start.y
                y_max = edge.end.y

            x_mins = []
            y_mins = []
            x_maxs = []
            y_maxs = []
            for intersected_edge in intersected_edges:
                if intersected_edge.start.x > intersected_edge.end.x:
                    x_mins.append(intersected_edge.end.x)
                    x_maxs.append(intersected_edge.start.x)
                else:
                    x_mins.append(intersected_edge.start.x)
                    x_maxs.append(intersected_edge.end.x)

                if intersected_edge.start.y > intersected_edge.end.y:
                    y_mins.append(intersected_edge.end.y)
                    y_maxs.append(intersected_edge.start.y)
                else:
                    y_mins.append(intersected_edge.start.y)
                    y_maxs.append(intersected_edge.end.y)

            intersections = []
            for x, y, x_min2, x_max2, y_min2, y_max2 in zip(x_values, y_values, x_mins, x_maxs, y_mins, y_maxs):
                if x <= x_max and x >= x_min and y <= y_max and y >= y_min and x <= x_max2 and x >= x_min2 and y <= y_max2 and y >= y_min2:
                    print(edge, coordinate, 'Square')
                    print(x, y)
                    print()
                    intersections.append(Coordinate(round(x, 6), round(y, 6)))

            if intersections:
                return intersections
            else:
                return None

        elif block.shape_type == ShapeType.Oval:
            return None

        else:
            raise ValueError(f'Unkonwn ShapeType: {block.shape_type}')

        if len(intersections) > 1:
            # Order intersections with right order, first encounter then second encounter
            # Finding distance between intersection coordinate and edge.start
            distance_edge_start_inter1 = round(math.sqrt(round((intersections[0].x - edge.start.x)**2 
                + (intersections[0].y - edge.start.y)**2, 5)), 5)

            distance_edge_start_inter2 = round(math.sqrt(round((intersections[1].x - edge.start.x)**2 
                + (intersections[1].y - edge.start.y)**2, 5)), 5)

            if distance_edge_start_inter1 > distance_edge_start_inter2:
                intersections = [intersections[1], intersections[0]]

        return intersections


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
        return round(self.end.x - self.start.x, 5)

    @property
    def delta_y(self) -> float:
        '''
        :return delta y
        '''
        return round(self.end.y - self.start.y, 5)
    
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
        if self.gradient == Infinity():
            return Infinity()
        return self.start.y - self.gradient*self.start.x

    @property
    def absolute_length(self) -> float:
        '''
        return absolute length
        '''
        return round(math.sqrt(round((self.delta_x)**2 + (self.delta_y)**2, 5)), 6)

    @property
    def midpoint(self) -> Coordinate:
        '''
        :returns the midpoint coordinate of an edge
        '''
        return Coordinate(round((self.start.x + self.end.x)/2, 6), round((self.start.y + self.end.y)/2, 6))

    @property
    def angle_from_x_axis(self) -> float:
        '''
        return positive degrees from the x axis
        '''
        angle = round(atan(self.gradient), 5)
        # converting arctan value to proper angle value according to position of end coord
        if self.end.x > 0:
            # converting negative arctan output to +ve value
            if angle < 0:
                angle += 360

        else:
            # converting negative arctan output to +ve value
            angle += 180

        return angle

    def angle_between(self, edge: Edge) -> float:
        '''
        returns the angle from in between two edges 
        
        #NOTE: Refer to iPad Pg-89
        '''
        if self.gradient == edge.gradient:
            if self.is_same_direction(edge):
                print('\n\n\nhappennnneddd\n\n\n')
                return 360
            
            else:
                return 180

        if self.start == edge.start:
            a = self.absolute_length
            b = edge.absolute_length

        else:
            intersection = self.intersection(edge)
            a = Edge(intersection, self.end, None).absolute_length
            b = Edge(intersection, edge.end, None).absolute_length

        c = Edge(self.end, edge.end, None).absolute_length
        C = round(acos( ( a**2 + b**2 - c**2 )/( 2*a*b ) ), 5)
        return C

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
    def visualize_edges(cls, edges: list[Edge], hide_turtle=True, speed=0, x_offset=20, y_offset=20, line_width=3, multiplier=8, terminate=False) -> None:
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

        turtle.setpos((edges[0].start.x - x_offset) * multiplier, (edges[0].start.y - y_offset) * multiplier)
        for edge in edges:
            turtle.down()
            turtle.setpos((edge.start.x - x_offset) * multiplier, (edge.start.y - y_offset) * multiplier)
            turtle.setpos((edge.end.x - x_offset) * multiplier, (edge.end.y - y_offset) * multiplier)
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
        if self.gradient != Infinity() and other.gradient != Infinity():
            if (self.gradient - other.gradient) != 0:
                x = round((self.y_intercept - other.y_intercept) / (self.gradient - other.gradient), 5)
                y = round(self.gradient * x + self.y_intercept, 3)
                return Coordinate(x, y)
            else:
                return None

        elif self.gradient == Infinity() and other.gradient != Infinity():
            x = self.start.x
            y = round(other.gradient*x + other.y_intercept, 3)
            return Coordinate(x, y)

        elif self.gradient != Infinity() and other.gradient == Infinity():
            x = other.start.x
            y = round(self.gradient*x + self.y_intercept, 3)
            return Coordinate(x, y)

        elif self.gradient == Infinity() and other.gradient == Infinity():
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
           
    def pointing_away_from_coord(self, coordinate: Coordinate) -> bool:
        '''
        if the coordinate exists before the receprical line intersecting the midpoint of the edge, 
        it's behind the edge if it exists after the receprical line intersecting the midpoint of the edge it's after

        :returns: whether the direction of the edge is pointing away from the coordinate or towards the coordinate behind it
        '''
        l1 = Edge(self.start, coordinate, None).absolute_length
        l2 = Edge(self.end, coordinate, None).absolute_length

        if l1 < l2:
            return True

        elif l1 > l2:
            return False

        else:
            raise ValueError("coordinate exactly on top in between, couldn't determine whether it's pointing away or to")

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
    TINY_EDGE_OFFSET = 0.2
    CURVE_THRESHOLD_LENGTH = 0.8

    # Debuggin switches
    DEBUG_APPLY_OFFSET = False
    DEBUG_FILTER_TINY_EDGES = False
    DEBUG_ORDERED_EDGES = False
    DEBUG_TO_SINGLY_LINKEDLIST = False

    def __init__(self, vertices: list[Coordinate] = []):

        # Dictionary to relate each vertices to its edges
        self.vertex_edges: dict[Coordinate: list[Edge]] = {vertex: [] for vertex in vertices}

        # Dictionary to relate each vertices to the vertices it is attached to in the other end
        self.vertex_vertices: dict[Coordinate: list[Coordinate]] = {vertex: [] for vertex in vertices}

        # Dictionary to relate each vertices to the ComponentPad it's on (ONLY if there is one)
        self.vertex_componentpad: dict[Coordinate: Optional[ComponentPad]] = {vertex: None for vertex in vertices}

    @property
    def vertex_count(self) -> int:
        '''
        return number of vertices in this graph
        '''
        return len(self.vertex_edges)

    @property
    def edge_count(self) -> int:
        '''
        return number of edges in this graph
        '''
        return sum(len(edges) for edges in self.vertex_edges.values())

    def add_vertex(self, vertex: Coordinate) -> None:
        '''
        adds the new vertex to the underlying data structures of the graph

        :param vertex: the new vertex to be added to our graph
        '''
        if vertex not in self.vertex_edges:
            self.vertex_edges[vertex] = []
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
        if edge not in self.vertex_edges[edge.start]:
            self.vertex_edges[edge.start].append(edge)
        if edge.reversed() not in self.vertex_edges[edge.end]:
            self.vertex_edges[edge.end].append(edge.reversed())

        if edge.end not in self.vertex_vertices[edge.start]:
            self.vertex_vertices[edge.start].append(edge.end)
        if edge.start not in self.vertex_vertices[edge.end]:
            self.vertex_vertices[edge.end].append(edge.start)

    def ordered_edges(self, ignore_non_tree=False) -> list[Ezdge]:
        '''
        DP algorithm to order edges,
        #NOTE: HIGHLY DEPENDENT ON 'Edge.anticlockwise_successors()'

        :return: an ordered list of how to traverse the trace in a continual manner
        '''
        ordered_edges = []

        visited = set()
        next_edge = list(self.vertex_edges.values())[0][0]
        while len(visited) < self.edge_count:

            # print()
            # print(next_edge, 'start')
            ordered_edges.append(next_edge)
            
            next_v = next_edge.end

            if len(self.vertex_edges[next_v]) == 1:
                # dead end must return
                next_edge = self.vertex_edges[next_v][0]
                visited.add(next_edge)
                # print(next_edge, 'DEADEND')

            else:
                successors = next_edge.anticlockwise_successors(self.vertex_edges[next_v])
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

                    # Edge.visualize_edges(ordered_edges, speed=1, terminate=True)
                    if ignore_non_tree:
                        # print(len(visited), self.edge_count, 'lskjdflksdjflksjdf')
                        return ordered_edges
                    else:
                        raise ValueError("Use Graph.ordered_edges_non_tree() for non-tree graphs")
                
        # Edge.visualize_edges(ordered_edges, speed=1)
        return ordered_edges

    @property
    def ordered_edges_non_tree(self) -> list[Edge]:
        '''
        DP algorithm to order edges,
        #NOTE: HIGHLY DEPENDENT ON 'Edge.anticlockwise_successors()'

        :return: an ordered list of how to traverse the trace in a continual manner
        '''
        ordered_edges = []

        visited = set()
        next_edge = list(self.vertex_edges.values())[0][0]
        first_edge = deepcopy(next_edge)
        backtracking_frontier = Queue()
        while len(visited) < self.edge_count:

            # print()
            # print(next_edge, 'start')
            ordered_edges.append(next_edge)
            if next_edge not in visited:
                backtracking_frontier.push(next_edge)
            
            next_v = next_edge.end

            if len(self.vertex_edges[next_v]) == 1:
                # dead end must return
                next_edge = self.vertex_edges[next_v][0]
                visited.add(next_edge)
                # print(next_edge, 'DEADEND')

            else:
                successors = next_edge.anticlockwise_successors(self.vertex_edges[next_v])
                # print(successors, 'successors')
                for edge in successors:
                    # print('potential edge', edge, edge not in visited, edge.reversed() != next_edge)
                    if edge not in visited and edge.reversed() != next_edge:
                        # print('yes')
                        next_edge = edge
                        visited.add(next_edge)
                        break

                    # else:
                        # pass
                        # print('no')
                else:
                    ### This is now an non-tree graph.
                    ### Backtracking !!!
                    if backtracking_frontier.empty:
                        # print(next_edge, 'Frontier Emptied!!!!')
                        if next_edge == first_edge:
                            next_edge = next_edge.reversed()
                            # print(f'Going the other side :) {next_edge}')
                        else:
                            raise ValueError("No Solution")

                    else:
                        next_edge = backtracking_frontier.pop()
                        # print(f'Backtracking to {next_edge}')

        if Graph.DEBUG_ORDERED_EDGES:
            Edge.visualize_edges(ordered_edges, speed=1, hide_turtle=False, line_width=2, terminate=True)

        return ordered_edges

    @property
    def ordered_edges_non_tree_diff_lists(self) -> list[list[Edge]]:
        '''
        exactly like ordered_edges_non_tree but return list of list of different continious edge orders
        '''
        #TODO:
        pass

    def __contains__(self, vertex: Coordinate) -> bool:
        '''
        checks if given vertex is already added to the graph or not

        :param vertex: vertex to check if it's in the graph or not
        :return: whether given vertex is in the graph or not
        '''
        if type(vertex) != Coordinate:
            raise ValueError("can only use 'in' operator '__contains__' for vertex objects (Coordinate objects)")

        return vertex in list(self.vertex_vertices.keys())

    def visualize(self, hide_turtle=True, x_offset=20, y_offset=20, speed = 0, line_width=3, multiplier=8, terminate=False) -> None:
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

        for edges in self.vertex_edges.values():
            if edges != []:
                turtle.setpos((edges[0].start.x - x_offset) * multiplier, (edges[0].start.y - y_offset) * multiplier)
                for edge in edges:
                    turtle.down()
                    turtle.setpos((edge.start.x - x_offset) * multiplier, (edge.start.y - y_offset) * multiplier)
                    turtle.setpos((edge.end.x - x_offset) * multiplier, (edge.end.y - y_offset) * multiplier)
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
        
        for vertex in list(self.vertex_edges.keys()):

            if vertex not in visited:
                # print(vertex, 'added new')
                new_graph = Graph([vertex])
                visited.add(vertex)

                for other_vertex in self.vertex_vertices[vertex]:
                    # print(other_vertex, 'added form vertex_vertices')
                    new_graph.add_vertex(other_vertex)
                    visited.add(other_vertex)

                for edge in self.vertex_edges[vertex]:
                    # print(edge, 'added from.vertex_edges')
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

                for edge in self.vertex_edges[vertex]:
                    # print(edge, 'added from.vertex_edges')
                    seperated_graphs[wanted_ind].add_edge(edge)
                # print()
        
        # Removing duplicate edges
        #TODO
        # for graph_ind, graph in enumerate(seperated_graphs):
        #     for vertex in graph.vertex_edges:
        #         seperated_graphs[graph_ind].vertex_edges[vertex] = list(set(graph.vertex_edges[vertex]))


        return seperated_graphs

    def apply_offsets(self, extra_offset=0, terminate_after=False) -> Graph:
        '''
        for debugging
        # trace_graphs_seperated_unoffseted[0].apply_offsets(terminate_after=True)

        The graph to execute .apply_offsets() to is a graph of continious lines of ZERO thickness,
        This function will create a new graph from the old one with the thickness applied :)

        :return: Graph with thickness applied. The edges are of thickness 0
        '''
        if Graph.DEBUG_APPLY_OFFSET:
            print('\nNEW CALL!!!!!!!!!!!!!!!')

        new_graph = Graph()

        ordered_edges = self.ordered_edges()

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
                    print('\nNew Iteration:')
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

                semicircle_vertices = Coordinate.generate_semicircle_coordinates(vertex1, vertex2, edge.delta_x, edge.delta_y)

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

                prev_semicircle_vertex = vertex1
                for ind, semicircle_vertex in enumerate(semicircle_vertices):
                    try:
                        new_graph.add_edge(Edge(prev_semicircle_vertex, semicircle_vertex, LASER_BEAM_THICKNESS))
                    except ValueError:
                        raise ValueError("BIG PROBLEMMMMMM, two identical coordinates generated, maybe the max point may be not")
                    prev_semicircle_vertex = semicircle_vertex

                # edge2 = Edge(vertex1, vertex2, LASER_BEAM_THICKNESS)  # Straight line connection
                edge2 = Edge(prev_semicircle_vertex, vertex2, LASER_BEAM_THICKNESS)
                new_graph.add_edge(edge2)

                if Graph.DEBUG_APPLY_OFFSET:
                    print('\nNew Iteration:')
                    print('PARALLEL EDGE DETECTED!!!')
                    print(f'm=infinity -> {gradient==Infinity()}, m=0 -> {gradient == 0}')
                    print()

                    print(f'Current edge index: {ind}')
                    print(f'Current edge : {edge}')
                    print()

                    # if ind != 0:
                    # in case of first edge is a parallel line, all the circle edges will be added and it will have a high index
                    try:
                        print(f'Previous offseted Vertex: {prev_vertex}')
                    except Exception:
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
                    # if ind != 0:
                    # in case of first edge is a parallel line, all the circle edges will be added and it will have a high index
                    try:
                        print(f'edge1 (prev to inverse): {edge1}')
                    except Exception:
                        print('No edge1 for first iteration')
                    # print(f'edge2 (inverse to current): {edge2}')  # it's replaced with a semicircle now
                    print()

                    print()
               
                ### 5- Setting previous variable for next iteration
                prev_vertex = vertex2
                prev_gradient = gradient
                if gradient != Infinity():
                    prev_y_intercept = y_intercept

        if Graph.DEBUG_APPLY_OFFSET:
            Edge.visualize_edges(self.ordered_edges(), hide_turtle=False, x_offset=25, y_offset=25, multiplier=10, speed=0)
            new_graph.visualize(speed=0, line_width=1, x_offset=25, y_offset=25, multiplier = 10, terminate=terminate_after)

        return new_graph

    def to_coordinate(self) -> list[Coordinate]:
        '''

        '''
        return []

    def remove_vertex(self, vertex: Coordinate) -> None:
        '''
        Specific sequence to undo add_vertex and resolve all the edges connected to it

        :param vertex: vertex to be removed from the graph
        '''
        if vertex not in self.vertex_vertices:
            raise ValueError("vertex is already not there!")

        # Case 1: vertex is a deadline
        if (len(self.vertex_vertices[vertex]) == 1):
            # Step 1: Remove the key entirely
            previous_vertex = self.vertex_vertices.pop(vertex)[0]
            self.vertex_edges.pop(vertex)

            # Step 2: Remove the vertex and edge values from other key vertices
            self.vertex_vertices[previous_vertex].remove(vertex)

            # Step 3: Remove the edges in the previous vertex that has anything to do with the to be deleted vertex
            edges_to_be_removed = []
            for edge in self.vertex_edges[previous_vertex]:
                if edge.start == vertex or edge.end == vertex:
                    edges_to_be_removed.append(edge)

            for edge in edges_to_be_removed:
                self.vertex_edges[previous_vertex].remove(edge)

        # Case 2: vertex is a link
        else:
            raise ValueError('not implemented yet')

    def remove_edge(self, edge: Edge) -> None:
        '''
        #TODO: THIS FUNCTION CAN ONLY BE APPLIED BEFORE EXECUTING .seperate()
        :param edge: edge to be removed from graph
        '''
        if edge.start not in self.vertex_vertices or edge.end not in self.vertex_vertices:
            # raise ValueError(f"{edge} is not in graph")
            return None

        if edge.start not in self.vertex_vertices[edge.end] or edge.end not in self.vertex_vertices[edge.start]:
            raise ValueError("Edge not properly implemented in graph")

        if len(self.vertex_vertices[edge.start]) == 1:
            # deadend at starting point of edge
            self.remove_vertex(edge.start)
            return None

        elif len(self.vertex_vertices[edge.end]) == 1:
            # deadend at ending point of edge
            self.remove_vertex(edge.end)
            return None

        # Step 1: identify previous verticies
        prev_vertex_list = deepcopy(self.vertex_vertices[edge.start])
        prev_vertex_list.remove(edge.end)

        # Step 2: identify after vertex
        after_vertex = edge.end

        # Step 3: Delete before vertex if there is only one of them, no other edge is attached to it, it's floating point now
        if len(prev_vertex_list) == 1:
            # prev_vertex = prev_vertex_list[0]  # not needed anywhere
            self.vertex_vertices.pop(edge.start)
            self.vertex_edges.pop(edge.start)

        # Step 4: Replace every existence of edge.start in each prev_vertex with after_vertex
        for prev_vertex in prev_vertex_list:
            # Replacing Vertices
            for ind1, prev_prev_vertex in enumerate(self.vertex_vertices[prev_vertex]):
                if prev_prev_vertex == edge.start:
                    self.vertex_vertices[prev_vertex][ind1] = after_vertex

            # Replacing Edges
            for ind2, prev_prev_edge in enumerate(self.vertex_edges[prev_vertex]):
                if prev_prev_edge.start == edge.start:
                    self.vertex_edges[prev_vertex][ind2].start = after_vertex

                if prev_prev_edge.end == edge.start:
                    self.vertex_edges[prev_vertex][ind2].end = after_vertex

        # Step 5: Replace every existence of edge.start in after_vertex with all the vertices/edges of prev_vertex
        # Deleting Vertices
        if self.vertex_vertices[after_vertex].count(edge.start) <= 1:  # only 0 or 1 count is allowed
            if edge.start in self.vertex_vertices[after_vertex]:  # checking if it's there or not
                self.vertex_vertices[after_vertex].remove(edge.start)
        else:
            raise ValueError('Multiple occurance of a vertex found!')

        # Deleting Edges
        edges_to_be_removed = []
        for prev_edge in self.vertex_edges[after_vertex]:
            if prev_edge.start == edge.start or prev_edge.end == edge.start:
                edges_to_be_removed.append(prev_edge)

        for edge_tobe_del in edges_to_be_removed:
            self.vertex_edges[after_vertex].remove(edge_tobe_del)

        for prev_vertex in prev_vertex_list:
            # Adding Vertices
            if prev_vertex not in self.vertex_vertices[after_vertex]:
                self.vertex_vertices[after_vertex].append(prev_vertex)

            # Adding Edges
            edge1 = Edge(prev_vertex, after_vertex, edge.thickness)
            if edge1 not in self.vertex_edges[after_vertex]:
                self.vertex_edges[after_vertex].append(edge1)

            edge2 = edge1.reversed()
            if edge2 not in self.vertex_edges[after_vertex]:
                self.vertex_edges[after_vertex].append(edge2)

    def filter_tiny_edges(self) -> None:
        '''
        Removes the stupid small infuriating edges that mess up with everything
        Affects self Graph
        '''
        edges_to_be_removed = []
        for vertex in self.vertex_vertices.keys():
            for edge in self.vertex_edges[vertex]:
                if abs(edge.delta_x) <= Graph.TINY_EDGE_OFFSET and abs(edge.delta_y) <= Graph.TINY_EDGE_OFFSET:
                    edges_to_be_removed.append(edge)
        
        for edge in edges_to_be_removed:
            self.remove_edge(edge)

        if Graph.DEBUG_FILTER_TINY_EDGES:
            print("Removed Edges:")
            for edge in edges_to_be_removed:
                print(edge)
            print()

    @classmethod
    def join(cls, *graphs: Graph) -> Graph:
        '''
        joins the input graphs

        :graphs: undefined number of graphs
        :return: one graph joined from the all the graphs given from *graphs attribute
        '''
        # Mode checking
        list_mode = False
        if len(graphs) == 1 and type(graphs[0]) == list:
            list_mode = True

        elif len(set([type(graph) for graph in graphs])) != 1:
            raise ValueError("All Arguments MUST be of type Graph OR a one list argument of all graphs")

        joined_graph = Graph()

        if list_mode:
            graphs = graphs[0]

        for graph in graphs:
            joined_graph.vertex_vertices.update(graph.vertex_vertices)
            joined_graph.vertex_edges.update(graph.vertex_edges)

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

    def to_singly_linkedlist(self, terminate_after=False) -> Node:
        '''
        Converts Graph to singly linked list

        #IMP: ONLY WORKS FOR GRAPHS THAT DOESN'T HAVE BRANCHS
            every vertices point to the next and previous vertex ONLY, creating a loop (or not)

        :return: Head Node of the linked list that has all the values of the graph
        '''
        # Checking if graph can be converted
        for vertex in self.vertex_vertices.keys():
            if len(self.vertex_vertices[vertex]) != 2:
                raise ValueError("every vertices must point to two other vertices only")

            if len(self.vertex_edges[vertex]) != 2:
                raise ValueError("every vertices must point to two other edges only")

        #TODO: didn't test if the vertices list values of the current vertex has in their vertices list the current vertex value

        # Converting!
        visited = set()

        first_vertex = list(self.vertex_vertices.keys())[0]
        visited.add(first_vertex)
        next_node = Node(first_vertex, None)  # the last node, doesn't have any heads

        while True:
            for vertex in self.vertex_vertices[next_node.vertex]:
                if vertex not in visited:
                    next_node = Node(vertex, next_node)
                    visited.add(vertex)
                    break
            else:
                if first_vertex in self.vertex_vertices[next_node.vertex]:
                    # it's a loop
                    # adding the last link which couldn't be added normally as it's in visited
                    next_node = Node(first_vertex, next_node)

                break

        if next_node.last_node.vertex == first_vertex:
            next_node.pre_last_node.parent = next_node  # joining the node to end as it's a loop

        # testing everything is ok, all vertices available in the linkedlist as the graph
        node_vertex_set = set(next_node.to_list())
        graph_vertex_set = set(self.vertex_vertices.keys())
        if node_vertex_set != graph_vertex_set:
            # print(next_node.to_list(), len(next_node.to_list()), len(node_vertex_set))
            # print()
            # print(self.vertex_vertices.keys(), len(self.vertex_vertices), len(graph_vertex_set))
            print(node_vertex_set.difference(graph_vertex_set), 'node - graph')
            print()
            print(graph_vertex_set.difference(node_vertex_set), 'graph - node')

            raise ValueError("HOW THE FUCK DID IT PASS THE FIRST TEST AND NOT PASS THIS ONE?!?!?!")

        if Graph.DEBUG_TO_SINGLY_LINKEDLIST:
            next_node.visualize(terminate=terminate_after)

        return next_node

