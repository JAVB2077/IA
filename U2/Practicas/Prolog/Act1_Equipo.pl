%Base de conocimientos
materia(miguel, fisica).
materia(miguel, lenguajes_interfaz).
materia(miguel, principios_electricos).

materia(oronzor, sistemas_programables).
materia(oronzor, lenguajes_interfaz).
materia(oronzor, principios_electricos).

alumno(miguel, mauricio).
alumno(miguel, maza).
alumno(miguel, cheo).
alumno(miguel, uziel).
alumno(miguel, javier).
alumno(miguel, tavo).

alumno(oronzor, mauricio).
alumno(oronzor, alejandra).
alumno(oronzor, zury).
alumno(oronzor, paola).
alumno(oronzor, toribio).
alumno(oronzor, joseph).

% Verificar si una lista es subconjunto de otra
subset([], _).
subset([H|T], L) :- member(H, L), subset(T, L).

% Diagnóstico basado en la presencia de todos los síntomas de una enfermedad
resultado(Maestro, Alumno) :-
 setof(A, alumno(Maestro, A), Resultado), % setof permite recopilar en una lista ordenada y sin
 subset(Resultado, Alumno). % verificar si una lista es un subconjunto de otra