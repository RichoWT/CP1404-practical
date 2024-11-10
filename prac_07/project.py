"""
CP1404
time started: 5:10pm (estimate - 1 day)
time finished: 11:46pm
"""
import datetime


class Project:

    def __init__(self, name='', start_date='', priority=0, cost_estimate=0.0, completion_percentage=0.0):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}, completion: {self.completion_percentage}"

    def is_complete(self):
        return self.completion_percentage == 100
