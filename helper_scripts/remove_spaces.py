import os

def showProgress(counter, total, message):
    percentage = round(100 * counter / total)
    output = message + ": "
    for i in range(0, percentage):
        output += "█"
    for i in range(percentage, 100):
        output += "-"
    output += (" {}/{}".format(counter, total))
    os.system('cls')
    print(output)

f = open(r"D:\GitHub\machinelearning\lelijk_weer_MvL\data\lelijk_weer_MvL.csv", "r")
t = open(r"D:\GitHub\machinelearning\lelijk_weer_MvL\data\lelijk_weer_MvL_no_spaces.csv", "w")
lines = f.readlines()
for i in range(len(lines)):
    l = lines[i]
    l = l.replace(' ', '')
    t.write(l)
    showProgress(i, len(lines), "Removing spaces")

f.close()
t.close()

