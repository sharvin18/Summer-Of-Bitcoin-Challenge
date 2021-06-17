
## A class for setting the data of each transaction.
## All the parameters that are required for determining
## the optimal solution are provided by this class.
class MemPoolTransaction():

    transactions = []
    current_parents=[]

    def __init__(self, txid, fee, weight, parent_list):

        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.ratio = round((float(fee)/float(weight)),6)
        self.parents = parent_list
        self.transactions.append(txid)
        self.isvalid = False

        if self.parents == "":
            self.isvalid = True
        else:
            self.current_parents = self.parents.split(";")
        
            for parent in self.current_parents:
                if parent in self.transactions:
                    self.isvalid = True
                else:
                    self.isvalid = False
                    break

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
    
    def get_parents(self):
        return self.parents

## All the operations that are performed for determining the optimal solutions 
## will be done by this class.
class block_operations():

    ## initliazing variables. 
    total_fees = 0
    total_weight = 0
    max_weight = 4000000
    final_transactions = []
    inputBlock = []

    ## Reads the input file and saves it in a list according to the determining class.
    def read_file(self, file_name):

        ## Read the file from the 2nd line.
        with open(file_name) as f:
            self.inputBlock = [MemPoolTransaction(*line.strip().split(',')) for line in f.readlines()[1:]]

        block_operations().sort_descending(self.inputBlock)

    ## Sorting the list according to the fee/weight ratio for maximum profit.
    def sort_descending(self, transactions):
        sorted_list = sorted(transactions,key= lambda e: e.get_ratio(),reverse=True)
        block_operations().check_transactions(sorted_list)
        
    ## Writing the transaction Ids to the output file.
    def write_to_file(self):

        file = open("block.txt","a")
        for i in self.final_transactions:
            file.write(str(i.get_txid()) + '\n')
        file.close()

    ## Checks whether the transaction is valid or not.
    def check_condition(self, current_transaction, current_weight):

        flag = False;
        weight = current_weight + current_transaction.get_weight()

        ## Check if weight is <4000000 and all parents are already included
        if weight <= self.max_weight and current_transaction.parent_is_valid():
            flag = True;
        
        return flag

    ## Updates the weight, fee and transations to be made after checking the validity of each transaction
    def check_transactions(self, all_inputs):

        for i in all_inputs:

            if(block_operations().check_condition(i, self.total_weight)):
                self.total_fees += i.get_fee()
                self.total_weight += i.get_weight()
                self.final_transactions.append(i)
        
        block_operations().end_transaction(self.total_fees, self.total_weight, len(self.final_transactions))
    
    ## Output the values 
    def end_transaction(self, tot_fee, tot_weight, tot_transactions):
            
        print("Total Fees:", tot_fee)
        print("Total Weight:", tot_weight)
        print("Total transactions:", tot_transactions)
    
        block_operations().write_to_file()


## The entire program is handled with the help of 2 classes.
## Simply pass the csv file name as the input file and 
## an output file with the optimal transactions will be generated.
if __name__ == '__main__':
    
    transactions = block_operations()
    transactions.read_file('mempool.csv')  ## Pass the file name