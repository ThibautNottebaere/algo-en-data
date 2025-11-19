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

# Eerst de Player-klasse uit deel 1 (moet in hetzelfde bestand staan of geïmporteerd worden)



# ==================== DEEL 2: KLASSE PASS ====================
class Pass:
    def __init__(self, sender, receiver, nr_of_times):
        self.sender = sender          # Player object
        self.receiver = receiver      # Player object
        self.nr_of_times = nr_of_times  # int

    def get_weight(self):
        return self.nr_of_times

    def get_start(self):
        return self.sender

    def get_end(self):
        return self.receiver

    def __eq__(self, other):
        if not isinstance(other, Pass):
            return NotImplemented
        return self.sender == other.sender and self.receiver == other.receiver
        # nr_of_times telt NIET mee voor gelijkheid!

    def __str__(self):
        return f"Pass from {self.sender.name} to {self.receiver.name}"


# ==================== TESTEN (0.5 punt) ====================
if __name__ == "__main__":
    # 3 Player objecten
    hazard = Player("Eden Hazard", 10)
    dembele = Player("Moussa Dembele", 19)
    vertonghen = Player("Jan Vertonghen", 5)
    lukaku = Player("Romelu Lukaku", 9)

    # 3 Pass objecten
    pass1 = Pass(hazard, dembele, 15)
    pass2 = Pass(vertonghen, lukaku, 8)
    pass3 = Pass(hazard, dembele, 22)   # zelfde sender+receiver als pass1!

    # Print één Pass
    print(pass1)   # verwacht: Pass from Eden Hazard to Moussa Dembele

    # Test __eq__
    print(pass1 == pass3)   # True  (zelfde spelers, aantal keren maakt niet uit)
    print(pass1 == pass2)   # False

    # Test get_weight
    print(pass1.get_weight())   # 15
    print(pass3.get_weight())   # 227

# Eerst de Player-klasse uit deel 1 (moet in hetzelfde bestand staan of geïmporteerd worden)




