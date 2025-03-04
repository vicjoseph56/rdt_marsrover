import re

class Grid:
    def __init__(self, length, width):
        self.length = length 
        self.width = width 
        self.grid = [['#' for i in range(length+1)] for j in range(width+1)]

    def print_values(self):
        print("Length: " + str(self.length))
        print("Width: " + str(self.width))

    def display_grid(self):
        for row in reversed(self.grid):
            print(row)


class Rover:
    def __init__(self, x, y, curr_dir, grid):
        self.x = int(x)
        self.y = int(y)
        self.curr_dir = curr_dir.upper()
        self.direction_array = ['N','E','S','W']
        self.direction_vectors = {
            'N': (0,1),
            'E': (1,0),
            'S': (0,-1),
            'W': (-1,0)
        }

        self.direction_char = {
            'N': '^',
            'E': '>',
            'S': 'v',
            'W': '<'
        }

        self.grid = grid
        self.grid.grid[self.y][self.x] = self.direction_char[self.curr_dir] ### Stored in y,x because of how arrays are accessed
         
    def print_values(self):
        print("X: " + str(self.x))
        print("Y: " + str(self.y))
        print("Current direction : " + str(self.curr_dir))

    def input_movement(self):
        self.movement_string = input("Enter movement string for rover: ")
        pattern = re.compile("^[LMR]+$", re.IGNORECASE)
        if bool(pattern.match(self.movement_string)) == False:
            print("Invalid movement string")
            exit()

    def move(self):

        movement_array = list(self.movement_string)
        movement_array = [m.upper() for m in movement_array]
        direction_index = self.direction_array.index(self.curr_dir)

        start_x,start_y = self.x,self.y

        for char in movement_array:

            if char == 'L':
                direction_index = direction_index - 1
                if direction_index < 0:
                    direction_index = 3
                self.curr_dir = self.direction_array[direction_index]


            elif char == 'R':
                direction_index = direction_index + 1
                if direction_index > 3:
                    direction_index = 0
                self.curr_dir = self.direction_array[direction_index]

            elif char == 'M':
                #include check for any invalid positioning at any point i.e. over the length/width of grid  
                movement = self.direction_vectors[self.curr_dir]
                self.x += movement[0]
                self.y += movement[1]
                if self.x > 5 or self.x < 0 or self.y > 5 or self.x < 0:
                    print("Rover moved out of bounds!")
                    exit()

            
            print("Location is " + str(self.x) + " " + str(self.y) + " " + self.curr_dir)
        self.grid.grid[self.y][self.x] = self.direction_char[self.curr_dir]
        self.grid.grid[start_y][start_x] = '#'
        self.grid.display_grid()



def verify_coords(input_text):
    pattern = re.compile("([0-9]+( [0-9]+ [NESW]))", re.IGNORECASE)
    print(input_text)
    if bool(pattern.match(input_text)) == False:
        print("Invalid coordinates provided")
        exit()
    else:
        print("Valid coordinates")



grid_dimensions =  input("Enter grid dimensions: ")
grid_tuple = grid_dimensions.split(' ')

try:
    grid_tuple = [int(x) for x in grid_tuple]
except ValueError:
    print("Enter valid integers only")
    exit()



plateau = Grid(grid_tuple[0], grid_tuple[1])
plateau.display_grid()


rover_1_coords = input("Enter coordinates and direction for Rover 1: ")
verify_coords(rover_1_coords)
rover_1_tuple = rover_1_coords.split(' ')
rover_1 = Rover(rover_1_tuple[0], rover_1_tuple[1], rover_1_tuple[2], plateau)

plateau.display_grid()
# movement_string_1 = "LMLMLMLMM"
rover_1.input_movement()
rover_1.move()

rover_2_coords = input("Enter coordinates and direction for Rover 2: ")
verify_coords(rover_2_coords)
rover_2_tuple = rover_2_coords.split(' ')
rover_2 = Rover(rover_2_tuple[0], rover_2_tuple[1], rover_2_tuple[2], plateau)

plateau.display_grid()
# movement_string_2 = "MMRMMRMRRM"
rover_2.input_movement()
rover_2.move()