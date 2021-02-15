#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import pyperclip as p
prev_clip = open("/Users/scottmolloy/Desktop/.alfredWork/functions/previous_clip.txt", "r")
content = prev_clip.read()
prev_clip.close()


def specPeak(intact):
    intact = int(intact)
    totalCarbons = 2
    shear = intact - 74
    rem  = shear
    unsaturations = 0
    if rem%14 == 0:
        print("check")
        saturations = int(rem/14)
        totalCarbons = int(totalCarbons+saturations)
        return(f"Total Carbons: {totalCarbons} Unsaturations: {unsaturations} Saturations: {saturations}")
    while rem%14:
        if rem < 0:
            return("Calculation failed")
        unsaturations += 1
        rem = rem - 26
        totalCarbons = totalCarbons + 2
    saturations = int(rem/14)
    totalCarbons = int(totalCarbons+saturations)
    return(f"Total Carbons: {totalCarbons} Unsaturations: {unsaturations} Saturations: {saturations}")

content = specPeak(content)


p.copy(content)