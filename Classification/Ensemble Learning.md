<h1>Ensemble learning</h1>

여러 개의 Classifier에 대한 예측을 결합하여 보다 정확한 최종 예측을 도출하는 기법<br><br>
random forest 및 boosting algorithm들은 decision tree 알고리즘을 기반으로 한다.<br>
decision tree의 단점인 overfitting을 많은 classifier르 결합하여 보완하고,<br>
장점인 직관적인 분류 기준은 강화된다.<br>

<h2>Voting</h2>

동일한 Data set을 서로 다른 알고리즘을 갖는 classifier로 결합하는 방식<br>

- Hard voting : 여러 classifier 간 다수결로 결정
- Soft voting : 여러 classifier 들의 class 확률을 평균하여 결정

soft voting의 예측 성능이 상대적으로 우수하여 주로 사용된다.<br>

```python
lr_clf = LogisticRegression()
knn_clf = KNeighborsClassifier(n_neighbors=8)

vo_clf = VotingClassifier( estimators=[('LR',lr_clf),('KNN',knn_clf)] , voting='soft' )
#LogisticRegression과 K-Nearest Neighbor classifier를 soft voting 한 결과는 다음과 같다.
```
<img width="350" alt="스크린샷 2021-04-19 오후 4 28 05" src="https://user-images.githubusercontent.com/54436228/115197807-5f092580-a12c-11eb-9796-03461da38c5f.png">
개별보다 voting했을 때의 성능이 좋아진 것을 확인할 수 있다.<br>

<h2>Bagging (Bootstrap Aggregating)</h2>

Bootstrap 분할 방식으로 sampling data set을 여러 classifier에 독립적으로 학습시킨 결과를 Aggregration하는 방식<br>

> Bootstrap : n_samples개의 데이터 포인트 중에서 무작위로 데이터를 n_samples 횟수만큼 반복 추출하는 방식<br>
> 만들어진 sample dataset은 원래 dataset의 크기와 같지만, 데이터 포인터가 누락 / 중복될 수 있다.

- Categorical Data : Voting으로 결과 집계
- Continuous Data : average로 결과 집계

<h3>Random forest</h3>

bootstrap에 의해 만들어진 sample dataset으로 decision tree를 만들때 후보 특성을 random하게 선택하여 분할한다.<br>

- max_features : 몇 개의 특성을 고를지 설정하는 매개변수<br>random forest의 트리를 분할하는 feature를 참조할 때 sqrt(전체 feature 개수)만큼 참조

후보 특성을 고르는 것을 매 노드마다 반복된다.<br>
즉, 트리의 각 분기는 다른 특성 부분 집합을 사용한다.<br>
max_features 를 n_features로 설정하면 특성 선택에 무작위성이 적용되지 않고, bootstrap에만 무작위성이 적용된다.<br>
max_features 값을 크게 하면 random forest의 트리들이 비슷해지며, 가장 두드러진 특성을 이용해 데이터에 잘 맞춰진다.<br>
mak_features 값을 낮추면 random forest의 트리들이 달라지며, 각 트리는 데이터에 맞축 위해 깊이가 깊어진다.<br>


<img width="700" src="https://user-images.githubusercontent.com/54436228/115263427-62be9b80-a170-11eb-8261-f361df9304a2.png">

> <h8> 출처 : tensorflow blog</h8>

오른쪽 맨 아래를 제외한 5개의 Decision Tree의 dicision boundary는 불완전한 경계를 나타낸다.<br>
오른쪽 맨 아래의 random forest의 dicision boundary는 위 5개의 평균으로 만들었으며, 훨씬 좋은 결정 경계가 만들어진다.<br>


<h2>Boosting</h2>

bagging의 경우 여러 classifier가 독립적으로 학습했다면<br>
boosting은 여러 weak classifier가 순차적으로 학습하며, 데이터에 가중치를 부여해 오류를 개선해나가는 방식<br>
결과는 좋지만 weak classifier를 순차적으로 학습하는 방식이므로 다소 시간이 소요되는 문제가 있다.<br>

<h3>AdaBoost (Adaptive boosting)</h3>

<img width="800" alt="스크린샷 2021-04-20 오전 10 34 54" src="https://user-images.githubusercontent.com/54436228/115324036-23219f00-a1c4-11eb-9a09-121e1ff0d277.png">

> <h8> 출처 : 파이썬 머신러닝 완벽 가이드</h8>

<h3>GBM (Gradient Boost Machine)</h3>

Adaboost와 유사하지만, 가중치 업데이트를 Gradient Descent를 이용<br>

- n_estimators : weak learner 개수
- learning_rate : weak learner가 순차적으로 오차를 보정하는 정도르 조절하는 계수

learning_rate를 낮추면 비슷한 복잡도의 모델을 만들기 위해 n_estimators 를 높여 트리를 추가해야한다.<br>
n_estimators가 클수록 모델이 복잡해지고 많은 시간이 소요되며, overfitting일 가능성이 높다.<br>
2개의 매개변수을 잘 조절해야하는데, 보통 가용시간과 메모리 한도에서 n_estimators를 맞춘 뒤 적절한 learning_rate을 찾는다.<br>

- max_depth : 매우 작게 설정하여 5보다 깊어지지 않게 한다.<br>

GBM에서는 max_depth를 작게 설정하여 메모리를 적게 사용 및 빠른 예측을 하고<br>
깊지않은 트리모델을 많이 연결하여 성능을 좋게한다.<br>

<h3>bagging과 boosting의 차이</h3>

<img width="500" src="https://user-images.githubusercontent.com/54436228/115329188-ead28e80-a1cc-11eb-8a94-9d6a8df6ba4d.png">

> <h8>출처 : bkshin.tistory </h8>

bagging은 병렬 학습으로 여러 classifier가 독립적이다.<br>
boosting은 순차적 학습으로 오류에 가중치를 부여하여 여러 classfier를 거치는 동안 오류에 집중하게 되어 bagging에 비해 오류가 적어 성능이 좋다.<br>
하지만 순차적 학습이므로 속도가 느리고 overfitting 될 가능성이 있다.<br>

GBM의 단점을 해결한 모델은 XGBoost, LightGBM 이다.<br>

<h2>Stacking</h2>
