"""
Render a map image file --- Not Implemented
Zoom in and out ----------- Not Implemented
View switch for map ------- Not Implemented
> Set Boundries by Pixel -- Not Implemented
> Place Towns ------------- Not Implemented
> Place Cities ------------ Not Implemented
> Place Landmarks --------- Not Implemented
> City View --------------- Not Implemented
> Nation View ------------- Not Implemented
> Region View ------------- Not Implemented
> Landmark View ----------- Not Implemented
Data recovery from click -- Not Implemented
> Name Recovery ----------- Not Implemented
> Description Recovery ---- Not Implemented
Save as a readable File --- Not Implemented
> Save in a formant ------- Not Implemented
> Reading Program --------- Not Implemented
"""

import random
import pygame
import sys
import math

pygame.init()

city_icon = None # add city icon
town_icon = None # add town icon
map_frame = pygame.image.load(".\\frame.png")
map_filename = None
interactive_map_file = None
screen = pygame.display.set_mode((1200, 700))
base_font = pygame.font.Font(None, 32) 
map_view = "City"

class Landmark:
    def __init__(self, icon, x, y, name, description):
        self.icon = icon
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.visible = True

    def toggle_visiblity(self):
        self.visible = not(self.visible)

class City(Landmark):
    def __init__(self, x, y, name, description, government_type=None, nation=None, religion="free"):
        super.__init__(city_icon, x, y, name, description)
        self.government_type = government_type
        self.nation = nation
        self.religion = religion

class Town(Landmark):
    def __init__(self, x, y, name, description, nation):
        super.__init__(town_icon, x, y, name, description)
        self.nation = nation

class Region:
    def __init__(self, name, description, color, pixels=[]):
        self.name = name
        self.description = description
        self.color = color
        self.pixels = pixels

    def add(self, pair):
        if pair not in self.pixels:
            self.pixels.append(pair)

    def remove(self, pair):
        if pair in self.pixels:
            self.pixels.remove(pair)

class Nation(Region):
    def __init__(self, name, description, government_type, capital, flag, color, pixels=[], religion="free"):
        super.__init__(name, description, color, pixels)
        self.government_type = government_type
        self.capital = capital
        self.flag = flag
        self.pixels = pixels
        self.religion = religion

class User_Input:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.rect = pygame.Rect(x, y, 140, 32)

    def text_input(self, event):
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key != pygame.K_RETURN:
                self.text += event.unicode

    def render(self):
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 1)
        
        text_surface = base_font.render(self.text, True, (0, 0, 0))

        screen.blit(text_surface, (file_input.rect.x+5, file_input.rect.y+5))

        file_input.rect.w = max(100, text_surface.get_width()+10)


file_input = User_Input(200, 200, '')
file_input_active = False
file_gotten = False
start_from_scratch = False
start_from_file = False

#Running Loop:
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if file_gotten == False:

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if file_input.rect.collidepoint(event.pos):
                    file_input_active = True
                else:
                    file_input_active = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("WOW!")
                    file_gotten = True
            
            if file_input_active:
                file_input.text_input(event)
        file_input.render()

    if file_input.text[-4:] == ".png" or file_input.text[-4:] == ".jpg":
        map_filename = file_input.text
    elif file_input.text[-4:] == ".txt":
        interactive_map_file = file_input.text
    else:
        file_gotten = False

    # print(file_input_active)

    if interactive_map_file == None and map_filename != None:
        start_from_scratch = True
    elif interactive_map_file != None and map_filename == None:
        start_from_file = True

    if start_from_scratch:
        map_image = pygame.image.load(".\\" + map_filename)
        interactive_map_file = map_filename[-4:] + ".txt"
        with open(interactive_map_file, "w") as write_file:
            write_file.write(f"--- Map File ---\nMap Image Filename: {map_filename}")
            

    elif start_from_file:
        with open(interactive_map_file, "r") as read_file:
            lines = read_file.readlines()
            map_filename = lines[len("Map Image Filename: "):]
            map_image = pygame.image.load(".\\" + map_filename)

    pygame.display.flip()
