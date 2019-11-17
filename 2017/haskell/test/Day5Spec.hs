module Day5Spec (spec) where

import           Day5
import           Test.Hspec

spec :: Spec
spec = do
  input <- runIO $ readFile "../data/Day5.input"

  describe "Day5 Part One" $ do
    it "0 3 0 1 -3 takes 5 steps to exit" $ do
      findExit "0 3 0 1 -3" `shouldBe` 5
    it "Individual test..." $ do
      findExit input `shouldBe` 375042

  describe "Day5 Part Two" $ do
    it "0 3 0 1 -3 takes 10 steps to exit" $ do
      findExitPt2 "0 3 0 1 -3" `shouldBe` 10
    it "Individual test..." $ do
      findExitPt2 input `shouldBe` 28707598
