from typing import List, Tuple, Dict
from collections import defaultdict
from queue import PriorityQueue

def max_cost_flow(n: int, m: int, p: int, orders: List[Tuple[int, int, List[int]]],
                  tool_prices: List[int], discounts: List[Tuple[List[int], int]]) -> int:
    # Создаем граф
    graph = defaultdict(dict)
    # Add edges from source to orders
    for i, (cost, num_tools, tool_ids) in enumerate(orders, 1):
        graph['source'][f'order_{i}'] = (cost, 0)
        for tool_id in tool_ids:
            graph[f'order_{i}'][f'tool_{tool_id}'] = (1, -tool_prices[tool_id-1])  # пропускн.способность=1, вес=-цена
    # Add edges from tools to sink
    for i, tool_price in enumerate(tool_prices, 1):
        graph[f'tool_{i}']['sink'] = (1, tool_price)  # пропускн.способность=1, вес=цена
    # Add edges for discounts
    for i, (tool_ids, discount_price) in enumerate(discounts, 1):
        graph['source'][f'discount_{i}'] = (float('inf'), 0)  # пропускн.способность=inf, вес=0
        for tool_id in tool_ids:
            graph[f'discount_{i}'][f'tool_{tool_id}'] = (1, -tool_prices[tool_id-1] + discount_price)  # скидка: пропускн.способность=1, вес=-цена + новая_цена

    # Find maximum cost flow
    MAX_FLOW = sum(cost for cost, _, _ in orders)  # максимум, который можем выполнить - это сумма стоимостей заказов
    max_cost = 0  # максимальная сумма прибыли, которую можно получить
    while MAX_FLOW > 0:
        # Step 1: Инициализация расстояний и родительских узлов
        dist = {v: float('inf') for v in graph}  # словарь расстояний
        parent = {v: None for v in graph}  # словарь родительских узлов
        dist['source'] = 0
        dist['sink'] = float('inf')
        parent['sink'] = None

        # Step 2: Алгоритм Беллмана-Форда для нахождения кратчайших путей от истока до стока
        pq = PriorityQueue()
        pq.put(('source', 0))
        while not pq.empty():
            u, u_cost = pq.get()
            if u_cost != dist[u]: continue  # Пропускаем вершины, которые мы уже обработали
            for v, (capacity, cost) in graph[u].items():
                if capacity > 0 and dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    parent[v] = u
                    pq.put((v, dist[v]))

        # Step 3: Если сток недостижим, выход из цикла
        if dist['sink'] == float('inf'): break

        # Step 4: Находим остаточный путь и находим аргумент минимума на этом пути
        flow = MAX_FLOW
        u = 'sink'
        while u != 'source':
            flow = min(flow, graph[parent[u]][u][0])  # взяли пропускную способность как аргумент минимума
            u = parent[u]

        # Step 5: Обновляем граф
        u = 'sink'
        while u != 'source':
            v = parent[u]
            graph[v][u] = (graph[v][u][0] - flow, graph[v][u][1])  # уменьшаем пропускную способность на поток
            graph.setdefault(u, dict()).setdefault(v, (0, 0))
            graph[u][v] = (graph[u][v][0] + flow, graph[u][v][1])  # увеличиваем пропускную способность на поток
            u = v
        max_cost += flow * dist['sink']  # добавляем прибыль соответствующую потоку
        MAX_FLOW -= flow    # уменьшаем максимальный поток, текущий на этой итерации
    print(graph)
    return max_cost

# Пример использования функции
n, m, p = map(int, input().split())
orders = []
for _ in range(n):
    cost, num_tools, *tool_ids = map(int, input().split())
    orders.append((cost, num_tools, tool_ids))

# tool_prices = list(map(int, input().split()))
tool_prices = []
for _ in range(m):
    tool_prices.append(int(input()))

discounts = []
for _ in range(p):
    tool_1, tool_2, discount_price = map(int, input().split())
    tool_ids = [tool_1, tool_2]
    discounts.append((tool_ids, discount_price))
max_profit = max_cost_flow(n, m, p, orders, tool_prices, discounts)
print(max_profit)