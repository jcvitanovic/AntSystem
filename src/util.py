""" Module util contains helper functions and classes for solving TSP problem.

"""

class City:
	"""Object representation of a city.
	
		Attributes:
			x (double) : cartesian coordinate
			y (double) : cartesian coordinate
			name (string) : city name



	"""

	def __init__(self, x, y, name):
		"""Constructor method for class City.
		
			Args:
				x (double) : cartesian coordinate to be set
				y (double) : cartesian coordinate to be set
				name (string) : city name to be set

		"""
		self.x = x
		self.y = y
		self.name = name

class Solution:
	"""Object representation of one particular solution for the TSP problem.

		Attributes:
			tour_length(double) : length of the tour for the solution
			city_permutation(list of int) : array of indicies of cities, represents order of visiting each city

	"""

	def __init__(self):
		"""Constructor method for class Solution.

		"""
		self.city_permutation = None
		self.tour_length = None

	def __cmp__(self, other):
		"""Implementation of comparable method for class Solutions. Objects of class Solution are compared by attribure tour_length.

		"""
		if self.tour_length > other.tour_length:
			return 1
		elif self.tour_length < other.tour_length:
			return -1
		else:
			return 0

def load_cities():
	"""Method for loading and initializing list of cities for TSP problem.

		Returns:
			list of City : list of objects of class City
	"""

def evaluate_solution(solution, city_list, distance_matrix = None):
	"""Method for evaluating fitness of the solution. Method computes tour length for object of class Solution

		Args:
			solution (Solution) : one instance of TSP solution
			city_list (list of City) : list of all cities
			distance_matrix (list of double) : n x n matrix with all distance values from each city to all other
		Returns:
			Solution : Solution object with updated length

	"""

def evaluate_population(solutions, city_list, distance_matrix = None):
	"""Entry point method for evaluating entire population of solutions. Accepts list of solutions and delegates the call to evaluate_solution method.

		Args:
			solutions (list of Solution) : list of instances of TSP solutions
			city_list (list of City) : list of all cities
			distance_matrix (list of double) : n x n matrix with all distance values from each city to all other

	"""