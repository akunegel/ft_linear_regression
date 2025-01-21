import csv
from estimatePrice import estimatePrice

def evaluateModel(test_data_file, theta_file):
    with open(theta_file, 'r') as file:
        theta0, theta1 = map(float, file.read().strip().split(','))

    with open(test_data_file, 'r') as file:
        dataset = csv.reader(file)
        next(dataset)
        test_data = [(float(row[0]), float(row[1])) for row in dataset]

    total_error = 0
    for mileage, actual_price in test_data:
        predicted_price = estimatePrice(mileage, theta0, theta1)
        error = abs(predicted_price - actual_price) / actual_price
        total_error += error

    average_error = total_error / len(test_data)
    precision = (1 - average_error) * 100

    print(f"Model Precision: {precision:.2f}%")

evaluateModel("data.csv", "theta.csv")