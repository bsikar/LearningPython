# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:   Evan Slyter
# Section:   565
# Assignment: 7.28 LAB: Kaprekar's Constant
# Date: 10/17/22

# does Kaprekar's routine to a number
def routine(num):
    user_list = list(num)

    user_listA = user_list[:]
    user_listA.sort()
    user_listB = user_list[:]
    user_listB.sort(reverse=True)

    numA = int("".join(user_listA))
    numB = int("".join(user_listB))

    return abs(numA - numB)


def check_length(number):
    if (len(str(number))) > 4:
        print("that number is too big")
        exit()

    elif (len(str(number))) < 4:
        number = str(number).zfill(4)
        return number
    else:
        return number


# input
user_num = input("Enter a four-digit integer: ")

kap_num = user_num
kap_num = check_length(kap_num)

count = 0

if kap_num[0] == kap_num[1] and kap_num[1] == kap_num[2] and kap_num[2] == kap_num[3]:
    print(f"{kap_num} > 0")
    print(f"{kap_num} reaches 0 via Kaprekar's routine in {count+1} iterations")
    exit()


# prints the first part
print(f"{int(user_num)} >", end=" ")

# prints the number for each iteration of Kaprekar's routine
while int(kap_num) != 6174:
    kap_num = routine(str(kap_num))
    count += 1
    if kap_num != 6174:
        print(f"{int(kap_num)} >", end=" ")
    else:
        print(f"{int(kap_num)}")
    kap_num = check_length(kap_num)

print(f"{int(user_num)} reaches 6174 via Kaprekar's routine in {count} iterations")
