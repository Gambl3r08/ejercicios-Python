#Roberto Lozada
#Luis Everley


from numpy import asarray
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import argsort
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed

def objective(v):
    x, y = v    
    return  (x**4) + (y**4) + (x**4) - (x**2) + (2*(y**2)) -(3*(x**2)) + (2*(x**2)) - y - x 
    
 

def in_bounds(point, bounds):
	
	for d in range(len(bounds)):
		
		if point[d] < bounds[d, 0] or point[d] > bounds[d, 1]:
			return False
	return True
 

def es_comma(objective, bounds, n_iter, step_size, mu, lam):
	best, best_eval = None, 1e+10
	
	n_children = int(lam / mu)
	
	population = list()
	for _ in range(lam):
		candidate = None
		while candidate is None or not in_bounds(candidate, bounds):
			candidate = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
		population.append(candidate)
	
	for epoch in range(n_iter):
		
		scores = [objective(c) for c in population]
		
		ranks = argsort(argsort(scores))
		
		selected = [i for i,_ in enumerate(ranks) if ranks[i] < mu]
		
		children = list()
		for i in selected:
			
			if scores[i] < best_eval:
				best, best_eval = population[i], scores[i]
				print('%d, Best: f(%s) = %.5f' % (epoch, best, best_eval))
                
			
			for _ in range(n_children):
				child = None
				while child is None or not in_bounds(child, bounds):
					child = population[i] + randn(len(bounds)) * step_size
				children.append(child)
		
		population = children
	return [best, best_eval]
 
 

seed(1)

bounds = asarray([[-5.0, 5.0], [-5.0, 5.0]])

n_iter = 5000

step_size = 0.15

mu = 5

lam = 100

best, score = es_comma(objective, bounds, n_iter, step_size, mu, lam)
print('Done!')
print('f(%s) = %f' % (best, score))