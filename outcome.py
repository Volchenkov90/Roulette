class Outcome:
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        if self.name == other.name and self.odds == other.odds:
            return True
        else:
            return False
    
    def __ne__(self, other):
        if self.name != other.name or self.odds != other.odds:
            return True
        else:
            return False

o1 = Outcome("Red", 1)
o2 = Outcome("Red", 1)

print(o1 == o2)


    