from matplotlib import pyplot as plt
import numpy as np
import random

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def target_function(x, y):
    return np.sin(x) + np.cos(y / 2)

class NeuralNetwork:
    def __init__(self):
        self.weights1 = np.random.rand(2, 4)
        self.weights2 = np.random.rand(4, 8)
        self.weights3 = np.random.rand(8, 12)
        self.weights4 = np.random.rand(12, 8)
        self.weights5 = np.random.rand(8, 8)
        self.weights6 = np.random.rand(8, 1)

    def forward_propagate(self, inputs):
        self.layer1 = sigmoid(np.dot(inputs, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        self.layer3 = sigmoid(np.dot(self.layer2, self.weights3))
        self.layer4 = sigmoid(np.dot(self.layer3, self.weights4))
        self.layer5 = sigmoid(np.dot(self.layer4, self.weights5))
        self.output = sigmoid(np.dot(self.layer5, self.weights6))
        return self.output

    def calculate_error(self, target):
        return np.mean(np.square(self.output - target))
    
class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = [NeuralNetwork() for _ in range(population_size)]

    def calculate_fitness(self, x, y, z):
        fitness_scores = []
        for network in self.population:
            output = network.forward_propagate(np.array([x, y]))
            error = np.mean(np.square(output - z))
            fitness_scores.append(1 / (error + 1e-6))
        return fitness_scores

    def select_parents(self, fitness_scores):
        parents = random.choices(self.population, weights=fitness_scores, k=2)
        return parents

    def crossover(self, parent1, parent2):
        child = NeuralNetwork()
        for child_weights, p1_weights, p2_weights in zip([child.weights1, child.weights2, child.weights3, child.weights4, child.weights5, child.weights6],
[parent1.weights1, parent1.weights2, parent1.weights3, parent1.weights4, parent1.weights5, parent1.weights6],
[parent2.weights1, parent2.weights2, parent2.weights3, parent2.weights4, parent2.weights5, parent2.weights6]):
            crossover_point = random.randint(0, len(p1_weights))
            child_weights[:crossover_point] = p1_weights[:crossover_point]
            child_weights[crossover_point:] = p2_weights[crossover_point:]
        return child

    def mutate(self, network):
        for weights in [network.weights1, network.weights2, network.weights3, network.weights4]:
            mutation_mask = np.random.rand(*weights.shape) < self.mutation_rate
            weights += np.random.randn(*weights.shape) * mutation_mask * 0.1
        return network

    def run_generation(self, x, y, z):
        fitness_scores = self.calculate_fitness(x, y, z)
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = self.select_parents(fitness_scores)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            new_population.append(child)
        self.population = new_population
        return min(fitness_scores)
    
population_size = 10
mutation_rate = 0.01
generations = 100

genetic_algorithm = GeneticAlgorithm(population_size, mutation_rate)
x_for_training = np.linspace(-1.5, 1.5, 31)
y_for_training = np.linspace(-1.5, 1.5, 31)

for generation in range(generations):
    generation_min_fitnesses = []
    for x in x_for_training:
        for y in y_for_training:
            z = target_function(x, y)
            generation_min_fitnesses.append(genetic_algorithm.run_generation(x, y, z))
            
best_network = genetic_algorithm.population[0]
errors = []
for x in x_for_training:
    for y in y_for_training:
        z = target_function(x, y)
        prediction = best_network.forward_propagate(np.array([x, y]))
        error = np.mean(np.square(prediction - np.array([z])))
        errors.append(error)
print("Results:")
for i, (x, y) in enumerate(zip(x_for_training, y_for_training)):
    print(f"Input Parameters: ({round(x, 1)}, {round(y, 1)}), Squared Error: {errors[i]};")
    
Z_nn = np.zeros((31, 31))
x_values = np.linspace(-1.5, 1.5, 31)
y_values = np.linspace(-1.5, 1.5, 31)
z_values = np.array([[target_function(x, y) for x in x_values] for y in y_values])
for i, x in enumerate(x_values):
    for j, y in enumerate(y_values):
        prediction = best_network.forward_propagate(np.array([x, y]))
        Z_nn[i, j] = prediction[0]
fig = plt.figure(figsize=(12, 6))
X, Y = np.meshgrid(x_values, y_values)
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X, Y, z_values, cmap='YlOrRd', edgecolor='none')
ax1.set_title('Target')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z_nn, cmap='YlOrRd', edgecolor='none')
ax2.set_title('Approximation')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)
plt.show()
error_matrix = np.reshape(errors, (31, 31))
X, Y = np.meshgrid(x_values, y_values)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, error_matrix, cmap='YlOrRd')
plt.colorbar(surf)
ax.set_title('Error Distribution')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Squared Error')
plt.show()

