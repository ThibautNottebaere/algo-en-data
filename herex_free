class Player:
    def __init__(self, name, number):
        self.name = name          # str
        self.number = number      # int

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name   # alleen naam telt!

    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.number < other.number   # laagste nummer eerst

    def __str__(self):
        return f"{self.name} ({self.number})"


# ==================== TESTEN (DIT MOET ERONDER STAAN!) ====================
if __name__ == "__main__":
    # 1. Drie spelers maken en in een lijst steken
    p1 = Player("Eden Hazard", 10)
    p2 = Player("Moussa Dembele", 19)
    p3 = Player("Jan Vertonghen", 5)

    spelers = [p1, p2, p3]

    # 2. Eén speler printen
    print(p1)                            # verwacht: Eden Hazard (10)

    # 3. Test __eq__ (naam gelijk = True, ook al nummer anders)
    p4 = Player("Eden Hazard", 7)        # zelfde naam, ander nummer
    print(p1 == p4)                      # moet True zijn
    print(p1 == p2)                      # False

    # 4. Test __lt__ + sorteren op nummer
    print("Voor sorteren:", spelers)
    gesorteerd = sorted(spelers)         # gebruikt automatisch __lt__
    print("Na sorteren op nummer:", gesorteerd)

    # Verwachte output:
    # Eden Hazard (10)
    # True
    # False
    # Voor sorteren: [Eden Hazard (10), Moussa Dembele (19), Jan Vertonghen (5)]
    # Na sorteren op nummer: [Jan Vertonghen (5), Eden Hazard (10), Moussa Dembele (19)]
