openFile = open("mod12activity.txt", "r")

letters = openFile.read()
letters = letters.split("\n")


B = [letters[0], letters[5], letters[10], letters[15], letters[20]]
I = [letters[1], letters[6], letters[11], letters[16], letters[21]]
N = [letters[2], letters[7], letters[12], letters[17], letters[22]]
G = [letters[3], letters[8], letters[13], letters[18], letters[23]]
O = [letters[4], letters[9], letters[14], letters[19], letters[24]]

message = input("message: ")

answer = ""

for x in range(len(message)):
    if message[x] == "B":
        answer = answer + B[(int(message[x + 1]) - 1)]
    elif message[x] == "I":
        answer = answer + I[(int(message[x + 1]) - 1)]
    elif message[x] == "N":
        answer = answer + N[(int(message[x + 1]) - 1)]
    elif message[x] == "G":
        answer = answer + G[(int(message[x + 1]) - 1)]
    elif message[x] == "O":
        answer = answer + O[(int(message[x + 1]) - 1)]
print(answer)
