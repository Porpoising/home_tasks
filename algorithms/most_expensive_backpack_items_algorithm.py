n, W = input().split()
item_list = []

for _ in range(int(n)):
    ci, wi = input().split()
    item_list.append([int(ci), int(wi)])
item_list.sort(key=lambda x: x[0] / x[1], reverse=True)

backpack = 0
W = int(W)
for _ in range(len(item_list)):
    if W != 0 and W >= item_list[_][1]:
        backpack += item_list[_][0]
        W -= item_list[_][1]

    elif W == 0:
        break

    elif W < item_list[_][1]:
        backpack += item_list[_][0] / (item_list[_][1] / W)
        break

print(format(backpack, '.3f'))
