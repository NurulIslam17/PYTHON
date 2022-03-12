
def find_max(numbers):
    maximum = numbers[0]
    for iteam in numbers:
        if iteam > maximum:
            maximum = iteam
    return maximum
