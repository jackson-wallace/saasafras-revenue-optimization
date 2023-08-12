import random
from case_model import month_twelve_revenue

# Parameters
POP_SIZE = 100
NUM_GEN = 10000
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.05
TOURNAMENT_SIZE = 5


# 1. Representation: Each employee allocation will be a chromosome
#    represented as a list of 12 lists (each containing 3
#    integers that sum to 20)
# 2. Randomly generate a population of such chromosomes
def initialize_population():
    population = []
    for _ in range(POP_SIZE):
        chromosome = []
        for _ in range(12):  # 12 months
            while True:
                a, b, c = (
                    random.randint(0, 20),
                    random.randint(0, 20),
                    random.randint(0, 20),
                )
                if a + b + c == 20:
                    chromosome.append([a, b, c])
                    break
        population.append(chromosome)
    return population


# 3. Selection: Select pairs of chromosomes based on their fitness to produce offspring
def tournament_selection(population):
    selected = []
    for _ in range(2):  # Select two parents
        aspirants = [random.choice(population) for _ in range(TOURNAMENT_SIZE)]
        aspirants.sort(key=month_twelve_revenue, reverse=True)
        selected.append(aspirants[0])
    return tuple(selected)


# 4. Crossover: Create offspring by recombining pairs of parents
def crossover(parents):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, 11)  # Between 1 and 11 (inclusive)
        child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
        child2 = parents[1][:crossover_point] + parents[0][crossover_point:]
        return child1, child2
    else:
        return parents[0], parents[1]


# 5. Mutation: Randomly modify offspring genes MUTATION_RATE percent of the time
def mutate(child):
    for month in child:
        if random.random() < MUTATION_RATE:
            while True:
                a, b, c = (
                    random.randint(0, 20),
                    random.randint(0, 20),
                    random.randint(0, 20),
                )
                if a + b + c == 20:
                    month[0], month[1], month[2] = a, b, c
                    break
    return child


def genetic_algorithm():
    population = initialize_population()

    for gen in range(NUM_GEN):
        new_population = []
        for _ in range(POP_SIZE // 2):
            parents = tournament_selection(population)
            child1, child2 = crossover(parents)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        # 7. Replacement: Replace the old population with the new one
        population = new_population

    # 8. Termination: Exit generational loop after specified number of generations
    population.sort(key=month_twelve_revenue, reverse=True)
    best_chromosome = population[0]
    return best_chromosome, month_twelve_revenue(best_chromosome)


# Execute GA
best_allocations, best_revenue = genetic_algorithm()
print("Best Allocations:")
print(best_allocations)
print("Best Revenue:", best_revenue)
