from abc import ABC, abstractmethod
from adminPanel import GetBalance, createAdminPanel
from datetime import datetime


class Users(ABC):
    def __init__(self, accountNumber, name, PhoneNumber, NIDNo, mail) -> None:
        self.accountNumber = accountNumber
        self.accountHolder = name
        self.PhoneNumber = PhoneNumber
        self.NIDNo = NIDNo
        self.mail = mail
        self.__balance = 0

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, newBalance):
        if newBalance >= 0:
            self.__balance = newBalance
        else:
            raise ValueError("Balance cannot be negative.")


class CreateAccount(Users, createAdminPanel):

    def __init__(self, accountNumber, name, PhoneNumber, NIDNo, mail) -> None:
        super().__init__(accountNumber, name, PhoneNumber, NIDNo, mail)
        self.transaction = []
        self.loanAmount = 0
        self.loanStatus = False  # False = No Loan
        self.loanPermit = 1

    def recordTransaction(self, transactionTypes, amount):
        transaction_date = datetime.now()
        transaction = (transaction_date, transactionTypes, amount)
        self.transaction.append(transaction)

    def deposit(self, amount):
        if amount > 0:
            print(self.accountHolder, ' have added', amount, 'tk')
            newAmount = self.balance + amount
            self.balance = newAmount
            self.depositBalance(amount)
            self.recordTransaction('Deposit', amount)
        else:
            raise ValueError('You have added less or equal 0 tk')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.withdrawnBalance(amount)
            print(self.accountHolder, ' have withdrawn >', amount, 'tk')
            self.recordTransaction('Deposit', amount)
        else:
            print('You haven\'t sufficient balance. Bankrupt!')

    def transfer(self, targetAccount, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            targetAccount.deposit(amount)
            print(f'{self.accountHolder} has transferred {amount} to {targetAccount.accountHolder}')
            self.recordTransaction('Transferred', amount)
        else:
            print('Failed to transfer money')

    def getTransaction(self):
        return self.transaction

    # Condition = Study / Tour / Medical
    def getLoan(self, condition, loanApplicable):
        if loanApplicable == 1:
            if self.balance > 500:
                self.loanAmount = self.balance * 2
                self.balance = self.balance + self.loanAmount
                conditions = condition
                loanMoney = self.loanAmount
                self.withdrawnBalance(loanMoney)
                self.totalProvidedLoans(loanMoney)
                self.loanStatus = True
                print('Loan Accepted in', conditions, '. Received >', self.loanAmount)
            else:
                print('Sorry No Loan will be applicable for you.')
        else:
            print('Loan Feature has turned off.')

    def clearLoan(self, PaidAmount):
        if PaidAmount > 0:
            self.balance = self.balance - PaidAmount
            self.loanAmount = self.loanAmount - PaidAmount
            remainingAmount = self.loanAmount - PaidAmount
            self.depositBalance(PaidAmount)
            self.totalClearLoans(PaidAmount)

        # If all dues has been cleared and user had paid more than loan. Then add to orginal Balance
            if self.loanAmount <= 0 and remainingAmount < 0:
                remainingAmount = remainingAmount * (-1)
                self.balance = self.balance + remainingAmount
                print('Balance', self.balance)

            if self.loanAmount == 0:
                self.loanStatus = False
                print('You have cleared your Loan')
            else:
                print('You have paid', PaidAmount, '. Remaining payable balance ', {self.loanAmount})

    def __repr__(self) -> str:
        if self.loanStatus is False:
            return f'Name > {self.accountHolder}\nMail > {self.mail}\nBalance > {self.balance}'
        else:
            return f'Name > {self.accountHolder}\nMail > {self.mail}\nBalance > {self.balance}\nLoan Amount >{self.loanAmount}'
