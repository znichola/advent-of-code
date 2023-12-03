import System.Posix (fileAccess)
import Data.List (isPrefixOf, unfoldr)
import qualified Data.Text as D
import Data.Text (pack, unpack)

main :: IO ()
main = do
    file <- readFile "input.txt"
    let content = lines file
    -- print $ map (\x -> if x == ';' then '|' else x) (head content)
    let g = last $ splitOn ":" $ head content
    print $ head content
    print $ splitOn ";" g
    let game = parseGame g
    print game

type Red = Int
type Green = Int
type Blue = Int

type Hand = (Red, Green, Blue)

type Game = [Hand]

parse:: String -> (Game, String)
parse "" = ([], "")
-- parse str = 

---

-- type Red = Int
-- type Green = Int
-- type Blue = Int
-- type Hand = (Red, Green, Blue)
-- type Game = [Hand]

-- Parse a single hand from a string
parseHand :: String -> Hand
parseHand handStr = case words handStr of
    [r, g, b] -> (read r, read g, read b)
    _         -> error "Invalid hand format"

-- Parse a game from a string
parseGame :: String -> Game
parseGame gameStr = map parseHand (splitOn ";" gameStr)

-- Utility function to split a string on a delimiter
splitOn :: String -> String -> [String]
-- splitOn delimiter = unfoldr (splitOnHelper delimiter)
--   where
--     splitOnHelper :: Eq a => [a] -> [a] -> Maybe ([a], [a])
--     splitOnHelper _ [] = Nothing
--     splitOnHelper delim str =
--       Just $ fmap (drop (length delim)) (breakOn delim str)
splitOn delim str = map unpack $ D.splitOn (pack delim) (pack str)

-- Utility function to break a list into two parts at the first occurrence of a delimiter
breakOn :: Eq a => [a] -> [a] -> ([a], [a])
breakOn delimiter list = case breakList delimiter list of
  Just (before, after) -> (before, drop (length delimiter) after)
  Nothing              -> (list, [])
  where
    breakList :: Eq a => [a] -> [a] -> Maybe ([a], [a])
    breakList _ [] = Nothing
    breakList sublist list@(x:xs)
      | sublist `isPrefixOf` list = Just ([], list)
      | otherwise = fmap (x:) <$> breakList sublist xs

-- main :: IO ()
-- main = do
--   let gameString = "6 green, 3 blue; 3 red, 1 green; 4 green, 3 red, 5 blue"
--       game = parseGame gameString
--   print game

