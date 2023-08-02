import networkx as nx
import itertools



def hanoi_graph(discs):

    graph = nx.Graph()    
    permutations = list(itertools.product(list(range(1, 4)), repeat=discs))

    for permutation in permutations:
        a, b, c, d, e = permutation
        
        aux = 1
        while aux < discs-1:

            if aux != a:
                graph.add_edge((a, b, c, d, e), (aux, b, c, d, e))

            if aux != b and b != a and aux != a:
                graph.add_edge((a, b, c, d, e), (a, aux, c, d, e))

            if aux != c and  c != a and c != b and aux != a and aux != b:
                graph.add_edge((a, b, c, d, e), (a, b, aux, d, e))

            if aux != d and d != a and d != b and d != c and aux != a and aux != b and aux != c:
                graph.add_edge((a, b, c, d, e), (a, b, c, aux, e))

            if aux != e and e != a and e != b and e != c and e != d and aux != a and aux != b and aux != c and aux != d:
                graph.add_edge((a, b, c, d, e), (a, b, c, d, aux))
            
            aux+=1
            
    return graph



def bfs(graph, start, end, counter=0):
    queue = [start]
    
    visited =[start]

    parents = {}
    
    found=False

    while queue:
        node = queue.pop(0)

        if node == end:
            path = [end]
            

            while end != start:
                counter+=1
                path.insert(0, parents[end])
                end = parents[end]
            
            found=True
            print("Caminho por extensão: ", path, "\nTotal de buscas: ",counter, "\n\n")
    
        for iterator in graph[node]:
            if iterator not in visited:

                visited.append(iterator)

                queue.append(iterator)

                parents[iterator] = node

    if(not found):
        print("Caminho por extensão não encontrado  \n")


def dfs(graph, start, end, visited, parents={}):

    for iterator in graph[start]:
        if iterator not in visited:
            visited.append(iterator)
            parents[iterator] = start
            if iterator == end:
                return parents
            res = dfs(graph, iterator, end, visited, parents)
            if res:
                global count
                count+=1
                return res
    return False



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
                global count
                count+=1
                return res
            visited.remove(iterator)
    return False

def ids(graph, start, end, limit):
    for i in range(limit):
        res = ldfs(graph, start, end, [start], i)
        if res:
            return res
    return False


def main():

    graph = nx.to_dict_of_lists(hanoi_graph(5))
    start = (1, 1, 1, 1, 1)
    end = (3, 3, 3, 3, 3)
    

    bfs(graph, start, end)


    global count
    count = 0
    res = dfs(graph, start, end, [start])
    if(not res):
        print("Caminho por profundidade não encontrado  \n")
    path = [end]
    while start != end:
        path.insert(0, res[end])
        end = res[end]

    print("Caminho por profundidade: ", path, "Total de buscas: ", count, "\n\n")

    count=0
    res = ids(graph, start, end, 50)
    if not res:
        print("Cidade não encontrada, pois o limite foi excedido")
        exit()
    path = [end]
    parent = res[end]
    while start != end:
        path.insert(0, res[end])
        end = res[end]

    print("Caminho por iteração: ", path, "Total de buscas: ", count, "\n\n")

    # res = ldfs(graph, start, end, [start], 10)
    # if(not res):
    #     print("Limite excedido, cidade não encontrada")
    #     exit()
    # path = [end]
    # while start != end:
    #     path.insert(0, res[end])
    #     end = res[end]

    # print("Caminho por profundidade limitada: ", path)
    


main()
