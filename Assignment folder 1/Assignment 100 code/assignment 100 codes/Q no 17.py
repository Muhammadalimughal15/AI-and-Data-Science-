def compute_net_amount():
    net_amount = 0
    while True:
        transaction = input("Enter a transaction (or 'quit' to finish): ")
        if transaction.lower() == 'quit':
            break
        action, amount = transaction.split()
        amount = int(amount)
        if action.upper() == 'D':
            net_amount += amount
        elif action.upper() == 'W':
            net_amount -= amount
    print(net_amount)

compute_net_amount()