import sys

# Алгоритм Дейкстры:
# 1) Кратчайшее расстояние от старта до каждой точки
# 2) Вычисление кратчайшего маршрута
graph = [[int(j) for j in i.strip('\n ').split()] for i in sys.stdin.readlines()]
start_, finish_ = [int(i) for i in graph[-1]]
del graph[-1]
for i in graph[:len(graph)]:
    graph.append([i[1], i[0], i[2]])

communications = {}
for start, finish, len_ in graph:
    communications[start] = communications.get(start, []) + [[finish, len_]]

# shortest_distance(кратчайший путь до старта) -> [[значение, путь]...]
shortest_distance = {key: [value, [start_, key]] for key, value in communications[start_]}
shortest_distance[start_] = [0, [start_]]
already_used = []


# Использую кеширование: при вызове функции в shortest_distance будут записываться кратчайшие пути от старта
# до всех вершин графа
# points(все возможные пути) -> [[значение, путь]...]
def way(place):
    already_used.append(place)
    points = []
    for i in [j for j in communications[place] if j[0] not in already_used]:
        if i[0] in shortest_distance:
            points.append(shortest_distance[i[0]])
        else:
            way(i[0])
            points.append(shortest_distance[i[0]])
    for i in range(len(points)):
        for j in communications[points[i][-1][-1]]:
            if j[0] == place:
                points[i][0] += j[1]
                points[i][1].append(place)
                break
    shortest_distance[place] = min(points, key=lambda x: x[0])


way(finish_)
print(shortest_distance[finish_][1])


