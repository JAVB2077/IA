/**JOSEPH ANAGEL VEGA BERNAL*/
familia(persona([tomas,garcia,perez],
        fecha(7,mayo,1960),
        trabajo(profesor,60)),
    persona([ana,lopez,ruiz],
        fecha(10,marzo,1962),
        trabajo(medica,90)),
    [persona([juan,garcia,lopez],
        fecha(5,enero,1990),
        estudiante),
    persona([maria,garcia,lopez],
        fecha(12,abril,1992),
        estudiante) ]).

familia(persona([jose,perez,ruiz],
        fecha(6,marzo,1963),
        trabajo(pintor,120)),
    persona([luisa,galvez,perez],
        fecha(12,mayo,1964),
        trabajo(medica,90)),
    [persona([juan_luis,perez,perez],
        fecha(5,febrero,1990),
        estudiante),
    persona([maria_jose,perez,perez],
        fecha(12,junio,1992),
        estudiante),
    persona([jose_maria,perez,perez],
        fecha(12,julio,1994),
        estudiante) ]).

% 3.Preguntar por los hombres casados.*/
casado(x):-familia(X,_,_).

% 4. Definir la relación casada(X) que se verifique si X es una mujer casada.
casada(X):-familia(_,X,_).

% 6.Determinar el nombre de todas las mujeres casadas que trabajan.
mujer_casada_trabajando(X):-familia(_,X,Lista),trabajo(X,Sueldos),member(persona(_,_,estudiante),Lista),Sueldos>0.


% 7.Definir la relación hijo(X) que se verifique si X figura en alguna lista de hijos.
hijo(X):-familia(_,_,Lista),member(persona(X,_,_),Lista).

%9.Definir la relación persona(X) que se verifique si X es una persona existente en la base de datos.
persona(X):-familia(_,_,Lista),member(persona(X,_,_),Lista).

% 10.Preguntar por los nombres apellidos de todas las personas existentes en la base de datos.
personaApellido(X):-familia(_,_,Lista),member(persona(X,_,_),Lista).

%% 11.Determinar todos los estudiantes nacidos antes de 1993.
estudiante_antes_1993(X):-familia(_,_,Lista),member(persona(X,fecha(Dia,Mes,Anio),estudiante),Lista),Anio<1993.

% 12.Definir la relación fecha_de_nacimiento(X,Y) de forma que si X es una persona, entonces Y es su fecha de nacimiento.
fecha_de_nacimiento(X,Y):-familia(_,_,Lista),member(persona(X,Y,_),Lista).

% 13.Buscar todos los hijos nacidos en 1992.
hijo_nacido_1992(X):-familia(_,_,Lista),member(persona(X,fecha(Dia,Mes,Anio),_),Lista),Anio=1992.

% 14.Definir la relación sueldo(X,Y) que se verifique si el sueldo de la persona X es Y.
sueldo(X,Y):-familia(_,_,Lista),member(persona(X,_,trabajo(_,Y)),Lista).

% 15.Buscar todas las personas nacidas antes de 1964 cuyo sueldo sea superior a 72 euros diarios.
persona_sueldo(X):-familia(_,_,Lista),member(persona(X,fecha(Dia,Mes,Anio),trabajo(_,Sueldo)),Lista),Anio<1964,Sueldo>72.


/**
Responder a las siguientes consultas:

1.Buscar los nombres de los padres de familia con tres hijos.
    familia(X,Y,Lista),length(Lista,3).
2.Definir la relación casado(X) que se verifique si X es un hombre casado.
3.Preguntar por los hombres casados.
    casado(X).familia
4.Definir la relación casada(X) que se verifique si X es una mujer casada.
5.Preguntar por las mujeres casadas.
    casada(X).
6.Determinar el nombre de todas las mujeres casadas que trabajan.
    casada(persona([X,_,_],_,trabajo(_,_))).
7.Definir la relación hijo(X) que se verifique si X figura en alguna lista de hijos.
8.Preguntar por los hijos.
    hijo(X).
9.Definir la relación persona(X) que se verifique si X es una persona existente en la base de datos.
    persona()
10.Preguntar por los nombres y apellidos de todas las personas existentes en la base de datos.
    persona(X).
11.Determinar todos los estudiantes nacidos antes de 1993.
    estudiante_antes_1993(X).
    persona(persona,fecha,(_,_,año))
12.Definir la relación fecha_de_nacimiento(X,Y) de forma que si X es una persona, entonces Y es su fecha de nacimiento.
    fecha_de_nacimiento(X,Y).
13.Buscar todos los hijos nacidos en 1992.
    hijo_nacido_1992(X).
14.Definir la relación sueldo(X,Y) que se verifique si el sueldo de la persona X es Y.
    sueldo(X,Y).
15.Buscar todas las personas nacidas antes de 1964 cuyo sueldo sea superior a 72 euros diarios.
16.Definir la relación total(L,Y) de forma que si L es una lista de personas, entonces Y es la suma de los sueldos de las personas de la lista L.
17.Calcular los ingresos totales de cada familia.
18. Buscar si existe familia con 3 hijos.
    familia(persona([X,_,_],_,_),_,[_,_,_]). solo para arrojar el nombre del padre 
*/