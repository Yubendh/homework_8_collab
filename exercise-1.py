def replace_last(numbers):

    if len(numbers) <= 1:
        return numbers

    return [numbers[-1]] + numbers[:-1]
