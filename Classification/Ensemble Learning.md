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

- Categorical Data : Voting으로 결과 집계
- Continuous Data : average로 결과 집계

<h3>Random forest</h3>
bagging의 대표적인 알고리즘은 random forest이다.<br>
여러 개의 decision tree classifier가 전체 데이터에서 bagging 방식으로 각자의 데이터를 sampling하여 개별적으로 학습으로 수행한 뒤, 최종적으로 모든 classifier가 vorting을 통해 예측 결정한다.<br>

<img width="700" src="https://user-images.githubusercontent.com/54436228/115263427-62be9b80-a170-11eb-8261-f361df9304a2.png">

> <h8> 출처 : tensorflow blog/h8>

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


<h3>Stacking</h3>
