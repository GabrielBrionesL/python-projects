# Function that takes a list and target parameter
def binary_search(list, target):
    # Assign counter to multiple variables: middle, start, end, steps
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    # While loop
    while(start<=end):
        print("Step", steps, ":", str(list[start:end+1]))

        # Increase the steps each time a split is done
        steps = steps+1
        middle = (start + end) // 2

        # Conditions to track target position
        if target == list[middle]:
            return middle
        #Uses index to search through lower end of list
        if target < list[middle]:
            end = middle - 1
        #Uses index to search through upper end of list
        else:
            start = middle + 1

    return -1

#range(stop)
numbers = range(12)
#Convert to list
list_1 = list(numbers)
target = 11

binary_search(list_1, target)