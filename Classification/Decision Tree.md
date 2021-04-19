<h2>Decision Tree</h2>

특정 기준으로 데이터를 구분하는 매우 쉽고 유연하게 적용될 수 있는 모델이다.<br>
Data Scaling이나 Normalization 등의 사전 가공의 영향이 매우 적다.<br>
<img width="350" alt="스크린샷 2021-04-19 오전 11 03 59" src="https://user-images.githubusercontent.com/54436228/115172397-25222a00-a100-11eb-9d9d-be42877dc946.png">

하지만 layer가 늘어나면, node와 leap가 증가한다.<br>
즉, over fitting이 발생하기 때문에 성능 저하를 제어하는 설정이 필요하다.<br>

<h4>feature_importances_</h4>
DecisionClassifier 객체는 feature_importances_ 을 통해 예측애 중요한 Feature들을 선택해준다.<br>

<h3>Decision tree Overfitting</h3>

3가지 유형의 classification 샘플 데이터를 생성한다.<br>
<img width="300" alt="스크린샷 2021-04-19 오전 11 25 38" src="https://user-images.githubusercontent.com/54436228/115173405-2fddbe80-a102-11eb-989a-4a2e89fbe053.png">

<h4>결정 트리에 제약을 주지 않을 경우</h4>

> dt_clf = DecisionTreeClassifier().fit(X_features, y_labels)
<img width="300" alt="스크린샷 2021-04-19 오전 11 31 20" src="https://user-images.githubusercontent.com/54436228/115174333-09208780-a104-11eb-99ef-30e7c83ed3a0.png">
파란색/초록색으로 크게 분류된 영역 사이에 빨간 점으로 다시 분류된 경계가 있음을 알 수 있다.<br>


<h4>결정 트리에 최소 6개의 leaf노드가 설정되도록 제약을 주는 경우</h4>

> dt_clf = DecisionTreeClassifier(min_samples_leaf = 6).fit(X_features, y_labels)
<img width="300" alt="스크린샷 2021-04-19 오전 11 31 40" src="https://user-images.githubusercontent.com/54436228/115174342-0de53b80-a104-11eb-9ec4-1f0b7f7841ed.png">
크게 분류된 영역 사이에 다른 점이 존재해도 따로 분류되지 않은 예측 오류임을 알 수 있다.<br>
예측 오류지만, 새로운 데이터의 예측에 대해선 더 좋은 성능을 낼 수 있다.<br>
