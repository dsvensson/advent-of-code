module Main (main) where

import           Day1
import           Day2
import           Day3
import           Day4
import           Day5

import           Day22

import           Criterion.Main

main :: IO ()
main = do
  input1 <- readFile "../data/day1.input"
  input2 <- readFile "../data/day2.input"
  input3 <- readFile "../data/day3.input"
  input4 <- readFile "../data/day4.input"
  input5 <- readFile "../data/day5.input"
  input22 <- readFile "../data/day22.input"

  defaultMain [ bgroup "day1" [ bench "pt1" $ whnf chronalCalibration input1
                              , bench "pt2" $ whnf chronalCalibrationPt2 input1 ]
              , bgroup "day2" [ bench "pt1" $ whnf inventoryManagementSystem input2
                              , bench "pt2" $ whnf inventoryManagementSystemPt2 input2 ]
              , bgroup "day3" [ bench "pt1" $ whnf noMatterHowYouSliceIt input3 ]
              , bgroup "day4" [ bench "pt1" $ whnf reposeRecord input4
                              , bench "pt2" $ whnf reposeRecordPt2 input4 ]
              , bgroup "day5" [ bench "pt1" $ whnf alchemicalReduction input5
                              , bench "pt2" $ whnf alchemicalReductionPt2 input5 ]
              , bgroup "day22" [ bench "pt1" $ whnf modeMazePt1 input22
                               , bench "pt2" $ whnf modeMazePt2 input22 ] ]
