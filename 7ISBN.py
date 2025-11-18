def isISBN13(code):
    if not (
        isinstance(code, str) and          # code moet een string zijn
        len(code) == 13 and                # code moet bestaan uit 13 karakters
        code.isdigit()                     # eerste negen karakters moeten cijfers zijn
    ):
        return False

    # prefix van de gegeven code controleren
    if code[:3] not in ('978', '979'):
        return False

    # controlecijfer berekenen
    controle = 0
    for i in range(12):
        if i % 2:
            controle += 3 * int(code[i])
        else:
            controle += int(code[i])

    controlecijfer = controle % 10
    controlecijfer = (10 - controlecijfer) % 10
    return controlecijfer == int(code[-1])



def overzicht(codes):
    groepen = {}
    for i in range(11):
        groepen[i] = 0

    for code in codes:
        if not isISBN13(code):
            groepen[10] += 1 #groep met sleutel 10 verhogen in dit geval is dat de groep voor de fouten
        else:
            groepen[int(code[3])] += 1
    print(f"Engelstalige landen: {groepen[0] + groepen[1]}")
    print(f"Franstalige landen: {groepen[2]}")
    print(f"Duitstalige landen: {groepen[3]}")
    print(f"Japan: {groepen[4]}")
    print(f"Russischtalige landen: {groepen[5]}")
    print(f"China: {groepen[7]}")
    print(f"Overige landen: {groepen[6] + groepen[8] + groepen[9]}")
    print(f"Fouten: {groepen[10]}")