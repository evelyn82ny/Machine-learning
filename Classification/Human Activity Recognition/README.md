<h2>Human Activity Recognition Using Smartphones Data Set</h2>

https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones

스마트폰 센서를 장착한 뒤 사람의 동작과 관련된 여러가지 feature를 수집한 데이터로<br>
결정 트리를 이용해 어떤 동작인지 예측한다.<br>

<h3>제약없는 결정 트리의 경우</h3>

결정 트리 예측 정확도 : **0.8548**<br>
<img width="739" alt="스크린샷 2021-04-19 오후 12 18 34" src="https://user-images.githubusercontent.com/54436228/115177788-e776ce80-a10a-11eb-90f6-5f0092591a66.png">

<h3>max_depth 설정한 결정 트리의 경우</h3>

> max_depths = [ 6, 8 ,10, 12, 16 ,20, 24]
<img width="350" alt="스크린샷 2021-04-19 오후 1 21 12" src="https://user-images.githubusercontent.com/54436228/115181169-4b50c580-a112-11eb-93a1-f814554aba4c.png">


depth = 8 일 때 **accuracy : 0.870716** 으로 가장 높고<br>
depth = 16 일 때 **mean_test_score : 0.851344** 으로 가장 최적이며, **accuracy : 0.857482** 이다.<br>

<h3>min_samples_split 까지 설정한 결정 트리의 경우</h3>

>params = {
    'max_depth' : [ 8 , 12, 16 ,20], 
    'min_samples_split' : [16,24],
}

> best_df_clf = grid_cv.best_estimator_<br>
best_estimator_ 사용하여 최적의 파라미터로 바로 예측한다.

<img width="530" alt="스크린샷 2021-04-19 오후 1 26 33" src="https://user-images.githubusercontent.com/54436228/115181430-e77acc80-a112-11eb-995c-bd6c77c323d5.png">

최적 파라미터에서의 예측 정확도는 **0.8717** 로 이전보다 증가함을 알 수 있다.<br>

<h3>best_estimator_ 사용하여 일부 feature 출력</h3>

<img width="556" alt="스크린샷 2021-04-19 오후 1 32 25" src="https://user-images.githubusercontent.com/54436228/115181848-be0e7080-a113-11eb-9081-f55a183c279c.png">
