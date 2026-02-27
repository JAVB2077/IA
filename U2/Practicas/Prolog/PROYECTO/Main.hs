import System.Process
import System.Exit
import System.IO
import Control.Monad (when)

-- Ejecuta una consulta a Prolog y muestra el resultado
consultarProlog :: String -> IO ()
consultarProlog consulta = do
  let cmd = "swipl"
  let args = ["-q", "-s", "familia.pl", "-g", consulta ++ ",halt."]
  (exitCode, stdout, stderr) <- readProcessWithExitCode cmd args ""
  case exitCode of
    ExitSuccess   -> putStrLn $ "Resultado: " ++ stdout
    ExitFailure _ -> putStrLn $ "Error ejecutando Prolog: " ++ stderr

-- Menú principal
main :: IO ()
main = do
  putStrLn "==== Consulta de Parentescos ===="
  putStrLn "1. Mostrar todas las dulcerias en la BD"
  putStrLn "2. listar los productos de una dulceria especifica"
  putStrLn "3. contar cuantas dulcerias hay"
  putStrLn "4. listar los nombres de los proveedores que surten a una dulceria especifica."
  putStrLn "5. contar el numero total de productos que surten los proveedores a las dulcerias."
  putStrLn "6. listar los productos de un proveedor especifico en orden alfabetico"
  putStrLn "7. Mostrar todas las dulcerias en la BD"
  putStrLn "8. Mostrar todas las dulcerias en la BD"
  putStrLn "9. Mostrar todas las dulcerias en la BD"
  putStrLn "10. Mostrar todas las dulcerias en la BD"
  putStrLn "0. Salir"
  putStr "Selecciona una opción: "
  hFlush stdout
  opcion <- getLine
  case opcion of
    "1" -> do
      --putStr "Nombre de la persona (ej. juan): "
      --hFlush stdout
      --dulceria <- getLine
      consultarProlog $ "listar_dulcerias"
      main
    --"2" -> do
      --putStr "Nombre de la persona (ej. maria): "
      --hFlush stdout
      --persona <- getLine
      --consultarProlog $ "consultar_hermanos(" ++ persona ++ ")"
      --main
    "2" -> do
      putStr "Ingrese el nombre de una dulceria (ej. dulce_placer): "
      hFlush stdout
      nombre_dulceria <- getLine
      consultarProlog $ "listar_productos_dulceria(" ++ nombre_dulceria ++ ")"
      main
    "3" -> do
      --putStr "Ingrese el nombre de una dulceria (ej. dulce_placer): "
      --hFlush stdout
      --nombre_dulceria <- getLine
      consultarProlog $ "contar_dulcerias"
      main
    "4" -> do
      consultarProlog $ "listar_proveedores"
    "5" -> do
      putStr "Ingrese el nombre de un proveedor (ej. bimbo): "
      hFlush stdout
      nombre_dulceria <- getLine
      consultarProlog $ "contar_productos_proveedor(" ++ nombre_dulceria ++ ")"
      main
    "6" -> do
      putStr "listar los productos de un proveedor especifico en orden alfabetico. (ej. bimbo): "
      hFlush stdout
      nombre_provedor <- getLine
      consultarProlog $ "listar_productos_proveedor_ordenados(" ++ nombre_provedor ++ ")"
      main
    "7" -> do
      putStr "Ingrese el nombre de una dulceria (ej. dulce_placer): "
      hFlush stdout
      nombre_dulceria <- getLine
      consultarProlog $ "listar_productos_dulceria(" ++ nombre_dulceria ++ ")"
      main
    "8" -> do
      putStr "Ingrese el nombre de una dulceria (ej. dulce_placer): "
      hFlush stdout
      nombre_dulceria <- getLine
      consultarProlog $ "listar_productos_dulceria(" ++ nombre_dulceria ++ ")"
      main
    "9" -> do
      putStr "Ingrese el nombre de una dulceria (ej. dulce_placer): "
      hFlush stdout
      nombre_dulceria <- getLine
      consultarProlog $ "listar_productos_dulceria(" ++ nombre_dulceria ++ ")"
      main
    "10" -> do
      putStr "Ingrese el nombre de una dulceria (ej. dulce_placer): "
      hFlush stdout
      nombre_dulceria <- getLine
      consultarProlog $ "listar_productos_dulceria(" ++ nombre_dulceria ++ ")"
      main
    "0" -> putStrLn "Hasta luego."
    _   -> do
      putStrLn "Opción no válida."
      main