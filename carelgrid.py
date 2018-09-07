class CarelGrid: 

    def __init__(self, map=None):
        if map is not None:
            self.map = map
        else:
            self.map = [[0 for x in range(6)] for y in range(4)]
            self.map[0][1] = 1
            self.map[1][0] = 2
            self.map[3][2] = 1 #  отрицательное значение построит блок стены

        self.carel_x = 0
        self.carel_y = 0
        self.carel_direction_x = 1
        self.carel_direction_y = 0
        self.carel_dead = False
    

    def  get_width(self): 
        return len(self.map[0])
    
    def  get_height(self): 
        return len(self.map)
  
    def  get_carel_x(self): 
        return self.carel_x
  
    def  get_carel_y(self):
        return self.carel_y
   
    def  get_carel_direction_x(self):
        return self.carel_direction_x
    
    def  get_carel_direction_y(self):
        return self.carel_direction_y
  
    def is_carel_dead(self): 
        return self.carel_dead
    
    def set_carel_x(self, x):
        self.carel_x = x
    

    def set_carel_y(self, y):
        self.carel_y = y
    
    def set_carel_direction_x(self, x):
        self.carel_direction_x = x
    

    def set_carel_direction_y(self, y):
        self.carel_direction_y = y
    
    def set_carel_dead(self, dead):
        self.carel_dead = dead
    
    def place_beeper(self, x, y): 
        self.map[y][x] = self.map[y][x] + 1
    
    def remove_beeper(self, x, y):
        self.map[y][x] = self.map[y][x] - 1
    
    def is_beeper(self, x, y): 
        if (self.map[y][x] <= 0):
            return False
        else:
            return True
    
    def get_beepers_number(self, x, y):
        return self.map[y][x]
    
    def build_wall_block(self):
        return "    \u25A0   "