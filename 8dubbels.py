def dubbel(list):
    dict = {}
    for item in list:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1

    for key in dict:
        if dict[key] == 2:
            return key
    return None




def dubbels(list):
    dict = {}
    lijst_eenmaal = set()
    lijst_tweemaal = set()

    for item in list:
        if item not in dict:
            dict[item] = 1
        else:
            dict[item] += 1
    for key in dict:
        if dict[key] == 1:
            lijst_eenmaal.add(key)
        else:
            lijst_tweemaal.add(key)
    return lijst_eenmaal, lijst_tweemaal