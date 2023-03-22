from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

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
    u: int # the "from" vertex
    v: int # the "to" vertex
    thickness: float

    def reversed(self) -> Edge:
        return Edge(self.v, self.u, self.thickness)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}, with thickness {self.thickness}"


class Graph:
    def __init__(self, vertices: list[Coordinate] = []) -> None:
        self._vertices: list[Coordinate] = vertices
        self._edges: list[list[Edge]] = [[] for _ in vertices]
        self._single_direction_edge: list[list[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices) # Number of vertices

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges)) # Number of edges

    # Add a vertex to the graph and return its index
    def add_vertex(self, vertex: Coordinate) -> int:
        self._vertices.append(vertex)
        self._edges.append([]) # add empty list for containing edges
        
        self._single_direction_edge.append([])

        return self.vertex_count - 1 # return index of added vertex

    # This is an undirected graph,
    # so we always add edges in both directions
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

        self._single_direction_edge[edge.u].append(edge)

    # Add an edge using vertex indices (convenience method)
    def add_edge_by_indices(self, u: int, v: int, thickness: float) -> None:
        edge: Edge = Edge(u, v, thickness)
        self.add_edge(edge)
        

    # Add an edge by looking up vertex indices (convenience method)
    def add_edge_by_vertices(self, first: Coordinate, second: Coordinate, thickness: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)

        self.add_edge_by_indices(u, v, thickness)

    # Find the vertex at a specific index
    def vertex_at(self, index: int) -> Coordinate:
        return self._vertices[index]

    # Find the index of a vertex in the graph
    def index_of(self, vertex: Coordinate) -> int:
        return self._vertices.index(vertex)

    # Find the vertices that a vertex at some index is connected to
    def neighbors_for_index(self, index: int) -> list[Coordinate]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def single_dir_neighbors_for_index(self, index: int) -> list[Coordinate]:
        return list(map(self.vertex_at, [e.v for e in self._single_direction_edge[index]]))

    # Lookup a vertice's index and find its neighbors (convenience method)
    def neighbors_for_vertex(self, vertex: Coordinate) -> list[Coordinate]:
        return self.neighbors_for_index(self.index_of(vertex))

    def single_dir_neighbors_for_vertex(self, vertex: Coordinate) -> list[Coordinate]:
        return self.single_dir_neighbors_for_index(self.index_of(vertex))


    # Return all of the edges associated with a vertex at some index
    def edges_for_index(self, index: int) -> list[Edge]:
        return self._edges[index]

    def single_dir_edges_for_index(self, index: int) -> list[Edge]:
        return self._single_direction_edge[index]


    # Lookup the index of a vertex and return its edges (convenience method)
    def edges_for_vertex(self, vertex: Coordinate) -> list[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    def single_dir_edges_for_vertex(self, vertex: Coordinate) -> list[Edge]:
        return self.single_dir_edges_for_index(self.index_of(vertex))


    # Make it easy to pretty-print a Graph
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            # desc += f"{self.vertex_at(i)} -> {self.single_dir_neighbors_for_index(i)} with thickness {self.edges_for_vertex(self.vertex_at(i))[0].thickness}\n"
            # desc += f"{self.vertex_at(i)} -> {[n for n in self.single_dir_neighbors_for_index(i)]}\n"
            desc += f"{self.vertex_at(i)} -> {[n for n in self.single_dir_edges_for_index(i)]}\n"
        return desc


