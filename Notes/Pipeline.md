1. Start with a set of candlesticks from your favorite API type shit 
2. Using the encoder of the VAE, convert each candle stick to a vector
	1. This is because the input to the transformer model has to be a set of vectors. We use the above fancy method of constructing the embedding vectors to maximize the information contained in each one 
3. The transformer outputs the probability distribution of the next candlestick in the sequence
4. We feed this probability distribution to the AAC model to make a buy / sell / wait decision