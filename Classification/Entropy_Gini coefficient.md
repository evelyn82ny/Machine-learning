<h2>Entropy</h2>
entropy는 주어진 데이터 집합의 impurity를 의미한다.<br>
주어진 데이터 집합에 같은 종류의 데이터가 많으면 entropy가 낮고,<br>
다른 종류의 데이터가 많으면 entropy가 높다.<br>

0과 1사이의 값을 가지며 1로 갈수록 혼합도가 높고, 0으로 갈수록 같은 데이터가 많은 혼합도가 적음을 의미한다.<br>

<h2>Infomation Gain 정보이득</h2>
Entropy을 기반으로 하며, Decision tree는 정보이득이 커지는 방향으로 분할 기준을 정한다.<br>
<img width="400" alt="스크린샷 2021-04-19 오후 2 14 15" src="https://user-images.githubusercontent.com/54436228/115184819-928e8480-a119-11eb-9767-a3acb1f6460e.png">
상위노드의 entropy에서 하위노도의 enttopy의 총합을 뺀다.<br>
즉, 특성 속성을 기준으로 entropy의 감소량에 대한 기대치를 의미한다.<br><br>

entropy는 0에 가까워질수록 impurity가 줄어든다.<br>
entropy가 줄어들수록 information gain이 커진다.<br>
그러므로 information gain이 더 큰 속성을 기준으로 구분한다.<br>

<h2>Gini coefficient</h2>

<img width="350" alt="스크린샷 2021-04-19 오후 2 28 33" src="https://user-images.githubusercontent.com/54436228/115185916-be126e80-a11b-11eb-9efb-aadfab72859b.png">

- A영역 : 붎평등 면적 (로렌츠 곡선과 완전균형 대각선과의 사이)
- B영역 : 삼각형 전체면적 - A영역

<img width="168" alt="스크린샷 2021-04-19 오후 2 28 46" src="https://user-images.githubusercontent.com/54436228/115186118-147fad00-a11c-11eb-8b73-0dd7cd4ed744.png">

<h4>0, 평등</h4>
로렌츠곡선이 완전균형 대각선에 수렴하여 일치될 때, A영역은 B영역에 의해 없어진다.<br>
지니 계수가 0으로 갈수록 데이터의 균일도가 높은 평등함을 의미한다.<br>
**즉, 지니 계수가 낮은 속성을 기준으로 분할한다.**<br>
<img width="216" alt="스크린샷 2021-04-19 오후 2 28 54" src="https://user-images.githubusercontent.com/54436228/115186142-219c9c00-a11c-11eb-8a3d-0ae82ea851fb.png">

<h4>1, 불평등</h4>
지니계수가 1로 갈수록 데이터의 impurity가 높은 불평등함을 의미한다.<br>
<img width="231" alt="스크린샷 2021-04-19 오후 2 29 14" src="https://user-images.githubusercontent.com/54436228/115186413-9ff93e00-a11c-11eb-8de4-a89c570ea8ed.png">

