"""
Title: Maximum Profit in Job Scheduling

Description:
We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, and a profit of `profit[i]` is earned.

You're given the `startTime`, `endTime` and `profit` arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time ranges.

If you choose a job that ends at time `X`, you will be able to start another job that starts at time `X`.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
"""
