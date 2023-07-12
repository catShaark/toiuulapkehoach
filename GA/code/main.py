import read_file
from Ga import *
from Solution import *

data = {}

data["Data/input1.txt"] = [6, 4, 2]
data["Data/input2.txt"] = [6, 4, 2]
data["Data/input3.txt"] = [6, 4, 2]
data["Data/input4.txt"] = [6, 4, 2]
data["Data/input5.txt"] = [6, 4, 2]
data["Data/input6.txt"] = [6, 4, 2]
data["Data/input7.txt"] = [6, 4, 2]
data["Data/input8.txt"] = [6, 4, 2]
data["Data/input9.txt"] = [6, 4, 2]
data["Data/input10.txt"] = [6, 4, 2]


for file_name in data.keys():

    input = read_file.read(file_name)

    sol = Solution(input)

    N = 20
    Gen = 10

    ga = Ga(N, Gen, sol)
    ga.run()
