size = n = int(input())
ind1 = ind2 = 0
turn_count = 0
el = 1
el_list = [['el' for i in range(n)] for j in range(n)]

while el <= size ** 2:
    if size == 1:
        el_list[0][0] = el
        break
    elif size == 2:
        for ind2 in range(n):
            el_list[ind1][ind2] = el
            el += 1
        ind1 += 1
        for ind2 in range(ind2, -1, -1):
            el_list[ind1][ind2] = el
            el += 1
        break
    else:
        if el_list[ind1][ind2] == 'el' and el_list[ind1][ind2 + 1] == 'el':
            for ind2 in range(ind2, n + ind2):
                el_list[ind1][ind2] = el
                el += 1
            turn_count += 1
            if (turn_count - 1) % 2 == 0:
                n -= 1
            ind1 += 1
        if el_list[ind1][ind2] == 'el' and el_list[ind1 + 1][ind2] == 'el':
            for ind1 in range(ind1, n + ind1):
                el_list[ind1][ind2] = el
                el += 1
            turn_count += 1
            if (turn_count - 1) % 2 == 0:
                n -= 1
            ind2 -= 1
        if el_list[ind1][ind2] == 'el' and el_list[ind1][ind2 - 1] == 'el':
            for ind2 in range(ind2, ind2 - n, -1):
                el_list[ind1][ind2] = el
                el += 1
            turn_count += 1
            if (turn_count - 1) % 2 == 0:
                n -= 1
            ind1 -= 1
        if el_list[ind1][ind2] == 'el' and el_list[ind1 - 1][ind2] == 'el':
            for ind1 in range(ind1, ind1 - n, -1):
                el_list[ind1][ind2] = el
                el += 1
            turn_count += 1
            if (turn_count - 1) % 2 == 0:
                n -= 1
            ind2 += 1
        if el == size ** 2 and size % 2 == 0:
            el_list[ind2][ind1] = el
            el += 1
        if el == size ** 2 and size % 2 == 1:
            el_list[ind1 - 1][ind2 + 1] = el
            el += 1

for i in range(size):
    for j in range(size):
        if j == size - 1:
            print(el_list[i][j])
        else:
            print(el_list[i][j], end=' ')
