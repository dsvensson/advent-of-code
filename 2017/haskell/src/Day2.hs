module Day2 (corruptionChecksum, corruptionChecksumPt2) where

import           Data.List (lines, words)

readSpreadsheet :: String -> [[Int]]
readSpreadsheet document = map nums $ lines document
  where nums line = map read $ words line

difference :: [Int] -> Int
difference xs = maximum xs - minimum xs

corruptionChecksum :: String -> Int
corruptionChecksum document = sum $ map difference spreadsheet
  where spreadsheet = readSpreadsheet document

dividing :: [Int] -> Int
dividing xs = foldl (\acc (x,y) -> acc + x `div` y) 0 divisible
  where test (x,y) = x `mod` y == 0
        variants = concatMap (\x -> zip (repeat x) $ filter (\y -> y /= x) xs) xs
        divisible = filter test variants

corruptionChecksumPt2 :: String -> Int
corruptionChecksumPt2 document = sum $ map dividing spreadsheet
  where spreadsheet = readSpreadsheet document
