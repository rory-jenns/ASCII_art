import sys, os
import ASCII

# Take Command line Arguments
# > python ASCII_cmd.py "input.png" "output.txt"
if len(sys.argv) == 3:
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    
    ASCII.make_ascii(in_file, out_file)

else:
    print("Statements take this form")
    print("python ASCII_cmd.py \"input.png\" \"output.txt\"")
