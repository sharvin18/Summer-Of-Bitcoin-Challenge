# Summer-Of-Bitcoin-Challenge
Code Challenge - Summer of Bitcoin - Solution

# Problem Statement

- Bitcoin miners construct blocks by selecting a set of transactions from their mempool. Each transaction in the mempool includes: fee, weight, parent transactions
- The miner selects an ordered list of transactions which have a combined weight below the maximum block weight.

TO DO:

```sh

1. Read a file mempool.csv, with the format: txid , fee , weight , parent_txids

2. We need to output a block of transaction ids which accumulate to a total weight of less 4000000

3. Condition for the block: Transactions with parent transcations can be included 
only if it's parent transactions have been included before

```

# Aproach:

- The logic behind my program is that to I have used the fee/weight ratio to maximize the fee for the miners. The greater value for the ratio are considered first. This approach is similar to the `Fractional Knapsack Algorithm` which uses the profit/weight ratio for maximizing the profit.
- For storing the input from csv file, I have used the `MemPoolTransaction` class that stores the following values for each transaction: txid, fee, weight, fee/weight ratio, parents, whether transaction is valid or not.
- The `BlockOperations` class is used to perform all the operations to achieve the optimal solution
- All the transactions are checked one by one in the descending order of their ratios. The two conditions that allow the transaction to take place are:
```python
total_weight <= 4000000 and transaction.parent should be already included:
    condition = True
```

# Output

```sh
# An output file block.txt with a total of 3214 transactions

Total Fees: 5769626
Total Weight: 3999940  ### Less than 4000000
Total transactions: 3214

```


