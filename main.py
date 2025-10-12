# A small library of utility functions

def is_prime(num):
    # Bug: This is not a correct primality test
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

def fibonacci(n):
    # Inefficient recursive implementation
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def get_file_content(filename):
    # No error handling for file not found
    f = open(filename, "r")
    return f.read()

# Poorly styled function
def someFunction(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    # very long line
    result = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p
    return result