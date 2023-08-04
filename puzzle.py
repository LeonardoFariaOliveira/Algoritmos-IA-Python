import datetime
import itertools
import networkx as nx

graph = nx.Graph()


def puzzle_graph():
    
    permutations = list(itertools.permutations(list(range(9)), 9))
    
    for permutation in permutations:

        a, b, c, d, e, f, g, h, i = permutation
    
        if len(set((a, b, c, d, e, f, g, h, i))) == 9:
          
            #A
            if b == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (b, a, c, d, e, f, g, h, i))
            if d == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (d, b, c, a, e, f, g, h, i))
            
            #B
            if a == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (b, a, c, d, e, f, g, h, i))
            if c == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, c, b, d, e, f, g, h, i))
            if e == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, e, c, d, b, f, g, h, i))
            
            #C
            if b == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, c, b, d, e, f, g, h, i))
            if f == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,f,d,e,c,g,h,i))
            
            #D
            if a == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (d, b, c, a, e, f, g, h, i))
            if e == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, e, d, f, g, h, i))
            if g == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, g, e, f, d, h, i))
            
            #E
            if b == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, e, c, d, b, f, g, h, i))
            if d == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,e,d,f,g,h,i))
            if f == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,f,e,g,h,i))
            if h == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,h,f,g,e,i))
            
            #F
            if c == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,f,d,e,c,g,h,i))
            if e == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,f,e,g,h,i))
            if i == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,e,i,g,h,f))
            
            #G
            if d == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, g, e, f, d, h, i))
            if h == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, d, e, f, h, g, i))
            
            #H
            if e == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, d, h, f, g, e, i))
            if g == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, d, e, f, h, g, i))
            if i == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, d, e, f, g, i, h))
            
            #I
            if f == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,e,i,g,h,f))
            if h == 0:
                graph.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,e,f,g,i,h))

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




def main():

    #Início
    print("Início do grafo: ", datetime.datetime.now())
    puzzle_graph()
    #Fim
    print("Término do grafo: ", datetime.datetime.now())

    graph = nx.to_dict_of_lists(graph)

    #Busca em extensão
    #(4, 5, 3, 2, 6, 0, 8, 1, 7)
    start = (8, 5, 4, 2, 7, 1, 3, 6, 0)
    end = (1,2,3,4,5,6,7,8,0)

    #Printa data e hora de início
    print("Início da busca: ", datetime.datetime.now())

    bfs(graph, start, end)

    #Printa data e hora de término
    print("Término da busca: ", datetime.datetime.now())