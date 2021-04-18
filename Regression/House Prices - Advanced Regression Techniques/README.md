<h2>House Prices - Advanced Regression Techniques</h2>
https://www.kaggle.com/c/house-prices-advanced-regression-techniques

<h3>Goal</h3>
It is your job to predict the sales price for each house. For each Id in the test set, you must predict the value of the SalePrice variable. 

<h3>Metric</h3>
Submissions are evaluated on Root-Mean-Squared-Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price. (Taking logs means that errors in predicting expensive houses and cheap houses will affect the result equally.)

***

<h4>target값 log변환하여 정규분포형태로 변환</h4>
<img width="550" alt="스크린샷 2021-04-18 오후 1 44 43" src="https://user-images.githubusercontent.com/54436228/115134568-41fd2580-a04c-11eb-9b0d-14898a9f2c11.png">

<h4>규제를 적용하지 않은 LinearRegression, Ridge, Lasso </h4>
<img width="291" alt="스크린샷 2021-04-19 오전 12 41 22" src="https://user-images.githubusercontent.com/54436228/115151477-009a6380-a0a8-11eb-956f-5c9abd0ca4df.png">

<img width="569" alt="스크린샷 2021-04-19 오전 12 43 35" src="https://user-images.githubusercontent.com/54436228/115151553-4d7e3a00-a0a8-11eb-82a2-a0d6deb82bf9.png">

<h4>K-5 교차검증한 결과</h4>
<img width="456" alt="스크린샷 2021-04-19 오전 12 45 49" src="https://user-images.githubusercontent.com/54436228/115151612-9df59780-a0a8-11eb-826c-c4ac128fb9ad.png">

<h4>최적의 alpha값으로 K-5 교차검증한 결과</h4>
<img width="438" alt="스크린샷 2021-04-19 오전 12 49 59" src="https://user-images.githubusercontent.com/54436228/115151742-34c25400-a0a9-11eb-8868-d4c5e4e8f7b9.png">
<img width="528" alt="스크린샷 2021-04-19 오전 12 53 41" src="https://user-images.githubusercontent.com/54436228/115151861-b619e680-a0a9-11eb-94d4-ca95eb7d972c.png">

<h4>이상치 제거 후, K-5 교차검증한 결과</h4>
![스크린샷 2021-04-19 오전 12 57 10](https://user-images.githubusercontent.com/54436228/115152105-bb2b6580-a0aa-11eb-8e33-a0ab7fe7983f.jpeg)

<img width="441" alt="스크린샷 2021-04-19 오전 12 57 36" src="https://user-images.githubusercontent.com/54436228/115152106-bebeec80-a0aa-11eb-9368-2a1e954a2351.png">

<img width="539" alt="스크린샷 2021-04-19 오전 1 01 55" src="https://user-images.githubusercontent.com/54436228/115152137-dac28e00-a0aa-11eb-9a6a-082a7bac0d6d.png">





