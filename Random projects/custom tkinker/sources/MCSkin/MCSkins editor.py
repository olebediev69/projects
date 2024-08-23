from PIL import Image, ImageTk
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import os
import threading
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initialize appearance mode and color theme globally
appearance_mode = 'light'
default_color_theme = 'green'

ctk.set_appearance_mode(appearance_mode)
ctk.set_default_color_theme(default_color_theme)


class MCSkinEditor:

    def __init__(self):
        self.master = tk.Tk()
        self.skin_image = Image.new("RGBA", (64, 64), (255, 255, 255, 0))
        self.initialize_ui()

    def initialize_ui(self):
        self.master.title("MCSkins Editor")
        self.master.geometry('700x700')

        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        self.menu_options = tk.Menu(self.menu)
        self.menu.add_cascade(label='Style', menu=self.menu_options)
        self.menu_options.add_command(
            label='Change Color Theme',
            command=self.change_color_theme
        )
        self.menu_options.add_command(
            label='Show 3D Preview',
            command=self.show_3d_preview
        )

        self.canvas = tk.Canvas(self.master, width=320, height=320, bg="white")
        self.canvas.pack(pady=20)

        self.skin_photo = ImageTk.PhotoImage(self.skin_image.resize((320, 320), Image.NEAREST))
        self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.skin_photo)

        self.canvas.bind("<B1-Motion>", self.draw_on_skin)

        self.master.mainloop()

    def change_color_theme(self):
        global default_color_theme
        default_color_theme = 'blue' if default_color_theme == 'green' else 'green'
        ctk.set_default_color_theme(default_color_theme)

        self.master.destroy()
        self.master = tk.Tk()
        self.initialize_ui()

        print(f"Color theme changed to: {default_color_theme}")

    def draw_on_skin(self, event):
        x, y = event.x // 5, event.y // 5
        if 0 <= x < 64 and 0 <= y < 64:
            self.skin_image.putpixel((x, y), (255, 0, 0, 255))  # Draw red pixel
            self.update_canvas()

    def update_canvas(self):
        self.skin_photo = ImageTk.PhotoImage(self.skin_image.resize((320, 320), Image.NEAREST))
        self.canvas.itemconfig(self.canvas_image, image=self.skin_photo)

    def save_skin(self):
        self.skin_image.save("skin.png")

    def show_3d_preview(self):
        self.save_skin()
        thread = threading.Thread(target=launch_3d_viewer)
        thread.start()


def launch_3d_viewer():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    texture_id = load_texture()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube(texture_id)
        pygame.display.flip()
        pygame.time.wait(10)


def load_texture():
    texture_surface = pygame.image.load('skin.png')
    texture_data = pygame.image.tostring(texture_surface, "RGBA", 1)
    width, height = texture_surface.get_rect().size
    glEnable(GL_TEXTURE_2D)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    return texture_id


vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)


def Cube(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    for vertex in vertices:
        glTexCoord2f(0, 0)
        glVertex3fv(vertex)
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


if __name__ == '__main__':
    MCSkinEditor()
