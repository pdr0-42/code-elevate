from pydantic import BaseModel


class Request(BaseModel):
    """
    A Pydantic model representing the input data for a prediction request.

    Attributes
    ----------
    CRIM : float
        Per capita crime rate by town.
    ZN : float
        Proportion of residential land zoned for lots over 25,000 sq. ft.
    INDUS : float
        Proportion of non-retail business acres per town.
    CHAS : int
        Charles River dummy variable (1 if tract bounds river; 0 otherwise).
    NOX : float
        Nitric oxides concentration (parts per 10 million).
    RM : float
        Average number of rooms per dwelling.
    AGE : float
        Proportion of owner-occupied units built prior to 1940.
    DIS : float
        Weighted distances to five Boston employment centers.
    RAD : float
        Index of accessibility to radial highways.
    TAX : float
        Full-value property tax rate per $10,000.
    PTRATIO : float
        Pupil-teacher ratio by town.
    LSTAT : float
        Percentage of lower status of the population.
    """

    CRIM: float
    ZN: float
    INDUS: float
    CHAS: int
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: float
    TAX: float
    PTRATIO: float
    LSTAT: float
