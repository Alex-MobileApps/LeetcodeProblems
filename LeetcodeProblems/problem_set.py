import json
from random import shuffle
from typing import List, Optional
from .problem import Problem


class ProblemSet():

    TAG_MODES = set(['all', 'any'])

    # Overrides

    def __init__(self, path: Optional[str] = None):
        """
        Creates a new problem set object

        Parameters
        ----------
        path : str, optional
            Location of JSON data containing problem information, by default None
            Each object in the JSON file must contain keys for each parameter in the 'Problem' object constructor
        """
        self.problems = {}
        self.tags = {}
        if path:
            self.loadJson(path)

    def __len__(self) -> int:
        """
        Number of problems in the set

        Returns
        -------
        int
            Number of problems
        """
        return len(self.problems)

    def __getitem__(self, key: int) -> Problem:
        """
        Find problem with a specified number from the set

        Parameters
        ----------
        key : int
            Number of the problem

        Returns
        -------
        Problem
            Problem information
        """
        return self.problems[key]


    # Public

    def add(self, problem: Problem) -> Problem:
        """
        Add a problem to the set

        Parameters
        ----------
        problem : Problem
            Problem to add

        Returns
        -------
        Problem
            Problem if added successfully

        Raises
        ------
        ValueError
            If the problem's number already exists in the set
        """
        if problem.num in self.problems:
            raise ValueError(f'Problem {problem.num} already exists')
        self.problems[problem.num] = problem
        for tag in problem.tags:
            self.tags[tag] = self.tags.get(tag, 0) + 1
        return problem

    def loadJson(self, path: str) -> None:
        """
        Add problems from a JSON file to the set

        Parameters
        ----------
        path : str
            Location of JSON data containing problem information
        """
        with open(path, 'r') as file:
            data = json.load(file)
            for d in data:
                self.add(Problem(**d))

    def remove(self, num: int) -> Problem:
        """
        Remove a problem from the set

        Parameters
        ----------
        num : int
            Number of the problem to remove

        Returns
        -------
        Problem
            Removed problem

        Raises
        ------
        ValueError
            If num is not an integer
        """
        if type(num) is not int:
            raise ValueError('Num must be an integer')
        if num not in self.problems:
            return
        problem = self.problems[num]
        del self.problems[num]
        for tag in problem.tags:
            if self.tags[tag] == 1:
                del self.tags[tag]
            else:
                self.tags[tag] -= 1
        return problem

    def selectRandom(self, count: int = 1, difficulty: Optional[str] = None, premium: Optional[bool] = None, tags: Optional[List[str]] = None, tag_mode: str = 'any') -> List[Problem]:
        """
        Select a random number of problems from the set, with specific filters

        Parameters
        ----------
        count : int, optional
            Number of problems to select, by default 1
        difficulty : str, optional
            Difficulty of problems to select ('easy', 'medium' or 'hard'), by default None
            If None, any difficulty can be selected
        premium : bool, optional
            Whether to select premium or non-premium problems, by default None
            If None, both premium and non-premium problems cans be selected
        tags : List[str], optional
            Tags used to select problems, by default None
            If None, any tag can be selected
        tag_mode : str, optional
            How tags are used to select problems, by default 'any'
            'all' : Selected problems must have all tags
            'any' : Selected problems must have at least one tag

        Returns
        -------
        List[Problem]
            Randomly selected problems

        Raises
        ------
        ValueError
            If an invalid difficulty or tag is requested
        """
        nums = set(self.problems.keys())

        if difficulty is not None:
            if difficulty not in Problem.DIFFICULTIES:
                raise ValueError('Difficulty must be in:', ', '.join(Problem.DIFFICULTIES))
            remove = set()
            for num in nums:
                if self[num].difficulty != difficulty:
                    remove.add(num)
            nums = nums.difference(remove)

        if tags is not None:
            for tag in tags:
                if tag not in self.tags:
                    raise ValueError('Tags must be in: ' + ', '.join(self.tags))
            if tag_mode not in ProblemSet.TAG_MODES:
                raise ValueError('Tag mode must be in: ' + ', '.join(ProblemSet.TAG_MODES))
            tags = set([tags]) if type(tags) == str else set(tags)
            remove = set()
            test = (lambda num: tags.intersection(self[num].tags)) if tag_mode == 'any' else (lambda num: self[num].tags.issuperset(tags))
            for num in nums:
                if not test(num):
                    remove.add(num)
            nums = nums.difference(remove)

        if premium is not None:
            remove = set()
            for num in nums:
                if self[num].premium != premium:
                    remove.add(num)
            nums = nums.difference(remove)

        nums = list(nums)
        shuffle(nums)
        if len(nums) > count:
            nums = nums[:count]
        return [self.problems[num] for num in nums]