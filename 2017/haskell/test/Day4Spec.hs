module Day4Spec (spec) where

import           Data.Text    (strip, unpack)
import qualified Data.Text.IO as TIO
import           Day4
import           Test.Hspec

spec :: Spec
spec = do
  input <- runIO $ TIO.readFile "../data/Day4.input"

  describe "Day4 Part One" $ do
    it "aa bb cc dd ee is valid" $ do
      (checkPassphrases ["aa bb cc dd ee"]) `shouldBe` 1
    it "aa bb cc dd aa is not valid - the word aa appears more than once." $ do
      (checkPassphrases ["aa bb cc dd aa"]) `shouldBe` 0
    it "aa bb cc dd aaa is valid - aa and aaa count as different words." $ do
      (checkPassphrases ["aa bb cc dd aaa"]) `shouldBe` 1
    it "Individual test..." $ do
      (checkPassphrases $ lines $ unpack $ strip input) `shouldBe` 451

  describe "Day4 Part Two" $ do
    it "abcde fghij is a valid passphrase." $ do
      (checkPassphrasesPt2 ["abcde fghij"]) `shouldBe` 1
    it "abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word." $ do
      (checkPassphrasesPt2 ["abcde xyz ecdab"]) `shouldBe` 0
    it "a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word." $ do
      (checkPassphrasesPt2 ["a ab abc abd abf abj"]) `shouldBe` 1
    it "iiii oiii ooii oooi oooo is valid." $ do
      (checkPassphrasesPt2 ["iiii oiii ooii oooi oooo"]) `shouldBe` 1
    it "oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word." $ do
      (checkPassphrasesPt2 ["oiii ioii iioi iiio"]) `shouldBe` 0
    it "Individual test..." $ do
      (checkPassphrasesPt2 $ lines $ unpack $ strip input) `shouldBe` 223
