% Hechos de animales
animal(aguila).
animal(pinguino).
animal(tigre).
animal(delfin).
animal(elefante).
animal(perro).
animal(gato).
animal(cocodrilo).
animal(serpiente).
animal(tortuga).
animal(caballo).

% Características de los animales
tiene_plumas(aguila).
tiene_plumas(pinguino).
puede_volar(aguila).
puede_nadar(pinguino).
puede_nadar(delfin).
puede_nadar(cocodrilo).
puede_nadar(tortuga).
es_mamifero(tigre).
es_mamifero(delfin).
es_mamifero(elefante).
es_mamifero(perro).
es_mamifero(gato).
es_mamifero(caballo).
es_carnivoro(tigre).
es_carnivoro(delfin).
es_carnivoro(perro).
es_carnivoro(gato).
es_carnivoro(cocodrilo).
es_carnivoro(serpiente).
es_herbivoro(elefante).
es_herbivoro(caballo).
es_reptil(cocodrilo).
es_reptil(serpiente).
es_reptil(tortuga).
vive_en_tierra(tigre).
vive_en_tierra(elefante).
vive_en_tierra(perro).
vive_en_tierra(gato).
vive_en_tierra(caballo).
vive_en_tierra(cocodrilo).
vive_en_tierra(serpiente).
vive_en_tierra(tortuga).
vive_en_agua(delfin).
vive_en_agua(cocodrilo).
vive_en_agua(tortuga).
es_domestico(perro).
es_domestico(gato).
es_domestico(caballo).

% Reglas para identificar animales
identificar_animal(Animal, Tipo) :-
    tiene_plumas(Animal), puede_volar(Animal), Tipo = 'aguila'.

identificar_animal(Animal, Tipo) :-
    tiene_plumas(Animal), puede_nadar(Animal), Tipo = 'pinguino'.

identificar_animal(Animal, Tipo) :-
    es_mamifero(Animal), vive_en_tierra(Animal), es_carnivoro(Animal), Tipo = 'tigre'.

identificar_animal(Animal, Tipo) :-
    es_mamifero(Animal), vive_en_agua(Animal), Tipo = 'delfin'.

identificar_animal(Animal, Tipo) :-
    es_mamifero(Animal), es_herbivoro(Animal), vive_en_tierra(Animal), Tipo = 'elefante'.

identificar_animal(Animal, Tipo) :-
    es_mamifero(Animal), vive_en_tierra(Animal), es_domestico(Animal), es_carnivoro(Animal), Tipo = 'perro'.

identificar_animal(Animal, Tipo) :-
    es_mamifero(Animal), vive_en_tierra(Animal), es_domestico(Animal), es_carnivoro(Animal), Tipo = 'gato'.

identificar_animal(Animal, Tipo) :-
    es_reptil(Animal), vive_en_tierra(Animal), puede_nadar(Animal), Tipo = 'cocodrilo'.

identificar_animal(Animal, Tipo) :-
    es_reptil(Animal), vive_en_tierra(Animal), Tipo = 'serpiente'.

identificar_animal(Animal, Tipo) :-
    es_reptil(Animal), vive_en_tierra(Animal), puede_nadar(Animal), Tipo = 'tortuga'.

identificar_animal(Animal, Tipo) :-
    es_mamifero(Animal), es_herbivoro(Animal), vive_en_tierra(Animal), es_domestico(Animal), Tipo = 'caballo'.
