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

<img width="311" alt="스크린샷 2021-04-20 오후 9 33 13" src="https://user-images.githubusercontent.com/54436228/115396651-31050d80-a220-11eb-838a-c9ff9b459c75.png">
<img width="150" alt="스크린샷 2021-04-20 오후 9 32 34" src="https://user-images.githubusercontent.com/54436228/115396890-745f7c00-a220-11eb-87ed-2fea8b6d4e43.png">
