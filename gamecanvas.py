from IPython.display import display, clear_output
import time
import copy

class GameCanvas:

    def __init__(self, speed=1):
        self.speed = speed    

    def draw(self, grid):
        clear_output(wait=True)
        canvas = self.change_canvas(grid)
        for line in canvas:
            for element in line:
                print(element, end='')
            print('')
        time.sleep(1/self.speed)


    #def change_canvas(self, grid): 
    #    view = []
    #    for i in range(grid.get_height()): 
    #        for j in range(grid.get_width()): 
    #            sector = []
    #            if (j == grid.get_carel_x() and i == grid.get_carel_y()):
    #                sector = self.draw_carel(str(grid.get_beepers_number(j, i)), grid)
    #            elif (grid.get_beepers_number(j,i) < 0):
    #                sector = grid.build_wall_block()
    #            else:
    #                sector = "    " + str(grid.get_beepers_number(j, i)) + "    "
    #            
    #            view += (sector)
    #        view += ("<br>")
    #        #if (i <= grid.get_height() - 2): 
    #        #    view += ("<br>")
    #    return view
    #    #Log.v("CarelDebug", view.getbeepers().toString())

    def change_canvas(self, grid):
        view = copy.deepcopy(grid.map)
        x = grid.get_carel_x()
        y = grid.get_carel_y()
        view[y][x] = self.draw_carel(grid.get_beepers_number(x, y), grid)
        carel_length = len(str(view[y][x]))
        for i, line in enumerate(view):
            for j, element in enumerate(line):
                view[i][j] = self.normalize_length(element, carel_length)
        return view

    def normalize_length(self, element, length):
        additional_length = length - len(str(element))
        if additional_length > 0:
            element = " "*(int(additional_length/2)) + str(element) + " "*(int(additional_length/2))
        else:
            return str(element)
        return element
    

    def draw_carel(self, beepers, grid):
        carel = ""
        beepers = str(beepers)
         
        if (not grid.is_carel_dead()):
            carel = "',(" + beepers + "):"
        else:
            carel = "',(" + beepers + ")%"

        carel_head = ""

        if (grid.get_carel_direction_x() == 1):
            carel_head = ">"
        elif (grid.get_carel_direction_x() == (-1)):
            carel_head = "<"
        elif (grid.get_carel_direction_y() == -1):
            carel_head = "^"
        elif (grid.get_carel_direction_y() == 1):
            carel_head = "v"

        return carel + carel_head