module Main (main) where

import           Data.Text      (strip, unpack)
import qualified Data.Text.IO   as TIO

import           Day1
import           Day2
import           Day4
import           Day5

import           Criterion.Main

main :: IO ()
main = do input1 <- readFile "data/Day1.input"
          input2 <- readFile "data/Day2.input"
          input4 <- TIO.readFile "data/Day4.input"
          input5 <- readFile "data/Day5.input"
          defaultMain [bgroup "day1" [bench "pt1" $ whnf inverseCaptcha input1
                                     ,bench "pt2" $ whnf inverseCaptcha input1]
                      ,bgroup "day2" [bench "pt1" $ whnf corruptionChecksum input2
                                     ,bench "pt2" $ whnf corruptionChecksum input2]
                      ,bgroup "day4" [bench "pt1" $ whnf checkPassphrases (lines $ unpack $ strip input4)
                                     ,bench "pt2" $ whnf checkPassphrases (lines $ unpack $ strip input4)]
                      ,bgroup "day5" [bench "pt1" $ whnf findExit input5
                                     ,bench "pt2" $ whnf findExitPt2 input5]]
