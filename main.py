class Car(object):
    def __init__(self, color, company, model, speed, mirrors):
        self.color = color
        self.company = company
        self.model = model
        self.speed = speed
        self.mirrors = mirrors or {}

    def getColor(self, color):
        print(self.color)

    # def getMirror(self, color):
    #     return self.mirrors[color]

    # def setMirror(self, color, color_name):
    #     self.mirrors[color] = color_name


audi = Car("red", "audi", "xyz", "100kmp", "leftMirror")

# audi.setMirror("yellow", "leftmirror")
audi.getColor("red")
