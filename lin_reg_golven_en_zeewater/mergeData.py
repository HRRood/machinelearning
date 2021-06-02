from os import listdir
from os import path
import os
import gzip

def showProgress(counter, total, message):
    percentage = round(100 * counter / total)
    output = message + ": "
    for i in range(0, percentage):
        output += "█"
    for i in range(percentage, 100):
        output += "-"
    os.system('cls')
    print(output)

dir = r"C:\Users\Marcus\OneDrive - De Haagse Hogeschool\Advanced Databases\Big_Data\Week 15\Opdracht 3 - KNMI\data\golven_en_zeewater\small_set"
mergeFile = path.join(dir, "dataMerged.gz")

newFile = gzip.open(mergeFile, "w")
counter = 0

for f in listdir(dir):
    counter += 1
    smallFile = gzip.open(path.join(dir, f) , "rt")
    newFile.write(smallFile.read().encode())
    smallFile.close()
    showProgress(counter, len(listdir(dir)), "Building combined data file")

newFile.close()


