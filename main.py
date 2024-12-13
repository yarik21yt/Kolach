from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
player = FirstPersonController()

planks = []
for i in range(15):
    for j in range(15):
        plank = Button(color='#ffffff', model='cube', position=(j,0,i), texture='planks.png', parent=scene, origin_y=0.5)
        planks.append(plank)

cobblestone = Entity(model='cube')
cobblestone.texture = 'cobblestone.png'
cobblestone.position = Vec3(5, 2, 5)

text = Text(text="TEST ¯\_(:-D)_/¯", scale=4, x=-0.8, y=-0.3)


def input(key):
  for plank in planks:
    if plank.hovered:
      if key == 'right mouse down':
        new = Button(color=color.white, model='cube', position=plank.position + mouse.normal,
                    texture='planks.png', parent=scene, origin_y=0.5)
        planks.append(new)
      if key == 'left mouse down':
        planks.remove(plank)
        destroy(plank)

def update():
    cobblestone.rotation_x = cobblestone.rotation_x + time.dt * 10
    cobblestone.rotation_y = cobblestone.rotation_y + time.dt * 10
    cobblestone.rotation_z = cobblestone.rotation_z + time.dt * 10







app.run()