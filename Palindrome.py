palProduct = 0
palMax = 0
num1=100



def isPalindrome(number):
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
                if (isPalindrome(palProduct) and (palMax < palProduct)):
                        palMax = palProduct
                        a = i
                        b = j


print "The maximum palindrome that is a product of two %d-digit numbers is [ %d ] made of %d * %d" % (len(str(num1)), palMax, a, b)