# Leetcode Problems

Randomly filter and select Leetcode problems to complete, to practice and improve your programming skills.

## Requirements
- Python 3

## Examples

Either manually add problems, or load from a JSON file

### From JSON

```
from LeetcodeProblems import ProblemSet

problemSet = ProblemSet('demo.json')

for problem in problemSet.selectRandom(count=3, difficulty='medium', tags=['sliding_window']):
    print(problem.num, problem.name, problem.url)
```
```
# Output
1004 Max Consecutive Ones III https://leetcode.com/problems/max-consecutive-ones-iii/
209 Minimum Size Subarray Sum https://leetcode.com/problems/minimum-size-subarray-sum/
904 Fruit Into Baskets https://leetcode.com/problems/fruit-into-baskets/
```

### Manually

```
from LeetcodeProblems import Problem, ProblemSet

problem1 = Problem(
    num=53,
    name='Maximum Subarray',
    url='https://leetcode.com/problems/maximum-subarray/',
    difficulty='easy',
    premium=False,
    tags=['sliding_window'])

problem2 = Problem(
    num=209,
    name='Minimum Size Subarray Sum',
    url='https://leetcode.com/problems/minimum-size-subarray-sum/',
    difficulty='medium',
    premium=False,
    tags=['sliding_window'])

problemSet = ProblemSet()
problemSet.add(problem1)
problemSet.add(problem2)

for problem in problemSet.selectRandom(count=1, tags=['sliding_window']):
    print(problem.num, problem.name, problem.url)
```
```
# Output
209 Minimum Size Subarray Sum https://leetcode.com/problems/minimum-size-subarray-sum/
```