{-# LANGUAGE LambdaCase        #-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE RecordWildCards   #-}
module Day22 (modeMazePt1, modeMazePt2) where

import           Algorithm.Search                 (aStar)
import           Control.Monad                    (guard)
import qualified Data.Attoparsec.ByteString.Char8 as P
import qualified Data.ByteString.Char8            as BS
import           Data.Maybe                       (fromJust)
import           Data.MemoTrie                    (memo2)

type RegionTypeSolver = Coord -> RegionType

data RegionType = Rocky | Wet | Narrow deriving (Enum, Show)
data ToolType = ClimbingGear | Torch | Neither deriving (Eq, Ord, Show)

type Depth = Int
type Coord = (Int, Int)

data State = State
 { stateCoord :: Coord
 , stateTool  :: ToolType } deriving (Eq, Ord, Show)

readInput :: String -> (Depth, Coord)
readInput = unwrap . P.parseOnly parser . BS.pack
  where unwrap (Right v) = v
        parser = do
          P.string "depth: "
          depth <- P.many1 P.digit
          P.endOfLine
          P.string "target: "
          dstX <- P.many1 P.digit
          P.char ','
          dstY <- P.many1 P.digit
          pure (read depth, (read dstX, read dstY))

genRegionTypeSolver :: Depth -> Coord -> RegionTypeSolver
genRegionTypeSolver depth (dstX, dstY) = regionType
  where regionType (x, y) = toEnum $ erosionLevel x y `mod` 3
        erosionLevel posX posY = (geologicIndex' posX posY + depth) `mod` 20183
        geologicIndex' = memo2 geologicIndex
        geologicIndex posX posY
          | posX == 0    && posY == 0    = 0
          | posX == dstX && posY == dstY = 0
          | posX == 0                    = posY * 48271
          | posY == 0                    = posX * 16807
          | otherwise                    = erosionLevel (posX - 1) posY *
                                           erosionLevel posX (posY - 1)

modeMazePt1 :: String -> Int
modeMazePt1 input = sum $ map regionRisk [(pX,pY) | pX <- [0..dstX], pY <- [0..dstY]]
  where (depth, target@(dstX, dstY)) = readInput input
        regionType = genRegionTypeSolver depth target
        regionRisk = fromEnum . regionType

compatibleTools :: RegionType -> [ToolType]
compatibleTools = \case
  Rocky  -> [ClimbingGear, Torch  ]
  Wet    -> [ClimbingGear, Neither]
  Narrow -> [Torch,        Neither]

possibleTools :: RegionTypeSolver -> Coord -> [ToolType]
possibleTools regionType = compatibleTools . regionType

possibleCoords :: Coord -> [Coord]
possibleCoords (x, y) = [(x', y') | (x', y') <- [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)], x' >= 0, y' >= 0]

neighbors :: (Coord -> [ToolType]) -> State -> [State]
neighbors possibleTools State{..} = do
  coord <- possibleCoords stateCoord
  tool <- possibleTools coord
  guard (tool `elem` validTools)
  pure (State coord tool)
  where validTools = possibleTools stateCoord

cost :: State -> State -> Int
cost State{stateTool=t1} State{stateTool=t2} = if t1 == t2 then 1 else 7 + 1

manhattan :: Coord -> State -> Int
manhattan c1 State{stateCoord=c2} = go c1 c2
  where go (x1,y1) (x2,y2) = abs (x1 - x2) + abs (y1 - y2)

modeMazePt2 :: String -> Int
modeMazePt2 input = fst . fromJust $ aStar candidates cost remainingCost isTargetState initialState
  where (depth, target@(dstX, dstY)) = readInput input
        regionType = genRegionTypeSolver depth target
        candidates = neighbors $ possibleTools regionType
        remainingCost = manhattan target
        initialState = State (0, 0) Torch
        isTargetState = (== State target Torch)
