import numpy as np 
import matplotlib.pyplot as plt 
import skfuzzy as fuzz 
from tabulate import tabulate 
from sklearn.metrics import mean_squared_error, mean_absolute_error

def get_y(x): 
    return np.cos(x/2) + np.sin(x/3) 

def get_z(x, y): 
    return 0.5 * np.sin(x + y) * np.cos(y) 

# Get values 
x_values = np.linspace(0, 25, 100) 
y_values = get_y(x_values) 
z_values = get_z(x_values, y_values) 

# Plot function Y 
plt.plot(x_values, y_values) 
plt.title("Function Y") 
plt.show() 

# Plot function Z 
plt.plot(x_values, z_values) 
plt.title("Function Z") 
plt.show() 

# Numbers of membership functions
mf_num_input = 6 
mf_num_output = 9 

# Means 
x_means = np.linspace(min(x_values), max(x_values), mf_num_input) 
y_means = np.linspace(min(y_values), max(y_values), mf_num_input) 
z_means = np.linspace(min(z_values), max(z_values), mf_num_output) 

# Sigmas 
x_sigma = (max(x_values) - min(x_values)) / mf_num_input / 2 
y_sigma = (max(y_values) - min(y_values)) / mf_num_input / 2 
z_sigma = (max(z_values) - min(z_values)) / mf_num_output / 2 

# Gaussian fuzzy membership functions 
x_mf_gaussian = [fuzz.gaussmf(x_values, x_means[i], x_sigma) for i in 
    range(mf_num_input)] 
y_mf_gaussian = [fuzz.gaussmf(np.linspace(min(y_values), max(y_values), 100), 
    y_means[i], y_sigma) for i in range(mf_num_input)] 
z_mf_gaussian = [fuzz.gaussmf(np.linspace(min(z_values), max(z_values), 100), 
    z_means[i], z_sigma) for i in range(mf_num_output)] 

# Plot gaussfm for X 
for i in range(mf_num_input): 
    plt.plot(x_values, x_mf_gaussian[i]) 
plt.title("Gaussmf for X") 
plt.show() 

# Plot gaussfm for Y 
for i in range(mf_num_input): 
    plt.plot(np.linspace(min(y_values), max(y_values), 100), y_mf_gaussian[i]) 
plt.title("Gaussmf for Y") 
plt.show() 

# Plot gaussfm for Z 
for i in range(mf_num_output): 
    plt.plot(np.linspace(min(z_values), max(z_values), 100), z_mf_gaussian[i]) 
plt.title("Gaussmf for Z") 
plt.show() 

# Get number of best function for value 
def get_fun_num(value, means, sigma): 
    best_func_value = -float("inf") 
    best_index = -1 
    for index, mean in enumerate(means): 
         if fuzz.gaussmf(value, mean, sigma) > best_func_value: 
             best_func_value = fuzz.gaussmf(value, mean, sigma) 
             best_index = index 
    return best_index 

# Table of values 
print("Values' table:") 
table = [["y\\x"] + [str(x) for x in x_means]] 
for y_value in y_means: 
     row = [round(y_value, 2)] 
     for x in x_means: 
        z = get_z(x, y_value) 
        row.append(round(z, 2)) 
     table.append(row) 
print(tabulate(table, tablefmt="grid")) 

# Table of function's name 
rules = {} 
print("Function's name's table:") 
table = [["y\\x"] + ["mx" + str(i) for i in range(1, mf_num_input + 1)]] 
for i in range(mf_num_input): 
     row = ["my" + str(i + 1)] 
     for j in range(mf_num_input): 
         z = get_z(x_means[j], y_means[i]) 
         best_func = get_fun_num(z, z_means, z_sigma) 
         row.append("mf" + str(best_func + 1)) 
         rules[(j, i)] = best_func 
     table.append(row) 
print(tabulate(table, tablefmt="grid")) 

# Print rules 
print("\nRules:") 
for rule in rules.keys(): 
    print(f"if (x is mx{rule[0] + 1}) and (y is my{rule[1] + 1}) then (z is mf{rules[rule] + 1})") 

# Model 
z_output = [] 
for x in x_values: 
    best_x_func = get_fun_num(x, x_means, x_sigma) 
    best_y_func = get_fun_num(get_y(x), y_means, y_sigma) 
    best_z_func = rules[(best_x_func, best_y_func)] 
    z_output.append(z_means[best_z_func]) 

# Plot results 
plt.plot(x_values, z_output, label="Model") 
plt.plot(x_values, z_values, label="True") 
plt.title("True func and model func") 
plt.legend() 
plt.show() 
# Get scores 
mse = mean_squared_error(z_values, z_output) 
mae = mean_absolute_error(z_values, z_output) 
print(f"\nMean Squared Error (MSE): {mse}") 
print(f"Mean Absolute Error (MAE): {mae}")
