def combisom(list, x):
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j and list[i] + list[j] == x:
                return True
    else:
        return False