import requests


def main():
    print("\n🔴WELCOME TO CURRENCY EXCHANGER🔴")
    while True:
        base_currency = input("\nBase Currency:💲 ").strip().upper()
        url = "https://api.frankfurter.app/latest?base=" + base_currency
        response = requests.get(url)
        if response.status_code == 200:
            output = response.json()
            if "rates" in output and output["rates"]:
                break
            else:
                print("🛑Error Try Again")
                continue
        else:
            print("🛑Enter a Valid currency")
            continue
    while True:
        target_currency = input("Target Currency:💲 ").strip().upper()
        if target_currency not in output["rates"]:
            print("🛑Enter a Valid currency")
            continue
        else:
            target_currency_value = float(output["rates"][target_currency])
            while True:
                try:
                    base_amount = int(input("\nWhat's the base amount? "))
                    total_amount = round(target_currency_value * base_amount, 1)
                    print(
                        f"\n💱 {base_amount} {base_currency} is {total_amount} {target_currency}"
                    )
                    repeat = (
                        input("Do you wanna try another time?(yes/no)").strip().lower()
                    )
                    if repeat == "yes":
                        main()
                    else:
                        return
                except ValueError:
                    continue

main()
