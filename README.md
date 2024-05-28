# model-01 (76점 / 25.067)

## idea
#### 자동차는 트랙의 가운데를 주행하지 않아도 되지만, 자동차의 중앙이 트랙의 밖으로 나가면 안된다. 현재 자동차의 진행 방향과 다음 waypoint로의 각도가 30도 이상이면 보상을 의미가 없을 정도로 낮은 숫자로 준다.

## 세부 조건
- Race Type : Time trial
- Environment simulation : 2022 re:Invent Championship - Counterclockwise
- Sensor(s) : Camera
- Action space type : Discrete
- Action space
No.	Steering angle (°)	Speed (m/s)
0	-30.0	1.00
1	-30.0	2.00
2	-30.0	3.00
3	-15.0	1.00
4	-15.0	2.00
5	-15.0	3.00
6	0.0	1.00
7	0.0	2.00
8	0.0	3.00
9	15.0	1.00
10	15.0	2.00
11	15.0	3.00
12	30.0	1.00
13	30.0	2.00
14	30.0	3.00

## 보상 함수
```
import math

def reward_function(params):
    # 주행 파라미터
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Menger Curvature에 따라 계산된 이상적인 heading 값 구하기
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)

    # 현재 진행 방향과 다음 waypoint 사이의 각도 차이 계산
    direction_diff = abs(track_direction - heading)
    direction_diff = min(direction_diff, 360 - direction_diff)

    # 방향 유지 보상
    if direction_diff > 30:
        # 각도 차이가 30도 이상일 때 매우 낮은 보상 (거의 의미 없는 수준)
        return float(1e-10)  # 예를 들어 1e-10과 같은 매우 낮은 수 사용
    else:
        # 각도 차이가 30도 이내일 때 방향에 대한 보상은 cos 함수를 사용해 계산
        return float(math.cos(math.radians(direction_diff)))

# AWS DeepRacer 콘솔에서 함수 호출
reward = reward_function({
    'waypoints': waypoints,  # track waypoints
    'closest_waypoints': [2, 3],  # indices of the closest waypoints
    'heading': current_heading  # current heading of the car
})
```
