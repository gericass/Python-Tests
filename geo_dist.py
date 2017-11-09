from geopy.distance import vincenty
newport_ri = (41.818425, 140.751687)
cleveland_oh = (41.841817, 140.766969)
print(vincenty(newport_ri, cleveland_oh).meters)