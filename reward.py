import math

def reward_function(params):
    best_waypoints = [
        [3.07856766, 0.72340284],
        [3.22294885, 0.71246001],
        [3.36864644, 0.70401991],
        [3.5153873, 0.69762471],
        [3.66294203, 0.69287269],
        [3.81112099, 0.68941637],
        [3.95977739, 0.68697655],
        [4.10881103, 0.68535985],
        [4.25813255, 0.68454425],
        [4.40740476, 0.68487459],
        [4.55614051, 0.68678066],
        [4.70400203, 0.69061259],
        [4.85071577, 0.69668525],
        [4.9959824, 0.7053682],
        [5.13949399, 0.71701803],
        [5.28093144, 0.73197514],
        [5.41996566, 0.75055956],
        [5.55627649, 0.77304541],
        [5.68960861, 0.79959385],
        [5.81987082, 0.83014024],
        [5.94681427, 0.86481496],
        [6.07014712, 0.90377025],
        [6.18942936, 0.94728685],
        [6.30395507, 0.99585867],
        [6.41305202, 1.04984072],
        [6.51548014, 1.10998658],
        [6.6098272, 1.17693733],
        [6.69419134, 1.25136048],
        [6.7662417, 1.33365999],
        [6.82221041, 1.42397109],
        [6.8652339, 1.51907272],
        [6.8927361, 1.61831873],
        [6.90063369, 1.72007673],
        [6.8907064, 1.82140844],
        [6.86585474, 1.92061633],
        [6.82793396, 2.01677092],
        [6.77363625, 2.10730546],
        [6.70614837, 2.19178966],
        [6.62744984, 2.27015808],
        [6.53891509, 2.3424323],
        [6.4423049, 2.40920038],
        [6.33877895, 2.4709007],
        [6.22939732, 2.52805451],
        [6.11518383, 2.581281],
        [5.99716732, 2.63130755],
        [5.87631349, 2.6788869],
        [5.75358736, 2.72482496],
        [5.62981361, 2.76983581],
        [5.49795385, 2.81748196],
        [5.36653228, 2.86606754],
        [5.23582086, 2.91617219],
        [5.10608545, 2.96835817],
        [4.97753098, 3.02305324],
        [4.85030286, 3.08055507],
        [4.72448568, 3.14103065],
        [4.60010155, 3.20451497],
        [4.47710816, 3.27090891],
        [4.35539677, 3.33997672],
        [4.23479045, 3.41134342],
        [4.11503552, 3.4844777],
        [3.99593324, 3.55896481],
        [3.87735057, 3.63452744],
        [3.76112555, 3.70750372],
        [3.64438782, 3.77888272],
        [3.5269279, 3.8479262],
        [3.40854622, 3.91383059],
        [3.28907016, 3.97573478],
        [3.16840795, 4.03286542],
        [3.04653527, 4.08445458],
        [2.92352354, 4.12983274],
        [2.79954008, 4.16844959],
        [2.67483535, 4.1998811],
        [2.54972314, 4.22385119],
        [2.42455262, 4.24026923],
        [2.29967154, 4.24928773],
        [2.17537492, 4.25143851],
        [2.0519893, 4.24673138],
        [1.92988415, 4.23511259],
        [1.80953541, 4.21625832],
        [1.69158535, 4.18960351],
        [1.57699061, 4.15418979],
        [1.46687968, 4.10923603],
        [1.36326716, 4.05300328],
        [1.26935171, 3.98333],
        [1.18960799, 3.89843752],
        [1.12366037, 3.80169848],
        [1.06962877, 3.69616091],
        [1.02635786, 3.58352703],
        [0.99299073, 3.46501511],
        [0.9688618, 3.34160486],
        [0.95340782, 3.21417646],
        [0.94611883, 3.08358362],
        [0.94652289, 2.95068531],
        [0.95419412, 2.81634386],
        [0.96867717, 2.68141396],
        [0.98966565, 2.54669521],
        [1.01688259, 2.4129264],
        [1.05002953, 2.28075009],
        [1.08879618, 2.15068818],
        [1.13289323, 2.02315058],
        [1.1820724, 1.89846424],
        [1.2361611, 1.77692443],
        [1.29518185, 1.6589132],
        [1.3595051, 1.54508585],
        [1.42955581, 1.43620334],
        [1.5061064, 1.33342543],
        [1.59003852, 1.2381625],
        [1.6822656, 1.15201261],
        [1.78499697, 1.07847614],
        [1.89512816, 1.01456508],
        [2.01127052, 0.95887708],
        [2.13248759, 0.91041879],
        [2.25812738, 0.86849456],
        [2.38758251, 0.8323991],
        [2.52045034, 0.80168538],
        [2.65635382, 0.77591211],
        [2.79492123, 0.75461261],
        [2.93577976, 0.73728318],
        [3.07856766, 0.72340284],
    ]

    x = params["x"]
    y = params["y"]

    distance_from_center = params["distance_from_center"]
    all_wheels_on_track = params["all_wheels_on_track"]
    is_left_of_center = params["is_left_of_center"]
    heading = params["heading"]
    progress = params["progress"]
    steps = params["steps"]
    speed = params["speed"]
    steering_angle = abs(params["steering_angle"])
    track_width = params["track_width"]
    is_offtrack = params["is_offtrack"]
    abs_steering = abs(params["steering_angle"])

    dist_from_best_waypoints = dist_from_line([x, y], best_waypoints)

    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the car is somewhere in between the track borders
    if not all_wheels_on_track:
        reward = 1e-3
    # Calculate 3 markers that are increasingly further away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if dist_from_best_waypoints <= marker_1:
        reward = 1
    elif dist_from_best_waypoints <= marker_2:
        reward = 0.5
    elif dist_from_best_waypoints <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3

    ABS_STEERING_THRESHOLD = 15
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    return float(reward)


def dist_points(x1, y1, x2, y2):
    return abs(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5


def dist_from_line(car_point, line_points):

    # Calculate all distances to racing points
    distances = []
    first_index = -1
    first_closest = 999
    for i in range(len(line_points)):
        distance = dist_points(
            x1=line_points[i][0], x2=car_point[0], y1=line_points[i][1], y2=car_point[1]
        )
        distances.append(distance)
        if first_closest > distance:
            first_closest = distance
            first_index = i

    second_index_a = first_index - 1 % len(line_points)
    second_index_b = first_index + 1 % len(line_points)

    if distances[second_index_a] < distances[second_index_b]:
        second_index = second_index_a
    else:
        second_index = second_index_b

    ax = line_points[first_index][0]
    ay = line_points[first_index][1]
    bx = line_points[second_index][0]
    by = line_points[second_index][1]
    cx = car_point[0]
    cy = car_point[1]

    numerator = abs((by - ay) * cx - (bx - ax) * cy + bx * ay - by * ax)
    denominator = math.sqrt((by - ay) ** 2 + (bx - ax) ** 2)

    try: 
        return numerator / denominator
    except:
        return distances[first_index]


# def direction_diff(closest_coords, second_closest_coords, car_coords, heading):

#     # Calculate the direction of the center line based on the closest waypoints
#     next_point, prev_point = next_prev_racing_point(closest_coords,
#                                                     second_closest_coords,
#                                                     car_coords,
#                                                     heading)

#     # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
#     track_direction = math.atan2(
#         next_point[1] - prev_point[1], next_point[0] - prev_point[0])

#     # Convert to degree
#     track_direction = math.degrees(track_direction)

#     # Calculate the difference between the track direction and the heading direction of the car
#     direction_diff = abs(track_direction - heading)
#     if direction_diff > 180:
#         direction_diff = 360 - direction_diff

#     return direction_diff
