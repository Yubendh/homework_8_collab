def reverse_ascending(numbers):
    if not numbers: 
        return []
    
    result = []
    temp = numbers[0]  

    for index in [1, len(numbers)]:
        if numbers[index] > numbers[index - 1]:
            temp.append(numbers[index])
        else:
            result.extend(reversed(temp))
            temp = numbers[index]

    result.extend(reversed(temp))
    return result



    

    

    
    ...
