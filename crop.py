import random

class Crop:
    """A generic food crop"""

    #constructor
    def __init__(self,growth_rate, light_need, water_need):
        #set attributes with an intial value
        
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        #underscore to indicate it is private

    def needs(self):
        #return a dictionary containing the light and water needs
        return {'light need':self._light_need,'water need':self._water_need}

    #method to report the current state of a cro[
    def report(self):
        #return a dictionary containing the type, status, growth and days growing
        return {'type':self._type,'status':self._status,'growth':self._growth,'days growing':self._days_growing}
    
    def update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"
    
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
            #increment number of days growing
            self._days_growing += 1
            #update the status of crop
            self.update_status()
            
def auto_grow(crop, days):
    #grow the crop
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)


def main():
    #intialise the class
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())
    auto_grow(new_crop,30)
    print(new_crop.report())
    
if __name__ == "__main__":
    main()
