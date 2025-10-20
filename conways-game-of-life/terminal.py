SIZE = 20


def load_glider():
    with open("./scenes/glider.txt", "r") as file:
        data = file.read().strip()
    return eval(data)


def print_cells(cells):
    for row in cells:
        for val in row:
            ch = "¤" if val else "."
            print(ch, end="")
        print()


from copy import deepcopy


def count_neighbors(cells, idx, idy):
    neighbors = []
    rows, cols = len(cells), len(cells[0])

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # skip the center cell itself
            nx, ny = idx + dx, idy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors.append(cells[nx][ny])
    return neighbors.count(True)


def step_cells(cells):
    new_cells = deepcopy(cells)
    for idx, row in enumerate(cells):
        for idy, val in enumerate(row):
            alive_neigh = count_neighbors(cells, idx, idy)
            if val and alive_neigh < 2:
                new_cells[idx][idy] = False
            elif val and alive_neigh in [2, 3]:
                new_cells[idx][idy] = True
            elif val and alive_neigh > 3:
                new_cells[idx][idy] = False
            elif not val and alive_neigh == 3:
                new_cells[idx][idy] = True
    return new_cells


if __name__ == "__main__":
    cells = load_glider()

    while True:
        print_cells(cells)
        try:
            input()
        except KeyboardInterrupt:
            break
        cells = step_cells(cells)
