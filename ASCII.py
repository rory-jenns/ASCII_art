import numpy as np
import matplotlib.pyplot as plt

INPUT_FILE = "alone_cafe_low_res.png"
OUTPUT_FILE = "ascii_cafe.txt"

# ascii = "$#H&@*+;:-,.  "
ascii = "  .,-:;+@&H###$"
size_of_ascii = len(ascii)

pic = plt.imread("INPUT_FILES"+INPUT_FILE)

pic = np.dot(pic[...,:3], [0.2989, 0.5870, 0.1140])

with open("OUTPUT_FILES/"+OUTPUT_FILE, "+w") as f:
    for row in pic:
        for pixel in row:
            char = ascii[int((pixel*size_of_ascii)//1)]
            f.write(char)
        f.write("\n")
