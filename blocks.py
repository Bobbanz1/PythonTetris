from block import Block
from position import Position


# L Block
#   0
# 000
class LBlock(Block):
    def __init__(self):
        super().__init__(id=1)
        # Key will be rotation state, a value from 0 to 3. with the various positions associated with each state
        self.cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 1), Position(0, 0), Position(1, 1), Position(2, 1)],
        }
        self.move(0, 3)


# J Block
# 0
# 000
class JBlock(Block):
    def __init__(self):
        super().__init__(id=2)
        # Key will be rotation state, a value from 0 to 3. with the various positions associated with each state
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)],
        }
        self.move(0, 3)


# I Block
# 0000
class IBlock(Block):
    def __init__(self):
        super().__init__(id=3)
        # Key will be rotation state, a value from 0 to 3. with the various positions associated with each state
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)],
        }
        self.move(-1, 3)


# O Block
# 00
# 00
class OBlock(Block):
    def __init__(self):
        super().__init__(id=4)
        # Key will be rotation state, a value from 0 to 3. with the various positions associated with each state
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            1: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            2: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
            3: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)],
        }
        self.move(0, 4)


# S Block
#  00
# 00
class SBlock(Block):
    def __init__(self):
        super().__init__(id=5)
        # Key will be rotation state, a value from 0 to 3. with the various positions associated with each state
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)],
        }
        self.move(0, 3)


# T Block
#  0
# 000
class TBlock(Block):
    def __init__(self):
        super().__init__(id=6)
        # Key will be rotation state, a value from 0 to 3. with the various positions associated with each state
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)],
        }
        self.move(0, 3)


# Z Block
# 00
#  00
class ZBlock(Block):
    def __init__(self):
        super().__init__(id=7)
        # Key will be rotation state, a value from 0 to 3. with the various positions associated with each state
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)],
        }
        self.move(0, 3)
