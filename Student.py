class Student:
  def __init__(self, lName, fName, ssn, email, age):
    self.lName = lName
    self.fName = fName
    self.ssn = ssn
    self.email = email
    self.age = age

  def __eq__(self, rhs):
    if rhs.__class__.__name__ == "Student":
      return self.ssn == rhs.ssn
    return self.ssn == rhs

  def __lt__(self, rhs):
    if rhs.__class__.__name__ == "Student":
      return self.ssn < rhs.ssn
    return self.ssn < rhs

  def __gt__(self, rhs):
    if rhs.__class__.__name__ == "Student":
      return self.ssn > rhs.ssn
    return self.ssn > rhs

