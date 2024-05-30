
import math
from qdpy import algorithms, containers, benchmarks, plots

grid = containers.Grid(shape=(64,64), max_items_per_bin=1, fitness_domain=((0., 1.),), features_domain=((0., 1.), ( 0., 1.)))
#What do these features mean? 
#:SOB:


algo = algorithms.RandomSearchMutPolyBounded(grid, budget=100000, batch_size=500, dimension=3, optimisation_task="maximization")
logger = algorithms.TQDMAlgorithmLogger(algo)


def eval_fn(ind):
    """An example evaluation function. It takes an individual as input, and returns the pair ``(fitness, features)``, where ``fitness`` and ``features`` are sequences of scores."""
    normalization = sum((x for x in ind))
    k = 10.
    score = 1. - sum(( math.cos(k * ind[i]) * math.exp(-(ind[i]*ind[i])/2.) for i in range(len(ind)))) / float(len(ind))
    fit0 = sum((x * math.sin(abs(x) * 2. * math.pi) for x in ind)) / normalization
    fit1 = sum((x * math.cos(abs(x) * 2. * math.pi) for x in ind)) / normalization
    features = (fit0, fit1)
    return (score,), features


#What are the individuals though? What makes them


print("\n" + algo.summary())
plots.default_plots_grid(logger)
