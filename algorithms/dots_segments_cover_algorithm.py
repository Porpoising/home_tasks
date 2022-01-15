from operator import itemgetter

segment_list = sorted([[int(_) for _ in input().split()]
                       for _ in range(int(input()))], key=itemgetter(1))
result_list = [segment_list[0]]


for _ in range(1, len(segment_list)):
    sl_0, sl_1 = segment_list[_][0], segment_list[_][1]
    if len(result_list[-1]) == 1:
        rl_0 = result_list[-1][0]
    else:
        rl_0, rl_1 = result_list[-1][0], result_list[-1][1]

    if len(result_list[-1]) == 1 and rl_0 not in range(sl_0, sl_1 + 1):
        result_list.extend([segment_list[_]])
    elif len(result_list[-1]) == 2:
        if rl_1 < sl_0:
            result_list.extend([segment_list[_]])
        elif rl_1 == sl_0:
            result_list[-1] = [rl_1]
        elif sl_0 > rl_0:
            result_list[-1][0] = sl_0
    print(result_list)


result_string = ''
for _ in result_list:
    result_string += str(_[0]) + ' '
print(len(result_list), result_string, sep='\n')
