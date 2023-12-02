import System.Posix (fileAccess)

main :: IO ()
main = do
    content <- readFile "input.txt"
    print $ head $ lines content

