Need to accurately predict [[Characteristics of Stock Movements]]
- However, since each vector is an *individual candlestick*, we need [[Descriptive Variables of Candlesticks]]


- Each vector needs to be a "candlestick" of the stock or similar
	- because a transformer predicts the next vector in a sequence of vectors.


- I hypothesize we will need a different vector space $W$ for each stock, because different stocks have different tendencies
.

- Let's predict the difference (positive or negative) of a candle stick as compared to the previous one (or the next ones difference from the current one in the context of prediction)
	- this price is a continuous variable. We can't use GloVe because it encodes discrete vector space
	- To maximize information contained in vector $w_i\in\mathbf{R}^n$, my first thought is either:
		1. An autoencoder
		2. **Variational** Autoencoder
			- This is preferred because it has a **smooth latent space** and a **Gaussian prior**, which makes sure all input combinations have a realistic output and prevents overfitting on certain types of candlesticks
	- However, there are a lot of options. Maybe we do a grid search to find the best? ![[Pasted image 20241109142813.png]]
