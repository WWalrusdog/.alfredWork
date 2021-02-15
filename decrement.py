#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as clip

def increment(example_string):
    example_string = example_string+" "
    digits = ["1","2","3","4","5","6","7","8","9","0"]

    def determineNumberLength(num):
        digits = ["1","2","3","4","5","6","7","8","9","0","."]
        length = 0
        bound = len(num)
        for i in range(bound):
            if num[i] in digits:
                length +=1
            else:
                return length
        return length

    incremented = ""
    i = 0
    while i < len(example_string):
        if example_string[i] in digits:
            numberLength = determineNumberLength(example_string[i:])
            number = example_string[i:(i+numberLength)]
            if "." in number:
                number = float(number)
            else:
                number = int(number)
            number = number-1
            incremented = incremented+str(number)
            i = i+numberLength
        incremented = incremented + example_string[i]
        i = i+1
    return(incremented[:-1])
com=increment(clip.paste())
clip.copy(com)