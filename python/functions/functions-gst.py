TAX_RATE = 0.1 # Constants should be in ALL CAPS
FLAT_SHIPPING = 10

def add_tax(amount):
    # total = amount * 1.1
    return amount * (1 + TAX_RATE) # Without return, the rest of the code cannot access the variable inside this function called add_gst

def add_shipping(amount):
    return amount + FLAT_SHIPPING

def calc_grand_total(amount):
    return add_tax(add_shipping(amount)) # This adds +$10, then multiples it by 1.1

# Main
subtotal = float(input('Subtotal: $'))
grand_total = calc_grand_total(subtotal) # This 
print(f'Total: ${grand_total:.2f}') #To format the result, you can put : colon, followed by specifier. This restricts it to 2 decimal places