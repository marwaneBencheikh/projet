import csv


def create_account(accounts, account_number, name, balance):
    accounts[account_number] = {"name": name, "balance": balance}
    print(f"Le compte a été créé avec succès. Numéro de compte : {account_number}, Nom : {name}, Solde : {balance}.")


def view_account(accounts, account_number):
    if account_number in accounts:
        account = accounts[account_number]
        print(f"Numéro de compte : {account_number}, Nom : {account['name']}, Solde : {account['balance']}")
    else:
        print("Le compte n'existe pas!")


def deposit(accounts, account_number, amount):
    if account_number in accounts:
        accounts[account_number]['balance'] += amount
        print(f"{amount} a été déposé sur le compte numéro {account_number}. Solde actuel : {accounts[account_number]['balance']}.")
    else:
        print("Le compte n'existe pas!")


def withdraw(accounts, account_number, amount):
    if account_number in accounts:
        if accounts[account_number]['balance'] >= amount:
            accounts[account_number]['balance'] -= amount
            print(f"{amount} a été retiré du compte numéro {account_number}. Solde actuel : {accounts[account_number]['balance']}.")
        else:
            print("Solde insuffisant pour le retrait!")
    else:
        print("Le compte n'existe pas!")


def save_to_csv(accounts, filename="accounts.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Numéro de compte", "Nom", "Solde"])
        for account_number, details in accounts.items():
            writer.writerow([account_number, details['name'], details['balance']])
    print("Les données ont été sauvegardées avec succès dans le fichier.")


def load_from_csv(filename="accounts.csv"):
    accounts = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                account_number, name, balance = row
                accounts[account_number] = {"name": name, "balance": float(balance)}
    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas.")
    return accounts


def menu():
    print("\nBienvenue à la gestion bancaire !")
    print("1. Créer un compte")
    print("2. Afficher un compte")
    print("3. Dépôt")
    print("4. Retrait")
    print("5. Quitter")
    
    return input("Choisissez une opération dans le menu : ")


def main():
    accounts = load_from_csv() 
    
    while True:
        choice = menu()
        
        if choice == "1":
            account_number = input("Entrez le numéro de compte : ")
            name = input("Entrez le nom du titulaire du compte : ")
            balance = float(input("Entrez le solde initial : "))
            create_account(accounts, account_number, name, balance)
        
        elif choice == "2":
            account_number = input("Entrez le numéro de compte pour l'afficher : ")
            view_account(accounts, account_number)
        
        elif choice == "3":
            account_number = input("Entrez le numéro de compte pour effectuer le dépôt : ")
            amount = float(input("Entrez le montant à déposer : "))
            deposit(accounts, account_number, amount)
        
        elif choice == "4":
            account_number = input("Entrez le numéro de compte pour effectuer le retrait : ")
            amount = float(input("Entrez le montant à retirer : "))
            withdraw(accounts, account_number, amount)
        
        elif choice == "5":
            print("Au revoir !")
            break
        
        else:
            print("Choix incorrect, veuillez réessayer.")


main()
