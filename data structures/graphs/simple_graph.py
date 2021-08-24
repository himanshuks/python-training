# Graph has mainly Edges
# Edges are like nodes connected to each other
# Use Dictionary to define each pair combination like Delhi - Goa
# Use input as array of tuples


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        # For each EDGE create a Dictionary
        # Taking 2 variables unpack the tuples
        # So X take first value, Y take second value
        # If present, append else create new record

        for x, y in self.edges:
            if x in self.graph_dict:
                self.graph_dict[x].append(y)
            else:
                self.graph_dict[x] = [y]

        print("Ready graph :", self.graph_dict)

    # Show all possible paths
    # Takes 3 parameters, start and end point
    # Path - by default blank else will be used in recursion

    def get_path(self, start, end, path=[]):

        # At least Start should get added in path
        path = path + [start]

        # When Start and End is same Edge
        if start == end:
            return [path]

        # When edge is last node with no forward paths
        if start not in self.graph_dict:
            return []

        all_paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)

                for p in new_paths:
                    all_paths.append(p)

        return all_paths

    # Shortest path between 2 edges
    # Similar to all possible paths
    def get_shortest_path(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)

                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
    ("New York", "Mexico"),
    ("New York", "Bengaluru"),
    ("New York", "Dubai"),
]

routed_graph = Graph(routes)

startPoint = "Mumbai"
endPoint = "New York"

z = routed_graph.get_path(startPoint, endPoint)
print(f"Path between {startPoint} and {endPoint} : {z}")

z = routed_graph.get_shortest_path(startPoint, endPoint)
print(f"Path between {startPoint} and {endPoint} : {z}")
