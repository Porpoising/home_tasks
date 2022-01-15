n = int(input().lower())
struct = {'global': []}


def get_namespace(nmspc, var, dictio):
    if var not in dictio[nmspc] and nmspc == 'global':
        return 'None'
    if var in dictio[nmspc]:
        for _ in range(len(dictio[nmspc])):
            if var == dictio[nmspc][_]:
                return nmspc

    for temp_nmspc, temp_var in dictio.items():
        for _ in range(len(temp_var)):
            if nmspc == temp_var[_]:
                nmspc = temp_nmspc
    end_nmspc = get_namespace(nmspc, var, dictio)
    return end_nmspc


for _ in range(n):
    request = [i for i in input().split()]
    if request[0] == 'create':
        struct[request[2]].append(request[1])
        struct[request[1]] = []
    if request[0] == 'add':
        struct[request[1]].append(request[2])
    if request[0] == 'get':
        print(get_namespace(request[1], request[2], struct))
