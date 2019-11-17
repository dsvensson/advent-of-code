module Day5Spec (spec) where

import           Day5
import           Test.Hspec

spec :: Spec
spec = do
    input <- runIO $ readFile "../data/day5.input"

    describe "Day5 Pt1" $
      it "Basic polymer reduction" $
        alchemicalReduction input `shouldBe` 10774

    describe "Day5 Pt2" $
      it "Shortest polymer variant" $
        alchemicalReductionPt2 input `shouldBe` 5122
