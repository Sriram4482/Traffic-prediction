import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class DQN:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.model = self.build_model()

    def build_model(self):
        model = Sequential([
            Dense(24, input_dim=self.state_size, activation="relu"),
            Dense(24, activation="relu"),
            Dense(self.action_size, activation="linear")
        ])
        model.compile(loss="mse", optimizer=Adam(learning_rate=0.001))
        return model

    def predict_action(self, state):
        return np.argmax(self.model.predict(np.array([state]))[0])

# Example Usage:
dqn = DQN(state_size=4, action_size=3)
state = np.array([5, 3, 2, 6])  # Example lane vehicle counts
action = dqn.predict_action(state)
print("Predicted Action:", action)
