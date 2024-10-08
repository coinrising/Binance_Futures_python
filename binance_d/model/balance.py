class Balance:

    def __init__(self):
        self.accountAlias = ""
        self.asset = ""
        self.balance = 0.0
        self.crossWalletBalance = 0.0
        self.crossUnPnl = 0.0
        self.availableBalance = 0.0
        self.withdrawAvailable = 0.0

    @staticmethod
    def json_parse(json_data):
        result = Balance()
        result.accountAlias = json_data.get_string("accountAlias")
        result.asset = json_data.get_string("asset")
        result.balance = json_data.get_string("balance")
        result.crossWalletBalance = json_data.get_string("crossWalletBalance")
        result.crossUnPnl = json_data.get_string("crossUnPnl")
        result.availableBalance = json_data.get_string("availableBalance")
        result.withdrawAvailable = json_data.get_string("withdrawAvailable")

        return result