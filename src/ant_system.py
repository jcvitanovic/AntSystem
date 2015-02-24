"""Module any_system contains implementation of core classes and methods for Any System algorithm.


"""
class AntSystem:
	"""Object representation of ant system algorithm. Encapsulates attributes and methods for running simulations of ant colony system.
		
		Attributes:
			//todo

	"""

	def __init__(self):
		"""Constructor method for class AntSystem. Initialization of all variables and paramaters of algorithm.
			
			Attributes:
				//todo

		"""
		pass

	

	def run(self):
		"""Entry point of Ant System algorithm, called after __init__. Simulates ant colony actions for given number of iterations.
		In each iteration all ants walk the tour and seek for solution. After ants return from walk, the pheromone trail on city edges is updated and evaporated.

		"""
		pass

	def __do_walk(self, Solution ant):
		"""

		"""

	def __update_trails(self, top_ants_num = None):
		"""Private method of class Ant System. Method is called in each iteration. Method perfoms task of updating pheromone trails for all paths between cities.
		If argument top_ants_num is given, trail is updated only for top_ants_num best ants solutions.

		"""
		pass

	def __evaporate_trails(self):
		"""

		"""
		pass
	
	def visualize(self):
		"""

		"""
		pass


