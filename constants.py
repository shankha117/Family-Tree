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
    Female = 'F'
    Male = 'M'


class Module(Enum):
    executor = "Executor"


class Class(Enum):
    add = "AddChild"
    get = "GetRelation"


class Methods(Enum):
    pu = 'get_paternal_uncle'
    mu = 'get_maternal_uncle'
    pa = 'get_paternal_aunt'
    ma = 'get_maternal_aunt'
    sil = 'get_sister_in_law'
    bil = 'get_brother_in_law'
    son = 'get_sons'
    d = 'get_daughters'
    s = 'get_siblings'
