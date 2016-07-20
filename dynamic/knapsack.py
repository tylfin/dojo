"""
More info see https://en.wikipedia.org/wiki/Knapsack_problem
"""

def knapsack(items, weights, values, capacity=7, value=0):
    if not items or capacity <= 0:
        return value

    item = items.pop()

    # if the capacity minus the weight of the item is 0, then we return
    if capacity - weights[item] < 0:
        return knapsack(items, weights, values, capacity, value)

    tmp1 = knapsack(list(items), weights, values, capacity, value)
    tmp2 = knapsack(list(items), weights, values, capacity - weights[item], value + values[item])
    return max(tmp1, tmp2)



def test():
    items = ['apple', 'pear', 'rock', 'bananas', 'lighter', 'peach']
    weights = {'apple': 1, 'pear': 1, 'rock': 10, 'bananas': 3, 'lighter': 0.5,
        'peach': 1}
    values = {'apple': 1, 'pear': 1, 'rock': 0, 'bananas': 3, 'lighter': 0.5,
        'peach': 1}
    max_value = knapsack(items, weights, values)
    print(max_value)
    # assert(max_value == 5)

if __name__ == "__main__":
    test()
