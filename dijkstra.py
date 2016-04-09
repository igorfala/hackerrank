# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
t = int(input())
def dijkstra(graph, s, edges):
    distance_so_far = {s:0}
    final_distance = {}
    while len(final_distance) < edges:
        #print distance_so_far, final_distance, edges, len(final_distance)
        temp = [g for g in distance_so_far if distance_so_far[g] == min(distance_so_far.values())][0]
        final_distance[temp] = distance_so_far[temp]
        del distance_so_far[temp]
        for neighbor in graph[temp]:
            if neighbor not in final_distance:
                if not neighbor in distance_so_far:
                    distance_so_far[neighbor] = final_distance[temp] + graph[temp][neighbor]
                elif distance_so_far[neighbor] > final_distance[temp] + graph[temp][neighbor]:
                    distance_so_far[neighbor] = final_distance[temp] + graph[temp][neighbor]
        if not distance_so_far: break 
    return final_distance
        
for _ in xrange(t):
    vertices, edges = map(int, raw_input().strip().split())
    graph = {}
    for vertice in xrange(1, vertices+1):
        graph[vertice] = {}
    for _ in xrange(edges):
        vertice, neighbor, cost = map(int, raw_input().strip().split())
        if neighbor in graph[vertice]:
            if graph[vertice][neighbor] > cost:
                graph[vertice][neighbor] = cost
        else:
            graph[vertice][neighbor] = cost
        if vertice in graph[neighbor]:
            if graph[neighbor][vertice] > cost:
                graph[neighbor][vertice] = cost
        else:
            graph[neighbor][vertice] = cost
    s = int(input())
    #print graph
    distances = dijkstra(graph,s, edges)
    verts = sorted([i for i in graph.keys() if i != s ])
    distances = [distances[i] if i in distances else -1 for i in verts]
    print " ".join([str(i) for i in distances])