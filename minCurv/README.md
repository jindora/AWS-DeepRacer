# minCuv (63.6점 / 28.729)


## idea
#### 자동차는 트랙의 가운데를 주행하지 않아도 되지만, 자동차의 중앙이 트랙의 밖으로 나가면 안된다. 현재 자동차의 진행 방향과 다음 waypoint로의 각도가 30도 이상이면 보상을 의미가 없을 정도로 낮은 숫자로 준다.


## 세부 조건
- Race Type : Time trial
- Environment simulation : 2022 re:Invent Championship - Counterclockwise
- Sensor(s) : Camera
- Action space type : Discrete
- Action space
![initial](https://github.com/jindora/AWS-DeepRacer/assets/67107084/9dc75b01-330d-46fe-82de-3f130f5b484a)

|No.|	Steering angle (°)|	Speed (m/s)|
|----|-------------------|--------------|
|0|	-30.0|	1.00|
|1|	-30.0|	2.00|
|2|	-30.0|	3.00|
|3|	-15.0|	1.00|
|4|	-15.0|	2.00|
|5|	-15.0|	3.00|
|6|	0.0|	1.00|
|7|	0.0|	2.00|
|8|	0.0|	3.00|
|9|	15.0|	1.00|
|10|	15.0|	2.00|
|11|	15.0|	3.00|
|12|	30.0|	1.00|
|13|	30.0|	2.00|
|14|	30.0|	3.00|

- **Framework : Tensorflow**
- **Reinforcement learning algorithm : PPO**
- **Hyperparameter**

|Hyperparameter|	Value|
|--------------|---------|
|Gradient descent batch size|	64|
|Entropy|	0.01|
|Discount factor|	0.99|
|Loss type|	Huber|
|Learning rate|	0.0003|
|Number of experience episodes between each policy-updating iteration|	20|
|Number of epochs|	10|


## 주행 결과

|Trial    |Time (MM:SS.mmm)    |Trial results (% track completed)    |Status    |Off-track|    Off-track penalty    |Crashes    |Crash penalty|
|-------|-------------|------------------------------|-------------|------------|--------------------|----------|--------------|
|1|	00:28.729|	100%|	Lap complete|	1|	2 seconds|	0|	--|
|2|	00:30.474|	100%|	Lap complete|	2|	4 seconds|	0|	--|
|3|	00:33.132|	100%|	Lap complete|	3|	6 seconds|	0|	--|
