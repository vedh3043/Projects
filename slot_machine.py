import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

   
    if winnings == 0:
        guaranteed_win = random.choice([True, False])
        if guaranteed_win:
            random_line = random.randint(1, lines)
            symbol = random.choice(list(values.keys()))
            winnings += values[symbol] * bet
            winning_lines.append(random_line)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a valid amount.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between $1 and $100")
        else:
            print("Please enter a valid amount.")

    return amount

def main():
    balance = deposit()
    
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}")
        else:
            print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
            balance -= total_bet

            slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
            print_slot_machine(slots)

            winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)
            balance += winnings

            if winnings > 0:
                print(f"You won ${winnings} on lines: {', '.join(map(str, winning_lines))}.")
            else:
                print("You didn't win this time.")

            print(f"Your new balance is ${balance}.")

            if balance <= 0:
                print("You ran out of money!")
                break

            play_again = input("Press Enter to play again (or 'q' to quit): ")
            if play_again.lower() == 'q':
                break

    print("Thank you for playing!")


main()
