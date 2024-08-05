def hebb_network(letters, expected_result, neurons_number): 
     for index in range(neurons_number): 
         letters[index] = [1] + letters[index] 
     weights = [[0] * len(letters[0]) for _ in range(neurons_number)]  
     # calculate weights 
     for index_of_letter in range(neurons_number): 
         for index_of_neuron in range(neurons_number): 
             for index_of_weight in range(len(weights[index_of_neuron])): 
                 weights[index_of_neuron][index_of_weight] += letters[index_of_letter][index_of_weight] * expected_result[index_of_letter][index_of_neuron] 
     # calculate output 
     actual_result = calculate_output(letters, weights, neurons_number) 
     # check ending rule 
     if actual_result == expected_result: 
         return weights 
     raise Exception('There is unsolvable problem of weight adaptation. Weights: ' + str(weights)) 

def calculate_output(letters, weights, neurons_number): 
     actual_result = [] 
     for index_of_letter in range(len(letters)): 
        letter_result = [] 
        for index_of_neuron in range(neurons_number): 
           s = 0 
           for index_of_weight in range(len(weights[index_of_neuron])): 
                s += weights[index_of_neuron][index_of_weight] * letters[index_of_letter][index_of_weight] 
           if s > 0: 
                letter_result += [1] 
           else: 
                letter_result += [-1] 
        actual_result += [letter_result] 
     return actual_result 

# letters 
v = [ 1, -1, 1, 
 1, -1, 1, 
 -1, 1, -1] 
l = [ 1, -1, -1, 
 1, -1, -1, 
 1, 1, 1] 
a = [ -1, 1, -1, 
 1, 1, 1, 
 1, -1, 1] 
y = [1, -1, 1, 
 -1, 1, -1, 
 -1, 1, -1] 

# expected result 
expected_result = [[ 1, -1, -1, -1], 
 [-1, 1, -1, -1], 
 [-1, -1, 1, -1], 
 [-1, -1, -1, 1]] 

# train network 
train_letters = [v, l, a, y] 
number_of_neurons = len(train_letters) 
final_weights = hebb_network(train_letters, expected_result, number_of_neurons) 
print("Weights:") 
for weights in final_weights:
    print(weights)

# test network 
mistake1 = [ -1, 1, -1, 
 1, 1, 1, 
 1, 1, 1] # a with mistake 
mistake2 = [ 1, -1, -1, 
 1, -1, -1, 
 1, -1, 1] # l with mistake 

letters_with_mistakes = [v, l, a, y, mistake1, mistake2] 
# add x0 = 1 to every letter 
for index in range(len(letters_with_mistakes)): 
     letters_with_mistakes[index] = [1] + letters_with_mistakes[index] 
actual_result = calculate_output(letters_with_mistakes, final_weights, number_of_neurons) 
print("\nResult (V, L, A, Y, A with mistake, L with mistake):")
for res in actual_result:
    print(res)
