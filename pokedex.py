#!/usr/bin/env python3 
# *- coding: utf-8 -*

import requests
import json
from time import sleep
import os as x
from colorama import init, Fore, Style
init()

url = "http://pokeapi.co/api/v2/pokemon/"

question = int(input(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"ingrese cuantos pokemones desea solicitar: "))
def buscarPokemon():
    cont = 0
    while cont < question:
        x.system("clear")
        num = int(input(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"Ingresa un numero: "))
        cont += 1
        """Permite buscar por numero un pokemon 
        que se encuentra en una url trayendo la informacion de este a la 
        terminal 
    
        args 
            num (int) que se castea a strings 
            dando un resultado como str(num)
            
            metodos = requests.get(), index, json, """
        title = """
                       POKEDEX 

               Created by: Hans Saldias

               by: 1LugarParaProgramar 
    """
        print(title)
    
        peticion = requests.get(url + str(num))
        respuesta = json.loads(peticion.content)
        nam = respuesta["name"]
        print(f"El nombre del pokemon llamado es: >> {nam} <<")
        height = respuesta['height']
        print(f"\nLa altura del pokemon es {height}\n")
        print(respuesta["species"])
        print("\notros pokemones de misma naturaleza y sus habilidades :\n")
        hability = respuesta["abilities"]
        for i in hability:
            print(i)
        input("\nPress start")
crea = "\nGracias por usar la pokedex By: Hans Saldias"
for i in crea:
    print(i, end=" * ", flush=True)
    sleep(0.1)

    





buscarPokemon()
