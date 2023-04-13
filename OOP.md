### OOP in JS
#### Types of properties
- Own properties are defined directly on the object instance itself
- Prototype properties are defined on the prototype
```javascript
function Bird(name) {
  this.name = name;  //own property
}
Bird.prototype.numLegs = 2; // prototype property

let duck = new Bird("Donald");
```
- Adding these properties to an array
```javascript
let ownProps = [];
let prototypeProps = [];

for (let property in duck) {
  if(duck.hasOwnProperty(property)) {
    ownProps.push(property);
  } else {
    prototypeProps.push(property);
  }
}
```

#### Constructor property
```javascript
let beagle = new Dog();
// Using object.constructor
console.log(beagle.constructor === Dog);
```

#### Setting multiple prototype properties
- Note: The side effect of using this is that the constructor property is erased so it needs to be included in the prototype
```javascript
Bird.prototype = {
    constructor: Bird,
    // ^Needs to be added to allow the use of object.constructor
    numLegs: 2, 
    eat: function() {
        console.log("nom nom nom");
    },
    describe: function() {
        console.log("My name is " + this.name);
    }
};
```

#### Inheritance
- DRY (Don't repeat yourself)
```javascript
// An example of repetitive code
Bird.prototype = {
  constructor: Bird,
  describe: function() {
    console.log("My name is " + this.name);
  }
};

Dog.prototype = {
  constructor: Dog,
  describe: function() {
    console.log("My name is " + this.name);
  }
};

// By making a superclass you can get rid of this repitition
function Animal() { };

Animal.prototype = {
  constructor: Animal, 
  describe: function() {
    console.log("My name is " + this.name);
  }
};
// Now the Dog and Bird classes can inherit from the Animal superclass
```

#### Creating from a superclass
- Best to use this method below
```javascript
let animal = Object.create(Animal.prototype);
```
- Setting the prototype of the child to be an instance of parent
```javascript
Bird.prototype = Object.create(Animal.prototype);
// Now Bird includes all properties from animal
let duck = new Bird("Donald");
duck.eat();
// Note you would also need to reset the constructor
Bird.prototype.constructor = Bird;
// Adding properties to the child
Bird.prototype.fly = function() {
  console.log("I'm flying!");
}
// You can also overrite a parent property by using the same name in the child prototype
Bird.prototype.eat = function() {
  return "peck peck";
}
```

#### Using Mixin's
- A mixin allows other objects to use a collection of functions
- A mixin takes any object and gives it it's methods
```javascript
let flyMixin = function(obj) {
  obj.fly = function() {
    console.log("Flying, wooosh!");
  }
}

let bird = {
  name: "Donald",
  numLegs: 2
}

let plane = {
  model: "777",
  numPassengers: 524
}

flyMixin(bird);
flyMixin(plane);

// Both bird and plane are assigned the fly property
bird.fly();
plane.fly();
```

#### Using Closure
- To protect properties within an object from being modified externally
- This can be done by changing the scope of a variable (defining it within the function)
```javascript
function Bird() {
  let hatchedEgg = 10;
  this.getHatchedEggCount = function() {
    return hachedEgg;
  }
}
let ducky = new Bird();
ducky.getHatchedEggCount();
```

#### Immediately Invoked Function Expression (IIFE)
- Invokes a function as soon as it's declared
```javascript
(function () {
  console.log("Greetings user!");
})();
```
- The function has no name nor stored in a variable
- Encased in (function) and invoked by (function)(); parethesis at the end.

#### This allows you to group functions into a module
```javascript
let myModule = (function () {
  return {
    one: function() {},
    two: function() {}
  }
})();
// Don't forget the parenthesis at the end to invoke it
```

