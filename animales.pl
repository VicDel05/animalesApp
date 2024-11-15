% Hechos
animal(aguila).
animal(pinguino).
animal(tigre).
animal(delfin).

tiene_plumas(aguila).
tiene_plumas(pinguino).
puede_volar(aguila).
puede_nadar(pinguino).
puede_nadar(delfin).
es_mamifero(tigre).
es_mamifero(delfin).
es_carnivoro(tigre).
vive_en_tierra(tigre).
vive_en_agua(delfin).

% Reglas para identificar animales
identificar_animal(Animal, Tipo) :-
    tiene_plumas(Animal), puede_volar(Animal), Tipo = 'aguila'.

identificar_animal(Animal, Tipo) :-
    tiene_plumas(Animal), puede_nadar(Animal), Tipo = 'pinguino'.

identificar_animal(Animal, Tipo) :-
    es_mamifero(Animal), vive_en_tierra(Animal), es_carnivoro(Animal), Tipo = 'tigre'.

identificar_animal(Animal, Tipo) :-
    es_mamifero(Animal), vive_en_agua(Animal), Tipo = 'delfin'.
