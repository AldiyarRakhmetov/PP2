import pygame as pg
import math

# Initialize Pygame and other starting vals (Lab 8)
pg.init()
running = True
WIDTH, HEIGHT = 1080, 1080
screen  = pg.display.set_mode((WIDTH, HEIGHT))
pg.font.init()

font = pg.font.SysFont("Comic Sans MC", 30)

UIcolor = [
    (0, 0, 0),        # Border 
    (255, 255, 255), # Folder
    (93, 145, 163), # Background
    (96, 173, 117) # Environment  (Lab 8)
]

ColorForDraw = {
    "Black"  :  (0, 0, 0),
    "Red"    :  (255, 0, 0),
    "Green"  :  (0, 255, 0),
    "Blue"   :  (0, 0, 255),
    "Yellow" :  (255, 255, 0),
    "White"  :  (255, 255, 255),
    "Pink"   :  (255, 0, 255),
    "Silver" :  (100, 100, 100),
    "Brown"  :  (185, 122, 87),
    "Orange" :  (255, 127, 39)
}

# The drawer itself (Lab 8)
class MAIN_FOLDER :
    def __init__(self):
        self.folder = pg.Surface((980, 1080))
        self.folder.fill(UIcolor[1])

        self.drawing   = False #Checking wether we draw or not (Lab 8)
        self.start_pos = None  # Starting position for shapes (Lab 8)

    def drawfolder(self):
        screen.blit(self.folder, (100, 0))

    def core(self, pos, mode, color):
        pos = (pos[0] - 100, pos[1])
        # Eraser (Lab 8)
        if mode == "eraser" and self.start_pos:
            pg.draw.circle(self.folder, UIcolor[1], pos, 10)
        
        # Circle (Lab 8)
        if mode == "circle" and self.start_pos:
            radious = max(abs(pos[0] - self.start_pos[0]), (pos[1] - self.start_pos[1]))
            pg.draw.circle(self.folder, color, self.start_pos, radious, 5)
        
        # Rectangle (Lab 8)
        if mode == "rect" and self.start_pos:
            rect = pg.Rect(*self.start_pos, pos[0] - self.start_pos[0], pos[1] - self.start_pos[1])
            pg.draw.rect(self.folder, color, rect, 5)

        # Pen (Lab 8)
        if mode == "pen" and self.start_pos:
            pg.draw.circle(self.folder, color, pos, 10)

        # Square (Lab 9)
        if mode == "square" and self.start_pos:
            pg.draw.rect(self.folder, helper.current_color, pg.Rect(self.start_pos[0], self.start_pos[1], helper.current_length, helper.current_length))
        
        # Right triangle (Lab 9)
        if mode == "right_tran" and self.start_pos:
            point1 = self.start_pos
            point2 = (pos[0], self.start_pos[1])
            point3 = (self.start_pos[0], pos[1])
            pg.draw.polygon(self.folder, helper.current_color, [point1, point2, point3], 5)
        
        # Equilateral triangle (Lab 9)
        if mode == "equiv_tran" and self.start_pos: 
            base_length = abs(pos[0] - self.start_pos[0])
            height = (math.sqrt(3) / 2) * base_length
            point1 = ((self.start_pos[0] + pos[0]) // 2, self.start_pos[1] - height)
            point2 = self.start_pos
            point3 = (pos[0], self.start_pos[1])
            pg.draw.polygon(self.folder, helper.current_color, [point1, point2, point3])
        
        # Rhombus (Lab 9)
        if mode == "romb" and self.start_pos:
            center_x, center_y = self.start_pos
            point1 = (center_x, center_y - helper.current_length)
            point2 = (center_x + helper.current_length, center_y)
            point3 = (center_x, center_y + helper.current_length)
            point4 = (center_x - helper.current_length, center_y)
            pg.draw.polygon(self.folder, helper.current_color, [point1, point2, point3, point4])

# Toolbar/helper class for controls (Lab 8)
class HELPER_FOLDER:
    def __init__(self):
        self.current_color  = ColorForDraw["Black"] 
        self.current_mode   = "pen"                 
        self.current_length = 50           

        # Buttons and their icons (Lab 8/9)
        self.eraser_but = pg.Rect(10, 10, 30, 30)                         
        self.rect_but   = pg.Rect(10, 85, 40, 30)                         
        self.circle_but = pg.Rect(10, 40, 40, 40)                        
        self.pen_but    = pg.Rect(10, 125, 30, 30)                        
        self.square_but = pg.Rect(10, 175, 30, 30)                        
        self.right_tran = pg.Rect(10, 225, 40, 40)                        
        self.points_rtran = [(10, 270), (10, 230), (40, 270)]             
        self.equiv_tran = pg.Rect(50, 225, 40, 40)                        
        self.points_etran = [(50, 270), (65, 230), (80, 270)]             
        self.pluse_but  = pg.Rect(50, 175, 30, 30)                        
        self.pluse_points = [(50, 190), (80, 190), (65, 175), (65, 205)]  
        self.minus_but  = pg.Rect(50, 125, 30, 30)                        
        self.minus_points = [(50, 140), (80, 140)]                        
        self.rombulus_b = pg.Rect(50, 10, 30, 30)                         
        self.romb_points  = [(50, 25), (65, 10), (80, 25), (65, 40)]     

        # Color selection (Lab 8)
        self.color_list = []
        cash = 1
        cash_x, cash_y = 0, (HEIGHT - 500) // 2
        cash_x1 = 50
        for color in ColorForDraw:
            if cash < 6:
                rect = pg.Rect(cash_x, cash_y, 50, 50) 
                self.color_list.append((rect, ColorForDraw[color]))
                cash += 1
                cash_y += 50
            else:
                cash_y -= 50
                rect = pg.Rect(cash_x1, cash_y, 50, 50) 
                self.color_list.append((rect, ColorForDraw[color]))
        
    # UI (Lab 8)
    def drawfolder(self):
        pg.draw.rect(screen, UIcolor[2], pg.Rect(0, 0, WIDTH, HEIGHT))
        pg.draw.rect(screen, UIcolor[3], pg.Rect(0, (HEIGHT - 500) // 2, 100, 250)) 
        for rect, color in self.color_list:
            pg.draw.rect(screen, color, rect)

        self.show_lenght    = font.render(f"{self.current_length / 5}", True, UIcolor[0])
        screen.blit(self.show_lenght, (50, 90))
        # Drawing icons (Lab 8/9)
        pg.draw.rect(screen, UIcolor[1], self.eraser_but)      
        pg.draw.circle(screen, UIcolor[0], (25, 65), 15, 5)    
        pg.draw.rect(screen, UIcolor[0], self.rect_but, 5)     
        pg.draw.rect(screen, UIcolor[0], self.pen_but)        
        pg.draw.rect(screen, UIcolor[0], self.square_but, 5)    
        pg.draw.polygon(screen, UIcolor[0], self.points_rtran)  
        pg.draw.polygon(screen, UIcolor[0], self.points_etran)  
        pg.draw.polygon(screen, UIcolor[0], self.romb_points)  
        pg.draw.line(screen, UIcolor[0], self.pluse_points[0], self.pluse_points[1], 5)  
        pg.draw.line(screen, UIcolor[0], self.pluse_points[2], self.pluse_points[3], 5)  
        pg.draw.line(screen, UIcolor[0], self.minus_points[0], self.minus_points[1], 5) 

    # click identification thingy (Lab 8)
    def get_color_and_mode(self, pos):
        for rect, color in self.color_list:
            if rect.collidepoint(pos): 
                self.current_color = color

        if self.eraser_but.collidepoint(pos): self.current_mode = "eraser"
        if self.rect_but.collidepoint(pos):   self.current_mode = "rect"
        if self.circle_but.collidepoint(pos): self.current_mode = "circle"
        if self.pen_but.collidepoint(pos):    self.current_mode = "pen"
        if self.square_but.collidepoint(pos): self.current_mode = "square"
        if self.right_tran.collidepoint(pos): self.current_mode = "right_tran"
        if self.equiv_tran.collidepoint(pos): self.current_mode = "equiv_tran"
        if self.rombulus_b.collidepoint(pos): self.current_mode = "romb"
        if self.pluse_but.collidepoint(pos):  self.current_length += 10  
        if self.minus_but.collidepoint(pos) and self.current_length >= 10:  self.current_length -= 10 


helper = HELPER_FOLDER()
folder = MAIN_FOLDER()


while running:
    screen.fill(UIcolor[2])


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button specifically (Lab 8)
                if event.pos[0] > 100:  
                    folder.drawing = True
                    folder.start_pos = (event.pos[0] - 100, event.pos[1])
                else: 
                    helper.get_color_and_mode(event.pos)
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  
                folder.drawing = False
        elif event.type == pg.MOUSEMOTION:
            if folder.drawing:  
                folder.core(event.pos, helper.current_mode, helper.current_color)


    helper.drawfolder()
    folder.drawfolder()  
    pg.display.flip()     