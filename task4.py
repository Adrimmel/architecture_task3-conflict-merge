import csv
import random
import time
from datetime import datetime

class SensorSimulator:
    def __init__(self, metric_name, unit, min_value, max_value):
        self.metric_name = metric_name
        self.unit = unit
        self.min_value = min_value
        self.max_value = max_value
        self.values = []

    def generate_value(self):
        return random.uniform(self.min_value, self.max_value)

    def record_value(self):
        current_time = datetime.now()
        value = self.generate_value()
        self.values.append((current_time, value))

    def average_values(self):
        if not self.values:
            return None
        total = sum(v for _, v in self.values)
        return total / len(self.values)

    def save_to_csv(self, filename):
        avg_value = self.average_values()
        if avg_value is not None:
            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), self.metric_name, avg_value, self.unit])
            self.values = []

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите числовое значение.")

def main():
    metric_name = input("Введите название метрики (например, температура): ")
    unit = input("Введите единицу измерения (например, °C): ")
    min_value = float(input("Введите минимальное значение: "))
    max_value = float(input("Введите максимальное значение: "))

    sensor = SensorSimulator(metric_name, unit, min_value, max_value)
    filename = f"{metric_name}_data.csv"


    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Дата и время', 'Метрика', 'Значение', 'Единица измерения'])

    try:
        while True:
            sensor.record_value()
            time.sleep(1)
            if len(sensor.values) >= 60:
                sensor.save_to_csv(filename)
    except KeyboardInterrupt:
        print("Симуляция завершена.")

if __name__ == "__main__":
    main()
