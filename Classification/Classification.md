<h2>Classification</h2>

예측하고자 하는 y변수가 discrete valued 갖는 경우

- 스팸메일인지 / 스팸메일이 아닌지
- 거래 사기인지 / 사기가 아닌지
- 암인지 / 암이아닌지 

위와 같은 문제처럼 negative class, positive class로 나눠 결과 도출하는 것을 classification이라고 한다.<br>
  
- binary classification : negative/positive 처럼 2가지 class로 분류
- multiclass classification : 3가지 이상의 class로 분류

binary classification에서 positive / negative class를 설정하는 기준은 **학습하고자 하는 대상**이다.<br>
> 기준이 정해져있는 것은 아니지만 일반적을 학습하고자 하는 대상에 기준을 둔다.
- 스팸메일 분류에서는 스팸 메일을 골라내야 하므로 : positive(스팸메일)
- 종양 분류에서는 악성 종양을 골라내야 하므로 : positive(di)
