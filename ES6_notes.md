#### Some new stuff
let vs var
```javascript
// It's better to use
let someVar = "something";
// over using
var someVar = "something";
/* as var creates a global variable where
let creates local variables to the scope
that it's declared in
*/
```

'const' it's best to get used to declaring variables as const unless you know the variable will change then use 'let'
- const objects like arrays and functions are still mutable, const only prevents reassingment

#### Object.freeze(someObj);
This function prevents any changes to the someObj
```javascript
let someObj = {
    name: "specialName",
    squence: "something",
};
Object.freeze(someObj);
```

#### Arrow Functions
- When the function were making doesn't need to have a name
- Create an inline function using the arrow method
```javascript
// () => instead of function()
const someFunc = () => {
    const someVar = "something";
    return someVar;
}

// For an even simpler function
const someFunc = () => "something";
// Here the variable declaration and 'return' can be omitted
```
- You can also pass arguments to an arrow function
```javascript
const doubler = (item) => item * 2;
doubler(4);
// If there is only a single parameter you can omit the ()
const doubler = item => item * 2;
// You can also pass mutiple arguments too
```

Be sure to set default parameters to functions so that they are able to run without an argument being specified (instead of throwing an error)

#### Rest Parameter with Function Parameters
- This allows us to pass in a varying number of arguments to a function (...args)
```javascript
function multiArgFunc(...args) {
    return `You passed in ${args.length} arguments.`;
}

// Sum function example
const sum = (...args) => {
  let answer = 0;
  for (let i = 0; i < args.length; i++) {
    answer += args[i];
  }
  return answer;
}
```

- The spread operator ...arr can also be used to unpack an array when used in an argument to a function
- - Does not work as an assignment
- - const speaded = ...arr; (X)

#### Destructuring Assignment
- Used to assign values directly from an object
```javascript
const user = {name: "Bob", age: 25};

// Previous way of doing it
const name = user.name;
const age = user.age;

// Using the desructing assignment
const {name, age} = user;

// You can also assing new variable names
const {name: userName, age: userAge} = user; 

// This can also be done with nested variables
const user = {
  somePerson: { 
    age: 25,
    email: 'somePerson@email.com'
  }
};

const {somePerson: {age: userAge, email: userEmail}} = user;
```

- You can also destructure an array
- - The difference from the spread operator ... is that it selects all where destructuring you can specify
```javascript
const [a, b,,, c] = [1, 2, 3, 4, 5, 6];
// This sets a=1, b=2 and c=5

// Swapping numbers using array destructuring
let a = 8, b = 6;
[a,b] = [b,a];

// You can also use both destructuring and the rest parameter to assing variables and collect the remaining
const [a, b, ...arr] = [1, 2, 3, 4, 5, 7];
```

- Desctructuring assignment to pass and object as fucntion parameters
```javascript
const profileUpdate = (profileData) => {
  const { name, age, nationality, location } = profileData;

}
// Using destructuring as function parameters
const profileUpdate = ({ name, age, nationality, location }) => {

}
```

#### Some useful ES6 additions
- Concise Object Literal Declarations Using Object Property Shorthand
```javascript
const getMousePosition = (x, y) => ({ x, y });
// No need to define by ({x: x, y: y})
```
- You can remove the function keyword and colon when defining functions IN OBJECTS
```javascript
const someObject = {
    name: "somePerson",
    sayHello() {
        return `Hello ${name}!`;
    }
};
```
- Class Syntax to Define a Constructor Function
```javascript
// Previous method
var SpaceShuttle = function(targetPlanet){
  this.targetPlanet = targetPlanet;
}
var zeus = new SpaceShuttle('Jupiter');

// Using ES6 class constructor
class SpaceShuttle {
  constructor(targetPlanet) {
    this.targetPlanet = targetPlanet;
  }
}
const zeus = new SpaceShuttle('Jupiter');
```

#### Module Script
- Extends the functionality of JS so that you can work with more js modules
```html
<script type="module" src="filename.js"></script>
```
A script using module can use import/export features you'd find in typical code
```javascript
// After your function declarations you can add export and the function name
const add = (x, y) => {
    return x + y;
}

export {add};

// Then in another .js file you can import it like this
import {add} from "./math_functions.js";

// You can use * to import all functions
import * as mathModule from "./math_functions.js";
```

#### JavaScript Promise
- It's used to do something, usually asynchronously
```javascript
const myPromise = new Promise((resolve, reject) => {
  if(condition here) {
    resolve("Promise was fulfilled");
  } else {
    reject("Promise was rejected");
  }
});
```
- - A promise has 3 states: pending, fulfilled and rejected

- Once a promise is fulfilled (resolve) then you can do the next thing using then()
```javascript
myPromise.then(result => {
    // Do stuff
});
// Then is executed immediately after your promis is fulfilled

myPromise.catch(error => {
    // Do stuff
});
// Catch is executed if the reject method is called
```
 - - 'result' comes from the argument given to the 'resolve' method
 - - 'error' come from the argument given to the 'reject' method

#### Functional Programming
- Example
```javascript
// Function that returns a string representing a cup of green tea
const prepareTea = () => 'greenTea';

/*
Given a function (representing the tea type) and number of cups needed, the
following function returns an array of strings (each representing a cup of
a specific type of tea).
*/
const getTea = (numOfCups) => {
  const teaCups = [];

  for(let cups = 1; cups <= numOfCups; cups += 1) {
    const teaCup = prepareTea();
    teaCups.push(teaCup);
  }
  return teaCups;
};
```