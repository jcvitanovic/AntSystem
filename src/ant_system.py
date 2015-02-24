"""Module any_system contains implementation of core class and methods for 
Any System algorithm.


"""
class AntSystem:
	"""Object representation of ant system algorithm.
	Encapsulates attributes and methods for simulating ant colony system.
		
		Attributes:
			//todo

	"""

	def __init__(self):
		"""Constructor method for class AntSystem.
		Initialization of all variables and paramaters of algorithm.
			
			Args:
				//todo

		"""
		pass	

	def run(self):
		"""Entry point of Ant System algorithm, called after __init__.
		Simulates ant colony actions for predefined number of iterations.
		In each iteration all ants walk the tour and seek for solution.
		After ants return from walk, the pheromone trail on city edges is 
		updated and evaporated.

		"""
		pass

	def __do_walk(self, Solution ant):
		"""Method that simulates walk of one ant and it's tour of the cities.
			Args:
				ant (Solution) : object of class Solution, one ant from colony
			Returns:
				Solution : updated object of class Solution, tour of cities 
				found by one ant
		"""
		pass

	def __update_trails(self, top_ants_num = None):
		"""Private method of class Ant System. Method is called in each
		iteration. Method perfoms task of updating pheromone trails for all 
		paths between cities.
		If argument top_ants_num is given, trail is updated only for 
		top_ants_num best ants solutions.

		"""
		pass

	def __evaporate_trails(self):
		"""

		"""
		pass
	
def visualize(self, Solution best_solution):
	"""Method for visualizing algorithm progress - optimal solution.
		Args:
			best_solution (Solution) : object of class Solution,
			tour of cities to be visualized

	"""
	pass


