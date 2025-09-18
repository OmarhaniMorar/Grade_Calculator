count = int(input("How many numbers do you want to enter? "))

nums = []

for i in range(count):
    n = int(input(f"Enter number {i+1}: "))
    nums.append(n)

print("Entered numbers:", nums)
def Calculate_the_arithmetic_mean(nums):
    return sum(nums) / len(nums)

def Greatest_least_value(nums):
    return max(nums), min(nums)

def More_odd_or_even_numb(nums):
    odd = 0
    even = 0
    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    if odd > even:
        return "More odd numbers"
    elif even > odd:
        return "More even numbers"
    else:
        return "Equal odd and even numbers"

"""
    def Greatest_least_value(nums):
        greatest = nums[0]
        least = nums[0]
        for n in nums:
            if n > greatest:
                greatest = n
            if n < least:
                least = n
        return greatest, least
"""

"""
    def Calculate_the_arithmetic_mean(nums):
        sum = 0
        for n in nums:
            sum += n
        return sum / len(nums)    
"""

mean = Calculate_the_arithmetic_mean(nums)
greatest, least = Greatest_least_value(nums)
more_odd_or_even = More_odd_or_even_numb(nums)


print("The arithmetic mean is:", mean)
print("The greatest value is:", greatest)
print("The least value is:", least)
print(more_odd_or_even)

    