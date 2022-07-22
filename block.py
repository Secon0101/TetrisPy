from enum import Enum
from vector import Vector


class BlockType(Enum):
    NONE = 0,
    T = 1,

class Block:
    """ 테트리스 블록 하나 """
    def __init__(self, type: BlockType = BlockType.T, pos: Vector = Vector(0, 0)):
        self.type = type
        self.shape = Block.get_shape(type)
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.pos = pos
    
    @staticmethod
    def get_shape(shape: BlockType) -> list[list[int]]:
        """ BlockShape에 맞는 이차원 배열을 반환한다. """
        match shape:
            case BlockType.T:
                return [[0, 1, 0],
                        [1, 1, 1],
                        [0, 0, 0]]
