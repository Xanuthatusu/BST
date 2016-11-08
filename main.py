import sys

from bst import BST
from Student import Student

def main():
  if len(sys.argv) != 4:
    print("wow man you gave me the wrong amount of arguments!!")
    return

  tree = BST()

  with open(sys.argv[1], "r") as openFile:
    for line in openFile:
      values = line.split()

      student = Student(*values)
      tree.insert(student)

  with open(sys.argv[2], "r") as openFile:
    for line in openFile:
      values = line.split()

      tree.delete(values[0])

  with open(sys.argv[3], "r") as openFile:
    for line in openFile:
      values = line.split()

      tree.retrieve(values[0])

main()

