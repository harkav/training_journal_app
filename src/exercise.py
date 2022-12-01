class Exercise: 

    def __init__(self, name, sets, reps, weight):
        self._name = name 
        self._sets = sets 
        self._reps = reps 
        self._weight = weight 


    def __str__(self): 
        return self._name + " " +  str(self._sets) + "x" + str(self._reps)+ " " + str(self._weight) + " kg"

 
