#!/usr/bin/env python3
import sys
import os
import re

def main():
    if len(sys.argv) < 3:
        print("Usage: ./generator.py [catagory] [problem]")
        exit(1)
    _, ctg, prob = sys.argv
    path = os.path.join('./', ctg, prob)
    os.makedirs(path, exist_ok=True)
    prob_num = re.search(r'^\d+', prob).group(0)
    code_file = os.path.join(path, prob_num + '.py')
    test_file = os.path.join(path, prob_num + '.txt')
    with open(code_file, 'w+') as _:
        pass
    with open(test_file, 'w+') as _:
        pass
    

if __name__ == "__main__":
    main()
