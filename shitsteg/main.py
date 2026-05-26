import random
import sys

from PIL import Image

FAIL_LETTER = 35  # is equal to '#'


def steg_hide(file: str, msg: str, file_dest: str | None = None):
    if not file_dest:
        file_dest = "hidden_" + file
    if not file_dest.lower().endswith(".png"):
        file_dest = file_dest.rsplit(".", 1)[0] + ".png"

    img = Image.open(file)
    pixels = img.load()
    if not pixels:
        exit(1)

    used_spots = set()
    used_spots.add((69, 69))

    def next_spot():
        while True:
            x, y = random.randbytes(2)
            if (x, y) not in used_spots:
                used_spots.add((x, y))
                return x, y

    px, py = 69, 69
    for char in msg:
        char = ord(char)
        char = char if 0 <= char <= 255 else FAIL_LETTER
        nx, ny = next_spot()

        pixels[px, py] = char, nx, ny
        px, py = nx, ny
    pixels[px, py] = FAIL_LETTER, 69, 69

    img.save(file_dest, format="PNG")


def steg_solve(file: str):
    buf = ""

    img = Image.open(file)
    pixels = img.load()
    if not pixels:
        exit(1)

    x, y = 69, 69
    while True:
        vals = pixels[x, y]
        if not isinstance(vals, tuple):
            exit(1)
        char, x, y = vals
        if x == 69 and y == 69:
            break
        buf += chr(char)

    print(buf)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Missing arguments")
        exit(1)

    match sys.argv[1]:
        case "hide":
            if len(sys.argv) != 4:
                print("Missing Source file and Msg")
                exit(1)
            steg_hide(sys.argv[2], sys.argv[3])

        case "solve":
            if len(sys.argv) != 3:
                print("Missing file to solve")
                exit(1)
            steg_solve(sys.argv[2])
