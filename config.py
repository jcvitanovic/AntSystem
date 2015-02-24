"""Module contains default values of configuration variables.
	Config variables:
		m (int) : population size
		top_ants_num (int) : number of best ants for trail updates
		alpha (double) : pheromone constant 
		beta (double) : heuristic constant
		iterations (int) : number of iterations
		pheromone_init (double) : initial value for pheromone trails on edges

""" 
m = 40
ro = 0.2
alpha = 1
beta = 0
iterations =  0
top_ants_num = 0
pheromone_init = 1 / 5000