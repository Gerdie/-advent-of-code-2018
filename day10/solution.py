import re
from time import sleep

import plotly

re_patt = 'position=<(?P<x>-?\s?\d+),\s(?P<y>-?\s?\d+)>\svelocity=<(?P<x_vel>-?\s?\d+),\s(?P<y_vel>-?\s?\d+)>'

points = []
velocities = []

with open('input.txt') as input_file:
    for line in input_file:
        match = re.search(re_patt, line)
        point = [int(match.group('x')), int(match.group('y'))]
        velocity = [int(match.group('x_vel')), int(match.group('y_vel'))]
        points.append(point)
        velocities.append(velocity)


def get_layout(title_num):
    return {
        "title": "Iteration {}".format(title_num),
        "xaxis": {"title": "x", },
        "yaxis": {"title": "y"}
    }


def get_graph_data():
    return {
        "x": [pt[0] for pt in points],
        "y": [pt[1] for pt in points],
        "marker": {"color": "blue", "size": 5},
        "mode": "markers",
        "name": "points",
        "type": "scatter",
    }


def apply_velocity():
    for idx, pt in enumerate(points):
        pt[0] += velocities[idx][0]
        pt[1] += velocities[idx][1]


iteration = 1
while True:
    apply_velocity()
    iteration += 1
    if iteration > 10500:
        fig = plotly.graph_objs.Figure(data=[get_graph_data()], layout=get_layout(iteration))
        plotly.offline.plot(fig, filename='plot.html')
        sleep(1)
    if iteration > 10700:
        break
