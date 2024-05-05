# optimal_way
Программа для поиска оптимального пути во взвешенном неориентированном графе, то есть в графе, где каждое ребро имеет вес. Задача из яндекс лицея.
Используется алгоритм Дейкстры.
Для решения большого класса задач про поиск оптимального маршрута, анализа дорожного траффика и т.д. используется математический аппарат, именуемый графом.
В моей программе присутствувет рекурсивная функция way(), которая и выполняет рассчет.
Формат ввода
В графе вершины пронумерованы. Граф является связанным, веса задаются методом, который называется «список ребер».

Входные данные имеют вид:

1 2 10  
2 5 6  
2 3 1  
3 4 1  
4 5 2  
1 5


Расшифруем, что означает эта запись:
1. Вершины 1 и 2 связаны ребром с весом 10,
2. Вершины 2 и 5 – ребром с весом 6,
3. Вершины 2 и 3 – ребром с весом 1
и т.д.
Последняя строка говорит о том, из какой вершины в какую надо найти оптимальный путь. В нашем случае, из первой вершины в пятую.

Формат вывода
Длина кратчайшего пути + кратчайший путь для указанных вершин
