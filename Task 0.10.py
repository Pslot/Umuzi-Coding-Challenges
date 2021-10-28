def common_letters():
  string_1 = input("Enter a word of your choice: ")
  string_2 = input("Enter a another word: ")
  s1 = set(string_1)
  s2 = set(string_2)
  lst = s1 and s2 #make a list of common letters
  print ("The common letters are ", lst)
  
common_letters()