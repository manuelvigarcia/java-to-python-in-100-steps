from abc import ABC, abstractmethod

class AbstractRecipe(ABC):

    def execute(self):
        self.get_ready()
        self.do_the_dish()
        self.cleanup()

    @abstractmethod
    def get_ready(self):
        pass

    @abstractmethod
    def do_the_dish(self):
        pass

    @abstractmethod
    def cleanup(self):
        pass

class Recipe1(AbstractRecipe):

    def get_ready(self):
        print('get raw materials')
        print('get utensils')

    def do_the_dish(self):
        print('do the dish')

    def cleanup(self):
        print('clean utensils')

class RecipeWithMicrowave(AbstractRecipe):
    def get_ready(self):
        print('Get the raw materials')
        print('Switch on the microwave')

    def do_the_dish(self):
        print('get stuff ready')
        print('Put it in the microwave')

    def cleanup(self):
        print('Clean up the utensils')
        print('Switch off the microwave')



recipe = Recipe1()
recipe.execute()

quick_recipe = RecipeWithMicrowave()
quick_recipe.execute()
