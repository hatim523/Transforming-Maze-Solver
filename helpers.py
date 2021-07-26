
def filter_paths(generated_paths: dict, new_paths: list):
    for path in new_paths:
        x_coordinate = path['current_row']
        y_coordinate = path['current_col']

        if (x_coordinate, y_coordinate) in generated_paths.keys():
            if path["iterations"] < \
                    generated_paths[(x_coordinate,
                                     y_coordinate)]["iterations"]:
                generated_paths[(x_coordinate, y_coordinate)] = path
        else:
            generated_paths[(x_coordinate, y_coordinate)] = path

    return generated_paths


def generate_path(path: list, iterations: int, coordinate: tuple,
                  visited: list, found: bool):
    return {
        "path": path,
        "iterations": iterations,
        "current_row": coordinate[0],
        "current_col": coordinate[1],
        "found": found,
        "visited": visited
    }
