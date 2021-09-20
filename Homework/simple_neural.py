import numpy as np  # подключаем библиотеку NumPy


def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # инициализируем функцию - сигмоид


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])  # массив входных данных (примеров)

training_outputs = np.array([[0, 1, 1, 0]]).T  # транспонированный массив ответов на примеры

synaptic_weights = 2 * np.random.random((3, 1)) - 1  # инициализируем массив весов с помощью генератора случайных чисел
# Меод обратного распространения
for _ in range(20000):
    input_layer = training_inputs
    # подставляем скалярное произведение весов и входных данных в функцию активации
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    # вычисляем ошибку
    err = training_outputs - outputs
    # вычисляем корректировки к весам
    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    # корректируем веса
    synaptic_weights += adjustments

print('Данные после обучения:', outputs, sep='\n')
# Даём сети новые данные для решения задачи
new_inputs = np.array([1, 1, 0])  # новый массив для решения
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print('Решение новой задачи: ', output)
