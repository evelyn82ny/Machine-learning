<h2>Encoding</h2>

sklearn의 ml 알고리즘은 모든 입력값을 숫자로 학습시킨다.<br>
그러므로 숫자가 아닌 다른 타입의 입력이 주어지는 경우 data preprocessing 후 학습을 진행해야 한다.<br>
이를 encoding이라고 한다.<br>

<h2>Label encoding</h2>

```python
items=['cpp', 'java', 'java', 'python', 'ruby','swift','ruby']
```

items을 label encoding 한 결과 : [0 1 1 2 3 4 3]<br>

- cpp : 0
- java : 1
- python : 2
- ruby : 3
- swift : 4

위와 같이 숫자로 인코딩 되었다.<br>

linear regression과 같은 ML 알고리즘은 숫자의 크고 작음이 영향을 줄 수 있으므로 위와 같이 적용되면 안된다.<br>

> tree 계열의 ml 알고리즘은 숫자의 특성에 영향받지 않으므로 상관없다.

<h2>One-Hot encoding</h2>

label encoding의 숫자 크고 작음의 문제를 해결하기 위해 feature 값의 유형에 따라 해당하는 column에만 1을 표시하고 나머지는 0으로 표시하는 방식이 One-Hot encoding 이다.<br>

```python
items=['cpp', 'java', 'java', 'python', 'ruby','swift','ruby']
```

<img width="200" alt="스크린샷 2021-05-10 오후 1 08 05" src="https://user-images.githubusercontent.com/54436228/117604824-4fac5380-b191-11eb-8a11-ff7258fce05a.png">

- cpp    : 1 0 0 0 0
- java   : 0 1 0 0 0
- python : 0 0 1 0 0
- ruby   : 0 0 0 1 0
- swift  : 0 0 0 0 1

items을 one-hot encoding 한 결과는 다음과 같다.<br>
하지만 아래와 같이 과정이 복잡하다.<br>

```python
encoder=LabelEncoder()
encoder.fit(items)      # 일단 label encoding을 한다.
labels=encoder.transform(items)

labels=labels.reshape(-1,1)  # 2차원으로 변경한다.

oh_encoder=OneHotEncoder()
oh_encoder.fit(labels)
oh_labels=oh_encoder.transform(labels)
```

<h2>get_dummies()</h2>

pandas의 get_dummies()를 사용할 경우 위의 과정을 알아서 다 처리해준다.<br>

```python
import pandas as pd

df=pd.DataFrame({'item':['cpp', 'java', 'java', 'python', 'ruby','swift','ruby']})
pd.get_dummies(df)
```

<img width="450" alt="스크린샷 2021-05-10 오후 1 19 55" src="https://user-images.githubusercontent.com/54436228/117605391-86369e00-b192-11eb-99c8-fed2f806e843.png">
