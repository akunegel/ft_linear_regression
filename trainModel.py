import csv
from estimatePrice import estimatePrice
import matplotlib.pyplot as plt

def trainModel(data_file, learning_rate, iterations):
    with open(data_file, 'r') as file:
        dataset = csv.reader(file)
        next(dataset)
        data = [(float(row[0]), float(row[1])) for row in dataset]
    
    mileages = [x for x, _ in data]
    prices = [y for _, y in data]
    mileage_mean = sum(mileages) / len(mileages)
    mileage_std = (sum((x - mileage_mean) ** 2 for x in mileages) / len(mileages)) ** 0.5
    price_mean = sum(prices) / len(prices)
    price_std = (sum((y - price_mean) ** 2 for y in prices) / len(prices)) ** 0.5

    normalized_data = [((x - mileage_mean) / mileage_std, (y - price_mean) / price_std) for x, y in data]
    
    m = len(normalized_data)
    theta0, theta1 = 0.0, 0.0

    errors = []

    for _ in range(iterations):
        sum0 = sum((estimatePrice(x, theta0, theta1) - y) for x, y in normalized_data)
        sum1 = sum((estimatePrice(x, theta0, theta1) - y) * x for x, y in normalized_data)
        new_theta0 = theta0 - learning_rate * (1 / m) * sum0
        new_theta1 = theta1 - learning_rate * (1 / m) * sum1

        theta0, theta1 = new_theta0, new_theta1

        error = sum((estimatePrice(x, theta0, theta1) - y) ** 2 for x, y in normalized_data) / m
        errors.append(error)

    plt.plot(range(iterations), errors)
    plt.xlabel('Itérations')
    plt.ylabel('Erreur')
    plt.title('Évolution de l\'erreur pendant l\'entraînement')
    plt.savefig("graphs/error_plot.png")
    plt.close()

    plt.scatter(mileages, prices, color='blue', label='Données')
    plt.plot(mileages, [estimatePrice((x - mileage_mean) / mileage_std, theta0, theta1) * price_std + price_mean for x in mileages], color='red', label='Régression linéaire')  # La droite de régression
    plt.xlabel('Kilométrage')
    plt.ylabel('Prix')
    plt.title('Répartition des données et régression linéaire')
    plt.legend()

    plt.savefig("graphs/regression_plot.png")
    plt.close()

    theta1 = theta1 * (price_std / mileage_std)
    theta0 = (theta0 * price_std) + price_mean - (theta1 * mileage_mean)

    with open("theta.csv", 'w') as file:
        file.write(f"{theta0},{theta1}")

    print(f"Training complete! Theta0: {theta0}, Theta1: {theta1}")
    print("The values have been saved to theta.csv.")

trainModel("data.csv", 0.21, 10)