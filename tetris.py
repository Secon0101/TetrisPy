from typing import Any, Callable, Optional
from block import Block, BlockType
from vector import Vector


class Tetris:
    """ 테트리스 플레이어 """
    
    def __init__(self, width: int = 10, height: int = 20):
        self.width = width
        self.height = height
        self.map = [[0] * width for _ in range(height)]
        
        self.on_map_update = lambda: None
        
        self.make_new_block()
    
    def add_events(self, on_map_update: Callable[[], Any]):
        """ 테트리스에서 실행되는 이벤트에 리스너를 연결할 수 있다. """
        self.on_map_update = on_map_update
    
    def play(self):
        """ 테트리스 게임을 시작한다. """
        self.on_map_update()
    
    
    # 함수
    def add_block_to_map(self, block: Block):
        """ 맵에 특정 블록을 넣는다. """
        for y in range(block.height):
            for x in range(block.width):
                if block.shape[y][x] == 1:
                    self.map[block.pos.y + y][block.pos.x + x] = block.shape[y][x]
    
    def remove_block_from_map(self, block: Block):
        """ 맵에서 특정 블록을 제거한다. """
        for y in range(block.height):
            for x in range(block.width):
                if block.shape[y][x] == 1:
                    self.map[block.pos.y + y][block.pos.x + x] = 0
    
    def make_new_block(self):
        """ 새로운 블록을 만들어 넣고 현재 블록으로 정한다. """
        block = Block(BlockType.T, Vector(self.width // 2, 0))
        block.pos.x -= block.width // 2
        
        self.current_block = block
        self.add_block_to_map(block)
        
        self.on_map_update()
    
    def move_pos(self, dir: Vector):
        """ 현재 블록을 이동시킨다. """
        if self.can_move(self.current_block, self.current_block.pos + dir):
            self.remove_block_from_map(self.current_block)
            self.current_block.pos += dir
            self.add_block_to_map(self.current_block)
            
            self.on_map_update()
    
    def can_move(self, block: Block, pos: Vector) -> bool:
        """ 블록을 해당 위치로 이동할 수 있는지 확인한다. """
        for y in range(block.height):
            for x in range(block.width):
                if block.shape[y][x] == 1:
                    return True
                    # if not (Vector(0, 0) <= block.pos + pos < Vector(self.width, self.height)):
                    #     return False
                    # if self.map[pos.y + y][pos.x + x] == 1:
                    #     return False
        return True
    
    def rotate(self, clockwise: Optional[bool]):
        """ 현재 블록을 회전시킨다. \n
        clockwise = True -> 오른쪽 \n
        clockwise = False -> 왼쪽 \n
        clockwise = None -> 180도 """
        pass
    
    
    # 키보드 입력 이벤트
    def key_right(self):
        """ 오른쪽 입력 """
        self.move_pos(Vector(1, 0))
        self.on_map_update()
    
    def key_left(self):
        """ 왼쪽 입력 """
        self.move_pos(Vector(-1, 0))
        self.on_map_update()
    
    def key_up(self):
        """ 위쪽 입력 """
        self.rotate(clockwise=True)
        self.on_map_update()
    
    def key_down(self):
        """ 아래쪽 입력 """
        self.move_pos(Vector(0, 1))
        self.on_map_update()
