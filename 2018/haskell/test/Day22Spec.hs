module Day22Spec (spec) where

import           Day22
import           Test.Hspec

spec :: Spec
spec = do
    input <- runIO $ readFile "../data/day22.input"

    describe "Day22 Pt1" $
      it "The total risk level" $
        modeMazePt1 input `shouldBe` 11359

    describe "Day22 Pt2" $ do
      it "The fewest number of minutes" $
        modeMazePt2 input `shouldBe` 976
