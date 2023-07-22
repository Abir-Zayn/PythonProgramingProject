
class GetBalance:
    savingAllmoney = []
    WithdrawingAllMoney = []
    TotalLoan = []
    clearingLoan = []
    loanFeature = True

    def __init__(self, userName, userId, Location, Phone, Position):
        self.userName = userName
        self.userId = userId
        self.Location = Location
        self.Phone = Phone
        self.Position = Position

    def depositBalance(self, newAmount):
        if newAmount >= 0:
            self.savingAllmoney.append(newAmount)

    def withdrawnBalance(self, newAmount):
        if newAmount >= 0:
            self.WithdrawingAllMoney.append(newAmount)

    def totalProvidedLoans(self, amount):
        self.TotalLoan.append(amount)

    def totalClearLoans(self, amount):
        self.clearingLoan.append(amount)


class createAdminPanel(GetBalance):

    def __init__(self, userName, userId, Location, Phone, Position):
        super().__init__(userName, userId, Location, Phone, Position)

    def calculateTotalBalance(self):
        totalSave = 0
        totalGone = 0
        amountRightNow = 0

        for num in self.savingAllmoney:
            totalSave += num

        for nums in self.WithdrawingAllMoney:
            totalGone += nums

        amountRightNow = totalSave - totalGone
        return amountRightNow

    def calculateTotalLoan(self):
        sum = 0
        totalLoan=0
        clearLoan=0
        for num in self.TotalLoan:
            totalLoan += num

        for num in self.clearingLoan:
            clearLoan += num

        sum = totalLoan - clearLoan
        return sum

    def onOffLoan(self, answer):
        if answer == 0:
            return 0
        elif answer == 1:
            return 0
