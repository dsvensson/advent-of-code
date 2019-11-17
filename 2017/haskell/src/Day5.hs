module Day5 (findExit, findExitPt2) where

import qualified Data.Sequence as S

execute :: S.Seq Int -> (Int -> Int) -> Int -> Int -> Int
execute program offset pc cycles
  | pc >= S.length program = cycles
  | otherwise = execute nextProgram offset nextPc (cycles + 1)
  where jmp = S.index program pc
        nextPc = pc + jmp
        nextProgram = S.adjust offset pc program

findExit :: String -> Int
findExit maze = execute program offset 0 0
  where program = S.fromList $ map read $ words maze
        offset jmp = jmp + 1

findExitPt2 :: String -> Int
findExitPt2 maze = execute program offset 0 0
  where program = S.fromList $ map read $ words maze
        offset jmp = if jmp >= 3 then jmp - 1 else jmp + 1
