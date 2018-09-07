class Carel:

    def __init__(self, game_canvas, grid):
        self.grid = grid
        self.x = grid.get_carel_x()
        self.y = grid.get_carel_y()
        self.direction_x = grid.get_carel_direction_x()
        self.direction_y = grid.get_carel_direction_y()
        self.dead = grid.is_carel_dead()
        self.game = game_canvas
        self.game.draw(self.grid)
    
    def show(self):
        self.game.draw(self.grid)

    def move(self):
        self.x += self.direction_x
        self.y += self.direction_y
        if self.is_out_of_bounds(self.x, self.y): 
            self.die()            
        self.update()
           

    def turn_left(self):

        if self.direction_x == 0:
            self.direction_x = self.direction_y
            self.direction_y = 0
        else:
            self.direction_y = self.direction_x * (-1)
            self.direction_x = 0
        
        self.update()        
    

    def drop_beeper(self): 
        if not self.dead:
            self.grid.place_beeper(self.x, self.y)
            self.update()        
    

    def collect_beeper(self): 
        if not self.dead:
            if self.is_beeper(): 
                self.grid.remove_beeper(self.x, self.y)
            else:
                self.die()
            self.update()
        
    

    def is_beeper(self): 
        if self.grid.is_beeper(self.x, self.y): 
            return True
        else:
            return False
    

    def is_front_clear(self):
        frontX = self.x + self.direction_x
        frontY = self.y + self.direction_y

        if self.is_out_of_bounds(frontX, frontY): 
            return False
        else:
            return True
    

    def update(self):
        self.grid.set_carel_dead(self.dead)
        if not self.dead: 
            self.grid.set_carel_x(self.x)
            self.grid.set_carel_y(self.y)        
            self.grid.set_carel_direction_x(self.direction_x)
            self.grid.set_carel_direction_y(self.direction_y)
        self.game.draw(self.grid)
    

    def die(self): 
        self.dead = True
    

    def is_out_of_bounds(self, x, y): 
        if (x >= self.grid.get_width() or y >= self.grid.get_height() or x<0 or y<0 or self.grid.get_beepers_number(x , y) < 0):
            return True
        else:
            return False