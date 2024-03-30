class Sparklers:

    def __init__(self, b1, c1):
        self.neededToCreate2 = b1
        self.count = c1
    
    def efficientUseTime(self):
        T = 0
        extinct = 0
        while self.count > 0:
            self.count -= 1
            extinct += 1
            T += 2
            if extinct >= self.neededToCreate2:
                self.count += 2
                extinct -= self.neededToCreate2
            
        return T
    

c1 = 100
b1 = 7
Igor = Sparklers(b1, c1)

print('Огни горели', Igor.efficientUseTime(), 'часов')