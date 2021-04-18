def plan(n, l, i, food):
    i += 1
    if n == 0:
        return food
    else:
        min_animal = min(l)
        num_min = l.count(min_animal)
        count = num_min
        l = [y for y in l if y != min_animal]
        l = [x - min_animal for x in l]
        n = n - count
        food += count * i
        return plan(n, l, i, food)



t = int(input())

for i in range(1, (t + 1)):
    num_animal = int(input())
    list_animal = input().split()
    list_animal = list(map(int, list_animal))
    answer = plan(num_animal, list_animal, 0, 0)
    print("Case #{}: {}".format(i, answer))
