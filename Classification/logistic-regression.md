> 모든 그래프는 Andrew Ng의 Machine Learning강의에서 사용

<h2>Classification</h2>

- binary classification : negative/positive 처럼 2가지 class로 분류
- multiclass classification : 3가지 이상의 class로 분류

binary classification에서 positive / negative class를 설정하는 기준은 **학습하고자 하는 대상**이다.<br>
> 기준이 정해져있는 것은 아니지만 일반적을 학습하고자 하는 대상에 기준을 둔다.
- 스팸메일 분류에서는 스팸 메일을 골라내야 하므로 : positive(스팸메일)
- 종양 분류에서는 악성 종양을 골라내야 하므로 : positive(악성종양) / negative(양성종양)

<h2>linear regression으로 예측하는 경우</h2>

classification 문제를 linear regression으로 해결할 경우 다음과 같은 문제가 발생된다.<br>

<img width="500" alt="스크린샷 2021-04-20 오후 4 57 05" src="https://user-images.githubusercontent.com/54436228/115359287-811ca980-a1f9-11eb-9146-46b042bfd6ba.png">

0.5 기준으로 linear regression이 제대로 분류하는 것처럼 보일 수 있다.<br>

새로운 데이터가 추가될 경우 이에 따른 기울기가 변하며, 오류가 발생된다.
<img width="600" alt="스크린샷 2021-04-20 오후 4 57 13" src="https://user-images.githubusercontent.com/54436228/115359313-8548c700-a1f9-11eb-9f61-450586833f78.png">

또한 0과 1로 분류하고자 할때 linear regression의 결과가 1보다 훨씬 크거나 0보다 작은 값에 대해서 처리가 어려워진다.

<h2>Logistic Regression</h2>

logistic regression은 0과 1사이의 예측 값을 갖는 sigmoid function으로 위의 문제를 해결한다.<br>

<img width="750" alt="스크린샷 2021-04-20 오후 9 58 19" src="https://user-images.githubusercontent.com/54436228/115399838-90185180-a223-11eb-84b4-c9990b8a9950.png">


<h2>Decision Boundary</h2>

Decision Boundary란 class를 나누는 경계로 학습을 통해 얻은 θ에 의해 결정된다.<br>

<img width="900" alt="스크린샷 2021-04-20 오후 10 34 25" src="https://user-images.githubusercontent.com/54436228/115404945-bf7d8d00-a228-11eb-91a5-fcc7b9e9db9d.png">

- predict 0 : x1 + x2 < 3 
- predict 1 : x1 + x2 >= 3 


<h3>non-linear dicision boundaries</h3>

polynomial에서 dimension이 높은 경우 아래와 같이 복잡한 모델이 된다.<br>

<img width="900" alt="스크린샷 2021-04-20 오후 10 47 53" src="https://user-images.githubusercontent.com/54436228/115407065-b2fa3400-a22a-11eb-818e-0584bd81f47d.png">
