from operator import truediv


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = node(data) #stap 1, de node class aanroepen en u eerste element aanmaken
        if self.head is None: #als de lijst leeg is, dan
            self.head = newnode
            return

        current = self.head #je begint bij de eerste
        while current.next is not None: #zolang de volgende node niet None is, zijn we nog niet aan het einde
            current = current.next #dus wnr we aan het einde van de lijst zijn, is de current node, de laatste node
        current.next = newnode

    def delete(self, data):
        if self.head is None:
            return

            # Als het te verwijderen element het eerste is
        if self.head.data == data:
            self.head = self.head.next #vikge
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Lege lijst")




