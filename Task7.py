import random
import matplotlib.pyplot as plt

def roll_dice(num_trials):
  sums = {}
  for _ in range(num_trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    sums[sum] = sums.get(sum, 0) + 1
  return sums

def calculate_probabilities(sums, num_trials):
  probabilities = {}
  for sum, count in sums.items():
    probabilities[sum] = count / num_trials
  return probabilities

def display_results(probabilities):
  print("Таблиця ймовірностей:")
  print("Сума\tІмовірність")
  for sum, probability in probabilities.items():
    print(f"{sum}\t{probability:.2%}")

  # Графік
  plt.bar(probabilities.keys(), probabilities.values())
  plt.xlabel("Сума")
  plt.ylabel("Імовірність")
  plt.title("Ймовірності сум при киданні двох кубиків")
  plt.show()

# Параметри симуляції
num_trials = 100000

# Моделювання кидків
sums = roll_dice(num_trials)

# Обчислення ймовірностей
probabilities = calculate_probabilities(sums, num_trials)

# Відображення результатів
display_results(probabilities)