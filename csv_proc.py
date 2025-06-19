import argparse
import csv
from tabulate import tabulate


def filter_data(data, column, operator, value):
    """Фильтрация данных по заданному условию."""

    filtered_data = []
    for row in data:
        if operator == '>':
            if float(row[column]) > float(value):
                filtered_data.append(row)
        elif operator == '<':
            if float(row[column]) < float(value):
                filtered_data.append(row)
        elif operator == '=':
            if row[column] == value:
                filtered_data.append(row)
        elif operator == '>=':
            if float(row[column]) >= float(value):
                filtered_data.append(row)
        elif operator == '<=':
            if float(row[column]) <= float(value):
                filtered_data.append(row)
    return filtered_data


def aggregate_data(data, column, aggregation):
    """Агрегация данных по заданной колонке."""

    values = [float(row[column]) for row in data]
    if aggregation == 'avg':
        try:
            return sum(values) / len(values)
        except ZeroDivisionError:
            return None
    elif aggregation == 'min':
        return min(values)
    elif aggregation == 'max':
        return max(values)


def main():
    parser = argparse.ArgumentParser(description='Обработка CSV-файла')
    parser.add_argument('file', help='Путь к CSV-файлу')
    parser.add_argument('--filter', type=str,
                        help='Условие фильтрации в формате "column:>:value"')
    parser.add_argument('--aggregate', type=str,
                        help='Условие агрегации в формате "column:aggregation"')
    args = parser.parse_args()

    with open(args.file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    if args.filter:
        column, operator, value = args.filter.split(':')
        data = filter_data(data, column, operator, value)

    if args.aggregate:
        column, aggregation = args.aggregate.split(':')
        result = aggregate_data(data, column, aggregation)
        print(f'Агрегированное значение: {result}')
    else:
        print(tabulate(data, headers='keys', tablefmt='fancy_grid'))


if __name__ == '__main__':
    main()
