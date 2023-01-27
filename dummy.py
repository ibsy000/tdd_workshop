# write a function that takes in a list of integers and 
# returns a new list of only the even numbers

# def getEven(arr):
#     return [num for num in arr if not num % 2]

def getEven(arr):
    arr2 = []
    for num in arr:
        if num % 2 == 0:
            arr2.append(num)
    return arr2