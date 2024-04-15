// experimenting with Maybe monad

const Nothing = (x) => ({
  isNothing: () => true,
  map: (fn) => Nothing(x),
  fold: (fn) => x,
  toString: () => `Nothing(${x})`
})

const Just = (x) => ({
  isNothing: () => false,
  map: (fn) => Maybe(fn(x)),
  fold: (fn) => fn(x),
  toString: () => `Just(${x})`
})

const Maybe = (x) => (x === undefined || x === null)
  ? Nothing(x)
  : Just(x)

console.log(Maybe(null).isNothing())
console.log(Maybe(undefined).isNothing())
console.log(Maybe(0).isNothing())

const isEmpty = (x) => x.length && x || undefined
const addOne = (x) => x + 1
const double = (x) => x * 2
const square = (x) => x ** 2

console.log(
  Maybe(5)
    .map(square)
    .map(double)
    .fold(addOne)
)

console.log(
  Maybe([])
    .map(square)
    .map((x) => (console.log(x), x))
    .map(double)
    .map((x) => (console.log(x), x))
    .fold(addOne)
)
