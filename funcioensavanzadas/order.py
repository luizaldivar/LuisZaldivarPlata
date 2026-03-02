import pandas as pd
orders_a = pd.read_csv('part2_orders_a.csv')
orders_b = pd.read_csv('part2_orders_b.csv')
customers = pd.read_csv('part2_customers.csv')
products = pd.read_csv('part2_products.csv')
# 1.1 Unir orders_a y orders_b con índice reiniciado
orders = pd.concat([orders_a, orders_b], ignore_index=True)

# 1.2 Ordenar por order_date (asc) y qty (desc)
orders = orders.sort_values(by=['order_date', 'qty'], ascending=[True, False])

# 1.3 Establecer order_date como índice y ordenar cronológicamente
orders['order_date'] = pd.to_datetime(orders['order_date']) 
orders = orders.set_index('order_date').sort_index()


# Realizar el merge (left join) validando relación muchos a uno

orders = pd.merge(
    orders, 
    customers[['customer_id', 'customer_name', 'city', 'segment']], 
    on='customer_id', 
    how='left',
    validate='many_to_one'
)
# 3.1 Merge con products para añadir detalles del producto
orders = pd.merge(
    orders, 
    products[['product_id', 'product', 'category', 'unit_price']], 
    on='product_id', 
    how='left'
)

# 3.2 Crear columna line_total (cantidad * precio unitario)
orders['line_total'] = orders['qty'] * orders['unit_price']

# 3.3 Ordenar por line_total descendente y mostrar el top 5
top_5_ventas = orders.sort_values(by='line_total', ascending=False).head(5)

print(top_5_ventas)
