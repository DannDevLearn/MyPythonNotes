class Personaje:
    def __init__(self, name: str, ability: str):
        self.name = name
        self.ability = ability

    def hello(self) -> str:
        return f"Hi my name is {self.name} and my ability is {self.ability}"
    
class SuperHero(Personaje):

    def __init__(self, name, ability, city: str):
        super().__init__(name, ability)
        self.city = city
    
    def save_the_day(self) -> str:
        return f"{self.name} is saving the day with {self.ability} in our city {self.city}"
    
class Villain(Personaje):

    def __init__(self, name, ability, enemy: str):
        super().__init__(name, ability)
        self.enemy = enemy

    def plan(self) -> str:
        return f"Wait! {self.name} will use a plan with {self.ability} againsts {self.enemy}"
    
hero = SuperHero("Captain Code", "Refactoringpower", "CofignCity")
bugman = Villain("BugMan", "Make Bugs", "Captain Code")

print(hero.hello())
print(bugman.hello())

print(hero.save_the_day())
print(bugman.plan())