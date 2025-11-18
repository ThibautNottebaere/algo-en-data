def zoek(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    else:
        return None