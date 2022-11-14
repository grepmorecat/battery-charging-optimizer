import uuid

class Cycle:
    def __init__(self):
        self.id = uuid.uuid4()

if __name__ == "__main__":
    c = Cycle()
    print(c.id)