import math
from random import random


class QAModel(object):
    def __init__(self, id, question, answer, ok):
        self.id = id
        self.question = question
        self.answer = answer
        self.ok = ok
        self.weight = math.floor((1+ok) * 100 * random())
