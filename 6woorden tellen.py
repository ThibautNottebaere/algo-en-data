def woorden_splitsen(data):
    file = open(data, 'r') #bekijkt het bestand
    inhoud = file.read() #bekijkt de inhoud van het bestand (dus de effectieve woorden)
    woorden = inhoud.split() #splitst alle woorden in een lijst
    gestript = []

    for i in woorden:
        gestript_woord = i.strip('?.!,:;()') #verwijdert alle leestekens die voor of achter een woord staan (dus don't blijft don't)
        gestript.append(gestript_woord)
    return gestript

def uncap(data):
    uncap = []
    woorden_list = woorden_splitsen(data)
    for woord in woorden_list:
        x = woord.lower()
        uncap.append(x)
    return uncap

def woorden_tellen(data):
    dict = {}
    woorden_list =uncap(data)
    for woord in woorden_list:
        if woord not in dict:
            dict[woord] = 1
        else:
            dict[woord] += 1
    return dict
