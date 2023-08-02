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

def bfs(graph, start, end):
    queue = [start]
    
    visited =[start]

    parents = {}
    
    found=False

    while queue:
        node = queue.pop(0)

        if node == end:
            path = [end]

            while end != start:
                path.insert(0, parents[end])
                end = parents[end]
            
            found=True
            print("Caminho: ", path)
    
        for iterator in graph[node]:
            if iterator not in visited:

                visited.append(iterator)

                queue.append(iterator)

                parents[iterator] = node

    if(not found):
        print("Caminho não encontrado")


start = sys.argv[1]
end = sys.argv[2]
count=0
for node in graph:
    if(node == start or node == end):
        count+=1
if count == 2:
    bfs(graph, start, end)
else:
    print("Cidade não encontrada")


