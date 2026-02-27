import System.Process
import System.Exit
import System.IO
import Control.Monad (when)

-- Ejecuta una consulta a Prolog y muestra el resultado
consultarProlog :: String -> IO ()
consultarProlog consulta = do
  let cmd = "swipl"
  let args = ["-q", "-s", "equipo.pl", "-g", consulta ++ ",halt."]
  (exitCode, stdout, stderr) <- readProcessWithExitCode cmd args ""
  case exitCode of
    ExitSuccess   -> putStrLn $ "Resultado: " ++ stdout
    ExitFailure _ -> putStrLn $ "Error ejecutando Prolog: " ++ stderr

-- Menú principal
main :: IO ()
main = do
  putStrLn "==== Consulta de Parentescos ===="
  putStrLn "1. ¿Qué escuelas participan en cierto deporte?"
  putStrLn "2. ¿Quiénes son los jugadores de una escuela determinada?"
  putStrLn "3. ¿Qué equipos han ganado más partidos?"
  putStrLn "4. ¿Qué jugadores tienen más de cierta edad?"
  putStrLn "5. ¿Cuántos jugadores hay en una escuela determinada?"
  putStrLn "6. "
  putStrLn "7. "
  putStrLn "8. "
  putStrLn "9. "
  putStrLn "10. "
  putStrLn "0. Salir"
  putStr "Selecciona una opción: "
  hFlush stdout
  opcion <- getLine
  case opcion of
    "1" -> do
      putStr "Nombre del deporte (ej. futbol): "
      hFlush stdout
      deporte <- getLine
      consultarProlog $ "listar_escuelas_deporte(" ++ deporte ++ ")"
      main
    --"2" -> do
      --putStr "Nombre de la persona (ej. maria): "
      --hFlush stdout
      --persona <- getLine
      --consultarProlog $ "consultar_hermanos(" ++ persona ++ ")"
      --main
    "2" -> do
      putStr "Ingrese el nombre de una escuela (ej. esc): "
      hFlush stdout
      jugadores <- getLine
      consultarProlog $ "listar_jugadores_escuela(" ++ jugadores ++ ")"
      main
    "3" -> do
      consultarProlog $ "listar_equipos_ganadores"
      main
    "4" -> do
      putStr "Ingrese edad (ej. 15): "
      hFlush stdout
      edad <- getLine
      consultarProlog $ "listar_jugadores_mayores(" ++ edad ++ ")"
      main    
    "5" -> do
      putStr "Ingrese el nombre de una escuela (ej. epfaa): "
      hFlush stdout
      nombre_escuela <- getLine
      consultarProlog $ "contar_jugadores_escuela(" ++ nombre_escuela ++ ")"
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