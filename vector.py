class Vector:
    """ X, Y 좌표를 저장하는 클래스 """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y
    
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self == other
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
