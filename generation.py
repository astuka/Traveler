import game_data as gd
import random as r

#generate new npc

#certain creatures live on certain planets

def city_generate():
    city = gd.City(gd.city_names[r.randrange(0,len(gd.city_names))],0,[])
    return city


def planet_generate(n):
    galaxy = []
    for i in range(n):
        gen_planet_name = gd.planet_names[r.randrange(0,len(gd.planet_names))]
        gen_planet_type = gd.planet_types[r.randrange(0,len(gd.planet_types))]
        gen_planet_size = gd.planet_sizes[r.randrange(0,len(gd.planet_sizes))]
        galaxy.append(gd.Planet(gen_planet_name, r.randrange(0,11), gen_planet_type, gen_planet_size, city_generate(),[]))
    return galaxy

def node_generator(galaxy):
    for i in galaxy:
        connected_planet = galaxy[r.randrange(0,len(galaxy))]
        if i != connected_planet and connected_planet not in i.nodes:
            i.nodes.append(connected_planet)
            connected_planet.nodes.append(i)



# def npc_generate(n):
#     for i in range(n):
#         