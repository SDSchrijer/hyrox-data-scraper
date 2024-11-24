# Built-in Python packages
import os
from enum import Enum

MODEL = 'HYROX Scraper'
VERSION = '1.0.0'
AUTHOR = 'Stef Schrijer'
DEPLOY = 0
ROOT = os.path.abspath(os.path.dirname(__file__))

class Division(Enum):
    open = "H"
    pro = "HPRO"
    elite = "HE"
    doubles = "HD"
    relay = "HMR"
    goruck = "HG"
    goruck_doubles = "HDG"

class Gender(Enum):
    male = "M"
    female = "W"