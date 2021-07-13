from typing import Union

iters_required_list = [[{'left': 0, 'right': 0, 'up': 0, 'down': 0}, {'left': 1, 'right': 0, 'up': 0, 'down': 0},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 0}, {'left': 1, 'right': 0, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 0}, {'left': 1, 'right': 1, 'up': 0, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 0, 'up': 0, 'down': 1}, {'left': 2, 'right': 0, 'up': 0, 'down': 1},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 0, 'right': 1, 'up': 0, 'down': 0}, {'left': 1, 'right': 1, 'up': 0, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 0}, {'left': 1, 'right': 1, 'up': 0, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 0, 'right': 0, 'up': 0, 'down': 1}, {'left': 2, 'right': 0, 'up': 0, 'down': 1},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 0, 'up': 0, 'down': 1}, {'left': 2, 'right': 0, 'up': 0, 'down': 1},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 1, 'right': 0, 'up': 0, 'down': 0}, {'left': 1, 'right': 0, 'up': 0, 'down': 0},
                        {'left': 1, 'right': 0, 'up': 2, 'down': 0}, {'left': 1, 'right': 0, 'up': 2, 'down': 0},
                        {'left': 1, 'right': 1, 'up': 0, 'down': 0}, {'left': 1, 'right': 1, 'up': 0, 'down': 0},
                        {'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 2, 'right': 0, 'up': 0, 'down': 1}, {'left': 2, 'right': 0, 'up': 0, 'down': 1},
                        {'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 1, 'right': 1, 'up': 0, 'down': 0}, {'left': 1, 'right': 1, 'up': 0, 'down': 0},
                        {'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 1, 'right': 1, 'up': 0, 'down': 0}, {'left': 1, 'right': 1, 'up': 0, 'down': 0},
                        {'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 2, 'right': 0, 'up': 0, 'down': 1}, {'left': 2, 'right': 0, 'up': 0, 'down': 1},
                        {'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}, {'left': 2, 'right': 0, 'up': 0, 'down': 1},
                        {'left': 2, 'right': 0, 'up': 0, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}, {'left': 3, 'right': 1, 'up': 0, 'down': 2},
                        {'left': 3, 'right': 1, 'up': 0, 'down': 2}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 0, 'right': 0, 'up': 1, 'down': 0}, {'left': 1, 'right': 0, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 0}, {'left': 1, 'right': 0, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 0, 'up': 1, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': 0, 'right': 2, 'up': 1, 'down': 3}, {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 1, 'right': 0, 'up': 2, 'down': 0}, {'left': 1, 'right': 0, 'up': 2, 'down': 0},
                        {'left': 1, 'right': 0, 'up': 2, 'down': 0}, {'left': 1, 'right': 0, 'up': 2, 'down': 0},
                        {'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': 1, 'right': 3, 'up': 2, 'down': 0}, {'left': 1, 'right': 3, 'up': 2, 'down': 0},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': 2, 'right': 0, 'up': 3, 'down': 1},
                        {'left': 2, 'right': 0, 'up': 3, 'down': 1}, {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}],
                       [{'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1},
                        {'left': -1, 'right': -1, 'up': -1, 'down': -1}]]


def can_move_to_right_from_current_position(current_position_point):
    return can_move_left(current_position_point)


def can_move_to_left_from_current_position(current_position_point):
    return can_move_right(current_position_point)


def can_move_to_up_from_current_position(current_position_point):
    return can_move_down(current_position_point)


def can_move_to_down_from_current_position(current_position_point):
    return can_move_up(current_position_point)


def can_move_right(move_to: Union[str, int]) -> bool:
    if type(move_to) == str:
        return True
    if move_to < 4:
        return True
    if 8 <= move_to <= 11:
        return True
    return False


def can_move_left(move_to: Union[str, int]) -> bool:
    if type(move_to) == str:
        return True
    if move_to % 2 == 0:
        return True
    return False


def can_move_up(move_to: Union[str, int]) -> bool:
    if type(move_to) == str:
        return True
    if move_to in [0, 1, 4, 5, 8, 9, 12, 13]:
        return True
    return False


def can_move_down(move_to: Union[str, int]) -> bool:
    if type(move_to) == str:
        return True
    if move_to <= 7:
        return True
    return False


def get_new_coordinate_based_on_direction(current_row, current_col, direction: str):
    if direction == "left":
        new_pos = current_row, current_col - 1
    elif direction == "right":
        new_pos = current_row, current_col + 1
    elif direction == "up":
        new_pos = current_row - 1, current_col
    else:
        new_pos = current_row + 1, current_col

    return new_pos


def get_point_in_matrix_given_coordinates(row, col, total_rows, total_cols, matrix) -> Union[int, str]:
    # check bound condition
    if row >= total_rows or col >= total_cols or row < 0 or col < 0:
        return None

    return matrix[row][col]


def transform_matrix(matrix):
    """
    Transforms given nxm matrix using left_rotate_number function
    """
    transformed_matrix = []
    for row in matrix:
        transformed_row = []
        for col in row:
            transformed_row.append(left_rotate_number(col))
        # adding row
        transformed_matrix.append(transformed_row)

    # converting list to tuple for consistency
    return transformed_matrix


def left_rotate_number(number: Union[str, int]):
    # special condition when it is starting or ending position
    if type(number) == str:
        return number
    rotated = number * 2
    return rotated if rotated <= 15 else rotated - 15


def get_starting_and_ending_point(matrix):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == 'B':
                starting_position = (i, j)
            elif col == 'X':
                ending_position = (i, j)

    return starting_position, ending_position


def get_iterations_required_to_move_right(current_point, move_to) -> int:
    if type(current_point) == str:
        current_point = 0
    if type(move_to) == str:
        move_to = 0
    return iters_required_list[current_point][move_to]["right"]
    iterations = 0
    while True:
        if can_move_right(move_to) and can_move_to_right_from_current_position(current_point):
            return iterations

        current_point = left_rotate_number(current_point)
        move_to = left_rotate_number(move_to)
        iterations += 1

        if iterations > 4:
            return -1

    # while True:
    #     if can_move_to_right_from_current_position(move_to):
    #         return iterations
    #
    #     iterations += 1
    #     move_to = left_rotate_number(move_to)
    #
    #     if iterations > 6:
    #         return -1


def get_iterations_required_to_move_up(current_point, move_to) -> int:
    if type(current_point) == str:
        current_point = 0
    if type(move_to) == str:
        move_to = 0
    return iters_required_list[current_point][move_to]["up"]
    iterations = 0
    while True:
        if can_move_up(move_to) and can_move_to_up_from_current_position(current_point):
            return iterations

        current_point = left_rotate_number(current_point)
        move_to = left_rotate_number(move_to)
        iterations += 1

        if iterations > 4:
            return -1

    # while True:
    #     if can_move_to_up_from_current_position(move_to):
    #         return iterations
    #
    #     iterations += 1
    #     move_to = left_rotate_number(move_to)
    #
    #     if iterations > 6:
    #         return -1


def get_iterations_required_to_move_down(current_point, move_to) -> int:
    if type(current_point) == str:
        current_point = 0
    if type(move_to) == str:
        move_to = 0
    return iters_required_list[current_point][move_to]["down"]
    iterations = 0
    while True:
        if can_move_down(move_to) and can_move_to_down_from_current_position(current_point):
            return iterations

        current_point = left_rotate_number(current_point)
        move_to = left_rotate_number(move_to)
        iterations += 1

        if iterations > 4:
            return -1

    # while True:
    #     if can_move_to_down_from_current_position(move_to):
    #         return iterations
    #
    #     iterations += 1
    #     move_to = left_rotate_number(move_to)
    #
    #     if iterations > 6:
    #         return -1


def get_iterations_required_to_move_left(current_point, move_to) -> int:
    if type(current_point) == str:
        current_point = 0
    if type(move_to) == str:
        move_to = 0
    return iters_required_list[current_point][move_to]["left"]
    iterations = 0
    while True:
        if can_move_left(move_to) and can_move_to_left_from_current_position(current_point):
            return iterations

        current_point = left_rotate_number(current_point)
        move_to = left_rotate_number(move_to)
        iterations += 1

        if iterations > 4:
            return -1


def find_shortest_path_from_solved_paths(found_paths: list):
    if not found_paths:
        return None

    return sorted(found_paths, key=lambda k: k['iterations'])[0]['path']


direction_mapping = {
    "left": "W",
    "right": "E",
    "up": "N",
    "down": "S"
}

finish_point = 'X'


def distance_left(first_coordinate, second_coordinate):
    return (first_coordinate[0] - second_coordinate[0]) ** 2 + (first_coordinate[1] - second_coordinate[1]) ** 2


def get_paths(iteration_num, current_row, current_col, path_generated, transformed_matrices, total_rows, total_cols,
              visited_points: list, ending_coordinates: tuple):
    current_matrix = transformed_matrices[iteration_num % 4]
    current_point = get_point_in_matrix_given_coordinates(current_row, current_col, total_rows, total_cols,
                                                          current_matrix)

    up_coordinate = get_new_coordinate_based_on_direction(current_row, current_col, "up")
    down_coordinate = get_new_coordinate_based_on_direction(current_row, current_col, "down")
    right_coordinate = get_new_coordinate_based_on_direction(current_row, current_col, "right")
    left_coordinate = get_new_coordinate_based_on_direction(current_row, current_col, "left")

    up_point = get_point_in_matrix_given_coordinates(up_coordinate[0], up_coordinate[1], total_rows, total_cols,
                                                     current_matrix)
    down_point = get_point_in_matrix_given_coordinates(down_coordinate[0], down_coordinate[1], total_rows, total_cols,
                                                       current_matrix)
    right_point = get_point_in_matrix_given_coordinates(right_coordinate[0], right_coordinate[1], total_rows,
                                                        total_cols,
                                                        current_matrix)
    left_point = get_point_in_matrix_given_coordinates(left_coordinate[0], left_coordinate[1], total_rows, total_cols,
                                                       current_matrix)

    up_iters = -1 if up_point is None or up_coordinate in visited_points else get_iterations_required_to_move_up(
        current_point, up_point)
    down_iters = -1 if down_point is None or down_coordinate in visited_points else get_iterations_required_to_move_down(
        current_point, down_point)
    right_iters = -1 if right_point is None or right_coordinate in visited_points else get_iterations_required_to_move_right(
        current_point, right_point)
    left_iters = -1 if left_point is None or left_coordinate in visited_points else get_iterations_required_to_move_left(
        current_point, left_point)

    up_path = construct_new_path(path_generated, up_iters, "up")
    down_path = construct_new_path(path_generated, down_iters, "down")
    right_path = construct_new_path(path_generated, right_iters, "right")
    left_path = construct_new_path(path_generated, left_iters, "left")

    generated_paths = []

    up_total_iters = iteration_num + up_iters
    down_total_iters = iteration_num + down_iters
    right_total_iters = iteration_num + right_iters
    left_total_iters = iteration_num + left_iters
    dimensions = (total_rows + total_cols) * 4

    if up_path is not None and up_total_iters <= dimensions:
        up_visited = list(visited_points)
        up_visited.append(up_coordinate)
        generated_paths.append({"path": up_path,
                                "iterations": up_total_iters,
                                "current_row": up_coordinate[0],
                                "current_col": up_coordinate[1],
                                "found": True if up_point == finish_point else False,
                                "visited": up_visited,
                                # "distance_left": (distance_left(up_coordinate, ending_coordinates)) * (
                                #         (up_total_iters) ** 2),
                                })

    if down_path is not None and down_total_iters <= dimensions:
        down_visited = list(visited_points)
        down_visited.append(down_coordinate)
        generated_paths.append({"path": down_path,
                                "iterations": down_total_iters,
                                "current_row": down_coordinate[0],
                                "current_col": down_coordinate[1],
                                "found": True if down_point == finish_point else False,
                                "visited": down_visited,
                                # "distance_left": (distance_left(down_coordinate, ending_coordinates)) * (
                                #         (down_total_iters) ** 2),
                                })

    if right_path is not None and right_total_iters <= dimensions:
        right_visited = list(visited_points)
        right_visited.append(right_coordinate)
        generated_paths.append({"path": right_path,
                                "iterations": right_total_iters,
                                "current_row": right_coordinate[0],
                                "current_col": right_coordinate[1],
                                "found": True if right_point == finish_point else False,
                                "visited": right_visited,
                                # "distance_left": (distance_left(right_coordinate, ending_coordinates)) * (
                                #         (right_total_iters) ** 2),
                                })
    if left_path is not None and left_total_iters <= dimensions:
        left_visited = list(visited_points)
        left_visited.append(left_coordinate)
        generated_paths.append({
            "path": left_path,
            "iterations": left_total_iters,
            "current_row": left_coordinate[0],
            "current_col": left_coordinate[1],
            "found": True if left_point == finish_point else False,
            "visited": left_visited,
            # "distance_left": (distance_left(left_coordinate, ending_coordinates)) * ((left_total_iters) ** 2),
        })

    return generated_paths


def construct_new_path(current_path: list, iters_required: int, direction: str):
    if iters_required == -1:
        return None

    current_path = list(current_path)
    if not current_path:
        current_path.append('')
    for i in range(iters_required):
        current_path.append('')

    if current_path:
        current_path[-1] = current_path[-1] + direction_mapping[direction]
    else:
        current_path = [direction_mapping[direction]]

    return current_path


def filter_paths(generated_paths: dict, new_paths: list):
    for path in new_paths:
        x_coordinate = path['current_row']
        y_coordinate = path['current_col']

        if (x_coordinate, y_coordinate) in generated_paths.keys():
            if path["iterations"] < generated_paths[(x_coordinate, y_coordinate)]["iterations"]:
                generated_paths[(x_coordinate, y_coordinate)] = path
        else:
            generated_paths[(x_coordinate, y_coordinate)] = path

    return generated_paths


def maze_solver(ar):
    print(ar)
    second_form = transform_matrix(ar)
    third_form = transform_matrix(second_form)
    fourth_form = transform_matrix(third_form)
    transformed_matrices = [
        transform_matrix(fourth_form), second_form, third_form, fourth_form
    ]

    total_rows = len(transformed_matrices[0])
    total_cols = len(transformed_matrices[0][0])

    explored_paths = []
    starting_coordinate, ending_coordinate = get_starting_and_ending_point(transformed_matrices[0])

    generated_paths = {
        (starting_coordinate[0], starting_coordinate[1]): {"path": [], "iterations": 0,
                                                           "current_row": starting_coordinate[0],
                                                           "current_col": starting_coordinate[1], "found": False,
                                                           "visited": []},
    }
    # generated_paths = [{"path": [], "iterations": 0, "current_row": starting_coordinate[0],
    #                     "current_col": starting_coordinate[1], "found": False,
    #                     "visited": []}]

    found_paths = []
    while generated_paths:

        # print(f"{generated_paths = }")
        key_for_exploring_path = next(iter(generated_paths))
        exploring_path = generated_paths[key_for_exploring_path]
        generated_paths.pop(key_for_exploring_path)
        # print(f"{exploring_path = }")
        explored_paths.append(exploring_path)

        # no need to explore finished path
        if exploring_path["found"]:
            #             print("*" * 5, "FOUND", '*' * 5)
            found_paths.append(exploring_path)
            #             if len(found_paths) > 15:
            break
            # continue

        # print(f"{exploring_path = }")

        # input()

        new_paths = get_paths(exploring_path["iterations"],
                              exploring_path["current_row"],
                              exploring_path["current_col"],
                              exploring_path['path'],
                              transformed_matrices,
                              total_rows,
                              total_cols,
                              exploring_path['visited'],
                              ending_coordinate)

        # print(f"{new_paths = }")

        generated_paths = filter_paths(generated_paths, new_paths)
        generated_paths = {k: v for k, v in sorted(generated_paths.items(), key=lambda item: item[1]["iterations"])}
        # exploring all paths therefore no need to sort
        # generated_paths = sorted(generated_paths, key=lambda k: k['iterations'])
        # print(f"{len(generated_paths) = }")

    # print(len(explored_paths))
    #     print(found_paths)
    return find_shortest_path_from_solved_paths(found_paths)


# example_8 = ((11, 5, 14, 0, 3, 0, 13, 4, 3, 7), (3, 8, 6, 0, 2, 8, 13, 12, 8, 6), (4, 12, 15, 15, 2, 1, 5, 5, 10, 7),
#              (4, 0, 2, 10, 3, 12, 11, 1, 4, 'X'), (4, 14, 12, 6, 10, 14, 13, 0, 4, 7),
#              (6, 4, 2, 5, 15, 4, 11, 9, 10, 13), (3, 12, 6, 5, 12, 2, 4, 15, 5, 9), (3, 6, 15, 5, 3, 15, 9, 4, 5, 5),
#              ('B', 1, 6, 4, 6, 3, 4, 8, 3, 13), (2, 13, 5, 11, 4, 14, 15, 12, 11, 6))
#
# example_8_sol = ['', '', '', 'EE', '', 'E', 'NNNN', 'N', 'E', 'NEEE', 'S', 'EE']
#
# sol = maze_solver(example_8)
# print(len(sol) == len(example_8_sol))
# print(sol)
