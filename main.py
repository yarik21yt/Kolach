from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from labels import *

app = Ursina()
player = FirstPersonController()

grasses = []
for i in range(15):
    for j in range(15):
        grass = Button(color='#ffffff', model='cube', position=(j,0,i), texture='grass.png', parent=scene, origin_y=0.5)
        grasses.append(grass)

cobblestone = Entity(model='cube')
cobblestone.texture = 'max.png'
cobblestone.position = Vec3(5, 2, 5)

text = Text(text=test_text, scale=4, x=-0.8, y=-0.3)


def input(key):
  for grass in grasses:
    if grass.hovered:
      if key == 'right mouse down':
        new = Button(color=color.white, model='cube', position=grass.position + mouse.normal,
                    texture='cobblestone.png', parent=scene, origin_y=0.5)
        grasses.append(new)
      if key == 'left mouse down':
        grasses.remove(grass)
        destroy(grass)
  if key == 'q':
     cobblestone.position = player.position
  if key == 'r':
     player.position = (0,0,0)
     

def update():
    cobblestone.rotation_x = cobblestone.rotation_x + time.dt * 10
    cobblestone.rotation_y = cobblestone.rotation_y + time.dt * 10
    cobblestone.rotation_z = cobblestone.rotation_z + time.dt * 10







app.run()