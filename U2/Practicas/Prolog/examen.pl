% Estructura de cada mascota:
% mascota(nombre(N), especie(E), raza(R), edad(A), duenio(persona(Nom, Ap, Tel)), historial([consulta(Fecha, Diagnostico, Tratamiento)])).

mascota(
    nombre(firulais),
    especie(perro),
    raza(labrador),
    edad(4),
    duenio(persona([juan], [perez], 1234567890)),
    historial([
        consulta(fecha(12, abril, 2023), moquillo, vacuna),
        consulta(fecha(15, junio, 2024), alergia, antihistaminico)
    ])
).

mascota(
    nombre(misu),
    especie(gato),
    raza(siames),
    edad(2),
    duenio(persona([ana], [lopez], 9876543210)),
    historial([
        consulta(fecha(10, enero, 2024), pulgas, desparasitante)
    ])
).

mascota(
    nombre(rocky),
    especie(perro),
    raza(pastor_aleman),
    edad(6),
    duenio(persona([carlos], [ramirez], 5551122334)),
    historial([
        consulta(fecha(5, febrero, 2023), moquillo, vacuna),
        consulta(fecha(7, marzo, 2024), infeccion_oido, antibiotico)
    ])
).

mascota(
    nombre(luna),
    especie(gato),
    raza(persa),
    edad(3),
    duenio(persona([maria], [gomez], 4445566778)),
    historial([
        consulta(fecha(20, julio, 2023), estres, tranquilizante)
    ])
).
% mascota(nombre(N), especie(E), raza(R), edad(A), duenio(persona(Nom, Ap, Tel)), historial([consulta(Fecha, Diagnostico, Tratamiento)])).

/**
1. Listar los nombres de todas las mascotas.
    ?-mascota(X, _, _, _, _, _).
2. Mostrar las razas de los perros registrados.
    ?-mascota(_, especie(perro), Raza, _, _, _).
3. Determinar cuántas mascotas hay en total.
    ?-findall(X, mascota(X, _, _, _, _, _), Mascotas), length(Mascotas, Total).
4. Obtener el nombre de todos los dueños de mascotas.
    ?-mascota(_, _, _, _, duenio(persona(Nombre,Apellido,Telefono)),_).
