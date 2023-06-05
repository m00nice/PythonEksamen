class Class:

    def __init__(self, subject, teacher, schedule):
        self._subject = subject
        self.__teacher = teacher
        self._schedule = schedule

    @property
    def schedule(self):
        return self._schedule
    
    @schedule.setter
    def schedule(self, value):
        self._schedule = value
    
    def getTeacher(self):
        return self.__teacher

    
