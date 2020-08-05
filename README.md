# Genetic Algorithm Natural Selection

This algorithm simulates a population of individuals with 6 initial traits, mutates the population though generations and visualizes real behaviourism of the society. It also saves and draws some plots to ease the burden of information visualization

### Nota Bene

If you have a question about the code or the hypotheses I made, do not hesitate to post a comment in the comment section below.
If you also have a suggestion on how this notebook could be improved, please reach out to me.

### Dependencies:

* [NumPy](https://numpy.org/)
* [Searborn](https://seaborn.pydata.org/)
* [Pandas](https://pandas.pydata.org/)
* [SciKit-Learn](https://scikit-learn.org/stable/)
* [SciPy](https://www.scipy.org/)
* [Matplotlib](https://matplotlib.org/)

# CMD arguments explained

The program is built according to some general rules and it uses the command line arguments in order to ensure a more automated usage. The arguments are as follows:

Arguments:

the defaults are taken from the main script, usually they are:

*  nr_ind_start = 10
*  nr_generations = 10
*  length = 400
*  width = 400
*  nat_selection = False
*  d_analysis = False
*  d_analysis_option = ''
*  file_path = ''

If we write in the cmd the following line: python Houses_Prices.py -h, the help list will appear in the following order:

```
Start the program in the following order, where [-c] is optional
python Houses_prices.py [-p nr] [-g nr] [-l nr] [-w nr] [-n] [-a opt] -f location_input
-p / --pop           | set the initial population, default 10
-g / --gen           | set the number of generations, default 10
-l / --length        | set the environment length, default 400
-w / --width         | set the environment width, default 400
-n / --nat           | run the natural selection algorithm
-a / --analysis      | run the data analysis algorithm
                     | options:
                     | s -> save plots
                     | d -> display plots
                     | sd -> save and display plots
-f / --file          | input/output file of the data
```

First, we get the arguments from the command line:

```
nr_ind_start = 10
nr_generations = 10
environment = (400, 400)
nat_selection = False
d_analysis = False
d_analysis_option = ''
file_path = 'natural_selection_data.csv'

# define the class objects
nr_ind_start, nr_generations, environment, nat_selection, d_analysis, d_analysis_option, file_path = get_arguments()
```

The command line influences the workflow of the algorithm with the following interpretation:

```Python
if d_analysis_option == 's':
    plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
    nr_crt += 1
if d_analysis_option == 'd':
    plt.show()
if d_analysis_option == 'sd':
    plt.savefig('Images/' + file_path[-5] + str(nr_crt) + '_plot.png')
    nr_crt += 1
    plt.show()
```

For further information, please open the get_arguments.py

# Program classes and modules

The main algorithm is split between 4 main modules and these are:
* get_arguments.py which has the main function of argument detection and decision
* DataAnalysisModule.py which has the class that displays data in form of plots
* Individual.py which has the class that has the individual's parameters, attributes and methods that make possible data manipulation
* NaturalSelection.py which is the main script and must be called in order to make the program functional

# Idea and mathematical reasoning

### Initial idea

Make a mathematical explanation of the universal population's asymptotic logistic growth and implement said algorithms in a working program

The genetic algorithm cycle is as the following:

![](https://www.researchgate.net/profile/Cesar_Analide/publication/265040479/figure/fig2/AS:295895267594241@1447558337273/Genetic-algorithm-evolution-cycle.png)

### Mathematical Reasoning

This simulation requires some mathematical knowledge, because a population is interpreted as a set of individual, who are also a set of traits, so we can write mathematicaly that and denote the following identities:

<a href="https://www.codecogs.com/eqnedit.php?latex=individual&space;=&space;\left\{\begin{matrix}&space;energy\\&space;life\;&space;expectancy\\&space;speed\\&space;strength\\&space;size\\&space;visual\:&space;sense\\&space;auditory\:&space;sense\\&space;\end{matrix}\right.,where\;&space;\left\{\begin{matrix}&space;individual\;&space;or\;&space;i\;&space;is\;&space;the\;&space;set\;&space;of\;&space;individual\;&space;traits\\&space;population\;&space;or\;&space;pop\;&space;is\;&space;the\;&space;set\;&space;of\;&space;individuals&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?individual&space;=&space;\left\{\begin{matrix}&space;energy\\&space;life\;&space;expectancy\\&space;speed\\&space;strength\\&space;size\\&space;visual\:&space;sense\\&space;auditory\:&space;sense\\&space;\end{matrix}\right.,where\;&space;\left\{\begin{matrix}&space;individual\;&space;or\;&space;i\;&space;is\;&space;the\;&space;set\;&space;of\;&space;individual\;&space;traits\\&space;population\;&space;or\;&space;pop\;&space;is\;&space;the\;&space;set\;&space;of\;&space;individuals&space;\end{matrix}\right." title="individual = \left\{\begin{matrix} energy\\ life\; expectancy\\ speed\\ strength\\ size\\ visual\: sense\\ auditory\: sense\\ \end{matrix}\right.,where\; \left\{\begin{matrix} individual\; or\; i\; is\; the\; set\; of\; individual\; traits\\ population\; or\; pop\; is\; the\; set\; of\; individuals \end{matrix}\right." /></a>

We will define a function named Fitness in order to select the most fitted individuals. A fitness of an organism is the mathematical function that generates a number based on the traits of the individual in order to establish the chance of survival of the individual: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\dpi{200}&space;\\\&space;Fitness\;&space;function\;&space;is\;&space;defined\;&space;as\;&space;\varphi:i\rightarrow\Re\\&space;Population&space;\;&space;fitness\;&space;function\;&space;is\;&space;defined\;&space;as\;&space;\phi:pop\rightarrow\Re" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\dpi{200}&space;\\\&space;Fitness\;&space;function\;&space;is\;&space;defined\;&space;as\;&space;\varphi:i\rightarrow\Re\\&space;Population&space;\;&space;fitness\;&space;function\;&space;is\;&space;defined\;&space;as\;&space;\phi:pop\rightarrow\Re" title="\\\ Fitness\; function\; is\; defined\; as\; \varphi:i\rightarrow\Re\\ Population \; fitness\; function\; is\; defined\; as\; \phi:pop\rightarrow\Re" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\dpi{300}&space;\small&space;Fitness\;&space;is\;&space;\varphi&space;(i)&space;=&space;energy{_{i}}&space;-&space;speed{_{i}}*strength{_{i}}*size{_{i}}^{3}&space;-&space;visual{_{i}}&space;-&space;auditory{_{i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\dpi{300}&space;\small&space;Fitness\;&space;is\;&space;\varphi&space;(i)&space;=&space;energy{_{i}}&space;-&space;speed{_{i}}*strength{_{i}}*size{_{i}}^{3}&space;-&space;visual{_{i}}&space;-&space;auditory{_{i}}" title="\small Fitness\; is\; \varphi (i) = energy{_{i}} - speed{_{i}}*strength{_{i}}*size{_{i}}^{3} - visual{_{i}} - auditory{_{i}}" /></a>

In order to clean the population of the worst fitted individual in the society, we need to calculate the mean value of the population's fitness and then establish the rule that those individuals that do not have at least 90% of the entire population mean fitness, won't reproduce. This value was chosen in order to ensure a more real world behaviour of a population, where only the fittest will reproduce. The mathematical functions are as followed: 

<a href="https://www.codecogs.com/eqnedit.php?latex=\huge&space;\phi(pop)&space;=&space;\frac{\sum_{k=0}^{card(k)}&space;\varphi(pop(k))}{card(pop)},\;&space;with\;&space;chance\;&space;of\;&space;multiplication\;&space;of\;&space;\left\{\begin{matrix}&space;0&space;&,\varphi(i)<\frac{9}{10}\phi(pop)\\&space;life\;&space;expectency&,otherwise&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\huge&space;\phi(pop)&space;=&space;\frac{\sum_{k=0}^{card(k)}&space;\varphi(pop(k))}{card(pop)},\;&space;with\;&space;chance\;&space;of\;&space;multiplication\;&space;of\;&space;\left\{\begin{matrix}&space;0&space;&,\varphi(i)<\frac{9}{10}\phi(pop)\\&space;life\;&space;expectency&,otherwise&space;\end{matrix}\right." title="\huge \phi(pop) = \frac{\sum_{k=0}^{card(k)} \varphi(pop(k))}{card(pop)},\; with\; chance\; of\; multiplication\; of\; \left\{\begin{matrix} 0 &,\varphi(i)<\frac{9}{10}\phi(pop)\\ life\; expectency&,otherwise \end{matrix}\right." /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\dpi{150}&space;\begin{matrix}&space;Chances\;&space;of\;&space;individual\;multiplication&space;\;&space;is\;&space;defined\;&space;as&space;M:iXpop\rightarrow\Re\\&space;M(i,pop)&space;=&space;randChance(i)&space;-&space;\gamma(pop)&space;-&space;1&space;\geq&space;0&space;\end{matrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\dpi{150}&space;\begin{matrix}&space;Chances\;&space;of\;&space;individual\;multiplication&space;\;&space;is\;&space;defined\;&space;as&space;M:iXpop\rightarrow\Re\\&space;M(i,pop)&space;=&space;randChance(i)&space;-&space;\gamma(pop)&space;-&space;1&space;\geq&space;0&space;\end{matrix}" title="\begin{matrix} Chances\; of\; individual\;multiplication \; is\; defined\; as M:iXpop\rightarrow\Re\\ M(i,pop) = randChance(i) - \gamma(pop) - 1 \geq 0 \end{matrix}" /></a>

Now, if an individual was able to divide, a series of mutations will take place on the features of the child. These mutations are probabilistic and mirror the behaviour of DNA strands when they break in order to be able to replicate. This act is implemented in a function and defined as the following:

<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{150}&space;\large&space;\begin{matrix}&space;The\;&space;mutation\;&space;function\;&space;is\;&space;defined\;&space;as\;&space;\mu:i\rightarrow&space;i\;&space;with\;&space;the\;&space;form:\\&space;\mu_i&space;=&space;\left\{\begin{matrix}&space;life\;&space;expectancy_i&space;&plus;&space;\delta_1&space;\\&space;speed_i&space;&plus;&space;\delta_2&space;\\&space;strength_i&space;&plus;&space;\delta_3&space;\\&space;size_i&space;&plus;&space;\delta_4&space;\\&space;visual_i&space;&plus;&space;\delta_5\\&space;auditory_i&space;&plus;&space;\delta_6&space;\end{matrix}\right.,&space;or\;&space;\bigcup_{k=0}^{card(traits)}(i(\Delta_k)&space;\pm\delta_k)&space;=&space;\mu(i),&space;where&space;\left\{\begin{matrix}&space;i(\Delta_k)\;&space;is\;&space;random\;&space;trait\;&space;of\;&space;parent\\&space;\delta_k\;&space;is\;&space;random\;&space;variation\;&space;of\;&space;the\;&space;trait&space;\end{matrix}\right.&space;\end{matrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{150}&space;\large&space;\begin{matrix}&space;The\;&space;mutation\;&space;function\;&space;is\;&space;defined\;&space;as\;&space;\mu:i\rightarrow&space;i\;&space;with\;&space;the\;&space;form:\\&space;\mu_i&space;=&space;\left\{\begin{matrix}&space;life\;&space;expectancy_i&space;&plus;&space;\delta_1&space;\\&space;speed_i&space;&plus;&space;\delta_2&space;\\&space;strength_i&space;&plus;&space;\delta_3&space;\\&space;size_i&space;&plus;&space;\delta_4&space;\\&space;visual_i&space;&plus;&space;\delta_5\\&space;auditory_i&space;&plus;&space;\delta_6&space;\end{matrix}\right.,&space;or\;&space;\bigcup_{k=0}^{card(traits)}(i(\Delta_k)&space;\pm\delta_k)&space;=&space;\mu(i),&space;where&space;\left\{\begin{matrix}&space;i(\Delta_k)\;&space;is\;&space;random\;&space;trait\;&space;of\;&space;parent\\&space;\delta_k\;&space;is\;&space;random\;&space;variation\;&space;of\;&space;the\;&space;trait&space;\end{matrix}\right.&space;\end{matrix}" title="\large \begin{matrix} The\; mutation\; function\; is\; defined\; as\; \mu:i\rightarrow i\; with\; the\; form:\\ \mu_i = \left\{\begin{matrix} life\;&space;expectancy_i + \delta_1 \\ speed_i + \delta_2 \\ strength_i + \delta_3 \\ size_i + \delta_4 \\ visual_i + \delta_5\\ auditory_i + \delta_6 \end{matrix}\right., or\; \bigcup_{k=0}^{card(traits)}(i(\Delta_k) \pm\delta_k) = \mu(i), where \left\{\begin{matrix} i(\Delta_k)\; is\; random\; trait\; of\; parent\\ \delta_k\; is\; random\; variation\; of\; the\; trait \end{matrix}\right. \end{matrix}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\dpi{150}&space;\begin{matrix}&space;Chances\;&space;of\;&space;individual\;mutation\;&space;is\;&space;defined\;&space;as\;&space;\nu:iXpop\rightarrow\Re\\&space;\nu(i,pop)&space;=&space;randChance(i)&space;-&space;M(i,pop)&space;-&space;0.3&space;\geq&space;0&space;\end{matrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\dpi{150}&space;\begin{matrix}&space;Chances\;&space;of\;&space;individual\;mutation\;&space;is\;&space;defined\;&space;as\;&space;\nu:iXpop\rightarrow\Re\\&space;\nu(i,pop)&space;=&space;randChance(i)&space;-&space;M(i,pop)&space;-&space;0.3&space;\geq&space;0&space;\end{matrix}" title="\begin{matrix} Chances\; of\; individual\;mutation\; is\; defined\; as\; \nu:iXpop\rightarrow\Re\\ \nu(i,pop) = randChance(i) - M(i,pop) - 0.3 \geq 0 \end{matrix}" /></a>

In the theory of genetic algorithms comes the notion of crowding effect. This effect is a factor on the population's ability to divide, quantifying the space that the society lives on. It starts small and increases as the population increses and stops the individuals to divide and suprapopulate the environment. Note that the environment was chosen as a rectagle with size l and w, but it can be generated as a surface of any shape and size to accommodate a more realistic population. The general formula is the following:

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\dpi{150}&space;\large&space;\gamma:pop&space;\rightarrow(0,1),\;&space;\gamma(pop)&space;=&space;\frac{\sum_{i=0}^{card(pop)}(s_i\pm&space;\Delta_i)^{2}}{env(l,w)},where\left\{\begin{matrix}&space;s_i\;&space;is\;&space;the\;&space;size\;&space;of\;&space;the\;&space;individual\\&space;\Delta_i\;&space;random\;&space;variation\;&space;of\;&space;the\;&space;base\;&space;size\;&space;through\;&space;mutation\\&space;env(l,w)&space;=&space;size\;&space;of\;&space;the\;&space;environment&space;\end{matrix}\right.&space;\\" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\dpi{150}&space;\large&space;\gamma:pop&space;\rightarrow(0,1),\;&space;\gamma(pop)&space;=&space;\frac{\sum_{i=0}^{card(pop)}(s_i\pm&space;\Delta_i)^{2}}{env(l,w)},where\left\{\begin{matrix}&space;s_i\;&space;is\;&space;the\;&space;size\;&space;of\;&space;the\;&space;individual\\&space;\Delta_i\;&space;random\;&space;variation\;&space;of\;&space;the\;&space;base\;&space;size\;&space;through\;&space;mutation\\&space;env(l,w)&space;=&space;size\;&space;of\;&space;the\;&space;environment&space;\end{matrix}\right.&space;\\" title="\large \gamma:pop \rightarrow(0,1),\; \gamma(pop) = \frac{\sum_{i=0}^{card(pop)}(s_i\pm \Delta_i)^{2}}{env(l,w)},where\left\{\begin{matrix} s_i\; is\; the\; size\; of\; the\; individual\\ \Delta_i\; random\; variation\; of\; the\; base\; size\; through\; mutation\\ env(l,w) = size\; of\; the\; environment \end{matrix}\right. \\" /></a>

The equation that allows the individuals to divide and increase the population. The number P(i) represents the death/life chances of an individual in the population:

<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\dpi{200}&space;\small&space;P(i)&space;=&space;(M(i,pop)-\omega(i)-\gamma(pop)),where\;&space;omega:i->(0,1),&space;\omega=\left\{\begin{matrix}&space;1,&space;&&space;life\;&space;expectancy&space;\le&space;0\\&space;0,&space;&&space;life\;&space;expectancy&space;\ge&space;1&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\dpi{200}&space;\small&space;P(i)&space;=&space;(M(i,pop)-\omega(i)-\gamma(pop)),where\;&space;omega:i->(0,1),&space;\omega=\left\{\begin{matrix}&space;1,&space;&&space;life\;&space;expectancy&space;\le&space;0\\&space;0,&space;&&space;life\;&space;expectancy&space;\ge&space;1&space;\end{matrix}\right." title="\small P(i) = (M(i,pop)-\omega(i)-\gamma(pop)),where\; omega:i->(0,1), \omega=\left\{\begin{matrix} 1, & life\; expectancy \le 0\\ 0, & life\; expectancy \ge 1 \end{matrix}\right." /></a>

### Python Implementation

The programming language used will be pthon, because it has many useful frameworks and libraries.

The program has the following stages:
* calculate fitness and delete unfit individuals:
```Python
fitness_average = 0
for ind in population:
    fitness_average += ind.fitness_function()

fitness_average = fitness_average / len(population)

temp_ind = []
for ind in population:
    if ind.fitness_function() >= fitness_average * 0.9 and ind.life_exp > 0:
        ind.life_exp -= 1
        temp_ind.append(ind)
population = temp_ind
```
* divide the current generation
```Python
mutant_temp = []
for ind in population:
    random.seed(ind.fitness_function())
    chance_of_child = random.random()
    
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
```
* Eliminate old individuals, make the new generation and save it in the .csv
```Python
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
```
* Repeat the cycle

# Data visualization

### Hypothesis

The simulation predicts accurately the evolution of a simple population of bacteria/virus with a small set of traits and can be used to exemplify the notion of genetic algorithm

### Overall analysis

To check the corectness of the mathematical identities and functions, the statistics of every individual is saved in a .csv and saved in a plot. These plots have the mission to encapsulate and display the evolution of the population though generations and verify if the parameters and notions are correctly implemented and designed. The most helpful plot is the following, it displays the evolution of the society in 348 generations and marks the total population that have ever lived:

<a data-flickr-embed="true" href="https://www.flickr.com/photos/189039256@N05/50191658566/in/album-72157715360379462/" title="00_plot"><img src="https://live.staticflickr.com/65535/50191658566_d9379d5fc2_o.png" width="2000" height="1000" alt="00_plot">

### Fitness analysis

[Herbert Spencer](https://en.wikipedia.org/wiki/Survival_of_the_fittest)'s well-known phrase "survival of the fittest" should be interpreted as: "Survival of the form (phenotypic or genotypic) that will leave the most copies of itself in successive generations.". In the simulation, it was difficult to implement a genotypic-like algorithm, so a more numerical fitness function was implemented, which resulted in a increase of population's average fitness level, as Herbert theorized. The following plots show the relation between the level of fitness and the number of individuals that share the same level:

<a data-flickr-embed="true" href="https://www.flickr.com/photos/189039256@N05/50191111563/in/album-72157715360379462/" title="01_plot"><img src="https://live.staticflickr.com/65535/50191111563_56dcfe44a1_o.png" width="2000" height="500" alt="01_plot"></a>

The following plot shows the relation between the current generation and it's fitness level:

<a data-flickr-embed="true" href="https://www.flickr.com/photos/189039256@N05/50191111463/in/album-72157715360379462/" title="03_plot"><img src="https://live.staticflickr.com/65535/50191111463_a7782f16a8_o.png" width="600" height="600" alt="03_plot"></a>

### Traits analysis and correlation with the fitness levels

These levels of general fitness can be seen as the result of 4 distinct main traits. These will be plotted and analysed further, in order to establish the main factors of the evolution of the simulated population:

<a data-flickr-embed="true" href="https://www.flickr.com/photos/189039256@N05/50191111553/in/album-72157715360379462/" title="02_plot"><img src="https://live.staticflickr.com/65535/50191111553_504270f2bb_o.png" width="2000" height="1000" alt="02_plot"></a>

As expected, the population is divided in categories and no two individuals share the exact same set of traits among the generations. As one can extract from the plots, the distribution is Gaussian, which approves the hypothesis and that the functions were correctly implemented. For further analysis, more generations and diverse environment are required, but will be implemented in future tests and improvements

To better analyse the data set, one needs to know the most important features of the population, so the next plot displays the first 5 features that increase the fitness and the first 5 features that decrease the general fitness of an individual

<a data-flickr-embed="true" href="https://www.flickr.com/photos/189039256@N05/50191658381/in/album-72157715360379462/" title="04_plot"><img src="https://live.staticflickr.com/65535/50191658381_395f9df85f_o.png" width="1000" height="1000" alt="04_plot"></a>

### Multi simulation tests
The algorithm ran for 5 distict populations, each with 100 generations and some information was revealed. The total population of each society respects the logistic growth and can be put side-by-side with a real population of slow self-replicating individuals:

<a data-flickr-embed="true" href="https://www.flickr.com/photos/189039256@N05/50188750827/in/dateposted-public/" title="5_civ_plot"><img src="https://live.staticflickr.com/65535/50188750827_253f3faec5_o.png" width="1800" height="800" alt="5_civ_plot"></a>

# Conclusion

The algorithm produces a population that resembles the behaviour and mutations that happen in the real world and can be used to analyse abstract modifications in traits among the individuals in a species, by making mathematical assumptions and notations according to a general rule.

This program was made for fun from the idea of genetic mutations and can be used by anyone.
