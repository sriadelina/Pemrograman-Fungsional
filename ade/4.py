def isPalindrome(s):
  s = s.lower()
  s = s.replace(" ","")
  return s == s[::-1]

#kata = (input("Input kata : "))
kata1 = "No lemon, no melon"
kata2 = "Madam, I’m Adam"
print (isPalindrome(kata1))
