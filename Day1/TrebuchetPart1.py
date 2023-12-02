with open('words.txt') as f:
    content = f.read()

def sumCalibration(values):
    total = 0
    for word in values:
        numbers = []
        for c in word:
            if c.isdigit():
                numbers.append(c)

        if len(numbers) == 1:
            total += int(numbers[0]*2)
        else:
            total += int(numbers[0] + numbers[-1])
    return total

print(sumCalibration(content.split()))
