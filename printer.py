from datetime import datetime

class Printer:

    def __init__(self):
        self.resourse = {
            "paper":100,
            "ink": 500

        }

    def report(self):
        for key in self.resourse:
            print(f"{key}: {self.resourse[key]}, ticket left")
            input()


    def is_resourse_sufficient(self):
        for key in self.resourse:
            if self.resourse[key] < 1:
                print(f"You do not have enough {key} to print")
                return False
        return True
        

    def print_ticket(self, station):
        print("----------Ticket----------")
        print("From Amritsar")
        print(f"To {station.name}")
        print(f"Cost: {station.cost}")
        print(f"Printed: {str(datetime.now())} ")
        print("---------------------------")
        input()

        for key in self.resourse:
            self.resourse[key] = self.resourse[key] - 1