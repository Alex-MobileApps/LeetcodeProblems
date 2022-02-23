from typing import List, Optional

class Problem():

    # Static variables

    DIFFICULTIES = set(['EASY', 'MEDIUM', 'HARD'])


    # Overrides

    def __init__(self, num: int, name: str, url: str, difficulty: str, premium: bool, categories: Optional[List[str]] = None):
        """
        Creates a new problem object

        Parameters
        ----------
        num : int
            Number that identifies the problem
        name : str
            Name of the problem
        url : str
            URL to find problem
        difficulty : str
            Difficulty of problem
        premium : bool
            Whether or not the problem is a premium question or not
        categories : List[str], optional
            Category to identify the problem, by default None
            If None, categories will be set to ['UNKNOWN']

        Raises
        ------
        ValueError
            If num is negative or not an integer, premium is not a boolean, name is empty, url is empty, or difficulty is invalid
        """
        if type(num) is not int or num <= 0:
            raise ValueError('Num be be a positive integer')
        if type(premium) is not bool:
            raise ValueError('Premium must be a boolean')
        if not name:
            raise ValueError('Name must be a non-empty string')
        if not url:
            raise ValueError('URL must be a non-empty string')
        difficulty = difficulty.upper()
        if difficulty not in Problem.DIFFICULTIES:
            raise ValueError('Difficulty must be in:', ', '.join(Problem.DIFFICULTIES))
        if categories is None:
            categories = ['UNKNOWN']
        elif type(categories) is str:
            categories = [categories.upper()]
        else:
            categories = [category.upper() for category in categories]
        self.num = num
        self.name = name
        self.url = url
        self.difficulty = difficulty
        self.premium = premium
        self.categories = set(categories)

    def __repr__(self) -> str:
        """
        String representation of the problem

        Returns
        -------
        str
            String representation of the problem
        """
        return f'Problem{{num: {self.num}, name: {self.name}, difficulty: {self.difficulty}, url: {self.url}}}'