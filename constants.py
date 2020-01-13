"""
This file holds All the constants for the project
"""
from enum import Enum


class Operations(Enum):
    """
    Status for the projects, documents and job
    """
    ADD = 'ADD_CHILD'
    GET = 'GET_RELATIONSHIP'


class Relations(Enum):
    pu = 'Paternal-Uncle'
    mu = 'Maternal-Uncle'
    pa = 'Paternal-Aunt'
    ma = 'Maternal-Aunt'
    sil = 'Sister-In-Law'
    bil = 'Brother-In-Law'
    son = 'Son'
    d = 'Daughter'
    s = 'Siblings'


class Gender(Enum):
    f = 'Female'
    m = 'Male'


class Module(Enum):
    pass


class Class(Enum):
    pass
