> 모든 그래프는 Andrew Ng의 Machine Learning강의에서 사용

<h2>Multiclass Classification</h2>

여러개의 class로 분류되는 문제를 multi-class classification이라고 한다.<br>
multi-class classificatoin은 one-vs-all (one-vs-rest) 알고리즘을 사용한다.<br>

<img width="842" alt="스크린샷 2021-04-21 오전 10 35 14" src="https://user-images.githubusercontent.com/54436228/115484175-46fce780-a28d-11eb-98d5-7b9707b7cdf3.png">


**n개의 class로 분류해야될 경우, n개의 binary classification으로 해결**<br>

위의 경우 3가지 class의 Data set이 있으므로 3번의 binary classification을 진행한다.<br>

<h3>class 1 : y = 1</h3>

<img width="391" alt="스크린샷 2021-04-21 오전 10 36 43" src="https://user-images.githubusercontent.com/54436228/115484340-9e02bc80-a28d-11eb-9bca-e0b4aa7f730f.png">

△을 기준으로 binary classification을 진행한다.<br>
positive : △ / negative : 나머지<br>
h(1) : y가 1(△)일 확률<br>


<h3>class 2 : y = 2</h3>

<img width="402" alt="스크린샷 2021-04-21 오전 10 36 49" src="https://user-images.githubusercontent.com/54436228/115484351-a4913400-a28d-11eb-8312-d93c2030f616.png">

ㅁ을 기준으로 binary classification을 진행한다.<br>
positive : ㅁ / negative : 나머지<br>
h(2) : y가 2(ㅁ)일 확률<br>


<h3>class 3 : y = 3</h3>

<img width="398" alt="스크린샷 2021-04-21 오전 10 37 03" src="https://user-images.githubusercontent.com/54436228/115484354-a78c2480-a28d-11eb-9d90-c9c57b9fc72c.png">

ㅇ을 기준으로 binary classification을 진행한다.<br>
positive : ㅇ / negative : 나머지<br>
h(3) : y가 3(ㅇ)일 확률<br>

<h2>Logistic Regression Classifier</h2>

y = i 일 확률을 예측한다.<br>
<img width="500" alt="스크린샷 2021-04-21 오전 10 54 42" src="https://user-images.githubusercontent.com/54436228/115485638-123e5f80-a290-11eb-9e3f-dd15c7514e1f.png">

새로운 input x에 대한 각각의 classifier를 적용하여 최대 확률을 갖는 class를 선택한다.<br>
<img width="500" alt="스크린샷 2021-04-21 오전 10 50 00" src="https://user-images.githubusercontent.com/54436228/115485679-27b38980-a290-11eb-8c03-ed3ddb5e00d1.png">
