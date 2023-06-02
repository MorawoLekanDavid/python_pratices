import matplotlib.pyplot as plt

data = {
    'A': [10, 15, 20, 25],
    'B': [5, 10, 15, 20],
    'C': [12, 18, 22, 28]
}

for key, values in data.items():
    plt.plot(values, label=key)

plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Values of Lists in Dictionary')
plt.legend()
plt.show()
