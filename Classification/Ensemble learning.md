<h2>Ensemble learning</h2>

여러 개의 Weak Classifier를 생성하고, 그 예측을 결합하여 보다 정확한 Strong Classifier를 통해 최종 예측을 도출하는 기법<br><br>
random forest 및 boosting algorithm들은 decision tree 알고리즘을 기반으로 한다.<br>
decision tree의 단점인 overfitting을 많은 classifier르 결합하여 보완하고,<br>
장점인 직관적인 분류 기준은 강화된다.<br>

<h3>Voting</h3>

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

<h3>Bagging (Bootstrap Aggregating)</h3>
모두 같은 알고리즘을 갖는 classifier이지만, sampling data set을 서로 다르게 가져가면서 학습을 수행하는 방식<br>

<h4>Random forest</h4>
bagging의 대표적인 알고리즘은 random forest이다.<br>
여러 개의 decision tree classifier가 전체 데이터에서 bagging 방식으로 각자의 데이터를 sampling하여 개별적으로 학습으 수행한 뒤, 최종적으로 모든 classifier가 vorting을 통해 예측 결정한다.<br>
개별적인 classifier의 기반 알고리즘은 decision tree이지만, 개별 트리가 학습하는 데이터 세트는 전체 데이터에서 일부가 중첩되게 sampling 된다.<br>

여러개의 데이터 세트를 중첩되게 분리하는 것을 **bootstrapping** 분할 방식이라고 한다.<br>

<h3>Boosting</h3>
<h3>Stacking</h3>
