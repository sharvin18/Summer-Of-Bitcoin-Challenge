
class MemPoolTransaction():

    transactions = []

    def __init__(self, txid, fee, weight, parents):

        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.ratio = round((float(fee)/float(weight)),6)
        self.parents = parents
        self.transactions.append(txid)
        self.isvalid = False

        if parents in self.transactions:
            self.isvalid = True
            

    def get_txid(self):
        return self.txid

    def get_fee(self):
        return self.fee         
  
    def get_weight(self):
        return self.weight

    def get_ratio(self):
        return self.ratio

    def parent_is_valid(self):
        return self.isvalid


class block_operations():

    total_fees = 0
    total_weight = 0
    max_weight = 4000000
    final_transactions = []
    inputBlock = []

    def read_file(self, file_name):

        with open(file_name) as f:
            self.inputBlock = [MemPoolTransaction(*line.strip().split(',')) for line in f.readlines()[1:]]

        block_operations().sort_descending(self.inputBlock)


    def sort_descending(self, transactions):
        sorted_list = sorted(transactions,key= lambda e: e.get_ratio(),reverse=True)
        block_operations().check_transactions(sorted_list)
        

    def write_to_file(self):

        file = open("block.txt","a")
        for i in self.final_transactions:
            file.write(str(i.get_txid()) + '\n')
        file.close()
        



    def check_condition(self, current_transaction):

        flag = False;
        weight = self.total_weight + current_transaction.get_weight()

        if weight <= self.max_weight and current_transaction.parent_is_valid():
            flag = True;
        
        return flag


    def check_transactions(self, all_inputs):

        for i in all_inputs:
            if(block_operations().check_condition(i)):
                self.total_fees += i.get_fee()
                self.total_weight += i.get_weight()
                self.final_transactions.append(i)
                
            
        print("Total Fees: ", self.total_fees)
        print("Total Weight: ", self.total_weight)
        print("Total transactions: ", len(self.final_transactions))
    
        block_operations().write_to_file()


if __name__ == '__main__':
    
    transactions = block_operations()
    transactions.read_file('mempool.csv')