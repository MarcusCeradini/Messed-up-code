num = int(input("Input a number: "))

def evenorodd(num):
    if num % 2 == 0:
        num = str(num)
        return num +  " is an even number"
    else:
        num = str(num)
        return num + " is an odd or null value"
        
print(evenorodd(num))