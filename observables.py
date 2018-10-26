class Observable:
  def __init__(self):
    self.observers = []

  def subscribe(self, observer):
    self.observers.append(observer)

class Observer:
  def next(self, value):
    raise NotImplementedError

class Alcoholic(Observable):
  def __init__(self):
    super().__init__()
    self.liverUnhappiness = 0

  def drink(self):
    self.liverUnhappiness += 1
    for observer in self.observers:
      observer.next(None)

class Therapist(Observer):
  def __init__(self):
    self.drinksObserved = 0

  def next(self, value):
    self.drinksObserved = self.drinksObserved + 1

edwin = Alcoholic()
alex = Alcoholic()
therapist = Therapist()
edwin.subscribe(therapist)
edwin.drink()
alex.subscribe(therapist)
alex.drink()
print(f"the therapist counted {therapist.drinksObserved} beers")
