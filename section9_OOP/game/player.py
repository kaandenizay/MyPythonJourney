class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3  # This is private attribute, not direct access
        # Data attribute must not have the same name as the property
        self._level = 1
        self._score = 0

    def _get_lives(self):  # We are using _ to indicate that these methods are hidden purpose
        # Indicate for the user, not really hidden, there is no need for clients to use them directly
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):  # We are using _ to indicate that these methods are hidden purpose
        # Indicate for the user, not really hidden, there is no need for clients to use them directly
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("Level cannot be less than 1")


    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)
    # Data attribute must not have the same name as the property

    @property
    def score(self):
        return self._score

    @score.setter # setter decorator format : property_name.setter
    def score(self, value):
        self._score = value

    """
    When you print an object, Python looks for a special method called __str__
    """
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)

