from abc import ABC, abstractmethod

class GammingConsole(ABC):

    @abstractmethod
    def up(self): pass

    @abstractmethod
    def down(self): pass

    @abstractmethod
    def left(self): pass

    @abstractmethod
    def right(self): pass


class MarioGame(GammingConsole):
    def up(self): print('jump')

    def down(self): print('goes down a hole')

    def left(self): pass

    def right(self): print('goes forward')


class ChessGame(GammingConsole):
    def up(self): print('Move piece up')

    def down(self): print('Move piece down')

    def left(self): print('Move piece left')

    def right(self): print('Move piece right')


games = [ChessGame(), MarioGame()]
for game in games:
    game.up()
    game.down()
    game.left()
    game.right()
    print()
