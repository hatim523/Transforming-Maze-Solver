from typing import Union

from helpers import generate_path
from maze import finish_point, Maze

direction_mapping = {"left": "W", "right": "E", "up": "N", "down": "S"}


class Ball:
    def __init__(self, maze: Maze, exploring_path_info):
        self.maze = maze
        self.current_row = exploring_path_info['current_row']
        self.current_col = exploring_path_info['current_col']
        self.path_generated = exploring_path_info['path']
        self.iterations = exploring_path_info['iterations']
        self.visited_points = exploring_path_info['visited']
        self.found = exploring_path_info['found']

        self.current_matrix = self.maze.get_maze_for_iteration(self.iterations)
        self.current_position_point = \
            self.get_point_in_matrix_given_coordinates(
                self.current_row, self.current_col)

    def can_move_to_right_from_current_position(self, current_point):
        return self.can_move_left(current_point)

    def can_move_to_left_from_current_position(self, current_point):
        return self.can_move_right(current_point)

    def can_move_to_up_from_current_position(self, current_point):
        return self.can_move_down(current_point)

    def can_move_to_down_from_current_position(self, current_point):
        return self.can_move_up(current_point)

    def can_move_right(self, move_to: Union[str, int]) -> bool:
        if type(move_to) == str:
            return True
        if move_to < 4:
            return True
        if 8 <= move_to <= 11:
            return True
        return False

    def can_move_left(self, move_to: Union[str, int]) -> bool:
        if type(move_to) == str:
            return True
        if move_to % 2 == 0:
            return True
        return False

    def can_move_up(self, move_to: Union[str, int]) -> bool:
        if type(move_to) == str:
            return True
        if move_to in [0, 1, 4, 5, 8, 9, 12, 13]:
            return True
        return False

    def can_move_down(self, move_to: Union[str, int]) -> bool:
        if type(move_to) == str:
            return True
        if move_to <= 7:
            return True
        return False

    def get_new_coordinate_based_on_direction(self, direction: str):
        if direction == "left":
            new_pos = self.current_row, self.current_col - 1
        elif direction == "right":
            new_pos = self.current_row, self.current_col + 1
        elif direction == "up":
            new_pos = self.current_row - 1, self.current_col
        else:
            new_pos = self.current_row + 1, self.current_col

        return new_pos

    def get_point_in_matrix_given_coordinates(self, row, col) -> \
            Union[int, str]:
        # check bound condition
        if row >= self.maze.total_rows or col >= self.maze.total_cols or \
                row < 0 or col < 0:
            return None

        return self.current_matrix[row][col]

    def get_iterations_required_to_move_right(self, move_to) -> \
            int:
        iterations = 0
        current_point = self.current_position_point

        while True:
            if self.can_move_right(move_to) and \
                 self.can_move_to_right_from_current_position(current_point):
                return iterations

            current_point = self.maze.left_rotate_number(current_point)
            move_to = self.maze.left_rotate_number(move_to)
            iterations += 1

            if iterations > 4:
                return -1

    def get_iterations_required_to_move_up(self, move_to) -> \
            int:
        iterations = 0
        current_point = self.current_position_point

        while True:
            if self.can_move_up(move_to) and \
                    self.can_move_to_up_from_current_position(current_point):
                return iterations

            current_point = self.maze.left_rotate_number(current_point)
            move_to = self.maze.left_rotate_number(move_to)
            iterations += 1

            if iterations > 4:
                return -1

    def get_iterations_required_to_move_down(self, move_to) -> \
            int:
        iterations = 0
        current_point = self.current_position_point

        while True:
            if self.can_move_down(move_to) and \
                    self.can_move_to_down_from_current_position(current_point):
                return iterations

            current_point = self.maze.left_rotate_number(current_point)
            move_to = self.maze.left_rotate_number(move_to)
            iterations += 1

            if iterations > 4:
                return -1

    def get_iterations_required_to_move_left(self, move_to) -> \
            int:
        iterations = 0
        current_point = self.current_position_point

        while True:
            if self.can_move_left(move_to) and \
                    self.can_move_to_left_from_current_position(current_point):
                return iterations

            current_point = self.maze.left_rotate_number(current_point)
            move_to = self.maze.left_rotate_number(move_to)
            iterations += 1

            if iterations > 4:
                return -1

    def construct_new_path(self, iters_required: int, direction: str):
        if iters_required == -1:
            return None

        current_path = list(self.path_generated)
        if not current_path:
            current_path.append('')
        for i in range(iters_required):
            current_path.append('')

        current_path[-1] = current_path[-1] + direction_mapping[direction]
        return current_path

    def get_paths(self):
        """
        Constructs all possible paths i.e. left, up,
            down, right from current position
        """

        # getting direction coordinates w.r.t current position
        up_coordinate = self.get_new_coordinate_based_on_direction("up")
        down_coordinate = self.get_new_coordinate_based_on_direction("down")
        right_coordinate = self.get_new_coordinate_based_on_direction("right")
        left_coordinate = self.get_new_coordinate_based_on_direction("left")

        up_point = self.get_point_in_matrix_given_coordinates(
            up_coordinate[0], up_coordinate[1])
        down_point = self.get_point_in_matrix_given_coordinates(
            down_coordinate[0], down_coordinate[1])
        right_point = self.get_point_in_matrix_given_coordinates(
            right_coordinate[0], right_coordinate[1])
        left_point = self.get_point_in_matrix_given_coordinates(
            left_coordinate[0], left_coordinate[1])

        # getting number of intervals required to visit the position
        up_iters = -1 if up_point is None or up_coordinate in \
            self.visited_points else \
            self.get_iterations_required_to_move_up(up_point)
        down_iters = -1 if down_point is None or down_coordinate in \
            self.visited_points else \
            self.get_iterations_required_to_move_down(down_point)
        right_iters = -1 if right_point is None or right_coordinate in \
            self.visited_points else \
            self.get_iterations_required_to_move_right(right_point)
        left_iters = -1 if left_point is None or left_coordinate in \
            self.visited_points else \
            self.get_iterations_required_to_move_left(left_point)

        # constructing path based on number of intervals and
        # currently generated path
        up_path = self.construct_new_path(up_iters, "up")
        down_path = self.construct_new_path(down_iters, "down")
        right_path = self.construct_new_path(right_iters, "right")
        left_path = self.construct_new_path(left_iters, "left")

        generated_paths = []

        up_total_iters = self.add_iterations(up_iters)
        down_total_iters = self.add_iterations(down_iters)
        right_total_iters = self.add_iterations(right_iters)
        left_total_iters = self.add_iterations(left_iters)
        dimensions = (self.maze.total_rows + self.maze.total_cols) * 4

        if up_path is not None and up_total_iters <= dimensions:
            up_visited = list(self.visited_points)
            up_visited.append(up_coordinate)
            generated_paths.append(generate_path(up_path, up_total_iters,
                                                 up_coordinate, up_visited,
                                                 True if
                                                 up_point == finish_point
                                                 else False))
        if down_path is not None and down_total_iters <= dimensions:
            down_visited = list(self.visited_points)
            down_visited.append(down_coordinate)
            generated_paths.append(generate_path(down_path, down_total_iters,
                                                 down_coordinate, down_visited,
                                                 True if
                                                 down_point == finish_point
                                                 else False))
        if right_path is not None and right_total_iters <= dimensions:
            right_visited = list(self.visited_points)
            right_visited.append(right_coordinate)
            generated_paths.append(generate_path(right_path, right_total_iters,
                                                 right_coordinate,
                                                 right_visited,
                                                 True if
                                                 right_point == finish_point
                                                 else False))
        if left_path is not None and left_total_iters <= dimensions:
            left_visited = list(self.visited_points)
            left_visited.append(left_coordinate)
            generated_paths.append(generate_path(left_path, left_total_iters,
                                                 left_coordinate, left_visited,
                                                 True if
                                                 left_point == finish_point
                                                 else False))

        return generated_paths

    def add_iterations(self, iters_to_add: int) -> int:
        return self.iterations + iters_to_add
