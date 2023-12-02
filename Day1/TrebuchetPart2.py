# reading the words from text file 
with open('words.txt') as f:
    content = f.read()

# mapping numbers in words to their integer values
hashmap = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

# test case
words = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]

def sumCalibration(values):
    total = 0
    for word in values:
        numbers = []
        for i in range(len(word)):
            if not word[i].isdigit():
                if i+3<=len(word) and word[i:i+3] in hashmap:
                    #print(word[i:i+3])
                    numbers.append(hashmap[word[i:i+3]])
                if i+4<=len(word) and word[i:i+4] in hashmap:
                    #print(word[i:i+4])
                    numbers.append(hashmap[word[i:i+4]])
                if i+5<=len(word) and word[i:i+5] in hashmap:
                    #print(word[i:i+5])
                    numbers.append(hashmap[word[i:i+5]])
            if word[i].isdigit():
                #print(word[i])
                numbers.append(word[i])
        #print(numbers)
        if len(numbers) == 1:
            total += int(str(numbers[0])*2)
        else:
            total += int(str(numbers[0]) + str(numbers[-1]))
    return total

#print(sumCalibration(words))
print(sumCalibration(content.split()))
