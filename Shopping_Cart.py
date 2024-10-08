def shop(items, d):
    total = 0
    for x in items:
        total += x
    if d:
        total = total - (total * 0.1)
    return total

cart = [19.99, 5.49, 12.89, 3.49, 99.99]
d = True

print(shop(cart, d))