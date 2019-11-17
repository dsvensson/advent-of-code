module Day1Spec (spec) where

import           Day1
import           Test.Hspec

spec :: Spec
spec = do
    input <- runIO $ readFile "../data/day1.input"

    describe "Day1 Pt1 " $
      it "find the final frequency calibration." $
        chronalCalibration input `shouldBe` 525

    describe "Day1 Pt2 " $
      it "find the first repeating frequency." $
        chronalCalibrationPt2 input `shouldBe` 75749
