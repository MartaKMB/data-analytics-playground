try:
    num = int(input("Enter number: "))
    result = 10/num
    print(f"result: {result}")
except ZeroDivisionError:
    num = 1
    result = 10/num
    print(f"result: {result}")
    print("cannot divide by zero")
except ValueError:
    print("that is not an int")
except:
    print("default except")
finally:
    print("finally")

print("end of program")

num_2 = int(input("Enter number: "))

if num_2 < 0:
    print(f"negative value {num_2}")
    raise ValueError("negative value is not supported")
