def maxmin(numbers):
    max = numbers[0]
    min = numbers[0]
    for number in numbers:
        if number > max:
            max = number
        elif number < min:
            min = number
    return [min,max]

print(maxmin([2,4,1,0,2,-1]))
print(maxmin([20,50,12,6,14,8]))
print(maxmin([100,-100]))