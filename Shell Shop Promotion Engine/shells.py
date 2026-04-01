def read_prices(fileName):
    prices=dict()
    try:
        with open(fileName,"r") as inf:
            for line in inf:
                line=line.strip()
                if not line:
                    continue
                parts=line.split(":")
                shell_name=parts[0]
                try:
                    shell_price=float(parts[1])
                except ValueError:
                    continue
                prices[shell_name]=shell_price

    except OSError:
        exit("error opening the file!!")
    return prices

def read_offers(fileName):
    offers=list()
    
    try:
        with open(fileName,"r") as inf:
            for line in inf:
                parts=line.split(":")
                offer_condition=parts[0].strip().split()
                free=parts[1].strip()
                offers.append((offer_condition,free))

    except OSError:
        exit("error opening the file!!")
    return offers

def read_cart(fileName):
    cart=list()
    try:
        with open(fileName,"r") as inf:
            for line in inf:
                line=line.strip()
                cart.append(line)
    except OSError:
        exit("error opening the file!!")
    return cart

def main():
    price_data=read_prices("prices.dat")
    offers=read_offers("offers.dat")
    cart=read_cart("cart.dat")

    offer_pool=cart[:]
    payable_cart=cart[:]
    tot_price=0.0

    for condition,free in offers:
        while True:
            temp=offer_pool[:]
            match=True
            for shell in condition:
                if shell in temp:
                    temp.remove(shell)
                else:
                    match=False
                    break

            if match and free in temp:
                offer_pool=temp
                offer_pool.remove(free)

                payable_cart.remove(free)

                condition_str=", ".join(condition)
                print(f"As you buy {condition_str}; you got {free} for free.")
            
            else:
                break
        
    for item in payable_cart:
            tot_price +=price_data.get(item,0.0)
        
    print(f"Final price: {tot_price:.2f} EUR")


main()