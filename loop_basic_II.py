# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(x):
    for i in range(len(x)):
        if x[i] > 0:
            x[i] = "big"
    return x

print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(x):
    counter = 0
    for i in range(len(x)):
        if x[i] > 0:
            counter = counter + 1
    x[len(x)-1] = counter
    return x

print(count_positives([1,6,-4,-2,-7,-2]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(x):
    sum = x[0]
    for i in range(1,len(x)):
        sum = sum + x[i]
    return sum

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(x):
    sum = x[0]
    for i in range(1,len(x)):
        sum = sum + x[i]
    return sum/len(x)

print(average([1,2,3,4]))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(x):
    return len(x)

print(length([37,2,1,-9]))



# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(x):
    if len(x) == 0:
        return "False"
    else:
        min = x[0]
        for i in range(1,len(x)):
            if min > x[i]:
                min = x[i]
        return min

print(minimum([37,2,1,-9]))
print(minimum([]))




# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False


def maximum(x):
    if len(x) == 0:
        return "False"
    else:
        max = x[0]
        for i in range(1,len(x)):
            if max < x[i]:
                max = x[i]
        return max


print(maximum([37,2,1,-9]))
print(maximum([]))



# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(x):
    sum = x[0]
    minimum = x[0]
    maximum = x[0]
    for i in range(1,len(x)):
        sum = sum + x[i]
        if maximum < x[i]:
            maximum = x[i]
        if minimum > x[i]:
            minimum = x[i]
    return {
        'sum': sum,
        'average': sum/len(x),
        'minimum': minimum,
        'maximum': maximum,
        'length': len(x)
    }


print(ultimate_analysis([37,2,1,-9]))





# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


def reverse_list(x):
    x.reverse()
    return x
print(reverse_list([37,2,1,-9]))

