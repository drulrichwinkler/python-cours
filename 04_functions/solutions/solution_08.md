# Solution 08 — What a closure captures

**a) The variable**

`tick` captures the variable `count`, not the value it held when the closure was
built. Both calls see and update the same binding, which is why `counter()`
returns `2`.

**b) Without `nonlocal`**

```
UnboundLocalError: cannot access local variable 'count' where it is not
associated with a value
```

The error is about *reading*, and the line looks like a write — which is the
point. Python decides at compile time whether a name is local to a function, and
the rule is: if a function assigns to a name anywhere in its body, that name is
local to the whole function. `count += 1` is an assignment, so `count` is local
throughout `tick` — including on the right-hand side, where it is read before
anything has been stored in it.

`nonlocal count` overrides that decision and points the name at the enclosing
function's binding. `global` does the same for module level.

**c) No effectively-final restriction**

**Possible:** a closure that accumulates. Counters, running totals, memo caches
and callbacks that update shared state need no wrapper object — the enclosing
function's local variable *is* the state. In Java the same thing needs a field, an
array of length one, or an `AtomicInteger`.

**Easy to get wrong:** closures created in a loop all share the loop variable, so
they all see its final value.

```python
handlers = [lambda: print(i) for i in range(3)]
for h in handlers:
    h()          # 2, 2, 2 -- not 0, 1, 2
```

The fix is to bind the value at creation time, usually with a default argument:
`lambda i=i: print(i)`. Java's restriction exists precisely to make this class of
bug impossible; Python trades it for the accumulator above.
