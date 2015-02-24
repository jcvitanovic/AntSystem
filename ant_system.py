"""Module any_system contains implementation of core class and methods for 
Any System algorithm.


"""
from config import *
from util import *
from random import randrange, choice, shuffle, sample

class AntSystem:
	"""Object representation of ant system algorithm.
	Encapsulates attributes and methods for simulating ant colony system.
		
		Attributes:
				city_list (list of City) : list of all cities
				distance_matrix (list of double, optional) : n x n matrix with
				all distances between cities

	"""

	def __init__(self, city_list, distance_matrix):
		"""Constructor for class AntSystem.
		Initialization of all variables and paramaters of algorithm.

			Args:
				city_list (list of City) : list of all cities
				distance_matrix (list of double, optional) : n x n matrix with
				all distances between cities
				//todo: rest

		"""
		city_num = len(city_list)
		self.city_list = city_list		
		self.distance_matrix = distance_matrix
		self.ant_population = []
		self.pheromone_trails = [[pheromone_init] * city_num] * city_num
		self.probability_matrix = [[None] * city_num] * city_num

			

	def run(self):
		"""Entry point of Ant System algorithm, called after __init__.
		Simulates ant colony actions for predefined number of iterations.

		"""
		for i in range(0, iterations):
			self.ant_population = []
			for j in range(0, m):
				ant = self.ant_population[j]
				ant = __do_walk(self, ant)
				ant = evaluate_solution(solution, city_list) #evaluate fitness of solution
				self.ant_population.append(ant)
			self.ant_population.sort() #sort by fitness : from shortest tour lenght to largest
			__update_trails(self, top_ants_num)
			__evaporate_trails(self)
			visualize(city_list, self.ant_population[0]) #visualize the best solution path

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
		iteration.
			Args:
				top_ants_num(int, optional) : trail is updated only for
				top_ants_num best ant solutions
		"""
		pass

	def __evaporate_trails(self):
		"""

		"""
		pass


