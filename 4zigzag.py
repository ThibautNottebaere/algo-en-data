def iszigzag(list):
    for i in range(len(list) - 1):
        if i % 2 == 0:  # even stukken
            if list[i] < list[i + 1]:
                return False
        else:  # oneven stukken
            if list[i] > list[i + 1]:
                return False
    return True


def zigzag_traag(list):
    list.sort()
    for i in range(0, len(list) - 1, 2):
        if i % 2 == 0:
            list[i], list[i + 1] = list[i + 1], list[i]


def zigzag_snel(reeks):
    for i in range(0, len(reeks), 2):
        if i > 0 and reeks[i] < reeks[i - 1]:
            reeks[i], reeks[i - 1] = reeks[i - 1], reeks[i]
        if i + 1 < len(reeks) and reeks[i] < reeks[i + 1]:
            reeks[i], reeks[i + 1] = reeks[i + 1], reeks[i]




