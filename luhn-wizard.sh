#!/bin/bash

echo "Starting Luhn Validator Setup..."

# Step 1: Check and Install Node.js and npm
if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Installing Node.js..."
    apt update && apt install -y nodejs npm
    echo "Node.js and npm installed."
else
    echo "Node.js is already installed."
fi

# Step 2: Check Node.js and npm Versions
echo "Node.js version: $(node -v)"
echo "npm version: $(npm -v)"

# Step 3: Clone the Luhn Repository
if [ ! -d "luhn" ]; then
    echo "Cloning the Luhn repository..."
    git clone https://github.com/paylike/luhn.git
else
    echo "Luhn repository already cloned."
fi

# Step 4: Navigate to the Repository and Install Dependencies
cd luhn || exit
echo "Installing dependencies..."
npm install --silent

# Step 5: Create the Test Script (Wizard)
cat <<EOF > test-luhn.js
const luhn = require('./index');
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

console.log("Welcome to the Luhn Validator Wizard!");
console.log("1. Validate a single card number");
console.log("2. Validate card numbers from a file");

rl.question("Choose an option (1 or 2): ", (option) => {
    if (option === "1") {
        rl.question("Enter the card number to validate: ", (pan) => {
            const isValid = luhn(pan) ? "valid" : "invalid";
            console.log(\`The PAN \${pan} is \${isValid}.\`);
            rl.close();
        });
    } else if (option === "2") {
        rl.question("Enter the file path containing card numbers: ", (filePath) => {
            const fs = require('fs');
            if (!fs.existsSync(filePath)) {
                console.log("File does not exist. Exiting...");
                rl.close();
                return;
            }
            const cardNumbers = fs.readFileSync(filePath, 'utf-8').split(/\r?\n/).filter(Boolean);
            cardNumbers.forEach((pan, index) => {
                const isValid = luhn(pan) ? "valid" : "invalid";
                console.log(\`Card \${index + 1} (\${pan}): \${isValid}\`);
            });
            rl.close();
        });
    } else {
        console.log("Invalid option. Exiting...");
        rl.close();
    }
});
EOF

# Step 6: Automatically Run the Wizard
echo "Setup complete. Launching the Luhn Validator Wizard..."
node test-luhn.js
