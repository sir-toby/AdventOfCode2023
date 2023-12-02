class Draw:
    redMax = 12
    greenMax = 13
    blueMax = 14

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return (
            "red: "
            + str(self.red)
            + ", green: "
            + str(self.green)
            + ", blue: "
            + str(self.blue)
        )

    def isValid(self):
        if (
            self.red <= self.redMax
            and self.green <= self.greenMax
            and self.blue <= self.blueMax
        ):
            return True
        else:
            return False


class Game:
    def __init__(self, id, draws):
        self.id = id
        self.draws = [Draw(draw["red"], draw["green"], draw["blue"]) for draw in draws]

    def __str__(self):
        returnString = "Game-Id: " + str(self.id) + ", draws: \n"
        for draw in self.draws:
            returnString = returnString + draw.__str__() + "\n"
        return returnString

    def isValid(self):
        for draw in self.draws:
            if draw.isValid() == False:
                return False
        return True

    def calculatePower(self):
        redMax = blueMax = greenMax = 0
        for draw in self.draws:
            if draw.red > redMax:
                redMax = draw.red
            if draw.blue > blueMax:
                blueMax = draw.blue
            if draw.green > greenMax:
                greenMax = draw.green
        return redMax * blueMax * greenMax


def main(inputFile):
    gameList = importFile(inputFile)
    print(part1(gameList))
    print(part2(gameList))


def part1(gameList):
    validGameSum = 0
    for game in gameList:
        if game.isValid():
            validGameSum += game.id
    return validGameSum


def part2(gameList):
    gamePowerSum = 0
    for game in gameList:
        gamePowerSum += game.calculatePower()
    return gamePowerSum


def importFile(inputFile):
    with open(inputFile, "r") as f:
        gameList = []
        for line in f:
            gameList.append(importLine(line))
            print(gameList[-1])
        return gameList


def importLine(line):
    draws = []
    gameId = int(line[line.find("Game ") + 5 : line.find(":")])
    drawsRaw = line[line.find(":") + 2 :].split("; ")
    for draw in drawsRaw:
        drawOutput = {"red": 0, "green": 0, "blue": 0}
        draw = draw.split(", ")
        for color in draw:
            for x in drawOutput.keys():
                try:
                    drawOutput[x] = int(color[: color.index(x) - 1])
                except:
                    pass
        draws.append(drawOutput)
    return Game(gameId, draws)


if __name__ == "__main__":
    inputFile = "./day02/input/input.txt"
    main(inputFile)
