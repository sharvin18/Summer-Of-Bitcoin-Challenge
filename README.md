# Summer-Of-Bitcoin-Challenge
Code Challenge - Summer of Bitcoin - Solution

# Problem Statement

- Bitcoin miners construct blocks by selecting a set of transactions from their mempool. Each transaction in the mempool includes: fee, weight, parent transactions
- The miner selects an ordered list of transactions which have a combined weight below the maximum block weight.

TO DO:

```sh
1. Read a file mempool.csv, with the format: txid , fee , weight , parent_txids
2. We need to output a block of transaction id's which accumulate to a total weight of less 4000000
3. Condition for the block: Transactions with parent transcations can be included only if it's parent transactions have been included before
```
