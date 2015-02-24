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
		"""Private method of class AntSystem. Method updates pheromone trails.
			Args:
				top_ants_num(int, optional) : trail is updated only for
				top_ants_num best ant solutions
		"""
		if top_ants_num is None:
			top_ants_num = len(self.ant_population) #if argument top_ants_num 
			#is not given, we update trails for all ants

		for i in range(0, top_ants_num):
			ant = self.ant_population[i]
			delta = 1 / ant.tour_length #shorter paths will leave stronger
			#pheromone trails
			for j in range(0, len(self.city_list) - 1):
				city_from = ant.city_permutation[j]
				city_to = ant.city_permutation[j + 1]
				self.pheromone_trails[city_from][city_to] += delta
				self.pheromone_trails[city_to][city_from] += delta


	def __evaporate_trails(self):
		"""Private method of class AntSystem. Method evaporates pheromone trails.

		"""
		city_num = len (self.city_list)
		for i in range(0, city_num):
			for j in range(i+1, city_num):
				self.pheromone_trails[i][j] *= (1 - ro)
				self.pheromone_trails[j][i] *= (1 - ro)


