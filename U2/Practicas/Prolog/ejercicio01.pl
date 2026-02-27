% Hechos: Género de las personas
hombre(juan).
hombre(carlos).
hombre(pedro).
mujer(ana).
mujer(maria).
mujer(laura).

% Hechos: Relaciones de parentesco (padre o madre)
padre(juan, carlos).
padre(juan, maria).
madre(ana, carlos).
madre(ana, maria).
padre(pedro, laura).
madre(maria, laura).

% Reglas:

% 1. X es progenitor de Y si es padre o madre.
progenitor(X, Y) :- padre(X, Y).
progenitor(X, Y) :- madre(X, Y).

% 2. X es abuelo de Y si X es hombre y progenitor de un progenitor de Y.
abuelo(X, Y) :- hombre(X), progenitor(X, Z), progenitor(Z, Y).

% 3. X es abuela de Y si X es mujer y progenitor de un progenitor de Y.
abuela(X, Y) :- mujer(X), progenitor(X, Z), progenitor(Z, Y).

% 4. X es hermano de Y si comparten ambos progenitores y X es hombre.
hermano(X, Y) :- hombre(X), padre(P, X), padre(P, Y), madre(M, X), madre(M, Y), X \= Y.

% 5. X es hermana de Y si comparten ambos progenitores y X es mujer.
hermana(X, Y) :- mujer(X), padre(P, X), padre(P, Y), madre(M, X), madre(M, Y), X \= Y.

% 6. X es antepasado de Y si es su progenitor o si es antepasado de su progenitor (recursión).
antepasado(X, Y) :- progenitor(X, Y).
antepasado(X, Y) :- progenitor(X, Z), antepasado(Z, Y).

% 7. X es nieto o nieta de Y si Y es abuelo o abuela de X.
nieto(X, Y) :- hombre(X), abuelo(Y, X).
nieto(X, Y) :- hombre(X), abuela(Y, X).
nieta(X, Y) :- mujer(X), abuelo(Y, X).
nieta(X, Y) :- mujer(X), abuela(Y, X).

% 8. X es tío de Y si X es hermano de un progenitor de Y.
tio(X, Y) :- hombre(X), hermano(X, P), progenitor(P, Y).
tia(X, Y) :- mujer(X), hermana(X, P), progenitor(P, Y).