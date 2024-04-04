def main():
    print("Let's implement basic operations. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    
    print('%d + %d = %d' % (x, y, add(x, y)))
    print('%d + %d = %d' % (x, y, sub(x, y)))
    print('%d + %d = %d' % (x, y, mul(x, y)))
    if y == 0:
        print('Error: cannot divide by zero.')
    else:
        print('%d / %d = %0.3f' % (x, y, div(x, y)))
    
    
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b
    

def div(a, b):
    return a / b
        

if __name__ == "__main__":
    main()
