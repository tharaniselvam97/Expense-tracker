
class ExpenseManager:
    def __init__(self):
        self.users = {}  # Dictionary to store user information
        self.expenses = []  # List to store expense records

    def add_user(self, user_id, name, email, mobile):
        self.users[user_id] = {
            "name": name,
            "email": email,
            "mobile": mobile,
            "balance": 0.0,
        }

    def add_expense(self, payer_id, amount, participants, expense_name):
        # Update payer's balance
        self.users[payer_id]["balance"] -= amount

        # Split the expense among participants
        num_participants = len(participants)
        share = amount / num_participants

        for participant in participants:
            self.users[participant]["balance"] += share

        # Record the expense
        self.expenses.append({
            "payer_id": payer_id,
            "amount": amount,
            "participants": participants,
            "expense_name": expense_name
        })

    def get_user_balance(self, user_id):
        return self.users.get(user_id, {}).get("balance", 0.0)

    def get_passbook(self, user_id):
        user_expenses = [
            exp
            for exp in self.expenses
            if user_id in exp["participants"] or exp["payer_id"] == user_id
        ]
        return user_expenses

    def calculate_owing(self):
        # Calculate who owes whom
        for user_id, user_data in self.users.items():
            if user_data["balance"] > 0:
                print(f"{user_data['name']} owes {user_data['balance']:.2f}")
            elif user_data["balance"] < 0:
                print(f"{user_data['name']} is owed {-user_data['balance']:.2f}")

if __name__ == "__main__":
    expense_manager = ExpenseManager()

    while True:
        print("\nExpense Sharing Application")
        print("1. Add User")
        print("2. Add Expense")
        print("3. Get User Balance")
        print("4. Check Who Owes Whom")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            mobile = input("Enter user mobile: ")
            expense_manager.add_user(user_id, name, email, mobile)
            print("User added successfully!")

        elif choice == "2":
            payer_id = input("Enter payer's user ID: ")
            amount = float(input("Enter expense amount: "))
            participants = input("Enter participant user IDs (comma-separated): ").split(",")
            expense_name = input("Enter expense name: ")
            expense_manager.add_expense(payer_id, amount, participants, expense_name)
            print("Expense recorded successfully!")

        elif choice == "3":
            user_id = input("Enter user ID: ")
            balance = expense_manager.get_user_balance(user_id)
            print(f"User balance: {balance:.2f}")

        elif choice == "4":
            expense_manager.calculate_owing()

        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
