import time

start_time = time.time()


def fib(n, m):
    pisano_list = [0, 1, 1]

    for _ in range(2, m ** 2 + 1):
        pisano_list.append((pisano_list[-1] % m + pisano_list[-2] % m) % m)
        if len(pisano_list) >= 5:
            if pisano_list[-3::] == [0, 1, 1]:
                print(pisano_list)
                del pisano_list[-3::]
                break

    print(pisano_list)
    print("--- %s seconds ---" % (time.time() - start_time))
    return pisano_list[n % len(pisano_list)]


print(fib(10, 2))