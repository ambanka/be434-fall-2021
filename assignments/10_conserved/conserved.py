#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-11-06
Purpose: I show conserved bases
"""
import argparse
import sys
import os
from io import StringIO
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I show conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        # nargs = 1, 
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    lines_list = file.read().split()
    # print(lines)
    # print(len(lines_list))
    # print(lines[1])
    
    line1 = lines_list[0]
    line2 = lines_list[1]
    # line3 = lines_list[2]

    # for line in lines_list[1]:
    #     line[1] == lin
 
    # for line in lines_list[0:]:
    #     print(line)
    #     for n in line[0:]:
    #         print(n)

                ## PSHLQYHERTHTGEKPYECHQCGQAFKKCSLLQRHKR
                ## HSHLQCHKRTHTGEKPYECNQCGKAFSQHGLLQRHKR
                ## x||||x|x|||||||||||x|||x||xxxx|||||||

    
    # x = enumerate(line1)
    # print(list(x))
    # map, filter?

    # lol = [1, 2]
    # def comparison(lol):
    #     if 1 == 2:
    #         return '|'
    #     else:
    #         return 'x'

    # for lines in lines_list:
    #     mapped = map(comparison, (line1), (line2))
    #     # map(comparison, (lines))
    # print(*list(mapped))



    # for lines in lines_list:
    #     for n in lines[0:]:
    #         mapped = map(comparison, lines)
    # print(*list(mapped))     
    # 
    # 
    #  
    # x = map(comparison, (line1), (line2))
    # print(list(x))


 ## this is the real code ##
    if len(lines_list) == 2:
        print(line1)
        print(line2)
        for n in range(len(line1)):
            if line1[n] == line2[n]:
                print('|', end='')
            else:
                print('X', end = '')

    if len(lines_list) == 3:
        line3 = lines_list[2]
        print(line1)
        print(line2)
        print(line3)
        for n in range(len(line1)):
            if line1[n] == line2[n] == line3[n]:
                print('|', end='')
            else:
                print('X', end = '')
    


## end real working code ##

    # for line in lines_list
    # for character in line


    # ok = [[item for item in lines_list] for x in item]
    # ok = [x for x in lines_list[1] if x in lines_list[2]]
    # print(ok)
    # # for n in ok:
    #     if n in 


    # for line in lines_list:
    #     for char in line:
    #         if char == char:
    #             print(char)
    #         else:
    #             print('X')

    #     print(line)

    # def prog():
    #     if char == char:
    #         print('Y')
    #     else:
    #         print('X')

    # # todd = lines_list[1]
    # # print(todd[1])

    # # def identical:


    # # map(print(n), line)
    # # for char in lines[1]:
    # #     print(char)

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
