import sys

graph = {
    'Oradea': {'Sibiu': 151, 'Zerind': 71,},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Arad': {'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75 },
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Dobreta': 75, 'Lugoj': 70},
    'Dobreta': { 'Craiova': 120, 'Mehadia': 75},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Fagaras': {'Bucharest': 211, 'Sibiu': 99},
    'Pitesti': {'Bucharest': 101, 'Craiova': 138, 'Rimnicu Vilcea': 97, },
    'Bucharest': {'Fagaras': 211, 'Giurgiu': 90, 'Pitesti': 101,  'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Eforie': 86,   'Urziceni': 98,},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142,},
    'Iasi': {'Neamt': 87, 'Vaslui': 92,},
    'Neamt': {'Iasi': 87}
}

def dks(graph, start, end):
    queue = [start]

    visited = [start]

    cost = {start: 0}

    parents = {}

    found = False

    path = {start: [start]}

    while queue:
        node = queue.pop(0)

        if node == end:
            print("Caminho: ", path[node], "- Custo: ", cost[node])
            found=True
            break

        for iterator in graph[node]:

            if iterator not in visited:

                if iterator not in cost or cost[iterator] > cost[node] + graph[node][iterator]:

                    cost[iterator] = cost[node] + graph[node][iterator]

                    path[iterator] = path[node] + [iterator]

                    queue.append(iterator)
                queue = sorted(queue, key=lambda x: cost[x])

    if(not found):
        print("Caminho não encontrado")

start = sys.argv[1]
end = sys.argv[2]
count=0
for node in graph:
    if(node == start or node == end):
        count+=1
if count == 2:
    dks(graph, start, end)
else:
    print("Cidade não encontrada")



