#!/bin/python3

import os
import sys

if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    rev=arr[::-1]
    print(" ".join(rev))
