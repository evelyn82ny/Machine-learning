<h2>House Prices - Advanced Regression Techniques</h2>
https://www.kaggle.com/c/house-prices-advanced-regression-techniques

<h3>Goal</h3>
It is your job to predict the sales price for each house. For each Id in the test set, you must predict the value of the SalePrice variable. 

<h3>Metric</h3>
Submissions are evaluated on Root-Mean-Squared-Error (RMSE) between the logarithm of the predicted value and the logarithm of the observed sales price. (Taking logs means that errors in predicting expensive houses and cheap houses will affect the result equally.)

***

<h4>target값 log변환하여 정규분포형태로 변환</h4>
<img width="550" alt="스크린샷 2021-04-18 오후 1 44 43" src="https://user-images.githubusercontent.com/54436228/115134568-41fd2580-a04c-11eb-9b0d-14898a9f2c11.png">

<h4>규제를 적용되지 않은 LinearRegression, Ridge, Lasso </h4>
<img width="291" alt="스크린샷 2021-04-19 오전 12 41 22" src="https://user-images.githubusercontent.com/54436228/115151477-009a6380-a0a8-11eb-956f-5c9abd0ca4df.png">

<img width="569" alt="스크린샷 2021-04-19 오전 12 43 35" src="https://user-images.githubusercontent.com/54436228/115151553-4d7e3a00-a0a8-11eb-82a2-a0d6deb82bf9.png">
