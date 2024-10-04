import sys

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def print_solution(self, distances):
        """Prints the shortest distance from the source to each vertex."""
        print("Vertex \tDistance from Source")
        for vertex in range(self.num_vertices):
            print(f"{vertex}\t{distances[vertex]}")

    def find_min_distance_vertex(self, distances, shortest_path_set):
        """Finds the vertex with the minimum distance from the set of vertices not yet processed."""
        min_distance = sys.maxsize
        min_index = -1

        for vertex in range(self.num_vertices):
            if distances[vertex] < min_distance and not shortest_path_set[vertex]:
                min_distance = distances[vertex]
                min_index = vertex

        return min_index

    def dijkstra(self, source_vertex):
        """Implements Dijkstra's algorithm to find the shortest path from the source vertex to all other vertices."""
        distances = [sys.maxsize] * self.num_vertices
        distances[source_vertex] = 0
        shortest_path_set = [False] * self.num_vertices

        for _ in range(self.num_vertices):
            # Get the vertex with the minimum distance that hasn't been processed yet
            current_vertex = self.find_min_distance_vertex(distances, shortest_path_set)
            shortest_path_set[current_vertex] = True

            # Update the distances for adjacent vertices
            for adjacent_vertex in range(self.num_vertices):
                if (self.adjacency_matrix[current_vertex][adjacent_vertex] > 0 and
                        not shortest_path_set[adjacent_vertex] and
                        distances[adjacent_vertex] > distances[current_vertex] + self.adjacency_matrix[current_vertex][adjacent_vertex]):
                    distances[adjacent_vertex] = distances[current_vertex] + self.adjacency_matrix[current_vertex][adjacent_vertex]

        self.print_solution(distances)

def main():
    """Main function to drive the program."""
    num_vertices = int(input("Enter the number of vertices: "))
    graph = Graph(num_vertices)

    print("Enter the adjacency matrix row by row (0 for no edge):")
    for i in range(num_vertices):
        row = list(map(int, input(f"Row {i}: ").split()))
        graph.adjacency_matrix[i] = row

    source_vertex = int(input("Enter the source vertex (0 to {}): ".format(num_vertices - 1)))
    graph.dijkstra(source_vertex)

if __name__ == "__main__":
    main()
