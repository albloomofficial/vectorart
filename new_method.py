from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, parse_path

d = "M100,200 C100,100 250,100 250,200 S400,300 400,200"
p = parse_path(d)

p
