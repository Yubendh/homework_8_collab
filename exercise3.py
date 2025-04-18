def remove_all_after(input_list, target):
    # first we write condition to Check if the input is a list. I learn the concept isinstace from w3school.
    if not isinstance(input_list, list):
        raise TypeError("The first argument must be a list.")
    
    # then Check if the list is empty
    if not input_list:
        return input_list  # We Return an empty list if input is empty

    # Next Check if the target exists in the list
    if target not in input_list:
        return input_list  # Return the list unchanged if the target is not found

    # Finally we find the index of the target and slice the list
    index = input_list.index(target)
    return input_list[:index + 1]
