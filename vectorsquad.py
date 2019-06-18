import drawSvg as draw
from PIL import Image
import random
from time import sleep

def generate_color(color_tracker):
    color_list = [["#FF7F50","#FF6347","#FF4500","#FFD700","#FFA500","#FF8C00"],
    ["#E0FFFF","#00FFFF","#00FFFF","#7FFFD4", "#66CDAA", "#AFEEEE","#40E0D0","#48D1CC"],
    ["#E6E6FA","#D8BFD8","#DDA0DD","#EE82EE","#DA70D6","#FF00FF","#BA55D3","#9370DB","#8A2BE2","#9400D3","#9932CC","#8B008B","#800080","#4B0082"]
    ]
    color_picker = random.randint(0,5)
    color_list = color_list[color_tracker]
    color = color_list[color_picker]
    return color

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

def create_offspring(startX, startY, offspring_i, offspring_counter):
    offspringnextX = startX + random.randint(1,10)*10*fibanocci[offspring_counter] * xaxisfibanocci(offspring_i)
    offspringnextY = startY + random.randint(1,10)*10*fibanocci[offspring_counter] * yaxisfibanocci(offspring_i)
    c = draw.Lines(startX,startY,
            offspringnextX,
            offspringnextY,
            stroke_width = 2,
            stroke_opacity = 0.6,
            stroke = generate_color(color_tracker))
    offspring_info = {
    "line" : c,
    "end_pointX" : offspringnextX,
    "end_pointY" : offspringnextY
    }
    return offspring_info

def offspring_growth(growth_startX, growth_startY):
    growth_counter = 3
    growth_i = 0

    growth_nextX = (
        growth_startX +
        2*fibanocci[growth_counter]*xaxisfibanocci(growth_i)
    )

    growth_nextY = (
        growth_startY +
        2*fibanocci[growth_counter]*yaxisfibanocci(growth_i)
    )

    d.append(draw.Lines(
            growth_startX,
            growth_startY,
            growth_nextX,
            growth_nextY,
            stroke_width = 2,
            stroke_opacity = 0.6,
            stroke = generate_color(color_tracker)
    ))
    growth_startX = growth_nextX
    growth_startY = growth_nextY

    while growth_counter < big_size:

        growth_nextX = (
            growth_startX +
            fibanocci[growth_counter]*xaxisfibanocci(growth_i)
        )

        growth_nextY = (
            growth_startY +
            fibanocci[growth_counter]*yaxisfibanocci(growth_i)
        )

        d.append(draw.Lines(
                growth_startX,
                growth_startY,
                growth_nextX,
                growth_nextY,
                stroke_width = 2,
                stroke_opacity = 0.6,
                stroke= generate_color(color_tracker)))
        growth_startX = growth_nextX
        growth_startY = growth_nextY

        growth_i+=1
        growth_counter+=1
        if growth_i > 3:
            growth_i = 0


def orange_figure(xstart,ystart,i):
    xcord = xstart
    ycord = ystart
    d.append(draw.Lines(xstart,ystart,xcord,ycord))
    counter = 0
    i = 0
    while counter < big_size:
        nextX= xcord + 2*fibanocci[counter]*xaxisfibanocci(i)
        nextY= ycord + 2*fibanocci[counter]*yaxisfibanocci(i)
        i+=1
        if i > 3:
            i = 0
        counter += 1
        d.append(draw.Lines(xcord,ycord,nextX,nextY,
                stroke_width = 2,
                stroke_opacity = 1,
                stroke = generate_color(color_tracker)
                ))
        xcord = nextX
        ycord = nextY
        no_of_spawns = random.randint(3,7)
        offspring_i = 0
        offspring_counter = 0

        for child in range(no_of_spawns):
            new_spawn = create_offspring(
            nextX,
            nextY,
            offspring_i,
            offspring_counter)
            d.append(new_spawn["line"])

            offspring_i += 1
            if offspring_i > 3:
                offspring_i = 0
            offspring_counter += 1
            offspring_growth(new_spawn["end_pointX"], new_spawn["end_pointY"])

d.append(draw.Rectangle(100*big_size,
                        -100*big_size,
                        -200*big_size,
                        200*big_size,
                        fill='white'))
fibanocci = [0, 1]
for x in range(100):
    fibanocci.append(fibanocci[x]+fibanocci[x+1])
for color_tracker in range(3):
    a = random.randint(-2000,2000)
    b = random.randint(-2000,2000)
    orange_figure(a,b,color_tracker)
d.savePng('example.png')
