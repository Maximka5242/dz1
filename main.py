from random import *

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 200
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.money -= 5  # трохи витрат на навчання

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10  # витрати на розваги

    def to_work(self):
        print("Time to work")
        self.money += 50
        self.gladness -= 4
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness < 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money < -50:
            print("Борги... вигнали з універу")
            self.alive = False

    def end_of_day(self, day):
        print("\n" + "-" * 20)
        print(f"Day: {day}")
        print(f"Gladness: {self.gladness}")
        print(f"Progress: {self.progress}")
        print(f"Money: {self.money}")
        print("-" * 20 + "\n")

    def live(self, day):
        if self.money < 20:
            self.to_work()
        elif self.progress < 0.5:
            self.to_study()
        else:
            live_cube = randint(1, 3)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()

        self.end_of_day(day)
        self.is_alive()

student_Nazar = Student("Nazar")

for day in range(1, 366):
    if not student_Nazar.alive:
        break
    student_Nazar.live(day)
