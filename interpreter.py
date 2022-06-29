import sys
import random

random.seed()

def read_program(input):
    program = []
    in_comment = False
    for c in input:
        if c == '#':
            in_comment = True
        elif c == '\n':
            in_comment = False

        if not in_comment and not c.isspace():
            program.append(c)

    return program

def stack_pop(stack):
    try:
        return stack.pop()
    except IndexError:
        return 0

def run_program(program):
    DIGITS = "0123456789ABCDEF"
    prgm = program[:]
    ip = 0
    state = 'c'
    stacks = [[],[]]
    stack_idx = 0
    stack = stacks[stack_idx]
    while ip >= 0 and ip < len(program):
        cmd = prgm[ip]
        # print(f"read {cmd} at {ip} in {state} stack is {stack}")
        if cmd in 'cp':
            state = cmd
            ip += 1
            continue

        if state == 'p':
            stack.append(ord(cmd))
        elif state == 'c':
            if cmd == 's':
                stack_idx = 1 - stack_idx
                stack = stacks[stack_idx]
            elif cmd in DIGITS:
                stack.append(DIGITS.find(cmd))
            elif cmd == '+':
                rhs = stack_pop(stack)
                lhs = stack_pop(stack)
                stack.append(lhs + rhs)
            elif cmd == '-':
                rhs = stack_pop(stack)
                lhs = stack_pop(stack)
                stack.append(lhs - rhs)
            elif cmd == '*':
                rhs = stack_pop(stack)
                lhs = stack_pop(stack)
                stack.append(lhs * rhs)
            elif cmd == '/':
                rhs = stack_pop(stack)
                lhs = stack_pop(stack)
                stack.append(lhs // rhs)
            elif cmd == 'e':
                print(chr(stack_pop(stack)), end='')
            elif cmd == ',':
                in_chr = sys.stdin.read(1)
                if not in_chr:
                    in_chr = chr(0)
                stack.append(ord(in_chr))
            elif cmd == '?':
                cond = stack_pop(stack)
                jmp_idx = stack_pop(stack)
                if cond != 0:
                    ip = jmp_idx - 1 # ip += 1 at end of loop
            elif cmd == ':':
                val = stack_pop(stack)
                stack.append(val)
                stack.append(val)
            elif cmd == '\\':
                top = stack_pop(stack)
                sec = stack_pop(stack)
                stack.append(top)
                stack.append(sec)
            elif cmd == 't':
                val = stack_pop(stack)
                stacks[1 - stack_idx].append(val)
            elif cmd == 'y':
                stack_pop(stack)
            elif cmd == 'z':
                pass
            elif cmd == 'r':
                bound = stack_pop(stack)
                stack.append(random.randrange(bound))
        ip += 1


if len(sys.argv) > 1:
    with open(sys.argv[1], "r") as in_file:
        prog = read_program(in_file.read())

        # for i, el in enumerate(prog):
        #     print(f"{i}: {el}")

        run_program(prog)
        #print()
else:
    text = sys.stdin.read()
    run_program(read_program(text))