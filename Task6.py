def greedy_algorithm(items, budget):
   
    items_sorted = sorted(items.items(), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)
    selected_items = []
    current_cost = 0

    for item, data in items_sorted:
        if current_cost + data["cost"] <= budget:
            selected_items.append(item)
            current_cost += data["cost"]

    return selected_items

def dynamic_programming(items, budget):

    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, data = list(items.items())[i - 1]
        for w in range(1, budget + 1):
            if data["cost"] <= w:
                dp[i][w] = max(data["calories"] + dp[i - 1][w - data["cost"]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        item, data = list(items.items())[i - 1]
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item)
            w -= data["cost"]

    return selected_items

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Жадібний алгоритм
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:", greedy_result)

# Динамічне програмування
dp_result = dynamic_programming(items, budget)
print("Динамічне програмування:", dp_result)