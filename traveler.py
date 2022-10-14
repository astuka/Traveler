import generation as g

galaxy = g.planet_generate(10)
g.node_generator(galaxy)

for i in galaxy:
    print(i.name+", a "+i.size+" "+i.type+" planet with the capital "+i.capital.name+". It has the following connections: ")
    for x in i.nodes:
        print(x.name)

#move command
    #satellites are just one area, just go back to ship
    #moving on planet means moving between cities