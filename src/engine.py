from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from bearlibterminal import terminal as blt

from map_objects.point import Point
from rect import Rect

if TYPE_CHECKING:
    from enum import Enum

SCREEN_WIDTH: int = 170
SCREEN_HEIGHT: int = 90
WINDOW_TITLE: str = "Dungeon Tycoon"


class Room(Rect):
    def __init__(self, position: Point, width: int, height: int):
        super(Room, self).__init__(position=position, width=width, height=height)
        self.door: Optional[Point] = None
        self.room_type: Optional[Enum] = None


def display_map(rooms: List[Room], map_area=None) -> None:
    if map_area:
        blt.put(x=map_area.left, y=map_area.top, c="\u250C")
        blt.put(x=map_area.right, y=map_area.top, c="\u2510")
        blt.put(x=map_area.left, y=map_area.bottom, c="\u2514")
        blt.put(x=map_area.right, y=map_area.bottom, c="\u2518")
        for i in range(1, map_area.right):
            blt.put(x=i, y=map_area.top, c="\u2500")
            blt.put(x=i, y=map_area.bottom, c="\u2500")
        for j in range(1, map_area.bottom):
            blt.put(x=map_area.left, y=j, c="\u2502")
            blt.put(x=map_area.right, y=j, c="\u2502")
    for room in rooms:
        for point in room:
            blt.put(x=point.x, y=point.y, c=".")


def main():
    map_area = Rect(position=Point(0, 0), width=130, height=60)
    blt.set(
        f"window: size={SCREEN_WIDTH}x{SCREEN_HEIGHT}, title={WINDOW_TITLE}, cellsize=8x8"
    )
    blt.set("input: filter={keyboard, mouse+}")

    blt.refresh()

    game_running = True

    rooms: List[Room] = []

    # create entrance
    entrance = Room(position=Point(5, 5), width=5, height=3)
    # add entrance
    rooms.append(entrance)

    while game_running:
        blt.clear()

        if blt.has_input():
            terminal_input = blt.read()

            if terminal_input in {blt.TK_ESCAPE, blt.TK_Q, blt.TK_CLOSE}:
                game_running = False

        # blt.puts(1, 1, "Hello World!")
        display_map(rooms=rooms, map_area=map_area)

        blt.refresh()


if __name__ == '__main__':
    blt.open()
    main()
    blt.close()
