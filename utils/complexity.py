from enum import IntEnum


class Complexity(IntEnum):
    """
    Enumeration of common algorithmic time/space complexities, ordered by asymptotic growth rate.
    """
    CONSTANT       = 0   # O(1)
    LOGARITHMIC    = 1   # O(log n)
    SQRT           = 2   # O(√n)
    LINEAR         = 3   # O(n)
    LINEARITHMIC   = 4   # O(n log n)
    QUADRATIC      = 5   # O(n^2)
    CUBIC          = 6   # O(n^3)
    EXPONENTIAL    = 7   # O(2^n)
    FACTORIAL      = 8   # O(n!)

    def __str__(self) -> str:
        mapping = {
            self.CONSTANT: "O(1)",
            self.LOGARITHMIC: "O(log n)",
            self.SQRT: "O(√n)",
            self.LINEAR: "O(n)",
            self.LINEARITHMIC: "O(n log n)",
            self.QUADRATIC: "O(n^2)",
            self.CUBIC: "O(n^3)",
            self.EXPONENTIAL: "O(2^n)",
            self.FACTORIAL: "O(n!)",
        }
        return mapping[self]

    @classmethod
    def from_string(cls, s: str) -> "Complexity":
        mapping = {
            "O(1)": cls.CONSTANT,
            "O(log n)": cls.LOGARITHMIC,
            "O(√n)": cls.SQRT,
            "O(n)": cls.LINEAR,
            "O(n log n)": cls.LINEARITHMIC,
            "O(n^2)": cls.QUADRATIC,
            "O(n^3)": cls.CUBIC,
            "O(2^n)": cls.EXPONENTIAL,
            "O(n!)": cls.FACTORIAL,
        }
        try:
            return mapping[s]
        except KeyError:
            raise ValueError(f"Unknown complexity string: {s}")
