import Data.Char (isDigit)
import Data.List (foldl', isPrefixOf, isSuffixOf)
import Data.Text (foldr', pack, replace, unpack)
import Language.Haskell.TH (match)
import System.Posix (fileAccess)

main :: IO ()
main = do
  putStrLn "Hello AoC"
  content <- readFile "input.txt"

  let codes = lines content

  -- print $ sum $ map extractCode codes

  -- print $ replace (pack "eight") (pack "8") $ pack $ head $ lines content
  let calc = map (extractCodeBonus matchDict) codes
  let result = zip codes calc
  print $ sum calc
  -- mapM_ (\(original, code) -> putStrLn $ original ++ ": " ++ show code) result

extractDigits :: String -> String
extractDigits = filter isDigit

extractFirstLast :: String -> String
extractFirstLast str = [head str, last str]

extractCode :: String -> Int
extractCode str = read $ extractFirstLast $ extractDigits str

-- bonus

-- lmatch :: String -> [(String, String)] -> String
-- lmatch [] _ = ""  -- Base case: empty string
-- lmatch line [] = line  -- Base case: no more matches
-- lmatch line ((match, digit):rest) =
--   if match `isPrefixOf` line
--     then digit ++ lmatch (drop (length match) line) ((match, digit):rest)
--     else head line : lmatch (tail line) ((match, digit):rest)

lMatch :: [String] -> String -> String
lMatch _ [] = ""
lMatch match line = do
  let matches = filter (`isPrefixOf` line) match
  if not (null matches) then head matches else lMatch match (tail line)

rMatch :: [String] -> String -> String
rMatch _ [] = ""
rMatch match line = do
  let matches = filter (`isSuffixOf` line) match
  if not (null matches) then head matches else rMatch match (init line)

extractCodeBonus :: [String] -> String -> Int
extractCodeBonus dict str = read $ replaceDigitWordsInString (lMatch dict str ++ rMatch dict str)

matchDict :: [String]
matchDict = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

-- extractCodeBonus :: String -> Int
-- extractCodeBonus str = read $ extractFirstLast $ extractDigits $ replaceDigitWordsInString str

replaceDigitWordsInString :: String -> String
replaceDigitWordsInString str = foldr replaceDigitWord str wordToDigitMapping

-- replaceDigitWordsInString str = foldl' (flip replaceDigitWord) str wordToDigitMapping

replaceDigitWord :: (String, String) -> String -> String
replaceDigitWord word str = unpack $ replace (pack $ fst word) (pack $ snd word) (pack str)

wordToDigitMapping :: [(String, String)]
wordToDigitMapping =
  [ ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9")
  ]

-- replaceWords :: String -> [(String, String)] -> String
-- replaceWords = foldr replaceIfInMappings
--   where
--     replaceIfInMappings :: (String, String) -> String -> String
--     replaceIfInMappings (digit, word) acc
--       | pack word `isPrefixOf` pack acc = digit ++ drop (length word) acc
--       | otherwise = acc
