def long_repeat(line):
    count = 0
    countList = []
    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            count += 1    
            countList.append(count)
        else:
             countList.append(count)
            count = 0    
    return max(countList) + 1