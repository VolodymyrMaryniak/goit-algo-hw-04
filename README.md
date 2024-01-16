# Homework 4

## Measurement results (total time of 5 executions)
Algorithm            | Time small data (10,000) | Time medium data (100,000) | Time large data (1,000,000)
-------------------- | ------------------------ | -------------------------- | ----------------------------
Bubble Sort          | 0.17331                  | 19.09123                   | 
Insertion Sort       | 0.07892                  | 8.32388                    |
Selection Sort       | 0.08822                  | 9.02629                    |
Merge Sort           | 0.00971                  | 0.08659                    | 14.76360
Quick Sort           | 0.00514                  | 0.07343                    | 15.06554
Shell Sort           | 0.00578                  | 0.10617                    | 39.61318
Radix Sort           | 0.00361                  | 0.03704                    | 9.83376
Python (sorted)      | 0.00025                  | 0.00414                    | 1.05487
Python (list.sort)   | 0.00023                  | 0.00399                    | 0.99057

## Conclusions
Native Python sorting algorithms show the best results. It's especially notable on the large data sets.
