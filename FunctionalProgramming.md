### Functional programming
#### A style of programming where solutions are simple, isolated functions, without any side effects outside of the fucntion scope
#### INPUT -> PROCESS -> OUTPUT
1. Isolated functions - there is no dependence on the state of the program, which includes global variables that are subject to change

2. Pure functions - the same input always gives the same output

3. Functions with limited side effects - any changes, or mutations, to the state of the program outside the function are carefully controlled
<hr>

#### Principles of functional programming
1. Don't alter a variable or object - create new variables and objects and return them if need be from a function. Hint: using something like const newArr = arrVar, where arrVar is an array will simply create a reference to the existing variable and not a copy. So changing a value in newArr would change the value in arrVar.

2. Declare function parameters - any computation inside a function depends only on the arguments passed to the function, and not on any global object or variable.

#### Array.prototype.map()
- Iterates over each item in an array
- Returns a new array containing the results of calling the callback function on each element
- Does this without mutating the original array
```javascript
const users = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 }
];

const names = users.map(user => user.name);
console.log(names);
```