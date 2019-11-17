module Day4Spec (spec) where

import           Day4
import           Test.Hspec

spec :: Spec
spec = do
    input <- runIO $ readFile "../data/day4.input"

    describe "Day4 Pt1" $
      it "Favorite minute for most sleepy guard * guard ID" $
        reposeRecord input `shouldBe` 98680

    describe "Day4 Pt2" $
      it "Most minute-favorizing sleeper's minute * guard ID" $
        reposeRecordPt2 input `shouldBe` 9763
