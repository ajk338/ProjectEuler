<<<<<<< HEAD


palProduct = 0
palMax = 0



=======
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
palProduct = 0
palMax = 0
>>>>>>> origin/master

def ifPal(number):
        number = str(number)
        reversed = number[::-1]
        if number==reversed:
                return True
        else:
                return False

a = 0
b = 0

for i in range(100,1000):
        for j in range(100,1000):
                palProduct = i * j
                if (ifPal(palProduct) and (palMax < palProduct)):
                        palMax = palProduct
                        a = i
                        b = j


<<<<<<< HEAD
print "The maximum palindrome that is a product of two 3-digit numbers is", palMax, "made from ", a, " * ", b
=======
print "The maximum palindrome that is a product of two 3-digit numbers is", palMax, "made from ", a, " * ", b
>>>>>>> origin/master
