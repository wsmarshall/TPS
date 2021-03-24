# python3

from collections import namedtuple
#import os

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)         

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack:
                if are_matching(opening_brackets_stack[-1], next):
                    opening_brackets_stack.pop()
            else:
                return i + 1
            
    if opening_brackets_stack:
        return len(text)
    
    return 'Success'

def main():
    testdir = './tests/'
    for i in range(1,55):
        fname = str(i)
        if i < 10:
            fname = '0' + fname
        with open(testdir + fname) as f:
            text = f.read()
            mismatch = find_mismatch(text)
            print(text,mismatch)
    # Printing answer, write your code here
    
def submit_main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
if __name__ == "__main__":
    submit_main()
