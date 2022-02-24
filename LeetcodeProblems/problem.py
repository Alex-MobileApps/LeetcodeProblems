from typing import List, Optional

class Problem():

    # Static variables

    DIFFICULTIES = set(['easy', 'medium', 'hard'])


    # Overrides

    def __init__(self, num: int, name: str, url: str, difficulty: str, premium: bool, tags: Optional[List[str]] = None):
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
            Difficulty of problem ('easy', 'medium' or 'hard')
        premium : bool
            Whether or not the problem is a premium question or not
        tags : List[str], optional
            Tags that identify the problem, by default None
            If None, tags will be set to []

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
        difficulty = difficulty.lower()
        if difficulty not in Problem.DIFFICULTIES:
            raise ValueError('Difficulty must be in:', ', '.join(Problem.DIFFICULTIES))
        if tags is None:
            tags = []
        elif type(tags) is str:
            tags = [tags.lower()]
        else:
            tags = [tag.lower() for tag in tags]
        self.num = num
        self.name = name
        self.url = url
        self.difficulty = difficulty
        self.premium = premium
        self.tags = set(tags)

    def __repr__(self) -> str:
        """
        String representation of the problem

        Returns
        -------
        str
            String representation of the problem
        """
        return f'Problem{{num: {self.num}, name: {self.name}, difficulty: {self.difficulty}, url: {self.url}}}'