from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os
from labels import *


app = Ursina()
player = FirstPersonController()
choosed = 1
# 1 - grass
# 2 - cobblestone
# 3 - planks
# 4 - wool
# 5 - max

blocks = []
for i in range(20):
    for j in range(20):
        grass = Button(color='#ffffff', model='cube', position=(j,0,i), texture='grass.png', parent=scene, origin_y=0.5)
        blocks.append(grass)

cobblestone = Entity(model='cube')
cobblestone.texture = 'max.png'
cobblestone.position = Vec3(10, 2, 10)

text = Text(text=test_text, scale=4, x=-0.8, y=-0.3)


def clear_world():
    global blocks
    for block in blocks:
        destroy(block)
    blocks = []


def save_world():
    with open('world.txt', 'w') as f:
        for block in blocks:
            f.write(f"{block.position.x},{block.position.y},{block.position.z},{block.texture}\n")

def load_world():
    clear_world()
    if os.path.exists('world.txt'):
        with open('world.txt', 'r') as f:
            for line in f:
                x, y, z, texture = line.strip().split(',')
                new_block = Button(color=color.white, model='cube', position=(float(x), float(y), float(z)),
                                   texture=texture, parent=scene, origin_y=0.5)
                blocks.append(new_block)


def input(key):
  global choosed
  for grass in blocks:
    if grass.hovered:
      if key == 'right mouse down' and choosed == 1:
        new = Button(color=color.white, model='cube', position=grass.position + mouse.normal,
                    texture='grass.png', parent=scene, origin_y=0.5)
        blocks.append(new)
      elif key == 'right mouse down' and choosed == 2:
        new = Button(color=color.white, model='cube', position=grass.position + mouse.normal,
                    texture='cobblestone.png', parent=scene, origin_y=0.5)
        blocks.append(new)
      elif key == 'right mouse down' and choosed == 3:
        new = Button(color=color.white, model='cube', position=grass.position + mouse.normal,
                    texture='planks.png', parent=scene, origin_y=0.5)
        blocks.append(new)
      elif key == 'right mouse down' and choosed == 4:
        new = Button(color=color.white, model='cube', position=grass.position + mouse.normal,
                    texture='wool.png', parent=scene, origin_y=0.5)
        blocks.append(new)
      elif key == 'right mouse down' and choosed == 5:
        new = Button(color=color.white, model='cube', position=grass.position + mouse.normal,
                    texture='max.png', parent=scene, origin_y=0.5)
        blocks.append(new)
      if key == 'left mouse down':
        blocks.remove(grass)
        destroy(grass)
  if key == 'q':
     cobblestone.position = player.position
  if key == 'r':
     player.position = (0,0,0)
  if key == 'l':
    load_world()
  if key == 'k':
    save_world()
  if key == '1':
    choosed = 1
  elif key == '2':
    choosed = 2
  elif key == '3':
    choosed = 3
  elif key == '4':
    choosed = 4
  elif key == '5':
    choosed = 5
    
     

def update():
    cobblestone.rotation_x = cobblestone.rotation_x + time.dt * 10
    cobblestone.rotation_y = cobblestone.rotation_y + time.dt * 10
    cobblestone.rotation_z = cobblestone.rotation_z + time.dt * 10







app.run()