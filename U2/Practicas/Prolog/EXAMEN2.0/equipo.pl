% equipo (escuela y deporte)
equipo(epfaa, basquetbol).
equipo(epfaa,voleybol).

equipo(esfao, futbol).
equipo(esfao, voleybol).

equipo(eca, basquetbol).

equipo(esc, futbol).
equipo(esc, voleybol).
equipo(esc, basquetbol).

%jugador(nombre,edad,escuela).
jugador(luis, 17,epfaa).
jugador(mainez, 17,epfaa).
jugador(jose, 16,esfao).
jugador(mario, 18,esfao).
jugador(alberto, 15,epfaa).
jugador(dana, 14,eca).
jugador(pao, 19,eca).
jugador(yio, 20,esc).
jugador(manuel, 19,esc).

%resultado(deporte escula1 escuela2 puntos1 puntos2).
resultado(futbol,esc,esfao,1,12).
resultado(voleybol,epfaa,esfao,10,11).
resultado(voleybol,epfaa,esc,19,13).
resultado(voleybol,esfao,esc,10,18).
resultado(basquetbol,esc,epfaa,10,12).
resultado(basquetbol,esc,eca,19,12).
resultado(basquetbol,eca,epfaa,10,22).

%reglas
%listar el nombre de escuelas con deportes en especifico
listar_escuelas_deporte(Deporte) :-
    findall(Escuela, equipo(Escuela, Deporte), Escuelas),
    format('Escuelas que practican ~w: ~w~n', [Deporte, Escuelas]).
%¿Quiénes son los jugadores de una escuela determinada?
listar_jugadores_escuela(Escuela) :-
    findall(Nombre, jugador(Nombre, _, Escuela), Jugadores),
    format('Jugadores de ~w: ~w~n', [Escuela, Jugadores]).

%¿Qué equipos han ganado mas partidos? es decir los equipos con mas puntos
listar_equipos_ganadores :-
    findall((Equipo, Puntos), (resultado(_, Equipo, _, Puntos, _), Puntos > 0), Lista),
    format('Equipos ganadores: ~w~n', [Lista]).

%¿Qué jugadores tienen mas de cierta edad?
listar_jugadores_mayores(Edad) :-
    findall(Nombre, (jugador(Nombre, EdadJugador, _), EdadJugador > Edad), Jugadores),
    format('Jugadores mayores de ~w: ~w~n', [Edad, Jugadores]).

%numero total de jugadores en una escuela
%¿Cuántos jugadores hay en una escuela determinada?
contar_jugadores_escuela(Escuela) :-
    findall(Nombre, jugador(Nombre, _, Escuela), Jugadores),
    length(Jugadores, Total),
    format('Total de jugadores en ~w: ~w~n', [Escuela, Total]).