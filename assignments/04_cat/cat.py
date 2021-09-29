#!/usr/bin/env python3
"""
Author : Amy Banka <abanka@email.arizona.edu>
Date   : 2021-09-22
Purpose: I concatenate files - that means join
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I concatenate files - that means join',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  
    parser.add_argument('fi',
                        help='Input files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))
            

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        default=False)


    args = parser.parse_args()

    return args

# --------------------------------------------------
def main():
    """Bwam bwam bwam bwaaaaa"""

    args = get_args()
    files = args.fi
    
    for i in files[0:]:
        if os.path.isfile(i.name):
            blah = open(i.name, "r")
            #take off the , "r" & add i.name.read().rstrip()
            ### wtf is r
            line_list = blah.readlines()
            blah.close()
            numbering = 1
            numbered_list_of_lines = []
            for q in line_list:
                numbered_lines = "{}".format(numbering) + " " + q.rstrip()
                numbering += 1
                print(numbered_lines)
      


# --------------------------------------------------
if __name__ == '__main__':
    main()
