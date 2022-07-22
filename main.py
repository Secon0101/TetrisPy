from tetris import Tetris
import keyboard
from os import system


tetris = Tetris()


def main():
    # 이벤트 연결
    tetris.add_events(on_map_update=print_map)
    keyboard.on_press(check_key)
    
    system("cls")  # 콘솔 창 클리어
    print('\033[?25l')  # 커서 숨기기
    
    tetris.play()
    keyboard.wait("esc")


def check_key(key: keyboard.KeyboardEvent):
    """ 키보드 입력에 맞는 테트리스 이벤트를 실행시킨다. """
    if key.name in ("right", "d"):
        tetris.key_right()
    if key.name in ("left", "a"):
        tetris.key_left()
    if key.name in ("up", "w"):
        tetris.key_up()
    if key.name in ("down", "s"):
        tetris.key_down()

def print_map():
    """ 콘솔 창에 맵을 출력한다. (테트리스 이벤트) """
    move(0, 0)
    print()  # 맨 첫 번째 칸 글자가 깨져서 한 칸 아래부터 함
    for row in tetris.map:
        for cell in row:
            print('■' if cell == 1 else '□', end=' ')
        print()

def move(x: int, y: int):
    """ 커서를 x, y 좌표로 이동시킨다. """
    print("\033[%d;%dH" % (x, y))


if __name__ == "__main__":
    main()
