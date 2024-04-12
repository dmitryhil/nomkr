from datetime import datetime, timedelta

def read_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0].strip()
            date = datetime.strptime(parts[1].strip(), '%Y-%m-%d')
            price = float(parts[2].strip())
            data.append((name, date, price))
    return data

def price_change_last_month(data, product_name):
    today = datetime.today()
    one_month_ago = today - timedelta(days=30)
    
    prices_last_month = []
    for item in data:
        if item[0] == product_name and item[1] >= one_month_ago and item[1] <= today:
            prices_last_month.append(item[2])
    
    if len(prices_last_month) < 2:
        return "Not enough data to calculate price change for the last month."
    
    initial_price = prices_last_month[0]
    final_price = prices_last_month[-1]
    price_change = final_price - initial_price
    
    return f"The price change for {product_name} in the last month is {price_change:.2f}."

# Приклад використання
filename = "C:/Users/Richard/Desktop/nomkr/products.txt"
data = read_data_from_file(filename)
product_name = "Product A"
print(price_change_last_month(data, product_name))
