# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]


def move_zeros(array):
    new_array = [item for item in array if not (type(item) != bool and item == 0)]
    return new_array + [0] * (len(array) - len(new_array))

