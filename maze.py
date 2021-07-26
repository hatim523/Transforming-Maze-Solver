from typing import Union

finish_point = 'X'
start_point = 'B'


class Maze:
    def __init__(self, maze):
        self.original_maze = maze

        self.transformed_maze = []
        self.starting_position = None
        self.ending_position = None

        self.total_rows = len(self.original_maze)
        self.total_cols = len(self.original_maze[0])

        self.save_transformations()
        self.get_starting_and_ending_point()

    def save_transformations(self):
        second_form = self.transform_matrix(self.original_maze)
        third_form = self.transform_matrix(second_form)
        fourth_form = self.transform_matrix(third_form)
        self.transformed_maze = [
            self.transform_matrix(fourth_form), second_form,
            third_form, fourth_form
        ]

    def transform_matrix(self, matrix):
        """
        Transforms given nxm matrix using left_rotate_number function
        """
        transformed_matrix = []
        for row in matrix:
            transformed_row = []
            for col in row:
                transformed_row.append(self.left_rotate_number(col))
            # adding row
            transformed_matrix.append(transformed_row)

        # converting list to tuple for consistency
        return transformed_matrix

    def left_rotate_number(self, number: Union[str, int]) -> Union[str, int]:
        # special condition when it is starting or ending position
        if type(number) == str:
            return number
        rotated = number * 2
        return rotated if rotated <= 15 else rotated - 15

    def get_maze_for_iteration(self, iteration_num) -> list:
        return self.transformed_maze[iteration_num % 4]

    def get_starting_and_ending_point(self):
        for i, row in enumerate(self.original_maze):
            for j, col in enumerate(row):
                if col == start_point:
                    self.starting_position = (i, j)
                elif col == finish_point:
                    self.ending_position = (i, j)
