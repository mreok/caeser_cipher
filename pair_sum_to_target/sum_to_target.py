def pairs_sum_to_target(list1, list2, target):
    pairs = []

    for i,value1 in enumerate(list1):
        for j,value2 in enumerate(list2):
            if value1 + value2 == target:
                pairs.append([value1, value2])

    return pairs

l1 = [2,3,4,5,6]
l2 = [4,3,2,5,3]
t = 10

p = pairs_sum_to_target(l1,l2,t)
print(p)