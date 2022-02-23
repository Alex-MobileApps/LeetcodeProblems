# Leetcode Problems

Helps practice Leetcode, by randomly selecting problems with specified difficulties and patterns.

## Requirements
- Python 3

## Usage

```
from LeetcodeProblems import Problem, ProblemSet
```
From JSON
```
problemSet = ProblemSet('demo.json')
problems = problemSet.selectRandom(count=5, difficulty='MEDIUM', categories=['SLIDING_WINDOW'])
for problem in problems:
    print(problem.num, problem.name, problem.url)

# Sample output
# 424 Longest Repeating Character Replacement https://leetcode.com/problems/longest-repeating-character-replacement/
# 209 Minimum Size Subarray Sum https://leetcode.com/problems/minimum-size-subarray-sum/
# 1004 Max Consecutive Ones III https://leetcode.com/problems/max-consecutive-ones-iii/
# 567 Permutation in String https://leetcode.com/problems/permutation-in-string/
# 438 Find All Anagrams in a String https://leetcode.com/problems/find-all-anagrams-in-a-string/
```
Manually
```
problem1 = Problem(
    num=53,
    name='Maximum Subarray',
    url='https://leetcode.com/problems/maximum-subarray/',
    difficulty='EASY',
    premium=False,
    categories=['SLIDING_WINDOW'])

problem2 = Problem(
    num=209,
    name='Minimum Size Subarray Sum',
    url='https://leetcode.com/problems/minimum-size-subarray-sum/',
    difficulty='MEDIUM',
    premium=False,
    categories=['SLIDING_WINDOW'])

problemSet = ProblemSet()
problemSet.add(problem1)
problemSet.add(problem2)

problems = problemSet.selectRandom(count=1, categories=['SLIDING_WINDOW'])
for problem in problems:
    print(problem.num, problem.name, problem.url)

# Sample output
# 209 Minimum Size Subarray Sum https://leetcode.com/problems/minimum-size-subarray-sum/
```