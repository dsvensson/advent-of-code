module Day1 (chronalCalibration, chronalCalibrationPt2) where

import qualified Data.Set as S

numbers :: String -> [Int]
numbers = map go . filter (/= "\n") . lines
  where go line@(sign:num) = case sign of
          '+' -> read num :: Int
          _   -> read line :: Int

chronalCalibration :: String -> Int
chronalCalibration = sum . numbers

chronalCalibrationPt2 :: String -> Int
chronalCalibrationPt2 = firstDuplicate (S.singleton 0) . scanl1 (+) . cycle . numbers
  where firstDuplicate acc (x:xs) = if x `S.member` acc then x
                                    else firstDuplicate (S.insert x acc) xs
