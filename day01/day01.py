def main(inputFile): 
    with open(inputFile,'r') as myfile: 
        inputList = myfile.readlines()
    print(inputList)
    print(part1(inputList))
    print(part2(inputList))


def part1(inputList):
    valueList = []
    for line in inputList: 
        first = firstDigit(line)
        last = lastDigit(line)
        #print(first, last)
        valueList.append(int(str(first)+str(last)))
    return sum(valueList)

def part2(inputList):
    searchterms = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    valueList = []
    for line in inputList:
        first = findLeft(line, searchterms)
        last = findRight(line, searchterms)
        valueList.append(int(str(first)+str(last)))
    return sum(valueList)

def findLeft(line, searchterms):
    finds = {s: (line.find(s) if line.find(s)>=0 else 99) for s in searchterms}
    lowest = sorted(finds.items(), key= lambda x: x[1])[0]
    return searchterms[lowest[0]]

def findRight(line, searchterms): 
    finds = {s: line.rfind(s) for s in searchterms}
    highest = sorted(finds.items(), key= lambda x: x[1], reverse=True)[0]
    return searchterms[highest[0]]

def firstDigit(string):
    for i in range(len(string)):
        try: return int(string[i])
        except: pass

def lastDigit(string): 
    for i in range(len(string)-1, -1, -1): 
        try: return int(string[i])
        except: pass

if __name__ == "__main__":
    inputFile = './input/input.txt'
    main(inputFile)