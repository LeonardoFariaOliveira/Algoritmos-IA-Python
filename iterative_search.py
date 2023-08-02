
import sys

graph = {
    'Oradea': ['Sibiu', 'Zerind'],
    'Zerind': ['Arad', 'Oradea'],
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Dobreta', 'Lugoj'],
    'Dobreta': ['Craiova', 'Mehadia'],
    'Craiova': ['Dobreta', 'Pitesti', 'Rimnicu Vilcea'],
    'Sibiu': ['Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Craiova', 'Pitesti', 'Sibiu'],
    'Fagaras': ['Bucharest', 'Sibiu'],
    'Pitesti': ['Bucharest', 'Craiova', 'Rimnicu Vilcea'],
    'Bucharest': ['Fagaras', 'Giurgiu', 'Pitesti', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Neamt': ['Iasi']
}

def ldfs(graph, start, end, visited, limit, parents={}, depth=0):

    if(depth == limit):
        return False

    for iterator in graph[start]:
        if iterator not in visited:
            visited.append(iterator)
            parents[iterator] = start
            if iterator == end:
                return parents
            res = ldfs(graph, iterator, end, visited, limit, parents, depth+1)
            if res:
                return res
            visited.remove(iterator)
    return False



def ids(graph, start, end, limit):
    for i in range(limit):
        res = ldfs(graph, start, end, [start], i)
        if res:
            return res
    return False



start = sys.argv[1]
end = sys.argv[2]
count=0
for node in graph:
    if(node == start or node == end):
        count+=1
if count == 2:
    res = ids(graph, start, end, 5)
    if not res:
        print("Cidade não encontrada, pois o limite foi excedido")
        exit()
    path = [end]
    parent = res[end]
    while start != end:
        path.insert(0, res[end])
        end = res[end]

    print("Caminho: ", path)
else:
    print("Cidade não encontrada")
