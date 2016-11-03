import sys

from bst import BST
from Student import Student

def main():
  if len(sys.argv) != 2:
    print("wow man you gave me the wrong amount of arguments!!")
    return

  tree = BST()

  with open(sys.argv[1], 'r') as openFile:
    for line in openFile:
      values = line.split()

      student = Student(*values)
      tree.insert(student)

main()

