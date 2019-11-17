{-# LANGUAGE QuasiQuotes #-}
module Day2Spec (spec) where

import           Data.String.QQ
import           Day2
import           Test.Hspec

sample1 = [s|
5 1 9 5
7 5 3
2 4 6 8|]

sample2 = [s|
5 9 2 8
9 4 7 3
3 8 6 5|]

spec :: Spec
spec = do
  input <- runIO $ readFile "../data/Day2.input"

  describe "Day2 Part One" $ do
    it "the spreadsheet's checksum would be 8 + 4 + 6 = 18." $ do
      corruptionChecksum sample1 `shouldBe` 18
    it "Individual test..." $ do
      corruptionChecksum input `shouldBe` 32020

  describe "Day2 Part Two" $ do
    it "the sum of the results would be 4 + 3 + 2 = 9." $ do
      corruptionChecksumPt2 sample2 `shouldBe` 9
    it "Individual test..." $ do
      corruptionChecksumPt2 input `shouldBe` 236
