class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1

    @staticmethod
    def get_count(): 
        return Player.count

messi = Player('Messi')
ronaldo = Player('Ronaldo')

print(Player.count)

print(messi.count)
print(ronaldo.count)

print(Player.get_count())

