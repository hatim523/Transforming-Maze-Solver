from ball import Ball
from helpers import filter_paths
from maze import Maze


def maze_solver(ar):
    maze = Maze(ar)

    generated_paths = {
        (maze.starting_position[0], maze.starting_position[1]): {"path": [], "iterations": 0,
                                                                 "current_row": maze.starting_position[0],
                                                                 "current_col": maze.starting_position[1],
                                                                 "found": False,
                                                                 "visited": []},
    }
    while generated_paths:
        key_for_exploring_path = next(iter(generated_paths))
        exploring_path = generated_paths[key_for_exploring_path]
        generated_paths.pop(key_for_exploring_path)

        ball = Ball(maze, exploring_path)
        if ball.found:
            return ball.path_generated

        new_paths = ball.get_paths()

        generated_paths = filter_paths(generated_paths, new_paths)
        generated_paths = {k: v for k, v in sorted(generated_paths.items(), key=lambda item: item[1]["iterations"])}

    return None