#!/usr/bin/env python3
"""
Author : abanka <abanka@localhost>
Date   : 2021-09-15
Purpose: Annoy People with Music
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='I annoy people with music',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('notes',
                        metavar= 'str',
                        type= str,
                        nargs= '*',
                        help= 'Solfege')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Julie Andrews warms up"""

    args = get_args()
    notes = args.notes
    response = {'Do': 'Do, A deer, a female deer', 'Re': 'Re, A drop of golden sun', 'Mi': 'Mi, A name I call myself', 'Fa': 'Fa, A long long way to run', 'Sol': 'Sol, A needle pulling thread', 'La': 'La, A note to follow sol', 'Ti': 'Ti, A drink with jam and bread'}
    

    for i in range(len(notes)):
        if notes[i] in response:
            print(response.get(notes[i]))
        else:
            print("I don't know " + '"' + notes[i] + '"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
