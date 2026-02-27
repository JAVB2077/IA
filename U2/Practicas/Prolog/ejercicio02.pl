/**
Angres Mauricio Guerrero de Jesus
Joseph Angel Vega Bernal
*/

% Estudiantes inscritos en cursos EC
inscrito(juan, programacion).
inscrito(juan, bases_de_datos).
inscrito(ana, programacion).
inscrito(maria, algoritmos).
inscrito(carlos, bases_de_datos).
inscrito(carlos, inteligencia_artificial).
inscrito(pedro, algoritmos).
inscrito(pedro, inteligencia_artificial).

%Profesores que imparten cursos
profesor(luis, programacion).
profesor(laura, bases_de_datos).
profesor(ana, inteligencia_artificial).
profesor(jorge, algoritmos).

%Prerrequisitos de los cursos
prerrequisito(programacion, algoritmos).
prerrequisito(bases_de_datos, programacion).
prerrequisito(inteligencia_artificial, bases_de_datos).

% 1. es_estudiante(X): Verifica si X es un estudiante (alguien que está inscrito en al menos un curso).
es_estudiante(X) :- inscrito(X, Y).

% 2. es_profesor(X): Verifica si X es un profesor (alguien que imparte al menos un curso).
es_profesor(X) :- profesor(X, Y).

% 3. curso_impartido_por(C, P): C es un curso impartido por el profesor P.
curso_impartido_por(C, P) :- profesor(P, C).

% 4. curso_tomado_por(C, E): C es un curso tomado por el estudiante E.
curso_tomado_por(C, E) :- inscrito(E, C).

%5. prerrequisito_indirecto(C1, C2): C1 es un prerrequisito indirecto de C2 si hay una cadena de prerrequisitos entre ellos (regla recursiva).
prerrequisito_indirecto(C1, C2) :- prerrequisito(C1, C2).
prerrequisito_indirecto(C1, C2) :- prerrequisito(C1, C3), prerrequisito_indirecto(C3, C2).

/**
Reglas por definir:
1. es_estudiante(X): Verifica si X es un estudiante (alguien que está inscrito en al menos un curso).
2. es_profesor(X): Verifica si X es un profesor (alguien que imparte al menos un curso).
3. curso_impartido_por(C, P): C es un curso impartido por el profesor P.
4. curso_tomado_por(C, E): C es un curso tomado por el estudiante E.
5. prerrequisito_indirecto(C1, C2): C1 es un prerrequisito indirecto de C2 si hay una cadena de prerrequisitos entre ellos (regla recursiva).

Consutas por realizar:
?- es_estudiante(juan).
?- es_profesor(laura).
?- curso_impartido_por(programacion, X).
?- curso_tomado_por(bases_de_datos, X).
?- prerrequisito_indirecto(algoritmos, inteligencia_artificial).
?- prerrequisito_indirecto(programacion, inteligencia_artificial).

*/