class Boss:

    def __init__(self, id_ : int, name : str, company : str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
    
    def __str__(self) -> str:
        return f"({self.id} : {self.name} : {self.company} : {self.workers})"
    
    def add_worker(self, worker):
        self.workers.append(str(worker))

class Worker:

    def __init__(self, id_ : int, name : str, company : str, boss : Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss
    
    def __str__(self) -> str:
        return f"{self.id} : {self.name} : {self.company} : {self.__boss}"
    
    @property
    def boss(self):
        return self.__boss
    
    @boss.setter
    def boss(self, value):
        if type(value) == Boss:
            self.__boss = value
        else:
            print("Значення повиннно бути типу Boss")

boss1 = Boss(1, "Bob", "Bob&Co")
boss2 = Boss(1, "Jake", "Jake&Finn")
worker1 = Worker(2, "Nick", "Bob&Co", boss1)
print(str(worker1))
boss1.add_worker(worker1)
print(str(boss1))
print(worker1.boss)
worker1.boss = boss2
print(worker1.boss)