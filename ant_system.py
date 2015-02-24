"""Module any_system contains implementation of core class and methods for 
Any System algorithm.


"""
from config import *
from util import *

class AntSystem:
	"""Object representation of ant system algorithm.
	Encapsulates attributes and methods for simulating ant colony system.
		
		Attributes:
				city_list (list of City) : list of all cities
				distance_matrix (list of double, optional) : n x n matrix with
				all distances between cities

	"""

	def __init__(self, city_list, distance_matrix):
		"""Constructor method for class AntSystem.
		Initialization of all variables and paramaters of algorithm.

			Args:
				city_list (list of City) : list of all cities
				distance_matrix (list of double, optional) : n x n matrix with
				all distances between cities

		"""
		self.city_list = city_list
		self.distance_matrix = distance_matrix
			

	def run(self):
		"""Entry point of Ant System algorithm, called after __init__.
		Simulates ant colony actions for predefined number of iterations.
		In each iteration all ants walk the tour and seek for solution.
		After ants return from walk, the pheromone trail on city edges is 
		updated and evaporated.

		"""
		for i in range(0, iterations):
			solutions = []
			for j in range(0, m):
				ant = Solution() #create solution
				ant = __do_walk(self, ant)
				ant = evaluate_solution(solution, city_list) #evaluate fitness of solution
				solutions.append(ant)
			solutions.sort() #sort by fitness : from shortest tour lenght to largest
			__update_trails(self, top_ants_num)
			__evaporate_trails(self)
			visualize(city_list, solutions[0]) #visualize the best solution path

	def __do_walk(self, ant):
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
		top_ants_num best ant solutions.

		"""
		pass

	def __evaporate_trails(self):
		"""

		"""
		pass


