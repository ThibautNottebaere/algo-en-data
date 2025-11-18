def samenvoegen(list1, list2):
    list = []
    i = 0
    j = 0
    lengte = min(len(list1), len(list2))
    while i < lengte and j < lengte:
        list.append(list1[i])
        list.append(list2[j])
        i += 1
        j += 1
    return list


def weven(list1, list2):
    list = []
    len1 = len(list1)
    len2 = len(list2)
    max_len = max(len1, len2)

    for i in range(max_len):
        a = list1[i % len1]
        b = list2[i % len2]
        list.append(a)
        list.append(b)
    return list

def ritsen(list1, list2):
    list = []
    len1 = len(list1)
    len2 = len(list2)
    min_len = min(len1, len2)

    for i in range(min_len):
        list.append(list1[i])
        list.append(list2[i])

    verschil = abs(len1 - len2)
    while verschil > 0:
        if len1 < len2:
            list.append(list2[len2 - verschil])
            verschil -= 1
        else:
            list.append(list1[len1 - verschil])
            verschil -= 1
    return list