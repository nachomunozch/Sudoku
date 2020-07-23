import pygame
pygame.init()

screen = (600, 500)
win = pygame.display.set_mode(screen)
pygame.display.set_caption("Sudoku!")

red = (255, 0, 0)
black = (0, 0, 0)
grey = (210, 210, 210)
blue = (0, 0, 255)
green = (0, 255, 0)

clock = pygame.time.Clock()

font = pygame.font.SysFont("Gill Sans MT (Body)", 50)
font2 = pygame.font.SysFont("comicsans", 25)
text_button = font2.render("Resolve",1,black)
text_next = font2.render("Play Next", 1, black)


rows = {}
columns = {}
cuadrants = {}
d = {}
cells = []
cellCount = 0
w = 0
modifying = ""


class Cell:

    def __init__(self, row, column, value):

        self.column = column
        self.row = row
        self.key = str(w)+str(row)+str(column)
        self.color = black

        self.visible = False
        self.modifiable = True
        self.modic = False
        self.done = False

        if self.row <= 3 and self.column <= 3:
            self.cuadrante = 1
        elif self.row <= 3 and self.column <= 6:
            self.cuadrante = 2
        elif self.row <= 3 and self.column <= 9:
            self.cuadrante = 3
        elif self.row <= 6 and self.column <= 3:
            self.cuadrante = 4
        elif self.row <= 6 and self.column <= 6:
            self.cuadrante = 5
        elif self.row <= 6 and self.column <= 9:
            self.cuadrante = 6
        elif self.row <= 9 and self.column <= 3:
            self.cuadrante = 7
        elif self.row <= 9 and self.column <= 6:
            self.cuadrante = 8
        elif self.row <= 9 and self.column <= 9:
            self.cuadrante = 9

        self.value = value
        self.correct_value = 0
        self.posible_values = []

        if self.value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

            self.correct_value = self.value
            self.done = True

            self.modifiable = False
            self.imposible_values = []
            self.posible_values = []

            for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                if n != self.value:
                    self.imposible_values.append(n)
                if n == self.value:
                    self.posible_values.append(n)


            rows[self.row].append(self.value)
            columns[self.column].append(self.value)
            cuadrants[self.cuadrante].append(self.value)

        else:
            self.imposible_values = []
            self.posible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


    def draw(self):
        global modifying

        if pos[0] > (self.column * 50) - 50 and pos[0] < self.column * 50 and pos[1] > (self.row * 50) - 50 and pos[1] < self.row * 50:
            pygame.draw.rect(win, grey, (self.column * 50, self.row * 50, -50, -50), 3)

        if self.value != self.correct_value:
            self.color = red
        else:
            self.color = black

        if self.value != 0:
            self.text = font.render(str(self.value), 1, self.color)
            win.blit(self.text, (17+(50*(self.column-1)), 12+(50*(self.row-1))))

        if click[0] > (self.column * 50) - 50 and click[0] < self.column * 50 and click[1] > (self.row * 50) - 50 and click[1] < self.row * 50:
            if self.modifiable:
                pygame.draw.rect(win, blue, (self.column * 50, self.row * 50, -50, -50), 5)

            modifying = self.key



    def modify(self):

        self.value = int(event.unicode)


    def resolve(self):

        l = []
        for u in self.posible_values:
            l.append(u)

        for x in l:
            if x not in columns[self.column] and x not in rows[self.row] and x not in cuadrants[self.cuadrante]:
                i = 0
                for m in d.keys():
                    if d[m].cuadrante == self.cuadrante and x in d[m].imposible_values and d[m].key != self.key:
                        i += 1
                if i == 8:
                    self.posible_values = [x]
                    self.imposible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    self.imposible_values.pop(self.imposible_values.index(x))
                    break
            else:
                self.imposible_values.append(x)
                self.posible_values.pop(self.posible_values.index(x))

        if len(self.posible_values) == 1:
            self.correct_value = self.posible_values[0]
            self.posible_values = []
            rows[self.row].append(self.correct_value)
            columns[self.column].append(self.correct_value)
            cuadrants[self.cuadrante].append(self.correct_value)
            self.done = True


def draw_grid():

    win.fill((255, 255, 255))

    pygame.draw.line(win, (0, 0, 0), (0, 0), (600, 0), 5)
    pygame.draw.line(win, (0, 0, 0), (0, 0), (0, 500), 5)
    pygame.draw.line(win, (0, 0, 0), (600, 0), (600, 500), 5)
    pygame.draw.line(win, (0, 0, 0), (0, 500), (600, 500), 5)

    pygame.draw.line(win, (0, 0, 0), (50, 0), (50, 450), 2)
    pygame.draw.line(win, (0, 0, 0), (100, 0), (100, 450), 2)
    pygame.draw.line(win, (0, 0, 0), (150, 0), (150, 450), 5)
    pygame.draw.line(win, (0, 0, 0), (200, 0), (200, 450), 2)
    pygame.draw.line(win, (0, 0, 0), (250, 0), (250, 450), 2)
    pygame.draw.line(win, (0, 0, 0), (300, 0), (300, 450), 5)
    pygame.draw.line(win, (0, 0, 0), (350, 0), (350, 450), 2)
    pygame.draw.line(win, (0, 0, 0), (400, 0), (400, 450), 2)
    pygame.draw.line(win, (0, 0, 0), (450, 0), (450, 450), 5)

    pygame.draw.line(win, (0, 0, 0), (0, 50), (450, 50), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 100), (450, 100), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 150), (450, 150), 5)
    pygame.draw.line(win, (0, 0, 0), (0, 200), (450, 200), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 250), (450, 250), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 300), (450, 300), 5)
    pygame.draw.line(win, (0, 0, 0), (0, 350), (450, 350), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 400), (450, 400), 2)
    pygame.draw.line(win, (0, 0, 0), (0, 450), (450, 450), 5)


def draw_buttons():

    pygame.draw.rect(win,grey,(475,25,100,50),0)
    if pos[0] > 475 and pos[0] < 575 and pos[1] > 25 and pos[1] < 75:
        pygame.draw.rect(win, blue, (475, 25, 100, 50), 0)
    win.blit(text_button, (494,42))

    pygame.draw.rect(win,grey,(475,100,100,50),0)
    if pos[0] > 475 and pos[0] < 575 and pos[1] > 100 and pos[1] < 150:
        pygame.draw.rect(win,blue,(475,100,100,50),0)
    win.blit(text_next,(488,42+75))

    return


def redrawGameWindow():


    draw_grid()
    draw_buttons()
    for n in d.keys():
        d[n].draw()


    pygame.display.update()
    return


sudokus = [[[5, 3, 0,  0, 7, 0,  0, 0, 0],
            [6, 0, 0,  1, 9, 5,  0, 0, 0],
            [0, 9, 8,  0, 0, 0,  0, 6, 0],

            [8, 0, 0,  0, 6, 0,  0, 0, 3],
            [4, 0, 0,  8, 0, 3,  0, 0, 1],
            [7, 0, 0,  0, 2, 0,  0, 0, 6],

            [0, 6, 0,  0, 0, 0,  2, 8, 0],
            [0, 0, 0,  4, 1, 9,  0, 0, 5],
            [0, 0, 0,  0, 8, 0,  0, 7, 9]],

            [[6,8,5,1,3,0,0,4,7],
             [7,0,0,0,0,0,0,1,0],
             [0,1,0,7,6,4,0,5,0],
             [9,0,0,0,7,0,5,0,4],
             [8,0,1,0,0,9,0,7,2],
             [4,0,3,0,0,6,0,0,0],
             [0,0,0,4,2,7,3,9,0],
             [0,4,0,9,0,0,0,6,8],
             [1,0,7,0,0,0,4,0,0]],

           [[0,0,7,0,1,0,0,0,5],
            [0,0,0,2,0,0,0,0,0],
            [5,0,1,9,8,4,0,7,0],
            [4,0,0,0,3,0,7,0,1],
            [0,1,8,7,0,5,6,9,0],
            [7,5,0,0,0,0,0,0,0],
            [9,6,2,0,7,8,0,1,0],
            [0,0,5,4,0,9,3,0,0],
            [3,0,4,0,6,1,8,0,9]]]


def initialize(sudoku):

    global cells, d, w, rows,columns, cuadrants, run, congratulations
    w += 1
    congratulations = 0

    rows = {x: [] for x in range(1, 10)}
    columns = {x: [] for x in range(1, 10)}
    cuadrants = {x: [] for x in range(1, 10)}

    d = {}
    for row in range(1, 10):
        for column in range(1, 10):
            d[str(w)+str(row)+str(column)] = Cell(row, column, sudoku[row-1][column-1])

    cells = []
    for key in d.keys():
        cells.append(d[key])

    c = 0
    check_if_solvable = 0
    while c < 81 and check_if_solvable < 100:
        c = 0
        check_if_solvable += 1
        for key in d.keys():
            if d[key].done:
                c += 1
            else:
                d[key].resolve()
    if check_if_solvable >= 100:
        run = False
    return

s = 0
initialize(sudokus[s])
click = (0,0)
resolveAll = False
run = True
while run:

    clock.tick(30)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            click = (mx,my)
            mod = False
            if mx > 0 and mx < 450 and my > 0 and my < 450:
                mod = True
        if event.type == pygame.KEYDOWN:
            if event.unicode in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                if d[modifying].modifiable:
                    d[modifying].modify()
                    old_mod = modifying
            if event.unicode == " ":
                for key in d.values():
                    del key

    if click[0] > 475 and click[0] < 575 and click[1] > 25 and click[1] < 75:
        resolveAll = True

    if resolveAll:
        cellCount += 50
        cells[cellCount//81].value = cells[cellCount//81].correct_value
        if cellCount > 80*81:
            resolveAll = False
            cellCount = 0

    if click[0] > 475 and click[0] < 575 and click[1] > 100 and click[1] < 150:
        click = (0, 0)
        if s >= len(sudokus)-1:
            s = 0
        else:
            s += 1
        initialize(sudokus[s])
        resolveAll = False
        cellCount = 0

    redrawGameWindow()

pygame.quit()
