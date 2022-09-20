def square(x):
  return x**2

def sum_squares(*n):
  sum = 0
  for i in n:
    sum += square(i)
  return sum

print(sum_squares(1,2,3))