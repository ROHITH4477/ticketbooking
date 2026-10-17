def calculate_ticket_price(price, tickets):
    if price <= 0 or tickets <= 0:
        raise ValueError("Invalid booking")
    return price * tickets


print("Movie: Avengers")
print("Total Amount: Rs.", calculate_ticket_price(200, 3))