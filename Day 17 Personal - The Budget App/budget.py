class Budget:
    def __init__(self, username):
        self.user = username
        self.categories = {}
        # self.category_names = []

    def view_all_categories(self):
        pass

    def add_category(self):
        # balance = 0
        new_cat = {}
        cat_name = input('\nPlease input a new category: ').title()
        cat_desc = input(f'Please give a short description for {cat_name}: ').title()

        if cat_name in self.categories.keys():
            print(f"\nCategory {cat_name} already exists")
            return None
        else:
            self.categories[cat_name] = []
            self.categories[cat_name].append(cat_name)
            self.categories[cat_name].append(cat_desc)
            self.categories[cat_name].append(0.00)
            return self.categories

    def deposit(self):
        all_categories = self.categories.keys()
        if len(all_categories) == 0:
            print('No available category, please add a category below\n')
            self.add_category()
            print('')
            self.deposit()
        else:
            count = 1
            for cat in all_categories:
                print(f'Category {count}: {cat}')
                count += 1
            choice = input(f'Please choose a category from the above: ').title()
            if choice in all_categories:
                try:
                    amount = int(input('How much do you want to deposit? ₦'))
                    previous_balance = self.categories[choice][2]
                    self.categories[choice][2] = previous_balance + amount
                    print(self.categories)
                except Exception as e:
                    print(e)

    def withdraw(self):
        all_categories = self.categories.keys()
        if len(all_categories) == 0:
            print('No available category, please add a category\n')
            self.add_category()
            print('')
            self.deposit()
            print('')
            self.withdraw()
        else:
            count = 1
            for cat in all_categories:
                print(f'Category {count}: {cat}')
                count += 1
            choice = input(f'Please choose a category from the above: ').title()
            if choice in all_categories:
                try:
                    amount = int(input('How much do you want to withdraw? ₦'))
                    previous_balance = self.categories[choice][2]
                    if amount <= previous_balance:
                        self.categories[choice][2] = previous_balance - amount
                        print(self.categories)
                    else:
                        print('You don\'t have sufficient funds, please deposit')
                        self.deposit()
                except Exception as e:
                    print(e)

    def check_balance(self):
        all_categories = self.categories.keys()
        if len(all_categories) == 0:
            print('No available category\n')
            return None
        else:
            print('\nPlease see all categories and balances:')
            for cat in self.categories:
                print(f'{cat} balance is ₦{self.categories[cat][2]:,.2f}')

    def transfer_balance(self):
        all_categories = self.categories.keys()
        if len(all_categories) < 2:
            print('Not enough categories, please add a category below')
            self.add_category()
            self.add_category()
        else:
            count = 1
            for cat in all_categories:
                print(f'Category {count}: {cat}')
                count += 1
            sender = input(f'Please choose the sender from the above: ').title()
            if sender in all_categories:
                count_2 = 1
                for cat in all_categories:
                    if not sender:
                        print(f'Category {count_2}: {cat}')
                    count_2 += 1
                receiver = input(f'Please choose the receiver from the above: ').title()
                if receiver in all_categories:
                    try:
                        amount = int(input('How much do you want to transfer? ₦'))
                        previous_sender_balance = self.categories[sender][2]
                        previous_receiver_balance = self.categories[receiver][2]
                        if amount <= previous_sender_balance:
                            self.categories[sender][2] = previous_sender_balance - amount
                            self.categories[receiver][2] = previous_receiver_balance + amount
                            print(self.categories)
                        else:
                            print('You don\'t have sufficient funds, please deposit\n')
                            self.deposit()
                    except Exception as e:
                        print(e)
                else:
                    print('Error!!! Category not found')
            else:
                print('Error!!! Category not found')
