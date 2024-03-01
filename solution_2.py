# Задача 2: Композиция функций для обработки заказов

def check_order(order):
  if not order["items"]:
    return False
  return True

def package_order(order):
  return f"Упакован заказ {order['id']}"

def send_order(check_order, package_order, order):
  if check_order(order):
    return f"Отправка: {package_order(order)}"
  else:
    return f"Отправка: Заказ {order['id']} пуст"

order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))
