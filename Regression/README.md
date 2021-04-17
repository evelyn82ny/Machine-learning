<h2>Regression</h2>

**Regression analysis란 관찰된 연속형 변수들 사이의 모델을 구현하여 적합도를 측정해 내는 분석 방법**이라고 wikipedia에 정의되어있다.<br>

<h3>Hypothesis</h3>
<img width="1045" alt="스크린샷 2021-04-17 오후 12 53 44" src="https://user-images.githubusercontent.com/54436228/115101053-1ad72300-9f7c-11eb-8950-9effd01a92d4.png">

- m : Number of training examples
- 𝑥′𝑠 : input variable or features
- 𝑦′𝑠 : output variable" or target value
- (x,y) : one training example
- (𝑥𝑖,𝑦𝑖) : i-th training example
- θ : Regression coefficient(Parameter)


**X(feature)** , **H(target)** 를 기반으로 하는 Supervised Learning 통해 최적의 **θ(coefficient)** 를 찾아낸다.<br>

<h3>Cost function</h3>

Hypothesis에 대한 값과 실제 데이터의 차이에 대한 값으로 정의된다.<br>
cost function을 **𝐽(𝜃)** 라고 하며, **𝐽(𝜃)의 값이 최소가 되도록 θ를 찾는다.**<br>
<img width="308" alt="스크린샷 2021-04-17 오후 1 14 47" src="https://user-images.githubusercontent.com/54436228/115101413-f761a780-9f7e-11eb-8f6b-061e1d118721.png">

**ℎ𝜃(𝑥)−𝑦** 를 error(오차)라고 하며, 오차의 값은 양수 / 음수의 값이 나온다.<br>
양수와 음수가 서로 상쇄되는 것을 막기위해 **ℎ𝜃(𝑥)−𝑦** 에 제곱을 한다.<br>
위 식은 모든 오차의 제곱을 더해 평균한 MSE(Mean Square Error)이며, 다양한 비용함수 중 가장 보편적으로 사용된다.<br>

 
 
