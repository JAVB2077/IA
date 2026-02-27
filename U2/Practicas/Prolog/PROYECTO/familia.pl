%hechos para una dulceria
%dulceria(nombre, telefono, productos).

dulceria(la_dulce_vida, 1234567890, [pastel, galletas, chocolates]).
dulceria(dulces_sorpresas, 9876543210, [caramelos, gomitas, chocolates]).
dulceria(dulce_placer, 5551122134, [pastel, gomitas, galletas]).

%proveeor(nombre, telefono, productos, dulcerias_surte).

proveedor(choorrol, 1234567890, [pastel, galletas], [la_dulce_vida, dulce_placer]).
proveedor(bimbo, 9876543210, [caramelos, gomitas], [la_dulce_vida]).
proveedor(xerox, 5551122334, [pastel, gomitas], [dulces_sorpresas]).
proveedor(humbrela, 5551122384, [chocolates], [la_dulce_vida]).

% 10 reglas propias para la dulceria 
    %Una de ellas con uso de sort en al menos una consulta
    %Uso de member en al menos una consulta
    %Uso de length en al menos una consulta

% 1. con uso de findall Listar los nombres de todas las dulcerias que hay.
listar_dulcerias :-
    findall(Nombre, dulceria(Nombre, _, _), Lista),
    format('~w~n', [Lista]).

% 2. con uso de member, listar los productos de una dulceria especifica.
listar_productos_dulceria(NombreDulceria) :-
    dulceria(NombreDulceria, _, Productos),
    format('Productos de ~w: ~w~n', [NombreDulceria, Productos]).

%3. con uso de length, contar cuantas dulcerias hay.
contar_dulcerias :-
    findall(Nombre, dulceria(Nombre, _, _), Lista),
    length(Lista, Total),
    format('Total de dulcerias: ~w~n', [Total]).

% 4. con uso de findall, listar los nombres de un proveedoresen orden alfabetico.
listar_proveedores :-
    findall(Nombre, proveedor(Nombre, _, _, _), Lista),
    sort(Lista, ListaOrdenada),
    format('Proveedores: ~w~n', [ListaOrdenada]).

% 5. contar el numero total de productos que tiene un proveedor especifico.
contar_productos_proveedor(NombreProveedor) :-
    proveedor(NombreProveedor, _, Productos, _),
    length(Productos, Total),
    format('Total de productos de ~w: ~w~n', [NombreProveedor, Total]).

% 6. con uso de sort, listar los productos de un proveedor especifico en orden alfabetico.
listar_productos_proveedor_ordenados(NombreProveedor) :-
    proveedor(NombreProveedor, _, Productos, _),
    sort(Productos, ProductosOrdenados),
    format('Productos de ~w en orden alfabetico: ~w~n', [NombreProveedor, ProductosOrdenados]).

% reglas
hijo(X, P) :- padre(P, X).
hijo(X, P) :- madre(P, X).

hermano(X, Y) :-
    padre(P, X), padre(P, Y),
    madre(M, X), madre(M, Y),
    X \= Y.

% imprimir todos los hijos de una persona como lista
consultar_hijos(P) :-
    findall(X, hijo(X, P), Lista),
    format('~w~n', [Lista]).

% imprimir todos los hermanos de una persona como lista
consultar_hermanos(P) :-
    findall(X, hermano(X, P), Lista),
    format('~w~n', [Lista]).