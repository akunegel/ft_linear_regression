import csv

def estimatePrice(mileage, theta0, theta1):
    return theta0 + (theta1 * mileage)

def predictPrice():
    with open('theta.csv', 'r') as file:
        reader = csv.reader(file)
        theta0, theta1 = map(float, next(reader))
    mileage = float(input("Enter mileage of the car: "))
    price = estimatePrice(mileage, theta0, theta1)
    print(f"The estimated price for a car with {mileage} mileage is {price:.2f}")

if __name__ == "__main__":
    predictPrice()