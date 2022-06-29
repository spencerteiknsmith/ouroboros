# Ouroboros
## Introduction
Ouroboros, named after the mythical creature, is an esolang designed such that any Ouroboros program can be fed a Ouroboros program, and produce a valid Ouroboros program as a result.

### General Description of Ouroboros
With one exception, each character in an Ouroboros program is read individually.

Ouroboros is primarily a stack-based language (like so many esolangs).

Ouroboros has multiple operation states. The current operation state of a program affects the interpretation of each character.

## Language Features
### Program Description
Once loaded, programs are stored as a zero-indexed array of characters.

Generally, every individual character in an input program is read directly into the program array, with the following exceptions:
- All whitespace is ignored (tabs, spaces, newlines, and carriage returns)
- If an octothorpe (`#`) is encountered, it and all following characters until the next newline are ignored

### Instruction Pointer
Ouroboros has an instruction pointer (IP) that begins at the first character in the program and starts moving left to right. The IP interprets each character individually as it reads them. Some commands cause the IP to move non-linearly. A program terminates when the IP moves out of the bounds of the program array.

### The Stacks
Ouroboros programs have access to two stacks that can hold integers. The stacks are treated as if initialized with an endless supply of 0s.

### Operation States
Ouroboros has multiple operation states, which can be switched into via certain commands. Programs begin in the command state.
#### Command state
Characters will be interpreted as commands and executed. Non-command characters will be passed over.
#### Push state
The ascii values of characters encountered will be pushed onto the stack, with the exception of state-switching character commands.

### Commands
- `c`: enter command state
- `p`: enter push state
- `s`: switch active stack
- `[0-9]`: push the digit on the stack
- `[A-F]`: push the hex value on the stack
- `+`: add top two elements on the stack and push the result
- `-`: subtract in like manner
- `*`: multiply in like manner
- `/`: divide in like manner, using integer division
- `e`: pop and print the top of the stack to stdout, interpreting numbers as ascii values of characters to print.
- `,`: read a character from stdin and store it's ascii value on the stack. If no character is available, push a 0.
- `?`: pop the top of the stack as the condition, and the next value as the jump index. If the condition is non-zero, move the instruction pointer to the jump index
- `:`: pop the top of the stack and push two copies of it back
- `\`: pop the top two elements of the stack and put them back in reverse order
- `t`: pop the top of the stack and push it to the other stack
- `y`: yeet the top of the stack
- `z`: do nothing (the default behavior for unknown commands, but this character is reserved)
- `r`: pop the top of the stack as `b`, and push a random number between `[0,b)`

## Possible Programs to Implement
The cool thing is that the output of a program can then be input to another program, or run as a program itself. Some fun adventures could be had in creating programs with special features.

### Notation
It will be helpful to use a function-like notation to describe Ouroboros programs. We define `p(i) = o` to mean that an Ouroboros program `p`, when fed input `i`, produces output `o`

### Special Programs
1. `p | ∀x(p(x) = x)`                           pretty easy
2. `p | p(p) = p`                               1. works, but the more complex `p` is the better - in particular, if `p` actually uses its input
3. `p | ∀x((x ∈ X) -> (p(x) = y and p(y) = x))` 1. works again (and makes `X = Σ*`), but can it be that `x != y`? And if so then maximize `X`
4. `p | p(*) = y and y(*) = p`                  should be relatively easy (`p` and `y` can each ignore input)
5. `p | ∀x(p(x) = y and y(*) = x)`              a little harder, but not bad (`y` can ignore its input)
7. `p | ∀x((x ∈ X) -> (p(x) = y and x(y) = p))` much much harder - try to maximize `X` - the only solutions might be trivial
8. `p | ∀x((x ∈ X) -> (p(x) = y and x(y) = y))` similar to 7.
9. `p | ∀x((x ∈ X) -> (p(x) = y and x(y) = x))` again, similar to 7.
10. `p | ∀x((x ∈ X) -> (p(x) = y and x(p) = y))`basically, `p` simulates its input running on itself
11. given a series of programs `x0, x1, ... xn`, `p | p(xn) = xn+1` fairly trivial (recognize input and switch to correct hard-coded production unit)
12. `p | p('|'.join(xs)) = s and s(xn) = xn+1 | xs=x0, x1, ... xn`  a little trickier (hopefully you read python)
13. `p | ∀i∀j((i∈ℤ and j∈ℤ and i!=j) -> p^i(x) != p^j(x)`           can you guarantee this to infinity?
14. `p` where repeated applications of `p` on an interesting input produces aesthetically pleasing results
