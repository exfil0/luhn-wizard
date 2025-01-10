import requests
import re
import json
from datetime import datetime

# Function to validate the card number using Luhn's algorithm
def luhn_check(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10 == 0

# Function to fetch BIN details using Binlist API
def fetch_bin_details(bin_number):
    try:
        response = requests.get(f"https://lookup.binlist.net/{bin_number}", headers={"Accept-Version": "3"})
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unable to fetch BIN details (status code: {response.status_code})"}
    except requests.RequestException as e:
        return {"error": f"An error occurred: {e}"}

# Function to validate a single card number
def validate_single_card():
    card_number = input("Enter the card number to validate: ")
    if not re.match(r"^\d{12,19}$", card_number):
        print("Invalid card number format. Must be 12-19 digits.")
        return

    is_valid = luhn_check(card_number)
    bin_number = card_number[:6]
    result = {
        "card_number": card_number,
        "is_valid": is_valid,
        "bin_details": None,
        "timestamp": datetime.now().isoformat()
    }

    print(f"The PAN {card_number} is {'valid' if is_valid else 'invalid'}.")

    if is_valid:
        print("Fetching BIN details...")
        bin_details = fetch_bin_details(bin_number)
        result["bin_details"] = bin_details
        print("BIN details:")
        print(bin_details)

    # Save the result to a JSON file
    with open("luhn_validation_report.json", "w") as file:
        json.dump(result, file, indent=4)
    print("Report saved to luhn_validation_report.json")

# Function to validate a batch of card numbers
def validate_batch_cards():
    file_path = input("Enter the file path containing card numbers: ")
    try:
        with open(file_path, "r") as file:
            card_numbers = file.read().splitlines()

        results = []

        for index, card_number in enumerate(card_numbers, start=1):
            if not re.match(r"^\d{12,19}$", card_number):
                print(f"Card {index} ({card_number}): invalid format.")
                results.append({
                    "card_number": card_number,
                    "is_valid": False,
                    "error": "Invalid format",
                    "timestamp": datetime.now().isoformat()
                })
                continue

            is_valid = luhn_check(card_number)
            bin_number = card_number[:6]
            result = {
                "card_number": card_number,
                "is_valid": is_valid,
                "bin_details": None,
                "timestamp": datetime.now().isoformat()
            }

            print(f"Card {index} ({card_number}): {'valid' if is_valid else 'invalid'}.")

            if is_valid:
                print("Fetching BIN details...")
                bin_details = fetch_bin_details(bin_number)
                result["bin_details"] = bin_details
                print("BIN details:")
                print(bin_details)

            results.append(result)

        # Save the results to a JSON file
        with open("luhn_validation_report.json", "w") as file:
            json.dump(results, file, indent=4)
        print("Batch report saved to luhn_validation_report.json")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main wizard function
def luhn_validator_wizard():
    print("Welcome to the Luhn Validator Wizard!")
    print("1. Validate a single card number")
    print("2. Validate card numbers from a file")

    choice = input("Choose an option (1 or 2): ")
    if choice == "1":
        validate_single_card()
    elif choice == "2":
        validate_batch_cards()
    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    luhn_validator_wizard()
