# CSCI-6212-1-Project-2
Repo for CSCI-6212-1 Project 2

## Running Instructions
Run it by:
`python3 proj-2.py`

## Graph
<img width="1000" height="600" alt="theoretical_vs_mean_median" src="https://github.com/user-attachments/assets/cc536346-5ce8-4ffd-85bc-d1ff3fa3e1e7" />

## Example Data
The output lloks like:
```
[Array Length] [Shifted by]   [Actual Max]   [Computed Max]  [Theoretical time] [Experimental time]  [Ratio (Experimental/Theoretical)]
------------------------------------------------------------------------------------------
10              2              9              9                3.32                438.94                132.14                        
100             52             99             99               6.64                756.00                113.79                        
1,000           964            999            999              9.97                1364.04               136.87                        
10,000          7,201          9,999          9,999            13.29               1713.98               128.99                        
100,000         79,558         99,999         99,999           16.61               2183.02               131.43                        
1,000,000       920,603        999,999        999,999          19.93               2749.96               137.97                        
10,000,000      4,637,653      9,999,999      9,999,999        23.25               2113.00               90.87                         
100,000,000     34,094,975     99,999,999     99,999,999       26.58               2426.97               91.32                         
1,000,000,000   18,450,563     999,999,999    999,999,999      29.90               2544.96               85.12                         
------------------------------------------------------------------------------------------
Median Ratio (Experimental/Theoretical)                               128.99
```
