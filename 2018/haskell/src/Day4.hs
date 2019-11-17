{-# LANGUAGE OverloadedStrings #-}
module Day4 (reposeRecord, reposeRecordPt2) where

import           Control.Applicative
import           Data.Attoparsec.ByteString.Char8
import qualified Data.ByteString.Char8            as BS
import           Data.List
import qualified Data.Map                         as M
import           Data.Ord

type GuardID = Int
data GuardMode = Awake | Sleeping deriving (Show)
data GuardEvent = NewGuardEvent GuardID | AwakeEvent | AsleepEvent deriving (Show)


timeParser :: Parser Int
timeParser = do
  char '['
  count 4 digit
  char '-'
  count 2 digit
  char '-'
  count 2 digit
  char ' '
  hour <- count 2 digit
  char ':'
  minute <- count 2 digit
  char ']'
  pure $ if hour == "23" then 0 else read minute

eventParser :: Parser GuardEvent
eventParser =
      (string "falls asleep">> pure AsleepEvent)
  <|> (string "wakes up" >> pure AwakeEvent)
  <|> switchGuardParser
  where switchGuardParser = do
          string "Guard #"
          guardID <- many digit
          string " begins shift"
          pure $ NewGuardEvent (read guardID)

rowParser :: Parser (GuardEvent, Int)
rowParser = do
  minute <- timeParser
  char ' '
  event <- eventParser
  pure (event, minute)

logParser :: Parser [(GuardEvent, Int)]
logParser = many $ rowParser <* endOfLine

readInput :: String -> [(GuardEvent, Int)]
readInput = unwrap . parseOnly logParser . BS.unlines . sort . BS.lines . BS.pack
  where unwrap (Right v) = v

explodeSleep :: [(GuardEvent, Int)] -> [(GuardID, [Int])]
explodeSleep = pick . foldl go (0, 0::Int, Awake, [])
  where go (guard, minute, mode, acc) (event, evMinute)  = case (mode, event) of
          (Awake, AsleepEvent) -> (guard, evMinute, Sleeping, acc)
          (Sleeping, AwakeEvent) -> (guard, evMinute, Awake, (guard, [minute..evMinute-1]):acc)
          (Awake, NewGuardEvent newGuard) -> (newGuard, evMinute, Awake, acc)
        pick (g, ts, m, acc) = acc

collectSleep :: [(GuardID, [Int])] -> [(GuardID, [Int])]
collectSleep = M.toList . foldl collect M.empty
  where collect m (guard, sleep) = M.insertWith (++) guard sleep m

reposeRecord :: String -> Int
reposeRecord = (uncurry (*)) . favorite . mrSleepy . collectSleep . explodeSleep . readInput
  where mrSleepy = maximumBy (comparing (length . snd))
        favorite (guard, sleep) = ((,) guard) . head . maximumBy (comparing length) . group . sort $ sleep


reposeRecordPt2 :: String -> Int
reposeRecordPt2 = grandSleeper . M.toList . M.fromListWith (++) . concat . map go . collectSleep . explodeSleep . readInput
  where go (guard, sleep) = map (\x -> (head x, [(guard, length x)])) . group . sort $ sleep
        grandSleeper input = let perMinute = map (\(minute, guards) -> (minute, maximumBy (comparing snd) guards)) input
                                 (minute, (guard, _)) = maximumBy (comparing (snd . snd)) perMinute
                             in minute * guard
