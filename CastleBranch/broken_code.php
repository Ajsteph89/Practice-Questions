<?php
/**
 * Class Palindrome
 */
class Palindrome {
    /**
     * String that will be parsed for palindrome.
     * @var string
     */
    protected $string;
    /**
     * Handle.
     */
    public function handle() 
    {
        do {
            $this->getInput();
            if ($this->string === 'exit') {
                echo "Goodbye!";
                exit;
            }
            $palindromes = $this->findPalindromes();
            $this->formatOutput($palindromes);

        } while (true);
    }
    /**
     * Get input from user.
     */
    private function getInput()
    {
        echo "Input: ";
        $this->string = rtrim(fgets(STDIN));
    }
    /**
     * Format string to desired output.
     *
     * @param $palindromes
     * @return string
     */
    private function formatOutput($palindromes)

    {
        $foundString = '';
        $palindromeCount = count($palindromes);
        foreach ($palindromes as $palindrome) {

            $foundString .= ', ' . $palindrome;

        }
        echo "This string contains {$palindromeCount} palindrome words (i.e.{$foundString})" . PHP_EOL;

    }
    /**
     * Determines if the given string
     * contains palindromes.
     *
     * @return array
     */
    private function findPalindromes() 
    {
        $palindromes = []; 
        $words = explode(" ",$this->string);

        foreach ($words as $word) {   
            $characters = str_split(strtolower($word));
            $charCount = count($characters);
            $palindromeFound = $word;
            
            for ($leftIndex = 0; $leftIndex < $charCount; $leftIndex++) {
//RIGHT INDEX SHOULD START AT CHARCOUNT -1
                $rightIndex = (int) ($charCount-1) - $leftIndex;
//COMPARISON OPERATOR SHOULD BE NOT EQUAL
                if ($characters[$leftIndex] !== $characters[$rightIndex]) {
                    $palindromeFound = false;
                    break;
                }
            }
// MISSING ; AFTER NULL
            ($palindromeFound) ? $palindromes[] = $palindromeFound: null;
        }
      
// TYPO IN VARIALBE NAME
      return $palindromes;
    }
}


$class = new Palindrome();
$class->handle();

/**
*Do we want to include single letter "palindromes" ie a or I?
  if not implement if (strlen($word)>1){} after for each on line 65
*Do we want to remove possible punctuation characters?
* add to getInput function 
$remove = ["'","!",";","•",",","\\","}","{","[","]"," ", "?"];
    $replace_with = [];
    echo "Input: ";
    $this->string = str_replace($remove, $replace_with, rtrim(fgets(STDIN)));
**/
