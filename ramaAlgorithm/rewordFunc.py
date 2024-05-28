import math

def reward_function(params):
    def ramer_douglas_peucker(points, epsilon):
        # 여기서는 기존 함수를 그대로 사용합니다.
        dmax = 0.0
        index = 0
        for i in range(1, len(points) - 1):
            d = point_line_distance(points[i], points[0], points[-1])
            if d > dmax:
                index = i
                dmax = d
        if dmax >= epsilon:
            results1 = ramer_douglas_peucker(points[:index + 1], epsilon)
            results2 = ramer_douglas_peucker(points[index:], epsilon)
            return results1[:-1] + results2
        else:
            return [points[0], points[-1]]

    def point_line_distance(point, start, end):
        # 여기서는 기존 함수를 그대로 사용합니다.
        if start == end:
            return distance(point, start)
        else:
            n = abs((end[0] - start[0]) * (start[1] - point[1]) - (start[0] - point[0]) * (end[1] - start[1]))
            d = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            return n / d

    def distance(point1, point2):
        # 여기서는 기존 함수를 그대로 사용합니다.
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    # waypoints를 순수 Python 리스트로 변환
    waypoints = [list(point) for point in params['waypoints']]
    # closest_waypoints도 순수 Python 리스트로 변환
    closest_waypoints = list(params['closest_waypoints'])
    heading = params['heading']
    speed = params['speed']
    x = params['x']
    y = params['y']

    epsilon = 1.5
    simplified_waypoints = ramer_douglas_peucker(waypoints, epsilon)

    closest_index = closest_waypoints[1]
    next_index = min(closest_index + 1, len(simplified_waypoints) - 1)
    next_point = simplified_waypoints[next_index]

    reward = 1.0

    direction_to_next_point = math.atan2(next_point[1] - y, next_point[0] - x)
    direction_diff = abs(direction_to_next_point - math.radians(heading))
    if direction_diff > math.pi:
        direction_diff = 2 * math.pi - direction_diff

    if direction_diff < math.radians(10):
        reward += 5

    if speed > 2.5:
        reward *= 0.5
    elif speed > 1.0:
        reward += 5

    return reward
