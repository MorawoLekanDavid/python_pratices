import numpy as np
import matplotlib.pyplot as plt

def logistic_growth(N0, r, K, generations):
    population = [N0]  # Initial population
    for _ in range(generations):
        N = population[-1]
        growth_rate = r * (1 - (N / K))
        new_population = N + growth_rate * N
        population.append(new_population)
    return population

# Parameters
N0 = 100  # Initial population size
r = 0.2  # Growth rate
K = 1000  # Carrying capacity
generations = 50

# Compute population growth
population = logistic_growth(N0, r, K, generations)

# Plot results
time = np.arange(generations + 1)
plt.plot(time, population)
plt.xlabel('Generation')
plt.ylabel('Population Size')
plt.title('Logistic Population Growth')
plt.grid(True)
plt.show()
