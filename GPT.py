import numpy as np
import random
import matplotlib.pyplot as plt

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

#Required for everything
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
IND_SIZE = 10
Num_Iter = 300
toolbox = base.Toolbox()
toolbox.register("attribute", random.random)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attribute, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evaluate(individual):
    return sum(individual),

toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)
#MAKE POPULATION
# popy = toolbox.population(n=50)

# result = algorithms.eaSimple(popy,toolbox,0.8,0.2,Num_Iter)
# print(result)
# for i in result:
#     print(i)
#     for j in i:
#         print(j)


#INIT
#Create Population, 
clean_population = toolbox.population(IND_SIZE)
for child in clean_population:
    eval = toolbox.evaluate(child) 
    child.fitness.values = eval
#Check Fittness Calculation

#Terminate If Good Enough
#If Not, Select top X
for i in range(Num_Iter):
    fought_population = toolbox.select(clean_population,len(clean_population))

    MateRate = 0.4
    MutationRate = 0.2
    #Mating
    for child1 in fought_population:
        for child2 in fought_population:
                if random.random() < MateRate:
                    toolbox.mate(child1, child2)
                    #Remove the fitness, so we can recheck them 
                    del child1.fitness.values
                    del child2.fitness.values
    #Mutate
    for child in fought_population:
        if random.random() < MutationRate:
                toolbox.mutate(child1) 
                del child.fitness.values
    #Evaluate
    #Init printing list. 
    ending = []

    #Main loop
    for child in fought_population:
        #ONly check those without a valid fitness. 
        if not child.fitness.valid:
            #Get an eval value 
            eval = toolbox.evaluate(child) 
            child.fitness.values = eval
            ending.append(eval)
        
    if eval == None:
        print("Terminate")
    clean_population[:] = fought_population




#STTEMPTING TO PLOT>
final_cur = []
final_neg_cur = []
for i in fought_population:
    print(i)
    cur = 0
    neg_cur = 0
    for x in i:
        if x > 0:
             cur += x
        else:
             neg_cur += x
    final_cur.append(cur)
    final_neg_cur.append(neg_cur)
print(final_cur)

plt.plot(final_cur,final_neg_cur,'o')
plt.show()

     
        



'''

"""MAP-ELITE SECTION GPT generated"""
# Define the fitness function (to be maximized)
def fitness_function(x, y):
    return np.sin(x) * np.cos(y)

# Define the behavior characterization function
def behavior_characterization(x, y):
    return np.floor(x * 10), np.floor(y * 10)

# Initialize parameters
population_size = 100
num_iterations = 1000
archive_grid = {}

# Main loop
for _ in range(num_iterations):
    # Generate random solutions
    solutions = np.random.rand(population_size, 2)  # Each row represents [x, y]

    # Evaluate fitness and behavior for each solution
    fitness_values = fitness_function(solutions[:, 0], solutions[:, 1])
    behaviors = np.array([behavior_characterization(x, y) for x, y in solutions])

    # Update archive
    for i in range(population_size):
        behavior = tuple(behaviors[i])
        if behavior not in archive_grid or fitness_values[i] > archive_grid[behavior][0]:
            archive_grid[behavior] = (fitness_values[i], solutions[i])

    # Selection and variation (elitist selection)
    elite_indices = np.argsort(-fitness_values)[:population_size // 2]
    elite_solutions = solutions[elite_indices]

    # Perform variation (e.g., mutation)
    mutated_solutions = elite_solutions + np.random.normal(scale=0.1, size=elite_solutions.shape)
    print(mutated_solutions.size)
    # Replace the old population with the mutated elite solutions
    solutions[:len(mutated_solutions)] = mutated_solutions

# Get the best solution from the archive
best_fitness = -np.inf
best_solution = None
for behavior, (fitness, solution) in archive_grid.items():
    if fitness > best_fitness:
        best_fitness = fitness
        best_solution = solution

print("Best solution found:", best_solution)
print("Fitness:", best_fitness)
print(archive_grid.items())
'''