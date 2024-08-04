def operation(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2
    if num2 == 0 + 0j:
        print("Error!")
        return None
    division_result = num1 / num2
    return (sum_result, difference_result, product_result, division_result)
num1 = input("Enter First Complex Number: ")
num2 = input("Enter Second Complex Number: ")
num1 = complex(num1)
num2 = complex(num2)
result = operation(num1, num2)
print(result)
