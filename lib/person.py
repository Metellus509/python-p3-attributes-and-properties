#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name=None,job=None):
        if name is not None:
            self.name=name
        if job is not None:
            self.job=job
    
    def getName(self):
        return self._name
    
    def setName(self,name):
        if isinstance(name,str) and (1<=len(name)<=25):
            self._name=name.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    def getJob(self):
        return self._job     

    def setJob(self,job):
        if job in APPROVED_JOBS:
            self._job=job
        else:
           print( "Job must be in list of approved jobs." )


    name=property(getName,setName)
    job=property(getJob,setJob)
