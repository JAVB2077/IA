
%Hechos
genero(matrix,ciencia_ficcion).
genero(inception,ciencia_ficcion).
genero(titanic,romance).
genero(avatar,aventura).
genero(shrek,animacion).

% Clasificación
clasificacion(matrix, adultos).
clasificacion(inception, adultos).
clasificacion(titanic, adultos).
clasificacion(avatar, adultos).
clasificacion(shrek, infantil).
clasificacion(robot_salvaje, infantil).
clasificacion(lego, infantil).
clasificacion(son_como_niños, comedia).
clasificacion(son_como_niños, adultos).

% Duración
duracion(matrix, larga).
duracion(inception, larga).
duracion(titanic, larga).
duracion(avatar, ultra_larga).
duracion(shrek, corta).

%plataformas
plataforma(matrix, netflix).
plataforma(inception, hbo).
plataforma(titanic, disney_plus).
plataforma(avatar, disney_plus).
plataforma(shrek, netflix).

%Reglas
para_niños(P) :- clasificacion(P, infantil), duracion(P, corta).
    %?- para_niños(P).

noche_intensa(P) :- genero(P,accion), genero(P, ciencia_ficcion), duracion(P, larga).
    %?- noche_intensa(P).

donde_ver(P, Plataforma) :- plataforma(P, Plataforma).
    %?- donde_ver(matrix, Plataforma).

recomendacion_clasificacion(Clasificacion, Pelicula) :- clasificacion(Pelicula, Clasificacion).
    %?- recomendacion_clasificacion(adultos, Pelicula).