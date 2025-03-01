def large_factorial(n):
    result = [1]  # Store digits of factorial

    for i in range(2, n + 1):
        carry = 0
        for j in range(len(result)):
            temp = result[j] * i + carry
            result[j] = temp % 10  # Store last digit
            carry = temp // 10  # Carry forward
            
        while carry:
            result.append(carry % 10)
            carry //= 10

    return ''.join(map(str, result[::-1]))  # Convert list to string

num = int(input("Enter a number: "))
print("Factorial:", large_factorial(num))



