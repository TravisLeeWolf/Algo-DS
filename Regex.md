## Regular expressions
### Used to match parts of strings, where you create the patterns that help do the matching

#### Using .test() method
- takes the regex and applies it to a string
- returns true/false if your pattern finds something/not
- finds only exactly what is in the regex, so in the case below World/WORLD won't return true
```javascript
let someStr = "Hello world!";
let myRegex = /world/;
myRegex.test(someStr)
```

```javascript
// You can use the or | operator to search either or
let myRegex = /yes|no/;

// Using i at the end of the regex ignores case sensitivity
let myRegex = /ignorecase/i; 
```

#### Using .match() method
- note it works in opposite direction to test()
- returns the text if matching
```javascript
let someStr = "The quick brown fox"
let myRegex = /fox/;
someStr.match(myRegex);
// Note: myRegex.test(someStr);
```

```javascript
// Using g you can global search, returning all matching patterns in the string
let someStr = "again, again, again";
let myRegex = /again/g;
someStr.match(myRegex);
// returns a list of all matching patterns

// Using the wildcard char . you can match any one extra character in a pattern
let sumStr = "hug, hum, hut";
let huRegex = /hu./g;

// Using char classes you can add some flexibilty to your matching
let bigStr = "big";
let bagStr = "bag";
let bgRegex = /b[aiu]g/;
bigStr.match(bgRegex);
bagStr.match(bgRegex);
// This matches all b_g words containing a,i,u

// You can also match trough a range
let strOne = "cat";
let strTwo = "bat";
let rangeRegex = /[a-e]at/;
// Also with numbers
let userName = "Bob123";
let userRegex = /[a-z0-9]/ig;

// Match single char not specified
/[^aeiou]/gi // This matches all char excluding a,e,i,o,u

// Match char occuring once or more
/s+/g // when matching Mississippi

// Matching a char occuring zero or more
/go*/ // the 'o' will be matched zero or more
```

#### Greedy vs Lazy matching
- A greedy match finds the longest possible part of a string that fits the pattern
- A lazy match finds the smallest possible
- Lazy match uses ?
```javascript
let someStr = "banana"
// greedy
/b[a-z]*a/ // returns ["banana"]
// lazy
/b[a-z]*?a/ // returns ["ba"]
```

```javascript
//^ is also used to find 'Something' if it's the first char set
/^Something/

// Then to find something at the end use $
/something$/
```

#### Shorthand for JS
```javascript
// In JS you can use this shorthand for alphanumeric
let longHand = /[A-Za-z0-9_]+/;
let shortHand = /\w+/;

// This searches for the inverse of the above
let shortHand = /\W/;

// To only select [0-9]
let shortDigits = /\d/;

// Naturally this will look for non-digit chars
let shortNotDigit = /\D/;
```

#### Other matchings
```javascript
// Matches whitespace
let spaceRegex = /\s/;

// Non-whitespace
let nonSpaceRegex = /\S/;

// For matching a specified range
let A4 = "aaaah";
let A2 = "aah";
let multipleA = /a{3,5}h/;

// Using ? checks for zero or one of the char
let rainbowRegex= /colou?r/;

// Check for mixed groups of chars
let testRegex = /P(engu|umpk)in/;
```

#### Lookaheads
- A positive lookahead will look to make sure the element in the search pattern is there, but won't actually match it.
- A negative lookahead will look to make sure the element in the search pattern is not there.

```javascript
let quRegex= /q(?=u)/;
let qRegex = /q(?!u)/;
```

#### More stuff
- Matching repititons
```javascript
// (\w+) is the word \1 is the repitition
let repeatRegex = /(\w+) \1 \1/;
```

- Replacing
```javascript
// Simple replace
let wrongText = "The sky is silver.";
let silverRegex = /silver/;
wrongText.replace(silverRegex, "blue");

// Using capture groups to switch words
"Code Camp".replace(/(\w+)\s(\w+)/, '$2 $1');
```