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
        
def main():
    #intialise the class
    new_crop = Crop(1,4,3)
    print(new_crop.needs())
    print(new_crop.report())
    
if __name__ == "__main__":
    main()
