import Student

def main():
  one = Student.Student("George", "Anthony", "3456432", "adiad@adnva.com", 16, None)
  two = Student.Student("Walters", "Bradley", "3456789", "erftgv@gmail.com", 16, one)
  current = two
  while (current != None):
    print current.fName
    current = current.nxt

main()

