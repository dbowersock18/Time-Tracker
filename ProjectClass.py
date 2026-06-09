class Project: 
    name: str
    time: int
    
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def test(self):
        print("test")