def hollow_square(n):
    if n <= 0:
     return ""
    if n == 1:
       return "*"
    
    result = ""

    for j in range(n):
        if j == 0 or j == n - 1:
          result += "*" * n
        else:
           result += "*" + " " * (n-2) + "*"
        result += "\n"

    return result

# Plugging in n = 7
print(hollow_square(7))


def number_pattern(n):
    
    if n <= 0:
        return ""  
    result = ""
    j = 1
    while j <= n:
        p = 1
        while p <=j:
            result += str(p)
            p += 1
        result += "\n"
        j += 1
    return result

# Plugging in n = 6
print(number_pattern(6))

def sum_of_natural_numbers(n):
   total = 0
   counter = 1
   while counter <= n:
      total += counter
      counter += 1

   return total

#plugging in n = 5, sum= 1 + 2 + 3 + 4 + 5 = 15
print(sum_of_natural_numbers(5)) 

def centered_star_pyramid(n):
   result = ""
   i = 1

   while i <= n:
      spaces = n - i
      stars = 2 * i - 1

      result += " " * spaces
      result += "*" * stars
      
      if i != n:
         result += "\n"
      
      i += 1

   return result 

#Plugging in n = 4
print(centered_star_pyramid(4))    