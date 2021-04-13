number = int(input())
natural_list = []
natural = 1

while True:
    if number >= (2 * natural + 1):
        natural_list.extend([natural, natural + 1])
        number -= 2 * natural + 1
        natural += 2
        continue
    elif number > natural:
        natural_list.append(natural)
        number -= natural
        natural += 1
        continue
    elif number == natural:
        natural_list.append(natural)
        break
    else:
        natural_list[-1] += number
        break

res_str = ''
for _ in natural_list:
    res_str += str(_) + ' '
print(len(natural_list), res_str, sep='\n')
