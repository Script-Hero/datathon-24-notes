Need to accurately predict [[Characteristics of Stock Movements]]
- However, since each vector is an *individual candlestick*, we need [[Descriptive Variables of Candlesticks]]


- Each vector needs to be a "candlestick" of the stock or similar
	- because a transformer predicts the next vector in a sequence of vectors.


- I hypothesize we will need a different vector space $W$ for each stock, because different stocks have different tendencies


- Let's predict the difference (positive or negative) of a candle stick as compared to the previous one (or the next ones difference from the current one in the context of prediction)
	- 
