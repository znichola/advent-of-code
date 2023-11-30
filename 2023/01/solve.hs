import Data.Char (isDigit)
import System.Posix (fileAccess)

main :: IO ()
main = do
  putStrLn "Hello AoC"
  content <- readFile "input.txt"
  print $ sum $ map extractCode $ lines content

extractDigits :: String -> String
extractDigits = filter isDigit

extractFirstLast :: String -> String
extractFirstLast str = [head str, last str]

extractCode :: String -> Int
extractCode str = read $ extractFirstLast $ extractDigits str
