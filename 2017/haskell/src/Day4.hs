module Day4 (checkPassphrases, checkPassphrasesPt2) where

import           Data.List
import qualified Data.Set  as S

checkPassphrase :: String -> Bool
checkPassphrase passphrase = length parts == length unique
  where parts = words passphrase
        unique = S.fromList parts

checkPassphrases :: [String] -> Int
checkPassphrases passphrases = length $ filter checkPassphrase passphrases

checkPassphrasePt2 :: String -> Bool
checkPassphrasePt2 passphrase = length parts == length valid
  where parts = words passphrase
        valid = S.fromList $ map sort parts

checkPassphrasesPt2 :: [String] -> Int
checkPassphrasesPt2 passphrases = length $ filter checkPassphrasePt2 passphrases
