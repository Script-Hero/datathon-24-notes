import torch
import torch.nn as nn

class StockTransformer(nn.Module):
    def __init__(self, n_features, seq_length, n_heads=8, n_layers=6, d_model=512, d_ff=2048, dropout=0.1):
        """
        Initialize a transformer for stock sequence prediction
        
        Args:
            n_features (int): Number of features in each input vector
            seq_length (int): Length of input sequences (k)
            n_heads (int): Number of attention heads
            n_layers (int): Number of transformer layers
            d_model (int): Internal dimension for transformer operations
            d_ff (int): Dimension of feed forward network
            dropout (float): Dropout rate
        """
        super().__init__()
        
        self.n_features = n_features
        self.seq_length = seq_length
        self.d_model = d_model
        
        # Input projection layer
        self.input_projection = nn.Linear(n_features, d_model)
        
        # Positional encoding
        self.pos_encoding = self._create_positional_encoding()
        
        # Transformer encoder layers
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=d_ff,
            dropout=dropout,
            batch_first=True
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        
        # Output projection
        self.output_projection = nn.Linear(d_model, n_features)
        
    def _create_positional_encoding(self):
        """Create positional encodings for the input sequence"""
        pos_encoding = torch.zeros(self.seq_length, self.d_model)
        position = torch.arange(0, self.seq_length, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, self.d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / self.d_model))
        
        pos_encoding[:, 0::2] = torch.sin(position * div_term)
        pos_encoding[:, 1::2] = torch.cos(position * div_term)
        
        return pos_encoding.unsqueeze(0)
        
    def forward(self, x):
        """
        Forward pass through the transformer
        
        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, seq_length, n_features)
            
        Returns:
            torch.Tensor: Output predictions of shape (batch_size, seq_length, n_features)
        """
        # Project input to d_model dimensions
        x = self.input_projection(x)
        
        # Add positional encoding
        x = x + self.pos_encoding[:, :x.size(1), :].to(x.device)
        
        # Pass through transformer encoder
        x = self.transformer_encoder(x)
        
        # Project back to feature space
        output = self.output_projection(x)
        
        return output
