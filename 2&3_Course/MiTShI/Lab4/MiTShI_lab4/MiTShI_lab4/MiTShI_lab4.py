import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input, Dense, Add
from tensorflow.keras.models import Model
from tensorflow.keras.layers import SimpleRNN
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

x_trn = np.linspace(0, 20, 80)
x_tst = np.linspace(20, 25, 20)
y = lambda x: np.cos(x / 2) + np.sin(x / 3)
z = lambda x: 0.5 * np.sin(x + y(x)) * np.cos(y(x))
y_trn = y(x_trn)
y_tst = y(x_tst)
z_trn = z(x_trn)
z_tst = z(x_tst)
X_train = np.vstack((x_trn, y_trn)).T
X_test = np.vstack((x_tst, y_tst)).T
Y_train = z_trn
Y_test = z_tst
def plot(Y_pred, label):
     plt.figure(figsize=(12, 8))
     plt.plot(x_tst, Y_test, label='Real data')
     plt.plot(x_tst, Y_pred, label=f'{label}')
     plt.xlabel('x')
     plt.ylabel('z')
     plt.title('Model`s result vs real data')
     plt.legend()
     plt.show()

plt.figure(figsize=(12, 8))
plt.plot(np.linspace(0, 25, 100), z(np.linspace(0, 25, 100)))
plt.xlabel('x')
plt.ylabel('z')
plt.title('Graph of the function')
plt.show()

def train_model(layers, neurons):
     model = Sequential()
     model.add(Dense(neurons, input_dim=2, activation='relu'))
     for _ in range(1, layers):
        model.add(Dense(neurons, activation='relu'))
     model.add(Dense(1, activation='linear'))
 
     model.compile(optimizer='adam', loss='mean_squared_error')
     history = model.fit(X_train, Y_train, epochs=100, batch_size=10, verbose=0, validation_split=0.2)
     Y_pred = model.predict(X_test)
     error = mean_absolute_error(Y_test, Y_pred)
     return history, error, Y_pred

results = {}
configurations = [(1, 10), (1, 20)]
for layers, neurons in configurations:
     history, error, pred = train_model(layers, neurons)
     results[f'Feed Forward {layers} Layer(s), {neurons} Neurons'] = error
     plot(pred, f'Feed Forward {layers} Layer(s), {neurons} Neurons')
for configuration, result in results.items():
     print(f"{configuration}: {result}")

def train_cascade_model(layers, neurons):
     inputs = Input(shape=(2,))
     resized_input = Dense(neurons, activation='relu')(inputs)
     x = Dense(neurons, activation='relu')(resized_input)
     for _ in range(1, layers):
        x = Dense(neurons, activation='relu')(x)
        x = Add()([x, resized_input])
     outputs = Dense(1, activation='linear')(x)
     model = Model(inputs=inputs, outputs=outputs)
     model.compile(optimizer='adam', loss='mean_squared_error')
     history = model.fit(X_train, Y_train, epochs=100, batch_size=10, verbose=0, validation_split=0.2)
 
     Y_pred = model.predict(X_test)
     error = mean_absolute_error(Y_test, Y_pred)
     return history, error, Y_pred

cascade_results = {}
cascade_configurations = [(1, 20), (2, 10)]
for layers, neurons in cascade_configurations:
     history, error, pred = train_cascade_model(layers, neurons)
     cascade_results[f'Cascade Forward {layers} Layer(s), {neurons} Neurons'] = error
     plot(pred, f'Cascade Forward {layers} Layer(s), {neurons} Neurons')
for configuration, result in cascade_results.items():
     print(f"{configuration}: {result}")

def train_elman_model(layers, neurons):
     model = Sequential()
     model.add(SimpleRNN(neurons, input_shape=(1, 2), return_sequences=True if layers > 1 else False))
     for _ in range(1, layers):
        model.add(SimpleRNN(neurons, return_sequences=True if _ < layers - 1 else False))
     model.add(Dense(1, activation='linear'))
     model.compile(optimizer='adam', loss='mean_squared_error')
     X_train_expanded = np.expand_dims(X_train, 1)
     X_test_expanded = np.expand_dims(X_test, 1)
     history = model.fit(X_train_expanded, Y_train, epochs=100, batch_size=10, verbose=0, validation_split=0.2)
     Y_pred = model.predict(X_test_expanded)
     error = mean_absolute_error(Y_test, Y_pred)
     return history, error, Y_pred

elman_results = {}
elman_configurations = [(1, 15), (3, 5)]
for layers, neurons in elman_configurations:
     history, error, pred = train_elman_model(layers, neurons)
     elman_results[f'Elman {layers} Layer(s), {neurons} Neurons'] = error
     plot(pred, f'Elman {layers} Layer(s), {neurons} Neurons')
for configuration, result in elman_results.items():
     print(f"{configuration}: {result}")
