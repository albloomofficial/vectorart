import drawSvg as draw
from PIL import Image
import random
from time import sleep

big_size = 20

d = draw.Drawing(200*big_size,
                200 * big_size,
                origin='center')

d.setPixelScale(2)  # Set number of pixels per geometry unit

def xaxisfibanocci(i):
    listofx = [1,1,-1,-1]
    return listofx[i]

def yaxisfibanocci(i):
    listofy =  [-1,1,1,-1]
    return listofy[i]

def create_offspring():
    no_of_spawns = random.randint(3,7)
    return no_of_spawns

def negative_random():
    negative_randomizer = random.random()
    if negative_randomizer >= 0.5:
        negative = -1
    else:
        negative = 1
    return negative


fibanocci = [0, 1]
for x in range(100):
    fibanocci.append(fibanocci[x]+fibanocci[x+1])


d.append(draw.Rectangle(100*big_size,
                        -100*big_size,
                        -200*big_size,
                        200*big_size,
                        fill='white'))

xcord = 0
ycord = 0
d.append(draw.Lines(0,0,xcord,ycord))
counter = 0
i = 0
while counter < 20:
    nextX= 2*fibanocci[counter]*xaxisfibanocci(i)
    nextY= 2*fibanocci[counter]*yaxisfibanocci(i)
    i+=1
    if i > 3:
        i = 0
    counter += 1
    d.append(draw.Lines(xcord,ycord,nextX,nextY,
            stroke_width = 4,
            stroke_opacity = 1,
            stroke = 'red',
            fill = 'red',
            fill_opacity = 1))
    xcord = nextX
    ycord = nextY
    offspring_random = random.random()


d.savePng('example.png')









#d.setRenderSize(400,200)  # Alternative to setPixelScale



# saveSvg.show()
#
# # Display in iPython notebook
# d.rasterize()  # Display as PNG
# d  # Display as SVG
