import numpy as np
import matplotlib.pyplot as plt

def make_ascii(inputf, outputf):
    # ascii = "$#H&@*+;:-,.  "
    ascii = "  .,-:;+@&H###$"
    size_of_ascii = len(ascii)

    try:
        path = "INPUT_FILES/"+inputf
        pic = plt.imread(path)
    except:
        print("ERROR\nFile Path does not exist")
        print("Check file is in ./INPUT_FILES")
        print("PATH:",path)
    
    pic = np.dot(pic[...,:3], [0.2989, 0.5870, 0.1140])

    with open("OUTPUT_FILES/"+outputf, "+w") as f:
        for row in pic:
            for pixel in row:
                char = ascii[int((pixel*size_of_ascii)//1)]
                f.write(char)
            f.write("\n")


if __name__ == "__main__":
    make_ascii("alone_cafe_low_res.png", "ascii_cafe.txt")