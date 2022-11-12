// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator#syntax


const greeting = (person) => {
    const name = person ? person.name : "stranger";
    return `Howdy, ${name}`;
  }
  
  console.log(greeting({ name: "Alice" }));  // "Howdy, Alice"
  console.log(greeting(null));   