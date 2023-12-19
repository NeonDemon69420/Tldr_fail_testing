import os

f = open("OutText.txt", "r")
text = f.readline()
text = f.readline()
text = f.readline()
text = f.readline()
f.close()

list = ""

for i in range(29, len(text)):
    list += text[i]

actual_list = eval(list)

for item in actual_list:
    command = "python3 tldr_fail_test.py " + item
    os.system(command=command)
