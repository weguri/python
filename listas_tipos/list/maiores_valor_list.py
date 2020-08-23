import heapq

lst = [2, 3, 5, 6, 8, 4, 2, 1]

# Os 3 maiores:
print(heapq.nlargest(3, lst))

# Os 3 menores
print(heapq.nsmallest(3, lst))
