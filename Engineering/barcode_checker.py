# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 11.11 LAB: Barcode Checker
# Date: 11/11/22

# inputs and variables
filename = input("Enter the name of the file: ")
barcodes_file = open(filename, "r")

barcodes = barcodes_file.read()
barcodes = barcodes.split("\n")
barcode = 0

# removes non valid barcodes
while barcode < len(barcodes):
    x = 0
    sum1 = 0
    sum2 = 0
    lastdigit = int(str(barcodes[barcode])[-1])
    splits = [[], []]

    for x in range(0, len(barcodes[barcode]) - 1, 2):
        splits[0].append(int(barcodes[barcode][x]))
        splits[1].append(int(barcodes[barcode][x + 1]))

    sum1 = sum(splits[0])
    sum2 = sum(splits[1]) * 3

    sum1 = sum1 + sum2
    sum1 = int(str(sum1)[-1])
    sum1 = 10 - sum1

    if sum1 != lastdigit:
        barcodes.pop(barcode)
        barcode = 0
        continue
    barcode += 1

print(f"There are {len(barcodes)} valid barcodes")

barcodes_file.close()

# writes good barcodes to new file
good_barcodes = open("valid_barcodes.txt", "w")
for barcode in barcodes:
    good_barcodes.write(barcode)
    good_barcodes.write("\n")

good_barcodes.close()
