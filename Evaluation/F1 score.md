# F1-score

> 아래 모든 수식은 wikipedia 에서, 아래 모든 그래프는 gaussian37.github.io 에서 사용했습니다.

F1 score는 recall과 precision의 조화 평균이며 수식은 다음과 같다.<br>

![png](/_img/evaluation/f1_score.png){: width="70%" height="70%"} <br>

### recall = 0.01 / precision = 1 인 경우

F1 = 2 * (0.01) / 1.01 = 0.0198<br>

### recall = 0.5 / precision = 0.5 인 경우

F1 = 2 * 0.25 / 1 = 0.5<br>

recall과 precision의 값이 비슷할수록 F1 score 값이 증가하여 좋아진다.<br>

### Harmonic Mean 조화 평균을 사용해야 하는 이유

한가지 값이 극단적으로 낮을땐 F1 score도 낮게 나오고, 두 값이 모두 높을 경우 F1 score도 높게 나와야 하기 떄문에 harmonic mean 조화 평균을 사용한다.<br>

- 산술 평균 arithmetic mean = (0.01 + 1) / 2 = 0.505
- 조화 평균 harmonic mean = 2 * (1 * 0.01) / (1 + 0.01) = 0.0198


## Arithmetic mean 산술 평균

Arithmetic mean 산술평균이란 주어진 모든 수의 합을 주어진 수의 개수로 나눈 값이다.<br>

![png](/_img/evaluation/arithmetic_mean_expression.png){: width=50%" height="50%"}<br>
![png](/_img/evaluation/arithmetic_mean.png){: width="60%" height="60%"}<br>

위 그래프는 1, 4, 7, 10, 13, 16, 19 인 7개의 데이터(파란점)와 7개의 평균인 10(빨간점)을 나타낸 그래프이다.<br>
위와 같이 산술 평균은 데이터가 선형이거나 등차 관계가 가까울때 사용한다.<br>

## Geometric mean 기하 평균

Geometric mean 기하 평균은 양수인 n개의 모든 데이터를 곱한 값에 n 제곱근한 결과이다.<br>

![png](/_img/evaluation/geometric_mean_expression.png){: width="60%" height="60%"}<br>
![png](/_img/evaluation/geometric_mean.png){: width="60%" height="60%"}<br>

위 그래프는 1, 3, 9, 27, 81, 243, 729 인 7개의 데이터(파란점)과 7개의 기하평균 27(빨간점)을 나타낸 그래프이다.<br>
위와 같이 기하 평균은 데이터가 등비 관계일 경우에 사용한다.<br>

### Data scale이 서로 다른 경우

- 가게 1은 4.5/5 와 68/100 의 점수를 받고
- 가게 2는 3/5 와 75/100의 점수를 받았다.

위와 같이 기준이 다른 점수를 받은 경우 더 좋은 평점을 받은 가게를 판별하기 위한 계산방법은 다음과 같다.<br>

![png](/_img/evaluation/fl_score_data_scales_are_different.png){: .align-center}{: width="90%" height="90%"}

산술 평균을 사용할 경우, 모든 데이터의 기준은 같아야 하므로 20을 곱하여 계산을 한다.