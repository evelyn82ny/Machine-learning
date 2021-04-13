<h2>Data scaling(feature scaling)</h2>

Multivariable Linear Regression 에서는 많은 feature를 이용하여 결과를 도출해낸다.<br>
각각의 feature들은 평수, 방의 개수, 지하철역까지의 거리 등 서로 다른 기준이기 때문에, 당연하게도 서로 다른 범위를 갖게 된다.<br>

**10이하의 범위를 갖는 x1**와 **400,000이상 2,000,000이하의 범위를 갖는 x2**인 2개의 feature가 있다.<br>
해당 hypothesis는 `H(x) = Θ1*x1 + Θ2*x2 , (Θ0 == 0으로 가정)` 으로 작성한다.<br>
이때 x2의 범위가 훨씬 크기때문에 `Θ1` 의 크기가 커지며.<br>
반대로 x1의 범위는 작기때문에 `Θ2` 의 크기가 작아진다.<br>

`Θ1, Θ2` 에 대한 그래프는 오른쪽과 같다.<br>
해당 그래프는 탐색을 많이 하게되므로 많은 시간이 소요되는 문제를 갖는다.<br>
<img width="913" alt="스크린샷 2021-04-13 오후 1 48 34" src="https://user-images.githubusercontent.com/54436228/114498413-01259b00-9c5f-11eb-9118-d398eca6b935.png">

Feature scaling을 통해 feature간의 범위를 조절하여 Θ값을 비슷하게 만든다.<br>
Θ값을 비슷하게 만들면 오른쪽과 같은 그래프가 나오며, 왼쪽 그래프보다 빨리 결과를 찾을 수 있다.<br>
<img width="960" alt="스크린샷 2021-04-13 오후 1 48 45" src="https://user-images.githubusercontent.com/54436228/114498420-04208b80-9c5f-11eb-9565-1c2ace42982d.png">

<h3>StandardScaler</h3>
표준편차를 사용한다.<br>

```python
import pandas as pd
from sklearn import preprocessing

x_train={ 'x1':[10, 12, 8, 9, 8], 
          'x2':[1500000, 2000000, 700000, 800000, 400000] }
x_train_DF=pd.DataFrame(x_train)

standard_scaler=preprocessing.StandardScaler()
standard_scaler.fit(x_train_DF)
print(standard_scaler.transform(x_train_DF))
```
<img width="197" alt="스크린샷 2021-04-13 오후 3 05 32" src="https://user-images.githubusercontent.com/54436228/114504361-b8271400-9c69-11eb-938b-47fec9701274.png">


<h3>MinMaxScaler</h3>
데이터 값을 0과 1사이로 변환한다.<br>

```python 
minmax_scaler=preprocessing.MinMaxScaler()
minmax_scaler.fit(x_train_DF)
print(minmax_scaler.transform(x_train_DF))
```
<img width="119" alt="스크린샷 2021-04-13 오후 2 20 05" src="https://user-images.githubusercontent.com/54436228/114500620-5ebbe680-9c63-11eb-8c25-f28889638f31.png">

<h3>MaxAbsScaler</h3>
데이터 값을 -1과 1로 변환한 뒤, 절대값이 0과 1사이로 mapping한다.<br>

```python
abs_scaler=preprocessing.MaxAbsScaler()
abs_scaler.fit(x_train_DF)
print(abs_scaler.transform(x_train_DF))
```
<img width="186" alt="스크린샷 2021-04-13 오후 3 17 37" src="https://user-images.githubusercontent.com/54436228/114505646-a9416100-9c6b-11eb-9ba0-4c67d54358c0.png">



<h3>RobustScaler</h3>
StandardScaler, MinMaxScaler, MaxAbsScaler 방법은 outlier에 크게 반응한다.<br>
RobustScaler는 outlier의 영향을 최소화한 기법이다.<br>

```python
rbs_scaler=preprocessing.RobustScaler()
rbs_scaler.fit(x_train_DF)
print(rbs_scaler.transform(x_train_DF))
```
<img width="125" alt="스크린샷 2021-04-13 오후 3 18 25" src="https://user-images.githubusercontent.com/54436228/114505654-aba3bb00-9c6b-11eb-95e8-928cadca8d67.png">
