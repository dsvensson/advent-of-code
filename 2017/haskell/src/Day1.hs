module Day1 (inverseCaptcha, inverseCaptchaPt2) where

import           Data.Char (digitToInt)


inverseCaptchaOffset :: Int -> String -> Int
inverseCaptchaOffset offset text = sum $ map fst $ filter eqTuple pairs
  where xs = map digitToInt text
        pairs = zip xs $ drop offset $ cycle xs
        eqTuple = uncurry (==)

inverseCaptcha :: String -> Int
inverseCaptcha = inverseCaptchaOffset 1

inverseCaptchaPt2 :: String -> Int
inverseCaptchaPt2 text = inverseCaptchaOffset offset text
  where offset = length text `div` 2
