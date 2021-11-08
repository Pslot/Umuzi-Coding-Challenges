numb = int

def number_to_time(numb):
  hour = numb // 60 #formular to convert number to hour
  minutes = numb % 60 #formular to convert number to minutes

  print( hour, " hour(s),", minutes, " minute(s)")
number_to_time(numb)