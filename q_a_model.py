import math
from random import random

#com
class QAModel(object):
    def __init__(self, id, question, answer, ok):
        self.id = id
        self.question = question
        self.answer = answer
        self.ok = ok
        self.weight = (1+ok) * random()
