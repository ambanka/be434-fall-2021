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
    # line_num = 0
    for i in files[0:]:
        if os.path.isfile(i.name):
            blah = open(i.name).read().rstrip()
            # print(type(blah))
            print(blah)
            # for line in blah[0:'\n']:
            #     line_num += 1
            #     print (line_num, line)

  

            # for line in blah:
            #     print(list(enumerate(line)))
    
    # for blah:
    #     enumerate('\n'):
    #     print('\n')

            # for q in enumerate('\n' in blah):
            #     print(q)


      # #line_num += 1
   # print(line_num)


# --------------------------------------------------
if __name__ == '__main__':
    main()
