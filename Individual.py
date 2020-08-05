#######################################################################################################################
# libraries section
import random
from datetime import datetime
from csv import writer
import copy


#######################################################################################################################
# functions implementation

#######################################################################################################################
# actual code
class Individual:
    # initialization method
    # Default values
    # life_exp = 3           # the number of generations before it dies
    # generation = x         # The generation when it was born
    # speed = 4              # the speed of the individual
    # strength = 10          # strength of the individual
    # size = 175             # the size in length of the individual
    # senses = (3000, 150)   # visual and auditory senses
    def __init__(self, energy_available=3000, life_exp=3, generation=0, speed=4, strength=5, size=5, senses=(100, 15)):
        self.energy = energy_available
        self.life_exp = life_exp
        self.generation = generation
        self.speed = speed
        self.strength = strength
        self.size = size
        self.visual = senses[0]
        self.auditory = senses[1]

        self.attr_list = ['speed', 'strength', 'size', 'visual', 'auditory']

    # the fitness function represents the expectancy of the individual's survival
    def fitness_function(self):
        return round(self.energy - self.speed * self.strength * self.size ** 3 - self.visual - self.auditory, 3)

    # define the mutation that occurs
    def mutation(self, child, generation):
        # generate the random seed
        random.seed()

        child = copy.copy(self)
        child.generation = generation
        # make the mutant's life expectancy the same as the parent's
        child.life_exp = self.life_exp + int(random.uniform(-1, 1))
        if child.life_exp <= 0:
            child.life_exp = self.life_exp + int(random.uniform(1, 4))

        # generate the random seed
        random.seed()

        # the random function will generate the number of mutated features(0 to 5)
        nr_of_mutations = int(random.uniform(1, len(child.attr_list)))

        # get the list of attributes that can be mutated
        attr_list = child.attr_list.copy()

        # search a number of attributes equal to the nr_of_mutations
        for mutation in range(0, nr_of_mutations):

            # get the attribute
            rand_attr = random.choice(attr_list)

            # remove it from list, in order to ensure that it isn't modified
            if rand_attr in attr_list:
                attr_list.remove(rand_attr)

            attr_value = getattr(child, rand_attr)
            # store the mutation value
            random_mutation_value = (random.uniform(-1, 1) * attr_value / 100)

            # if the mutated attribute is less than 0, then don't mutate
            if attr_value + random_mutation_value > 0:
                # the attribute can be modified with 1% percent of the actual value
                setattr(child, rand_attr, round(attr_value + random_mutation_value, 3))
            else:
                continue

        return child

    # standard methods
    def __str__(self):
        return f"Individual with life exp at {self.life_exp}, " \
               f"created in generation {self.generation}, " \
               f"with fitness at {self.fitness_function()} and attributes: " \
               f"{self.speed}  speed | " \
               f"{self.strength} strength | " \
               f"{self.size} size | " \
               f"{self.visual} visual | " \
               f"{self.auditory} auditory |\n"

    # save the current individual to the csv file
    def save_individual(self, file_name='natural_selection_data.csv', generation=0):
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            list_of_elem = [generation,
                            self.life_exp,
                            self.generation,
                            self.speed,
                            self.strength,
                            self.size,
                            self.visual,
                            self.auditory,
                            self.fitness_function()]
            csv_writer.writerow(list_of_elem)
