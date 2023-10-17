import numpy as np
from PIL import Image

width = 1024
height = 1024

field = np.zeros((height, width), dtype=np.uint8)

ant_x = 512
ant_y = 512

direction = 0

while ant_x >= 0 and ant_x < width and ant_y >= 0 and ant_y < height:
    field[ant_y, ant_x] = 255 - field[ant_y, ant_x]

    if field[ant_y, ant_x] == 0:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

    if direction == 0:
        ant_y -= 1
    elif direction == 1:
        ant_x += 1
    elif direction == 2:
        ant_y += 1
    elif direction == 3:
        ant_x -= 1

image = Image.fromarray(field, mode='L')
image.save('ant_path.bmp')

black_cells = np.sum(field == 0)

print(black_cells)
