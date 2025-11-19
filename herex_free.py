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




# ==================== DEEL 3: PASSGRAPH ====================
class PassGraph:
    def __init__(self):
        self.players = []                    # lijst van Player objecten
        self.adj = {}                        # dict: sender_name → lijst van Pass objecten

    def add_player(self, player):
        if not any(p.name == player.name for p in self.players):
            self.players.append(player)
            self.adj[player.name] = []       # lege lijst voor uitgaande passes

    def has_player(self, speler):
        if isinstance(speler, str):
            name = speler
        else:  # Player object
            name = speler.name
        return any(p.name == name for p in self.players)

    def get_player(self, name):
        for p in self.players:
            if p.name == name:
                return p
        return None

    def add_pass(self, sender, receiver, times=1):
        if times <= 0:
            return  # of raise ValueError("times must be positive")

        if not self.has_player(sender) or not self.has_player(receiver):
            return

        sender_name = sender.name
        # Zoek of er al een pass bestaat sender → receiver
        for pass_obj in self.adj[sender_name]:
            if pass_obj.receiver.name == receiver.name:
                pass_obj.nr_of_times += times
                return

        # Nieuwe pass als die nog niet bestaat
        new_pass = Pass(sender, receiver, times)
        self.adj[sender_name].append(new_pass)

    def get_pass(self, sender_name, receiver_name):
        if sender_name not in self.adj:
            return None
        for pass_obj in self.adj[sender_name]:
            if pass_obj.receiver.name == receiver_name:
                return pass_obj
        return None

    def neighbors(self, sender_name):
        return self.adj.get(sender_name, [])

    def total_weight(self, subset=None):
        if subset is None:
            subset = [p.name for p in self.players]

        total = 0
        for sender_name in subset:
            if sender_name not in self.adj:
                continue
            for pass_obj in self.adj[sender_name]:
                if pass_obj.receiver.name in subset:
                    total += pass_obj.nr_of_times
        return total

    def pass_intensity(self, subset=None):
        if subset is None:
            subset = [p.name for p in self.players]

        n = len(subset)
        if n < 2:
            return 0.0

        teller = self.total_weight(subset)
        noemer = n * (n - 1)
        return teller / noemer

    def top_pairs(self, k=5):
        all_passes = []
        for pass_list in self.adj.values():
            all_passes.extend(pass_list)
        # sorteer dalend op nr_of_times
        all_passes.sort(key=lambda p: p.nr_of_times, reverse=True)
        return all_passes[:k]

    def distribution_from(self, sender_name):
        if sender_name not in self.adj:
            return []
        passes = self.adj[sender_name]
        # maak lijst (receiver_name, count)
        result = [(p.receiver.name, p.nr_of_times) for p in passes]
        result.sort(key=lambda x: x[1], reverse=True)
        return result


# ==================== TESTEN (1 punt) ====================
if __name__ == "__main__":
    graph = PassGraph()

    # 4 spelers
    hazard = Player("Eden Hazard", 10)
    kdb = Player("Kevin De Bruyne", 7)
    lukaku = Player("Romelu Lukaku", 9)
    courtois = Player("Thibaut Courtois", 1)

    for p in [hazard, kdb, lukaku, courtois]:
        graph.add_player(p)

    # 6 passes toevoegen
    graph.add_pass(hazard, kdb, 20)
    graph.add_pass(hazard, lukaku, 15)
    graph.add_pass(kdb, lukaku, 25)
    graph.add_pass(kdb, hazard, 10)
    graph.add_pass(lukaku, hazard, 5)
    graph.add_pass(courtois, kdb, 30)

    # Analyse testen
    print("Total weight hele team:", graph.total_weight())
    print("Pass intensity hele team:", graph.pass_intensity())

    subset = ["Eden Hazard", "Kevin De Bruyne", "Romelu Lukaku"]
    print("Intensity aanval:", graph.pass_intensity(subset))

    print("\nTop 3 pairs:")
    for p in graph.top_pairs(3):
        print(f"{p} (times: {p.nr_of_times})")

    print("\nPasses van De Bruyne:")
    for receiver, count in graph.distribution_from("Kevin De Bruyne"):
        print(f"  → {receiver}: {count}")
