from __future__ import annotations

import tensorflow as tf
import keras


class Animal:
    def __init__(self):
        print("This is Animal class")

class Dog(Animal):
    def __init__(self, a: str):
        super().__init__()
        self.a = a
        print(f"This is passed value: {self.a}")
        print("This is Dog class")

class CustomTFModel:
    def __init__(self, layers: list[int]):
        self.model_layers = []
        for i in range(len(layers) - 1):
            self.model_layers.append(
                keras.layers.Dense(
                    layers[i + 1],
                    activation='sigmoid',
                    use_bias=True,
                    kernel_initializer='glorot_uniform'
                )
            )
        self.loss_fn = None
        self.optimizer = None

    def forward(self, x):
        for layer in self.model_layers:
            x = layer(x)
    
    def compile(self, loss='mse', optimizer='sgd', learning_rate=0.01):
        """Set loss function and optimizer manually"""
        if loss == 'mse':
            self.loss_fn = keras.losses.MeanSquaredError()
        elif loss == 'binary_crossentropy':
            self.loss_fn = keras.losses.BinaryCrossentropy()
        else:
            raise ValueError(f"Loss '{loss}' not supported.")

        if optimizer == 'sgd':
            self.optimizer = keras.optimizers.SGD(learning_rate)
        elif optimizer == 'adam':
            self.optimizer = keras.optimizers.Adam(learning_rate)
        else:
            raise ValueError(f"Optimizer '{optimizer}' not supported.")

    def fit(self, X, y, epochs=100, verbose=True):
        """Custom training loop (like model.fit)"""
        X = tf.convert_to_tensor(X, dtype=tf.float32)
        y = tf.convert_to_tensor(y, dtype=tf.float32)

        for epoch in range(epochs):
            with tf.GradientTape() as tape:
                y_pred = self.forward(X)
                loss = self.loss_fn(y, y_pred)

            grads = tape.gradient(loss, self.get_trainable_variables())
            self.optimizer.apply_gradients(zip(grads, self.get_trainable_variables()))

            if verbose:
                print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.numpy():.4f}")

    def get_trainable_variables(self):
        """Collect trainable variables from all layers"""
        variables = []
        for layer in self.model_layers:
            variables += layer.trainable_variables
        return variables

    def predict(self, X):
        """Predict using the trained model"""
        X = tf.convert_to_tensor(X, dtype=tf.float32)
        return self.forward(X).numpy()


if __name__ == "__main__":
    import numpy as np
    d = Dog("cat")

    # XOR dataset
    X = np.array([[0,0], [0,1], [1,0], [1,1]], dtype=np.float32)
    y = np.array([[0], [1], [1], [0]], dtype=np.float32)

    model = CustomTFModel([2, 8, 1])  # 2 input, 1 hidden with 8 units, 1 output
    model.compile(loss='mse', optimizer='adam', learning_rate=0.1)
    model.fit(X, y, epochs=500)

    print("Predictions:")
    print(model.predict(X))