
import random
import json
from generators.Generator import Generator
from util import Filters



class Organization(Generator):
    def __init__(self, redis, features={}):

        Generator.__init__(self,redis,features)


