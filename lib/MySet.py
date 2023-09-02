# A Set is a data structure that is used for storing a collection of unique values.

# They are useful for problems that involve finding repeated values, or removing duplicate values.
class MySet:
  
  def __init__(self, enumerable = []):
    self.dictionary = {}
    for value in enumerable:
      self.dictionary[value] = True

  def has(self, value):
    return value in self.dictionary
  
  def add(self, value):
    self.dictionary[value] = True
    return self
  
  def delete(self, value):
    self.dictionary.pop(value, None)
    return self
  
  def size(self):
    return len(self.dictionary)
  
  def clear(self):
    self.dictionary.clear()
    return self
  
   

      
      
