# odd or even
def even_or_odd(number):
 if number %2 == 0:
  return "Even"
 else: 
  return "Odd"
 
 #Convert a Number to a String!
 def number_to_string(num):
    return str(num)
 #Vowel Count
def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels + 1
    return num_vowels