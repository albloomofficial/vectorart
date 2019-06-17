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
    if offspring_random > 0.2:
        branches = create_offspring()
        for branch in range(branches):
            nextXchild = random.random()*(1.5**counter)*negative_random()
            nextYchild = random.random()*(1.5**counter)*negative_random()
            d.append(draw.Lines(xcord,ycord,nextXchild,nextYchild,
            stroke_width = random.random()*3,
            stroke = 'green',
            stroke_opacity = 0.7,
            fill = 'green',
            fill_opacity = random.random()))
            random_length = random.randint(2,6)
            grand_fibanocci = fibanocci
            grand_counter = random.randint(0,3)
            grand_i = grand_counter
            xcordchild = nextXchild
            ycordchild = nextYchild
            for little_one in range(random_length):
                nextXgrand = (grand_i*grand_fibanocci[grand_i]*xaxisfibanocci(grand_i))*random.randint(100,1000)*random.random()
                nextYgrand = (grand_i*grand_fibanocci[grand_i]*yaxisfibanocci(grand_i))*random.randint(100,1000)*random.random()
                d.append(draw.Lines(xcordchild,
                                    ycordchild,
                                    nextXgrand,
                                    nextYgrand,
                                    stroke_width = 4,
                                    stroke = 'black',
                                    stroke_opacity = 0.25,
                                    fill = 'black',
                                    fill_opacity = 1
                                    ))
                distance = ((nextXgrand-xcordchild)**2+(nextYgrand-ycordchild**2))**(1.0/2)
                print(distance)
                xcordchild = nextXgrand
                ycordchild = nextYgrand
                grand_counter +=1
                grand_i += 1
                if grand_i > 3:
                    grand_i = 0


d.savePng('example.png')









#d.setRenderSize(400,200)  # Alternative to setPixelScale



# saveSvg.show()
#
# # Display in iPython notebook
# d.rasterize()  # Display as PNG
# d  # Display as SVG
