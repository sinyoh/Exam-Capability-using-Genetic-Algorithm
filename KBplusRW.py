from random import randint, random, randrange

# constant variables
max_pages = 200
mutationRate = 0.15  # value: 0-1
number_of_generation = 100
initial_population_size = 50
elitism = True 

class subject:
    def __init__(self, name, weight, value, type):
        self.name = name
        self.weight = weight
        self.value = value
        self.type = type

    def print(self):
        print("Name : " + self.name)
        print("Weight : ", self.weight)
        print("Value : ", self.value)
        if self.type == 0:
            print("Type : Mudah dipahami")
        elif self.type == 1:
            print("Type : Normal")
        elif self.type == 2:
            print("Type : Susah dipahami")
        print("")

subjects = []
# subjects.append(subject("Bab1", 60, 20, 2))
# subjects.append(subject("Bab2", 15, 20, 1))
# subjects.append(subject("Bab3", 5, 5, 0))
# subjects.append(subject("Bab4", 10, 100, 1))
# subjects.append(subject("Bab5", 20, 50, 1))
# subjects.append(subject("Bab6", 12, 15, 2))
# subjects.append(subject("Bab7", 50, 28, 2))
# subjects.append(subject("Bab8", 30, 40, 1))
# subjects.append(subject("Bab9", 28, 10, 0))
# subjects.append(subject("Bab10", 60, 25, 2))
# subjects.append(subject("Bab11", 25, 30, 1))
# subjects.append(subject("Bab12", 50, 10, 0))

# len(subjects) = len(subjects)

class chromosome:
    def __init__(self):
        self.genes = [] # sepanjang jumlah subjects
        self.total_weight = 0
        self.total_value = 0

        for i in range(len(subjects)):

            self.genes.append(randint(0, 1))
            if(self.genes[i] == 1):
                if subjects[i].type == 0:
                    self.total_weight += (subjects[i].weight - round((subjects[i].weight * (20/100))))

                elif subjects[i].type == 1:
                    self.total_weight += subjects[i].weight

                elif subjects[i].type == 2:
                    self.total_weight += (subjects[i].weight + round((subjects[i].weight * (30/100))))

                self.total_value += subjects[i].value

    def setgenes(self, genes):
        self.genes = genes
        self.total_weight = 0
        self.total_value = 0

        for i in range(len(subjects)):
            if(self.genes[i] == 1):

                if subjects[i].type == 0:
                    self.total_weight += (subjects[i].weight - round((subjects[i].weight * (20/100))))

                elif subjects[i].type == 1:
                    self.total_weight += subjects[i].weight

                elif subjects[i].type == 2:
                    self.total_weight += (subjects[i].weight + round((subjects[i].weight * (30/100))))

                self.total_value += subjects[i].value

    def print(self):
        print(self.genes)
        self.setgenes(self.genes)
        print("Total weight : ", self.total_weight)
        print("Total value : ", self.total_value)

    # Menentukan kromosom valid/tidak
    def evaluate(self):
        self.setgenes(self.genes)
        if(self.total_weight > max_pages):
            return 0
        else:
            return self.total_value

    # Evaluate yang lebih baik (utk tournament)
    def __lt__(self, other):
        return (self.evaluate() < other.evaluate())

    def __gt__(self, other):
        return (self.evaluate() > other.evaluate())

    # Mutasi
    def mutate(self):
        index = randint(0, len(subjects) - 1)
        if(self.genes[index] == 1):
            self.genes[index] = 0
        else:
            self.genes[index] = 1



def crossover1(chromosome1, chromosome2):
    # 1 POINT CROSSOVER, menentukan point crossovernya dari 1/2 kromosom each
    child_gene = [] #temp
    
    # cross_point = randrange(1, len(subjects), 1) -> kalau ingin random crosspoint e
    
    # 1 0 1 0 1  1 1 0 0 0  0  1
    # 1 0 1 0 1  1 1 0 0 0  0  2
    cross_point = len(subjects)/2
    
    for i in range(len(subjects)):
        if(i < cross_point):
            child_gene.append(chromosome1.genes[i])
        else:
            child_gene.append(chromosome2.genes[i])
    child = chromosome()
    child.setgenes(child_gene)
    # print(child_gene)
    # child.print()
    return child


def crossover2(chromosome1, chromosome2):
    # 1 POINT CROSSOVER
    child_gene = []
    
    # cross_point = randrange(1, len(subjects), 1) -> kalau ingin random crosspoint e
    cross_point = len(subjects)/2
    
    for i in range(len(subjects)):
        if(i < cross_point):
            child_gene.append(chromosome2.genes[i])
        else:
            child_gene.append(chromosome1.genes[i])
    child = chromosome()
    child.setgenes(child_gene)
    return child


def tournament(popul):
    newpopulation = population()
    if (elitism):
        temp = 1
    else:
        temp = 0
    while(len(newpopulation.chromosome) < len(popul.chromosome)):

        # ! FIRST BATTLE
        index1 = random()
        angka1 = popul.findIndex(index1)

        index2 = random()
        angka2 = popul.findIndex(index2)

        while(angka2 == angka1):
            index2 = random()
            angka2 = popul.findIndex(index2)
        if(popul.chromosome[angka1] < popul.chromosome[angka2]):
            winner1 = popul.chromosome[angka2]
        else:
            winner1 = popul.chromosome[angka1]

        # ! SECOND BATTLE
        index1 = random()
        angka1 = popul.findIndex(index1)
        
        index2 = random()
        angka2 = popul.findIndex(index2)
        while(angka2 == angka1):
            index2 = random()
            angka2 = popul.findIndex(index2)
        if(popul.chromosome[angka1] < popul.chromosome[angka2]):
            winner2 = popul.chromosome[angka2]
        else:
            winner2 = popul.chromosome[angka1]

        # ! CROSSOVER
        child1 = crossover1(winner1, winner2)
        child2 = crossover2(winner1, winner2)

        # ! MUTATION
        rate = random()
        if(rate <= mutationRate):
            winner1.mutate()

        rate = random()
        if(rate <= mutationRate):
            winner2.mutate()

        rate = random()
        if(rate <= mutationRate):
            child1.mutate()

        rate = random()
        if(rate <= mutationRate):
            child2.mutate()

        # check apakah len population baru itu sudah 50 belom
        if (len(newpopulation.chromosome) == initial_population_size - temp):
            break
        newpopulation.chromosome.append(winner1)
        if (len(newpopulation.chromosome) == initial_population_size - temp):
            break
        newpopulation.chromosome.append(winner2)
        if (len(newpopulation.chromosome) == initial_population_size - temp):
            break
        newpopulation.chromosome.append(child1)
        if (len(newpopulation.chromosome) == initial_population_size - temp):
            break
        newpopulation.chromosome.append(child2)

    # ! ELITISM
    if(elitism):
        newpopulation.chromosome.append(max(popul.chromosome))

    newpopulation.totalVal()
    newpopulation.hitungRoulette()
    return newpopulation


class population:
    def __init__(self) -> None:
        self.chromosome = []
        self.roulette = []
        self.totalValue = 0

    def hitungRoulette(self):
        
        for i in range(len(self.chromosome)):
            if (i == 0):
                self.roulette.append((self.chromosome[i].evaluate())/self.totalValue)

            else:
                self.roulette.append((self.chromosome[i].evaluate()/self.totalValue)+self.roulette[i-1])

    def totalVal(self):
        for i in self.chromosome:
            self.totalValue += i.evaluate()

    def findIndex(self, index):
        for i in range(len(self.roulette)):
            if (i == 0):
                if (index <= self.roulette[i]):
                    return i
            else:
                if(index >= self.roulette[i-1] and index <= self.roulette[i]):
                    return i


# popul = population()
# for i in range(initial_population_size):
#     popul.chromosome.append(chromosome())
#     # print(popul)

# popul.totalVal()
# popul.hitungRoulette()

# for i in range(number_of_generation):
#     popul = tournament(popul)

# print("Most Optimal Solution")
# biggest = popul.chromosome[0].evaluate()
# for i in popul.chromosome:
#     if biggest <= i.evaluate():
#         biggest = i.evaluate()
#         solution = i

# for i in popul.chromosome:
#     if biggest == i.evaluate():
#         solution = i
#         break
# solution = max(popul.chromosome)
# solution.print()
# for i in range(len(subjects)):
#     if(solution.genes[i] == 1):
#         subjects[i].print()
