<h2>Confusion Matrix</h2>

Confusion Matrix 오차 행렬이란 binary Search의 예측 오류가 얼마이며, 어떤 유형의 예측 오류가 발생하고 있는지를 나타내는 지표이다.

<img width="750" alt="스크린샷 2021-04-22 오후 12 58 48" src="https://user-images.githubusercontent.com/54436228/115658601-09bf5500-a374-11eb-80e0-ec5185cb2319.png">

<h4>Positive(암인 경우) / Negative(암이 아닌 경우)</h4>

- TN (True Negative) : 실제 암이 아닌 경우를 -> 암이 아니라고 제대로 예측 
- FP (False Positive) : 실제 암이 아닌 경우를 -> 암이 맞다고 잘못 예측
- FN (False Negative) : 실제 암인 경우를 -> 암이 아니라고 잘못 예측 
- TP (True Positive) : 실제 암인 경우를 -> 암이 맞다고 제대로 예측

<h2>Accurary</h2>

Accuracy 정확도 = **(TN + TP)** / (TN + FP + FN + TP)<br>
전체 데이터에서 **제대로 얘측**한 비율이다.

하지만 데이터가 imbalanced 한 경우 사용하면 안된다.<br>
1000명중 998명은 암이 아니고 2명만 암인 경우 적합한 평가 지표가 아니다.<br>


<h2>Precision (PPV, Positive Predictive Value)</h2>

positive로 예측한 것 중 실제 값도 positive로 제대로 예측한 비율이다.
Precision 정밀도 = TP / (FP + TP)<br>

<h3>recall보다 precision이 상대적으로 중요한 지표가 되는 경우 : 스팸 메일</h3>


<h2>Recall</h2>

실제 값이 positive인것 중 positive로 제대로 예측한 비율이다.<br>
Recall 재현융 = TP / (FN + TP)<br>

<h3>precision보다 recall이 상대적으로 중요한 지표가 되는 경우 : 암 진단, 금융 사기 판별</h3>