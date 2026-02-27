% Base de conocimientos: síntomas asociados a enfermedades de plantas
sintoma(mildiu, manchas_amarillas).
sintoma(mildiu, moho_blanco).
sintoma(mildiu, hojas_marchitas).

sintoma(oidio, polvo_blanco).
sintoma(oidio, hojas_rizadas).
sintoma(oidio, crecimiento_reducido).

sintoma(roña, manchas_negras).
sintoma(roña, frutos_deformados).
sintoma(roña, caida_prematura_hojas).

sintoma(fusariosis, marchitez).
sintoma(fusariosis, coloracion_marron).
sintoma(fusariosis, pudricion_raices).

% Verificar si una lista es subconjunto de otra
subset([], _).
subset([H|T], L) :- member(H, L), subset(T, L).

% Diagnóstico basado en la presencia de todos los síntomas de una enfermedad
diagnostico(Enfermedad, SintomasPaciente) :-
    setof(S, sintoma(Enfermedad, S), SintomasEnfermedad), % setof permite recopilar en una lista ordenada y sin duplicados los resultados de una consulta
    subset(SintomasEnfermedad, SintomasPaciente). % verificar si una lista es un subconjunto de otra

% Consultas
% diagnostico(Enfermedad, [manchas_amarillas, moho_blanco, hojas_marchitas]).

