from typing import List, Optional, Set


map_str: list[str] = [
    "??????????????????????????????",
    "#...............??????????????",
    "#.#############.??????????????",
    "#.#.#.T#........??????????????",
    "#.#......#..............#.#..#",
    "#.##########.############.#..#",
    "#.....##......##......#....###",
    "#...####..##..##..##..#..#...#",
    "#.........##......##.....#.C.#",
    "##############################",
]


class Point:
    def __init__(self, x: int, y: int, char: str) -> None:
        self.x: int = x
        self.y: int = y
        self.char: str = char
        self.start = False
        self.end = False
        self.distance = 99999
        self.cost = 1
        self.came_from: Optional[Point] = None

    @property
    def is_wall(self):
        return self.char == "#"

    def is_path(self):
        if self.char != "?" and self.char != "#":
            return True
        else:
            return False

    def __str__(self):
        return self.char

    def __repr__(self) -> str:
        return self.__str__()


class Mapper:
    def __init__(self) -> None:
        self.map: List[List[Point]] = []
        self.points_set: Set[Point] = set()

    def get_init_points(self):
        start, end = (None, None)
        for point in self.points_set:
            if point.char == "C":
                start = point
            elif point.char == "T":
                end = point
        return start, end

    def update(self, map_str: List[str]):
        for i_row, row in enumerate(map_str):
            row_points = []
            for i_char, char in enumerate(row):
                new_points = Point(i_char, i_row, char)
                row_points.append(new_points)
                self.points_set.add(new_points)
            self.map.append(row_points)

    def check_print(self):
        printable = ""
        for row in self.map:
            printable = f"{printable}\n{row}"
        printable = f"{printable}"
        from time import sleep

        sleep(0.5)
        print(printable)

    def get_point(self, x: int, y: int) -> Optional[Point]:
        if x < 0 or y < 0:
            return None

        for point in self.points_set:
            if point.x == x and point.y == y:
                return point
        return None

    def euclidian_distance(self, point_a: Point, point_b: Point):
        import math

        return math.sqrt(
            math.pow((point_a.x - point_b.x), 2) + math.pow((point_a.y - point_b.y), 2)
        )

    def get_neighbors(self, point: Point):
        base_x = point.x
        base_y = point.y
        neighbors_list: List[Point] = []
        neighbors_list.extend(self._get_point_list(self.get_point(base_x - 1, base_y)))
        neighbors_list.extend(self._get_point_list(self.get_point(base_x + 1, base_y)))
        neighbors_list.extend(self._get_point_list(self.get_point(base_x, base_y - 1)))
        neighbors_list.extend(self._get_point_list(self.get_point(base_x, base_y + 1)))
        return neighbors_list

    def _get_point_list(self, point: Optional[Point]) -> List[Point]:
        if point is None:
            return []
        else:
            return [point]

    def compute_path(self, start: Point, end: Point):
        closed_list = []
        open_list = []
        open_list.append(start)
        while open_list != []:
            open_list.sort(key=lambda a: a.distance)
            compute_point = open_list.pop(0)
            if compute_point.is_path() is False:
                continue
            if compute_point is end:
                for p in closed_list:
                    p.char = "-"
                return
            for neigh in self.get_neighbors(compute_point):
                if neigh.is_path() is False:
                    continue
                if neigh in closed_list:
                    continue
                if neigh in open_list:
                    if neigh.cost <= compute_point.cost:
                        continue
                neigh.came_from = compute_point
                neigh.cost = compute_point.cost + 1
                neigh.distance = neigh.cost + self.euclidian_distance(neigh, end)
                if neigh not in open_list:
                    open_list.append(neigh)
            self.check_print()
            compute_point.char = "-"
            closed_list.append(compute_point)
        else:
            print("cest pas bon")

    def retrieve_path(self, start: Point, end: Point):
        path = []
        path.append(end)
        came = end.came_from
        while came is not None:
            path.append(came)
            came.char = "+"
            if came is start:
                break
            print(came.x, came.y)
            came = came.came_from
        path.reverse()
        return path


mapper = Mapper()


def main():
    mapper.update(map_str)

    start, end = mapper.get_init_points()

    start = mapper.get_point(1, 1)
    end = mapper.get_point(10, 3)
    end.char = "E"
    a = mapper.compute_path(start, end)
    print(mapper.retrieve_path(start, end))
    mapper.check_print()


if __name__ == "__main__":
    main()
