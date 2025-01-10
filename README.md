# Luhn Validator Wizard

This repository contains a Python script that validates card numbers using the Luhn algorithm, fetches BIN details using the Binlist API, and generates professional JSON reports for single and batch validations.

## Features

- **Luhn Algorithm Validation**: Checks the validity of card numbers.
- **BIN Details Fetching**: Fetches additional details for valid card numbers using the [Binlist API](https://binlist.net/).
- **JSON Reports**:
  - Generates structured JSON reports for both single and batch validations.
  - Saves reports to `luhn_validation_report.json`.

---

## Installation and Usage

### Step 1: Clone the Repository

```bash
git clone https://github.com/exfil0/luhn-wizard.git
cd luhn-wizard
```

### Step 2: Install Dependencies

Ensure Python is installed on your system:

```bash
python3 --version
```

If Python is not installed, install it:

```bash
sudo apt update && sudo apt install -y python3
```

Additionally, install the `requests` library if not already installed:

```bash
pip install requests
```

### Step 3: Run the Script

```bash
python3 luhn_validator.py
```

---

## Wizard Options

1. **Validate a Single Card Number**: Enter a card number to validate its validity and fetch BIN details. The result is saved as a JSON report.
2. **Validate Batch Card Numbers**: Provide a file path containing card numbers (one per line) for validation and BIN details fetching. The results are saved as a batch JSON report.

---

## Example Output

### Single Card Validation
```bash
Welcome to the Luhn Validator Wizard!
1. Validate a single card number
2. Validate card numbers from a file
Choose an option (1 or 2): 1
Enter the card number to validate: 4111111111111111
The PAN 4111111111111111 is valid.
Fetching BIN details...
BIN details:
{
    "scheme": "visa",
    "type": "debit",
    "brand": "Visa Debit",
    "bank": {
        "name": "Example Bank",
        "country": "US"
    }
}
Report saved to luhn_validation_report.json
```

### Batch Card Validation
```bash
Welcome to the Luhn Validator Wizard!
1. Validate a single card number
2. Validate card numbers from a file
Choose an option (1 or 2): 2
Enter the file path containing card numbers: test-cards.txt
Card 1 (4111111111111111): valid
BIN details:
{
    "scheme": "visa",
    "type": "debit",
    "brand": "Visa Debit",
    "bank": {
        "name": "Example Bank",
        "country": "US"
    }
}
Card 2 (1234567812345670): invalid
Card 3 (4000001234567899): valid
BIN details:
{
    "scheme": "visa",
    "type": "credit",
    "brand": "Visa",
    "bank": {
        "name": "Another Bank",
        "country": "UK"
    }
}
Batch report saved to luhn_validation_report.json
```

---

## Notes

- The script uses the [Binlist API](https://binlist.net/) to fetch BIN details. Ensure your internet connection is active.
- Ensure the card numbers provided are in the correct format (12-19 digits).
- JSON reports are saved to `luhn_validation_report.json` in the current directory.

---

## License

This project is licensed under the [MIT License](LICENSE).
