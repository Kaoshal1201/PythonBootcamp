# Define the exchange rate from USD to INR
exchange_rate = 74.83  

def convert_usd_to_inr(amount):
    """
    Convert an amount of USD to INR.

    Args:
        amount (float): The amount of USD to convert.

    Returns:
        float: The converted amount in INR.
    """
    return amount * exchange_rate

def main():
    print("USD to INR Currency Converter")
    print("----------------------------")

    amount = float(input("Enter the amount in USD: "))

    result = convert_usd_to_inr(amount)
    print(f"{amount} USD is equal to {result:.2f} INR")

if __name__ == "__main__":
    main()