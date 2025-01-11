import json

class purchaseanalysis:
    def __init__(self, purchases):
        self.purchases = purchases
    #Функция для получения минимальной цены
    def get_min_price(self):
        return min(item["price"] for item in self.purchases)

    # Функция для расчета общей выручки
    def total_revenue(self):
        result = sum(item["price"] * item["quantity"] for item in self.purchases)
        return f"Общая выручка: {result}"

    # Функция для сортировки товаров по категориям
    def items_by_category(self):
        new_dict = {}
        for item in self.purchases:
            new_dict.setdefault(item['category'], []).append(item['item'])
        return f'Товары по категориям: {new_dict}'

    # Функция для получения товаров, купленных выше минимальной цены
    def expensive_purchases(self, min_price):
        new_list = [item for item in self.purchases if item['price'] > min_price]
        return f'Покупки дороже {min_price}: {new_list}'

    # Функция для расчета средней цены по категориям
    def average_price_by_category(self):
        new_dict = {}
        for item in self.purchases:
            new_dict.setdefault(item['category'], []).append(item['price'])

        for category in new_dict:
            new_dict[category] = sum(new_dict[category]) / len(new_dict[category])
        return f'Средняя цена по категориям: {new_dict}'

    # Функция для поиска товара, с наибольшим кол-во проданных товаров
    def most_frequent_category(self):
        new_dict = {}
        for item in self.purchases:
            new_dict[item['category']] = new_dict.get(item['category'], 0) + item['quantity']
        max_category = max(new_dict, key=new_dict.get)
        return f'Категория с наибольшим количеством проданных товаров: {max_category}'

    # Функция для обработки всех данных
    def collect_all_results(self):
        min_price = self.get_min_price()
        results = [
            self.total_revenue(),
            self.items_by_category(),
            self.expensive_purchases(min_price),
            self.average_price_by_category(),
            self.most_frequent_category(),
        ]
        return "\n".join(results)


# Данные
with open("data.json", "r", encoding="utf-8") as file:
    purchases = json.load(file)

# Выполнение анализа
analysis = purchaseanalysis(purchases)
print(analysis.collect_all_results())

input('Нажми enter чтобы закрыть консоль')