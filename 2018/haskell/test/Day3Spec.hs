module Day3Spec (spec) where

import           Data.List
import           Day3
import           Test.Hspec


spec :: Spec
spec = do
    input <- runIO $ readFile "../data/day3.input"

    describe "Day3 Pt1" $
       it "How many square inches of fabric are within two or more claims?" $
         noMatterHowYouSliceIt input `shouldBe` 110195

    -- describe "Day3 Pt2" $
    --   it "What is the ID of the only claim that doesn't overlap?" $
    --     noMatterHowYouSliceItPt2 input `shouldBe` 894
