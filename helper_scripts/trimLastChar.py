import os
t = open(r"C:\Users\Marcus\OneDrive - De Haagse Hogeschool\Advanced Databases\Big_Data\Week 15\Opdracht 3 - KNMI\data\golven_en_zeewater\dataMerged.txt", "r")
f = open(r"C:\Users\Marcus\OneDrive - De Haagse Hogeschool\Advanced Databases\Big_Data\Week 15\Opdracht 3 - KNMI\data\golven_en_zeewater\dataMergedClean.txt", "w")
lines = t.readlines()
for i in lines:
    i = i[:-2] + "\n"
    f.write(i)

t.close()
f.close()




