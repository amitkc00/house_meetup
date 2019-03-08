import graphics

    # ============= HOUSE BODY =============

class House(object):

    def __init__(self, graphics_window, house_x_left, house_distance_from_bottom, house_width, house_height):
        # define house bottom left and height and width
        self.spec = {}
        self.spec['house_x_left'] = house_x_left
        self.spec['house_distance_from_bottom'] = house_distance_from_bottom
        self.spec['house_width'] = house_width
        self.spec['house_height'] = house_height
        self.graphics_window = graphics_window


    def calculate_spec(self):
        self.spec['house_y_bottom'] = self.graphics_window.height - self.spec['house_distance_from_bottom']
        self.spec['house_x_center'] = self.spec['house_x_left']  + self.spec['house_width']/2

        # def createHouse
        # based on above, calculate house top right which is needed to create rectangle
        self.spec['house_x_right'] = self.spec['house_x_left'] + self.spec['house_width']
        self.spec['house_y_top'] = self.spec['house_y_bottom'] - self.spec['house_height'] 


        # calculate three points for the roof
        self.spec['house_x_bottom'] = self.graphics_window.height - self.spec['house_distance_from_bottom']
        self.spec['roof_height'] = 50
        self.spec['roof_left_point'] =  graphics.Point (self.spec['house_x_left'], self.spec['house_y_top'])
        self.spec['roof_right_point'] = graphics.Point(self.spec['house_x_right'], self.spec['house_y_top'])
        self.spec['roof_top_y'] = self.spec['house_y_top'] - self.spec['roof_height']
        self.spec['roof_top_point'] = graphics.Point (self.spec['house_x_center'], self.spec['roof_top_y'])


        # calculate door spec
        self.spec['door_height'] = 60
        self.spec['door_width'] = 30
        self.spec['door_x_left'] = self.spec['house_x_center'] - self.spec['door_width']/2
        self.spec['door_x_right'] = self.spec['house_x_center'] + self.spec['door_width']/2
        self.spec['door_top_y'] = self.spec['house_y_bottom'] - self.spec['door_height']


        # calculate window spec
        self.spec['window_width'] = 20
        self.spec['window_height'] = 30
        self.spec['door_space'] = 15

        self.spec['left_window_right_side'] = self.spec['door_x_left'] - self.spec['door_space']
        self.spec['left_window_left_side'] = self.spec['left_window_right_side'] - self.spec['window_width']
        self.spec['right_window_left_side'] = self.spec['door_x_right'] + self.spec['door_space']
        self.spec['right_window_right_side'] = self.spec['right_window_left_side'] + self.spec['window_width']

        self.spec['window_top'] = self.spec['door_top_y']
        self.spec['window_bottom'] = self.spec['door_top_y'] + self.spec['window_height']

        self.spec['left_window_bottom_left'] = graphics.Point(self.spec['left_window_left_side'], self.spec['window_bottom'])
        self.spec['left_window_top_right'] = graphics.Point(self.spec['left_window_right_side'], self.spec['window_top'])


        self.spec['right_window_bottom_left'] = graphics.Point(self.spec['right_window_left_side'], self.spec['window_bottom'])
        self.spec['right_window_top_right'] = graphics.Point(self.spec['right_window_right_side'], self.spec['window_top'])


    def create_body(self):

        p1 =  graphics.Point(self.spec['house_x_left'], self.spec['house_y_bottom'])
        p2 = graphics.Point(self.spec['house_x_right'], self.spec['house_y_top'])

        # draw main rectangle of house
        self.body = graphics.Rectangle(p1,p2)
        self.body.setFill("pink")


    def create_roof(self):
        # ============= HOUSE ROOF =============
        self.roof = graphics.Polygon(self.spec['roof_left_point'], self.spec['roof_right_point'], self.spec['roof_top_point'])
        self.roof.setFill("yellow")


    def create_door(self):
        # ============= HOUSE DOOR =============
        p1 = graphics.Point(self.spec['door_x_left'], self.spec['house_y_bottom'])
        p2 = graphics.Point(self.spec['door_x_right'], self.spec['door_top_y'])
        self.door = graphics.Rectangle(p1,p2)
        self.door.setFill("blue")


    def create_windows(self):
        # ============ WINDOWS ================
        self.left_window = graphics.Rectangle(self.spec['left_window_bottom_left'], self.spec['left_window_top_right'])
        self.left_window.setFill("purple")

        self.right_window = graphics.Rectangle(self.spec['right_window_bottom_left'], self.spec['right_window_top_right'])
        self.right_window.setFill("purple")



    def create_components(self):
    	self.create_body()
    	self.create_roof()
    	self.create_door()
    	self.create_windows()
    	self.components = [self.body, self.roof, self.door, self.left_window, self.right_window]


    #Move house if you wish.
    def move(self, delta_x, delta_y):
        for component in self.components:
            component.move(delta_x, delta_y)


    # ============ DRAW HOUSE COMPONENTS =============
    def draw(self): 
        for component in self.components:
            component.draw(self.graphics_window)


def main():
    # ============= WINDOW ==================
    graphics_window_width = 1200
    graphics_window_height = 600
    graphics_window = graphics.GraphWin("My House", graphics_window_width, graphics_window_height)
    house = House(graphics_window, 100, 50, 200, 100)

    house.calculate_spec()
    house.create_components()
    house.draw()

    # ============ PAUSE FOR CLICK ON WINDOW =============
    graphics_window.getMouse() # pause for click in window
    graphics_window.close()

if __name__ == "__main__":
    main()

