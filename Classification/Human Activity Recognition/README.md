<h2>Human Activity Recognition Using Smartphones Data Set</h2>

https://archive.ics.uci.edu/ml/datasets/human+activity+recognition+using+smartphones

스마트폰 센서를 장착한 뒤 사람의 동작과 관련된 여러가지 feature를 수집한 데이터로<br>
결정 트리를 이용해 어떤 동작인지 예측한다.<br>

<h3>제약없는 결정 트리의 경우</h3>

결정 트리 예측 정확도 : **0.8548**<br>
<img width="739" alt="스크린샷 2021-04-19 오후 12 18 34" src="https://user-images.githubusercontent.com/54436228/115177788-e776ce80-a10a-11eb-90f6-5f0092591a66.png">

<h3>max_depth 설정한 결정 트리의 경우</h3>

> max_depths = [ 6, 8 ,10, 12, 16 ,20, 24]
<img width="272" alt="스크린샷 2021-04-19 오후 12 42 58" src="https://user-images.githubusercontent.com/54436228/115178988-53f2cd00-a10d-11eb-9cf2-9425eb339152.png">

depth = 8 일 때 **accuracy : 0.870716** 으로 가장 높고<br>
depth = 16 일 때 **mean_test_score : 0.851344** 으로 가장 최적임을 알 수 있다.<br>
