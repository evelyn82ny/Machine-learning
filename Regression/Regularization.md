<h2>Regularization</h2>

regression coefficient가 기하급수적으로 커지면서 overfitting이 발생된다.<br>
overfitting은 새로운 Data에 대한 예측 성능이 낮아지므로 이를 해결하기 위한 regularization이 필요하다.<br> 

**regularization는 모든 특성을 유지하되 𝜃에 영향을 주는 magnitude/values 를 줄이는 방식이다.**<br>

아래 그래프의 경우 demension이 높은 𝜃3, 𝜃4을 최소화 해야한다.<br>
𝜃3, 𝜃4를 0에 근접하게될수록 2차함수 형태로 간단해지며 overfitting하는 경향이 줄어든다.<br>
<img width="746" alt="스크린샷 2021-04-21 오후 12 02 21" src="https://user-images.githubusercontent.com/54436228/115490665-7d406400-a299-11eb-94e5-a8f2057c66cd.png">

𝜃3, 𝜃4에 penalty를 부여하여 최적화된 θ을 구한 뒤, 다시 penalty를 제거하는 방식이다.<br>

θ에 penalty를 부여하는 cost function은 다음과 같다.<br>
<img width="704" alt="스크린샷 2021-04-21 오후 12 02 31" src="https://user-images.githubusercontent.com/54436228/115490669-7f0a2780-a299-11eb-80d4-06dd5a3f77d9.png">

위 식에서 λ는 Regularization parameter로 cost fuction와 regularization의 균형 유지를 통해 모델을 simple하게 만들어 overfitting을 줄인다.<br>
λ가 너무 커지면 θ의 총합의 영향이 줄어 𝜃0만 남게 되는 underfitting 되므로 적절한 값을 설정해야 한다.<br>
 
