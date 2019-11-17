module Day2 (inventoryManagementSystem, inventoryManagementSystemPt2) where

import           Data.List

inventoryManagementSystem :: String -> Int
inventoryManagementSystem = multiplyLengths . map findRecurrences . lines
  where findRecurrences = nub . filter (>1) . map length . group . sort
        multiplyLengths = product . map length . group . sort . concat

pairs :: [a] -> [(a, a)]
pairs l = [(x,y) | (x:ys) <- tails l, y <- ys]

inventoryManagementSystemPt2 :: String -> [String]
inventoryManagementSystemPt2 = map commonLetters . filter distance1 . pairs . lines
  where distance1 = (== 1) . length . filter (uncurry (/=)) . uncurry zip
        commonLetters = map fst . filter (uncurry (==)) . uncurry zip
