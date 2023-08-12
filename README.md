# SaaSafras Revenue Optimization

## Introduction

This project provides a Python-based solution to optimize the monthly allocations of employees in order to maximize the 12th-month revenue for a SaaS company named "SaaSafras". The optimization technique used is a Genetic Algorithm (GA), which iteratively evolves a set of solutions to find a near-optimal allocation.

## Files and Descriptions

1. **case_model.py**: Contains the function `month_twelve_revenue()` that calculates the revenue at the end of month twelve based on employee allocations.

2. **ga.py**: Contains the implementation of the genetic algorithm, which optimizes the monthly allocations to maximize the 12th-month revenue.

## How to Run

1. Ensure both `case_model.py` and `ga.py` are in the same directory.
2. Run the `ga.py` file:

```bash
python ga.py
```

This will execute the genetic algorithm and display the best allocations along with the corresponding revenue.

## Detailed Breakdown

### case_model.py

- **month_twelve_revenue(allocations)**:
  - `allocations`: A list of monthly employee allocations.
  - Returns the revenue at the end of the 12th month based on the provided allocations.

### ga.py

- **Parameters**:

  - POP_SIZE: Population size for each generation.
  - NUM_GEN: Number of generations for the algorithm to run.
  - CROSSOVER_RATE: Probability of crossover between two parents.
  - MUTATION_RATE: Probability of mutating an individual.
  - TOURNAMENT_SIZE: Number of individuals selected for tournament selection.

- **Core Functions**:
  - `initialize_population()`: Generates an initial population of random employee allocations.
  - `tournament_selection(population)`: Selects two parent allocations based on their fitness.
  - `crossover(parents)`: Combines two parent allocations to produce offspring.
  - `mutate(child)`: Introduces small random changes in the offspring allocations.
  - `genetic_algorithm()`: Main function that initializes the population, evolves it over several generations, and returns the best allocation.

## Conclusion

By leveraging the power of genetic algorithms, this project aims to determine the most optimal employee allocation strategy for SaaSafras, helping the company maximize its revenue at the end of the 12th month.
