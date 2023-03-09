myDict = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}

for name, gradeList in myDict.items():
    print(name, sum(gradeList)/len(gradeList))