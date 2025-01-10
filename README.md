# Luhn Wizard - v1

This repository contains a Bash script that automates the setup and running of a Luhn Validator Wizard. The wizard helps validate single card numbers or batches of card numbers from a file using the Luhn algorithm.

## Features

- Automates the installation of **Node.js** and **npm** if not already installed.
- Clones the [Paylike Luhn](https://github.com/paylike/luhn) repository for Luhn validation.
- Automatically installs dependencies required for the Luhn Validator.
- Runs a wizard to:
  - Validate a single card number.
  - Validate a batch of card numbers from a file.

---

## Installation and Usage

### Step 1: Clone the Repository

```bash
git clone https://github.com/exfil0/luhn-wizard.git
cd luhn-wizard
```

### Step 2: Make the Script Executable

```bash
chmod +x luhn-wizard.sh
```

### Step 3: Run the Script

```bash
./luhn-wizard.sh
```

---

## What Happens When You Run the Script?

1. **Checks for Node.js**: Installs Node.js and npm if not present.
2. **Clones the Luhn Repository**: If the Luhn repository is not already present, it will be cloned.
3. **Installs Dependencies**: Installs required Node.js packages for Luhn validation.
4. **Launches the Wizard**: Automatically starts the Luhn Validator Wizard.

---

## Wizard Options

1. **Validate a Single Card Number**: Enter a test card number to validate, and the script will determine its validity using the Luhn algorithm.
2. **Validate Batch Card Numbers**: Provide a file path containing card numbers (one per line), and the wizard will validate all numbers in the file.

---

## Example Output

### Single Card Number Validation
```bash
Welcome to the Luhn Validator Wizard!
1. Validate a single card number
2. Validate card numbers from a file
Choose an option (1 or 2): 1
Enter the card number to validate: 4111111111111111
The PAN 4111111111111111 is valid.
```

### Batch Card Number Validation
```bash
Welcome to the Luhn Validator Wizard!
1. Validate a single card number
2. Validate card numbers from a file
Choose an option (1 or 2): 2
Enter the file path containing card numbers: test-cards.txt
Card 1 (4111111111111111): valid
Card 2 (1234567812345670): invalid
Card 3 (4000000000000002): valid
```

---

## Notes

- The script assumes a Debian-based Linux distribution (e.g., Ubuntu, Kali).
- Ensure you have necessary permissions to install software if running the script on a fresh system.

---

## License

This project is licensed under the [MIT License](LICENSE).

