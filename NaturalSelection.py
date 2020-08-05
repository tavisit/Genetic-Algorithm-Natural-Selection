#######################################################################################################################
# libraries section
import copy
from csv import writer
import random
from datetime import datetime

from scipy.stats import skew
#######################################################################################################################
# custom-made classes and libraries
import Individual
from get_arguments import get_arguments
import DataAnalysisModule


#######################################################################################################################
# functions implementation

# the population crowdness in the environment
# as the population increases, the probability of dividing
# lowers as the population takes more space
# environment is the actual surface calculated in (population.size) metric **2
def crowding_effect(population=Individual.Individual(),
                    environment=(Individual.Individual().size, Individual.Individual().size)):
    # define the space occupied by the population
    crowd_effect = 1
    pop_space = 0
    for person in population:
        pop_space += person.size ** 2

    return pop_space / (environment[0] * environment[1]) * 10


def random_start_population(seed):
    indiv = Individual.Individual()
    indiv = indiv.mutation(indiv, 0)
    return indiv


def natural_selection_algorithm(start_pop=10,
                                generations=10,
                                environment=(400, 400),
                                file_path='natural_selection_data.csv'):
    print('\n\n\n\n')
    print('#' * 100)
    print('Natural selection Algorithm')
    print('#' * 100)

    # initialize the population
    population = []
    for i in range(start_pop):
        population.append(random_start_population(random.seed(datetime.now())))

    # print the current generation
    print('Generation {:>3}, population is {:>4} '
          'with crowding coefficient of {:>5}'.format(0,
                                                      len(population),
                                                      round(crowding_effect(population, environment), 4)))
    # save the initial population
    for ind in population:
        ind.save_individual(file_path, 0)

    # for loop in order to simulate the population over nr_generations times
    for i in range(1, generations + 1):

        # fitness and delete unfitted individuals
        fitness_average = 0
        for ind in population:
            fitness_average += ind.fitness_function()

        fitness_average = fitness_average / len(population)

        temp_ind = []
        for ind in population:
            # the individual can reproduce if its fitness is
            # 80% of the population fitness
            if ind.fitness_function() >= fitness_average * 0.9 and ind.life_exp > 0:
                ind.life_exp -= 1
                temp_ind.append(ind)
        population = temp_ind

        # mutate the current generation
        mutant_temp = []
        for ind in population:
            # if > 0.3, multiply
            # otherwise, don't
            random.seed(ind.fitness_function())
            chance_of_child = random.random()

            # the chance of replication is delta = chance_child - crowding_effect - 0.2
            # if delta >= 0, then replicate
            # if delta < 0 , then don't replicate
            if chance_of_child - round(crowding_effect(population, environment), 4) >= 0.1:
                # if > 0.3, mutate
                # otherwise, don't
                random.seed(chance_of_child *
                            crowding_effect(population, environment) *
                            float(datetime.now().microsecond))

                chance_of_mutation = random.random()

                mutant = copy.copy(ind)
                if chance_of_mutation >= 0.3:
                    mutant = ind.mutation(mutant, i)

                mutant.generation = i
                mutant_temp.append(mutant)

        # eliminate the old individuals
        temp_ind = []
        for ind in population:
            if ind.life_exp > 0:
                ind.save_individual(file_path, i)
                temp_ind.append(ind)
        population = temp_ind

        temp_ind = []
        # make the new generation
        for ind in mutant_temp:
            ind.save_individual(file_path, i)
            population.append(ind)

        # check if the population is empty
        if len(population) < 1:
            print('The population is dead!')
            exit(1)

        # print the current generation
        print('Generation {:>3}, population is {:>4} '
              'with crowding coefficient of {:6.4f},'
              'newborn population is: {:>4}'.format(i,
                                                    len(population),
                                                    round(crowding_effect(population, environment), 4),
                                                    len(mutant_temp)))


def visual_analysis_df(file_path='natural_selection_data.csv',
                       d_analysis_option=''):
    print('\n\n\n\n')
    print('#' * 100)
    print('Data visualization and plotting')
    print('#' * 100)
    import matplotlib
    import pandas as pd
    import numpy as np
    # These are the plotting modules adn libraries we'll use:
    import matplotlib.pyplot as plt
    import seaborn as sns
    import math

    data_frame = pd.read_csv(file_path)
    nr_crt = 0
    # Increase of population per generation
    fig = plt.figure(figsize=(20, 10))
    plt.suptitle('Population Growth Analysis')
    fig.add_subplot(221)
    plt.title('Population Growth per generation')
    data_frame['Nr_Gen'] = data_frame['Generation'].value_counts()
    plt.plot(data_frame['Nr_Gen'], color='black')
    plt.xlabel('Generation')
    plt.ylabel('Population')

    fig.add_subplot(222)
    plt.title('Population Growth per generation')
    plt.hist(data_frame['Nr_Gen'], color='blue')
    plt.xlabel('Generation')
    plt.ylabel('Population')

    fig.add_subplot(223)
    plt.title('Total number of individuals who lived')
    plt.plot(data_frame['Generation'], c='red')
    plt.ylabel('Total Population')
    plt.xlabel('Generation')

    fig.add_subplot(224)
    plt.title('Total number of individuals who lived')
    plt.hist(data_frame['Generation'], color='green')
    plt.ylabel('Total Population')
    plt.xlabel('Generation')
    if d_analysis_option == 's':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
    if d_analysis_option == 'd':
        plt.show()
    if d_analysis_option == 'sd':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
        plt.show()

    # show general information
    plt = data_analysis.general_information_plotting(data_frame, 'Fitness')
    if d_analysis_option == 's':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
    if d_analysis_option == 'd':
        plt.show()
    if d_analysis_option == 'sd':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
        plt.show()

    fig = plt.figure(figsize=(20, 10))
    plt.suptitle('General Analysis')
    fig.add_subplot(221)
    subtitle = 'Skew of Speed after logarithm is ' + str(np.log(data_frame.Speed).skew())
    plt.title(subtitle)
    plt.hist(np.log(data_frame.Speed), color='red')

    fig.add_subplot(222)
    subtitle = 'Skew of Strength after logarithm is ' + str(np.log(data_frame.Strength).skew())
    plt.title(subtitle)
    plt.hist(np.log(data_frame.Strength), color='blue')

    fig.add_subplot(223)
    subtitle = 'Skew of Size after logarithm is ' + str(np.log(data_frame.Size).skew())
    plt.title(subtitle)
    plt.hist(np.log(data_frame.Size), color='green')

    fig.add_subplot(224)
    subtitle = 'Skew of Senses after logarithm is ' + str(np.log(data_frame.Visual + data_frame.Auditory).skew())
    plt.title(subtitle)
    plt.hist(np.log(data_frame.Visual + data_frame.Auditory), color='orange')

    if d_analysis_option == 's':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
    if d_analysis_option == 'd':
        plt.show()
    if d_analysis_option == 'sd':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
        plt.show()

    # show feature average per generation
    sns.jointplot(data_frame['Generation'], data_frame['Fitness'], data_frame, 'hex',color = 'red')
    plt.suptitle('Generation vs Fitness Analysis')
    if d_analysis_option == 's':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
    if d_analysis_option == 'd':
        plt.show()
    if d_analysis_option == 'sd':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
        plt.show()

    # feature ranking plot
    data_frame_temp = data_frame.drop(['Nr_Gen', 'Born_Generation'], axis=1)
    plt = data_analysis.feature_ranking_plotting(data_frame_temp, 'Fitness', 5)
    plt.suptitle('Fitness important features')
    if d_analysis_option == 's':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
    if d_analysis_option == 'd':
        plt.show()
    if d_analysis_option == 'sd':
        plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
        nr_crt += 1
        plt.show()


#######################################################################################################################
# actual code
#######################################################################################################################

# starting variables
# these will be also gathered from arguments
nr_ind_start = 10
nr_generations = 10
environment = (400, 400)
nat_selection = False
d_analysis = False
d_analysis_option = ''
file_path = 'natural_selection_data.csv'

# define the class objects
data_analysis = DataAnalysisModule.DataAnalysisClass()
nr_ind_start, nr_generations, environment, nat_selection, d_analysis, d_analysis_option, file_path = get_arguments()
#######################################################################################################################
# run the natural selection algorithm from the function below
if nat_selection:
    # open the .csv and start writing the head of the file
    with open(file_path, 'w', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        list_of_elem = ['Generation', 'Life_Expectancy', 'Born_Generation', 'Speed', 'Strength', 'Size', 'Visual',
                        'Auditory', 'Fitness']
        csv_writer.writerow(list_of_elem)

    natural_selection_algorithm(nr_ind_start, nr_generations, environment, file_path)

#######################################################################################################################

if d_analysis:
    visual_analysis_df(file_path, d_analysis_option)
