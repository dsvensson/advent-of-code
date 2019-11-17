module Day2Spec (spec) where

import           Data.List
import           Day2
import           Test.Hspec


spec :: Spec
spec = do
    input <- runIO $ readFile "../data/day2.input"

    describe "Day2 Pt1" $
      it "Find box checksum." $
        inventoryManagementSystem input `shouldBe` 5658

    describe "Day2 Pt2" $
      it "Common letters of correct boxes." $
        inventoryManagementSystemPt2 input `shouldBe` ["nmgyjkpruszlbaqwficavxneo"]
