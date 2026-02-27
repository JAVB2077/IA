% -------------------------
% Base de conocimiento
% -------------------------

% biblioteca(Nombre, Ciudad, Responsable, Empleados, Libros, Prestamos).

biblioteca(bib_central, ciudad_mexico,
    persona(ana, responsable),
    [persona(juan, bibliotecario), persona(mario, tecnico), persona(luisa, bibliotecario)],
    [libro("Rayuela", "Julio Cortázar", 1963),
     libro("Cien años de soledad", "Gabriel García Márquez", 1967),
     libro("El Aleph", "Jorge Luis Borges", 1949)],
    [prestamo(laura, "Rayuela"), prestamo(carlos, "El Aleph")]
).

biblioteca(bib_norte, guadalajara,
    persona(jorge, responsable),
    [persona(marcos, tecnico), persona(elena, bibliotecario)],
    [libro("Ficciones", "Jorge Luis Borges", 1944),
     libro("Los premios", "Julio Cortázar", 1960),
     libro("Pedro Páramo", "Juan Rulfo", 1955)],
    [prestamo(laura, "Ficciones"), prestamo(ana, "Pedro Páramo")]
).

biblioteca(bib_sur, puebla,
    persona(claudia, responsable),
    [persona(luis, bibliotecario)],
    [libro("Bestiario", "Julio Cortázar", 1951),
     libro("Aura", "Carlos Fuentes", 1962)],
    [prestamo(jose, "Aura")]
).

trabaja_en(X, Ciudad):-biblioteca(_,Ciudad,Responsable,Empleados,_,_),member(persona(X,_),Empleados);member(persona(X,_),Responsable).

libro_antiguo(X):-biblioteca(_,_,_,_,Libros,_),member(libro(X,_,Anio),Libros),Anio<2000.

lector(X):-biblioteca(_,_,_,_,_,Prestamos),member(prestamo(X,_),Prestamos).

cantidad_empleados(Biblioteca, Cantidad):-biblioteca(Biblioteca,_,_,Empleados,_,_),length(Empleados,Cantidad).

libros_biblioteca(Biblioteca, Cantidad):-biblioteca(Biblioteca,_,_,_,Libros,_),length(Libros,Cantidad).

/**
1. Buscar la consulta y que de nombres de los responsables de bibliotecas con más de 2 empleados.
    biblioteca(_,_, persona(X,_,_),Empleados,_,_),Empleados >2.

2. Definir la relación trabaja_en(X, Ciudad) que se verifique si una persona trabaja en una biblioteca de dicha ciudad.
3. Preguntar por las personas que trabajan en bibliotecas de una ciudad específica(consulta).
    trabaja_en(elena,guadalajara).

4. Definir la relación libro_antiguo(X) que se verifique si un libro fue publicado antes del año 2000.
    libro_antiguo(X):-biblioteca(_,_,_,_,Libros,_),member(libro(X,_,Anio),Libros),Anio<2000.
        libro_antiguo('El Aleph'). 

5. Determinar el nombre de todos los lectores que han pedido prestado un libro antiguo.
    biblioteca(_,_,_,_,Libros,Prestamos),member(prestamo(X,Y),Prestamos),member(libro(Y,_,Anio),Libros),Anio<2000.
    
6. Definir la relación lector(X) que se verifique si X figura en alguna lista de préstamos.
    lector(X):-biblioteca(_,_,_,_,_,Prestamos),member(prestamo(X,_),Prestamos). segun yo esta bien pero no se por que no funca

7. Preguntar por los nombres de todos los lectores registrados en todas las bibliotecas.
8. Determinar todos los libros prestados en más de una biblioteca.
    % No se puede hacer porque no hay libros prestados en más de una biblioteca.

9. Definir la relación libros_autor(A, Libros) para obtener los libros escritos por un mismo autor.
10. Buscar los responsables de bibliotecas que tengan al menos un libro del autor "Julio Cortázar".
11. Definir la relación cantidad_empleados(Biblioteca, Cantidad) que devuelva la cantidad de empleados.
    cantidad_empleados(Biblioteca, Cantidad):-biblioteca(Biblioteca,_,_,Empleados,_,_),length(Empleados,Cantidad).

12. Calcular cuántos libros tiene cada biblioteca.
libros_biblioteca(Biblioteca, Cantidad):-biblioteca(Biblioteca,_,_,_,Libros,_),length(Libros,Cantidad).
**/
