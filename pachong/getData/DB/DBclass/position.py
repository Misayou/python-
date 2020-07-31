class Position:
    id = None
    positionName = ''

    def __init__(self, id, positionName):
        self.id = id
        self.positionName = positionName


    def __str__(self):
        return str(self.id)+' '+self.positionName
