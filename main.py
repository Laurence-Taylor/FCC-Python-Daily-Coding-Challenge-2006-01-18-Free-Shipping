def gets_free_shipping(cart, minimum):
    items_dict = {
        "shirt" : 34.25,
        "jeans" : 48.50,
        "shoes" : 75.00,
        "hat" : 19.95,
        "socks" : 15.00,
        "jacket" : 109.95
    }
    total = 0
    for item in cart:
        total += items_dict[item]
    return total >= minimum 

if __name__ == '__main__':
    print(gets_free_shipping(["shoes"], 50))
    print('-------')
    print(gets_free_shipping(["hat", "socks"], 50))
    print('-------')
    print(gets_free_shipping(["jeans", "shirt", "jacket"], 75))
    print('-------')
    print(gets_free_shipping(["socks", "socks", "hat"], 75))
    print('-------')
    print(gets_free_shipping(["shirt", "shirt", "jeans", "socks"], 100))
    print('-------')
    print(gets_free_shipping(["hat", "socks", "hat", "jeans", "shoes", "hat"], 200))