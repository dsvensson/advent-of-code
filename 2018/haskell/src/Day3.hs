module Day3 (noMatterHowYouSliceIt, noMatterHowYouSliceItPt2) where

import qualified Data.Map.Strict as M
import qualified Data.Set        as S
import           Text.Regex.TDFA

-- https://github.com/Nycander/adventofcode2018/blob/master/day3.hs

readInput :: String -> [(Int, Int, Int, Int, Int)]
readInput input = map go (input =~ "#([^ ]+) @ ([^,]+),([^:]+): ([^x]+)x([0-9]+)" :: [[String]])
  where go matches = let [cid,x,y,w,h] = map (\x -> read x :: Int) $ tail matches
                     in (cid, x, y, w, h)

toCoords :: [(Int, Int, Int, Int, Int)] -> [(Int, (Int, Int))]
toCoords input = do
  (cid, x, y, w, h) <- input
  xs <- [x..x + w - 1]
  ys <- [y..y + h - 1]
  pure (cid, (xs, ys))

noMatterHowYouSliceIt :: String -> Int
noMatterHowYouSliceIt = M.foldr overlaps 0 . foldl accountSlice M.empty . toCoords . readInput
  where accountSlice m (_, (x, y)) = M.insertWith (+) (x, y) 1 m
        overlaps value acc = if value > 1 then succ acc else acc

noMatterHowYouSliceItPt2 :: String -> Int
noMatterHowYouSliceItPt2 input = 1
