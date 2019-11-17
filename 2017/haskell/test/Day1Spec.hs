module Day1Spec (spec) where

import           Day1
import           Test.Hspec

spec :: Spec
spec = do
  input <- runIO $ readFile "../data/Day1.input"

  describe "Day1 Part One" $ do
    it "1122 produces a sum of 3." $ do
      inverseCaptcha "1122" `shouldBe` 3
    it "1111 produces 4 because each digit matches the next." $ do
      inverseCaptcha "1111" `shouldBe` 4
    it "1234 produces 0 because no digit matches the next." $ do
      inverseCaptcha "1234" `shouldBe` 0
    it "91212129 produces 9 because the only digit that matches the next one is the last digit, 9." $ do
      inverseCaptcha "91212129" `shouldBe` 9
    it "Individial test..." $ do
      inverseCaptcha input `shouldBe` 1341

  describe "Day1 Part Two" $ do
    it "1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead." $ do
      inverseCaptchaPt2 "1212" `shouldBe` 6
    it "1221 produces 0, because every comparison is between a 1 and a 2." $ do
      inverseCaptchaPt2 "1221" `shouldBe` 0
    it "123425 produces 4, because both 2s match each other, but no other digit has a match." $ do
      inverseCaptchaPt2 "123425" `shouldBe` 4
    it "123123 produces 12." $ do
      inverseCaptchaPt2 "123123" `shouldBe` 12
    it "12131415 produces 4." $ do
      inverseCaptchaPt2 "12131415" `shouldBe` 4
    it "Individial test..." $ do
      inverseCaptchaPt2 input `shouldBe` 1348
