import random

rand = random
rand.seed()


def get_invalid(x, y, final):
    invalids = []
    if x == 9 or x == 0 or y == 0 or y == 6:
        invalids = [0, 1, 2, 3]
    # Get Left
    if x != 0:
        num = final[x-1][y]
        invalids.append(num)
        #invalids.append(num + 1)
        #invalids.append(num - 1)
    # Get Up
    if y != 0:
        num = final[x][y-1]
        invalids.append(num)
        #invalids.append(num + 1)
        #invalids.append(num - 1)
    return invalids


def generate_final():
    # stock = [14, 14, 14, 14, 16, 14, 14, 14, 14]

    stock = [8, 8, 8, 8, 10, 8, 8, 8, 8]

    final = [[-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1]]

    # final = [[-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1]]

    for idx, i in enumerate(final):
        for idy, j in enumerate(i):
            sides = get_invalid(idx, idy, final)
            count = 0
            while count < 100:
                tmp = rand.randint(0, 8)
                if tmp not in sides and stock[tmp] > 0:
                    stock[tmp] -= 1
                    final[idx][idy] = tmp
                    count = 100
                count += 1

    return [stock, final]


def get_inv_stain(x, y, final):
    invalids = []
    # if x == 9 or x == 0 or y == 0 or y == 6:
        # invalids.append(0)
    # Get Left
    if x != 0:
        num = final[x-1][y]
        if num == 0 or num == 1:
            invalids.append(num)
            # invalids.append(1)
        # invalids.append(num)
    # Get Up
    if y != 0:
        num = final[x][y-1]
        if num == 0 or num == 1:
            invalids.append(num)
            # invalids.append(1)
        # invalids.append(num)
    return invalids


def generate_stain():
    # 0 - Black
    # 1 - Walnut
    # 2 - Burned
    final = [[-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1]]

    # final = [[-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1],
    #          [-1, -1, -1, -1, -1, -1, -1, -1]]

    for idx, i in enumerate(final):
        for idy, j in enumerate(i):
            sides = get_inv_stain(idx, idy, final)
            count = 0
            while count < 100:
                tmp = rand.randint(0, 2)
                if tmp not in sides:
                    final[idx][idy] = tmp
                    count = 100
                count += 1
    return final


def generate_ratio_stain(final):
    count = [0, 0, 0]
    for j in final:
        for i in j:
            count[i] += 1
    for idx, c, in enumerate(count):
        count[idx] = (count[idx]/70)*100
    return count


# test = generate_stain()
# for j in test:
#     print(j)
#
# ratio = generate_ratio_stain(test)
# print(ratio)

# while 1:
#     test = generate_stain()
#     count = 0
#     for i in test[0]:
#         count += i
#     if count == 0:
#         for j in test[1]:
#             print(j)
#         ratio = generate_ratio_stain(test[1])
#         print(ratio)
#         break

it = 0
while 1:
    print(it)
    it += 1
    test = generate_final()
    count = 0
    for i in test[0]:
        count += i
    if count <= 5:
        for j in test[1]:
            print(j)
        break

print(test[0])





