module Day5 (alchemicalReduction, alchemicalReductionPt2) where

import           Data.Char
import           Data.List
import           Debug.Trace

reduce :: [Int] -> [Int]
reduce = foldr go []
  where go b (a:acc) = if (a == b - 32) || (a - 32 == b) then acc else (b:a:acc)
        go b []      = [b]

alchemicalReduction :: String -> Int
alchemicalReduction = length . reduce . map ord . filter ((/=) '\n')

alchemicalReductionPt2 :: String -> Int
alchemicalReductionPt2 = minimum . map go . variants . repeat . map ord . filter ((/=) '\n')
  where variants = zip (map (\x -> [ord x, ord x - 32]) ['a'..'z'])
        go (x, polymer) = length . reduce . filter (not . flip elem x) $ polymer
