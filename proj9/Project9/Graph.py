import random
from queue import Queue


# Custom Graph error
class GraphError(Exception): pass


class Graph:
    """
    Graph Class ADT
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """
        __slots__ = ['source', 'destination']

        def __init__(self, source, destination):
            """
            DO NOT EDIT THIS METHOD!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: ID of Vertex where this edge ends
            """
            self.source = source
            self.destination = destination

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination}"

        __str__ = __repr__

    class Path:
        """
        Class representing a Path through the Graph
        """
        __slots__ = ['vertices']

        def __init__(self, vertices=[]):
            """
            DO NOT EDIT THIS METHOD!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            """
            self.vertices = vertices

        def __eq__(self, other):
            return self.vertices == other.vertices

        def __repr__(self):
            return f"Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add a Vertex id to the path
            :param vertex: the vertex ID, an integer
            :return: None
            """
            self.vertices.append(vertex)
            return None

        def remove_vertex(self):
            """
            Remove the most recently added vertex id from the path
            :return: None
            """
            if len(self.vertices):
                self.vertices.pop()
            return None

        def last_vertex(self):
            """
            Returns the last vertex id in the path
            :return: a vertex id if the path is not empty otherwise None
            """
            if len(self.vertices):
                return self.vertices[-1]
            return None

        def is_empty(self):
            """
            Return whether the path is empty
            :return: integer
            """
            return len(self.vertices) == 0

    class Vertex:
        """
        Class representing a Vertex in the Graph
        """
        __slots__ = ['ID', 'edges', 'visited', 'destination_set', 'fake']

        def __init__(self, ID):
            """
            Class representing a vertex in the graph
            :param ID : Unique ID of this vertex
            """
            self.edges = []
            self.destination_set = set()
            self.ID = ID
            self.visited = False
            self.fake = False

        def __repr__(self):
            return f"Vertex: {self.ID}"

        __str__ = __repr__

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: Vertex to compare
            :return: Bool, True if same, otherwise False
            """
            if self.ID == other.ID and self.visited == other.visited:
                if self.fake == other.fake and len(self.edges) == len(other.edges):
                    edges = set((edge.source.ID, edge.destination) for edge in self.edges)
                    difference = [e for e in other.edges if (e.source.ID, e.destination) not in edges]
                    if len(difference) > 0:
                        return False
                    return True

        def add_edge(self, destination):
            """
            Adds an outgoing edge from this vertex to the input vertex
            Does nothing if the edge is already in self.edges
            :param destination: vertex id of the vertex to form an edge with
            :return: None
            """
            if destination in self.destination_set:
                return None
            self.destination_set.add(destination)
            self.edges.append(Graph.Edge(self, destination))
            return None

        def degree(self):
            """
            Return the number of outgoing edges from self
            :return: the number of outgoing edges
            """
            return len(self.edges)

        def get_edge(self, destination):
            """
            Return the edge from self to destination if it exists
            :return: an Edge object or None if the edge is not found
            """
            for edge in self.edges:
                if edge.destination == destination:
                    return edge
            return None

        def get_edges(self):
            """
            Return a list of all outgoing edges from self
            :return: a list of Edge objects or [] if self has no outgoing edges
            """
            return self.edges

        def set_fake(self):
            """
            Sets the fake flag
            :return: None
            """
            self.fake = True
            return None

        def set_real(self):
            """
            Clears the fake flag
            :return: None
            """
            self.fake = False
            return None

        def visit(self):
            """
            Sets the visited flag
            :return: None
            """
            self.visited = True
            return None

    def __init__(self, size=0, connectedness=1, filename=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        :param: filename: The name of a file to use to construct the graph.
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.filename = filename
        self.construct_graph()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are IDentical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        if len(self.adj_list) == len(other.adj_list):
            for key, value in self.adj_list.items():
                if key in other.adj_list:
                    if not self.adj_list[key] == other.adj_list[key]:
                        return False
                else:
                    return False
            return True
        return False

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: A generator object that returns a tuple of the form (source ID, destination ID)
        used to construct an edge
        """
        random.seed(10)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    yield [i, j]

    def get_vertex(self, ID):
        """
        Returns the vertex object with specified ID or returns None if a vertex
        with ID is not in the graph
        :param ID: the id of the vertex to return
        :return: the desired vertex or None if the vertex is not in the graph
        """
        return self.adj_list.get(ID, None)

    def construct_graph(self):
        """
        Add edges to the graph either randomly or from a file
        If adding edges randomly then add self.size number of edges
        If adding edges from file then add all edges contained in the file
        :return: None
        """
        def get_edges():
            """Yields edges from either file or Graph.generate_edges()"""
            if self.filename:
                try:
                    with open(self.filename, 'r') as file:
                        for line in file:
                            yield list(map(int, line.split()))
                except FileNotFoundError:
                    raise GraphError("incorrect filename")
                except ValueError:
                    raise GraphError("incorrect file contents")
            else:
                if self.size <= 0:
                    raise GraphError("self.size should be a positive integer")
                if not 0 < self.connectedness <= 1:
                    raise GraphError("self.connectedness should be in (0,1]")
                yield from self.generate_edges()

        for uv in get_edges():
            if len(uv) != 2:
                continue
            (source_ID, destination_ID) = uv

            # make sure that source and destination are both nodes in the graph
            source_vertex = self.get_vertex(source_ID)
            if source_vertex is None:
                source_vertex = Graph.Vertex(source_ID)
                self.adj_list[source_ID] = source_vertex

            destination_vertex = self.get_vertex(destination_ID)
            if destination_vertex is None:
                destination_vertex = Graph.Vertex(destination_ID)
                self.adj_list[destination_ID] = destination_vertex

            source_vertex.add_edge(destination_ID)

        return None

    def BFS(self, start, target):
        """
        Performs a breadth first search for target starting at start
        Returns the same information as Graph.DFS
        :param start: the id of the vertex to start the search at
        :param target: the id of the vertex to search for
        :return path: same as Graph.DFS
        """
        if self.get_vertex(start) is None:
            return Graph.Path()
        if self.get_vertex(target) is None:
            return Graph.Path()
        if start == target:
            return Graph.Path([start])

        # if u == discovery[v], then there is an edge from u to v in the graph
        discovery = {}
        queue = Queue()

        queue.put(start)
        self.get_vertex(start).visit()

        # allows us to stop as soon as we find target
        target_found = False

        while not queue.empty() and not target_found:
            current_ID = queue.get()
            if current_ID == target:
                break
            current = self.get_vertex(current_ID)
            for edge in current.get_edges():
                opposite_ID = edge.destination
                opposite = self.get_vertex(opposite_ID)
                if not opposite.visited:
                    opposite.visit()
                    discovery[opposite_ID] = current_ID
                    if opposite_ID == target:
                        target_found = True
                        break
                    queue.put(opposite_ID)

        if not target_found:
            return Graph.Path()

        # walk up the discovery tree from target to start
        path = []
        while start != target:
            path.append(target)
            target = discovery[target]
        path.append(start)

        return Graph.Path(path[::-1])

    def DFS(self, start, target, path=Path()):
        """
        Performs a depth first search for target starting at start
        Returns a path from start to target
        If any of the inputs are bad or if there is no path from start to target
        then returns an empty path
        :param start: the id of the vertex to start the search at
        :param target: the id of the vertex to search for
        :param path: the Path object to store the path from start to target
        :return path: returns the possibly modified path parameter or returns Path()
        """
        if self.get_vertex(start) is None:
            return Graph.Path()
        if self.get_vertex(target) is None:
            return Graph.Path()
        if start == target:
            path.add_vertex(target)
            return path

        start_vertex = self.get_vertex(start)
        start_vertex.visit()
        path.add_vertex(start)
        for edge in start_vertex.get_edges():
            opposite_ID = edge.destination
            opposite = self.get_vertex(opposite_ID)
            if not opposite.visited:
                self.DFS(opposite_ID, target, path)
                # found target, remove_vertex() is not called again
                if path.last_vertex() == target:
                    return path
        path.remove_vertex()

        return Graph.Path()


def fake_emails(graph, mark_fake=False):
    """
    Returns a list of all fake email addresses in the graph
    Removes from the graph all edges (emails) that point to a fake email address (vertex)
    :param graph: the graph that contains the email information
    :param mark_fake: whether to set the fake flag on fake email addresses (vertices)
    :return fake_ids: a list of fake email address ids
    """

    def check_fake_emails(start, emails=list()):
        """
        Finds fake email addresses that are reachable from start by DFS
        Removes from the graph the final edge in the path from u to v for all
        fake addresses v that are reachable from u=start
        :param start: the vertex to start a DFS at
        :param emails: the list of fake email addresses
        :return: None
        """
        start_vertex = graph.get_vertex(start)
        if start_vertex.visited and not start_vertex.fake:
            return False
        start_vertex.visit()

        if start_vertex.degree() == 0:
            start_vertex.set_fake()
            return True

        sv_edges = start_vertex.get_edges()
        edge_i = 0
        while edge_i < len(sv_edges):
            edge = sv_edges[edge_i]
            opposite_ID = edge.destination
            is_fake = check_fake_emails(opposite_ID, emails)

            if is_fake:
                sv_edges[edge_i], sv_edges[-1] = sv_edges[-1], sv_edges[edge_i]
                sv_edges.pop()
                start_vertex.destination_set.remove(opposite_ID)
            else:
                edge_i += 1

        return False

    fake_ids = []
    for vertex_id in graph.adj_list:
        if check_fake_emails(vertex_id, fake_ids):
            fake_ids.append(vertex_id)

    if not mark_fake:
        for vertex_id in fake_ids:
            graph.get_vertex(vertex_id).set_real()

    return fake_ids

