# fractional knapsack using greedy approach

val = []
n = int(input("enter number of values:"))
for i in range(n):
    v = int(input(f"enter value {i+1}:"))
    val.append(v)
wt = []
for i in range(n):
    w = int(input(f"enter weight {i+1}:"))
    wt.append(w)
capacity = int(input("enter capacity of knapsack:"))

def fractionalKnapsack(val, wt, capacity):
    n = len(val)
    items = [[val[i], wt[i]] for i in range(n)]
    items.sort(key=lambda x: x[0]/x[1], reverse=True) #computes ratio for an item x = [value, weight].
    #Why: greedy choice — pick item with highest value per unit weight first to maximize value.
    result = 0.0
    currentCapacity = capacity

    for i in range(n):
        if items[i][1] <= currentCapacity:
            result += items[i][0]
            currentCapacity -= items[i][1]
        else:
            result += (items[i][0]/items[i][1]) * currentCapacity
            break
    return result

if __name__ == "__main__":
#    val = [100, 120, 60]
#    wt = [20, 30, 10]
#    capacity = 50
    max_value = fractionalKnapsack(val, wt, capacity)
    print("maximum value is:", max_value)