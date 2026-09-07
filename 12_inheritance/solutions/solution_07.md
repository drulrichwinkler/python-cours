# Solution 07 — `super()` is not your parent

**a) What `super()` looks up**

The **next class after the current one in the MRO of the object's type**. Not the
class in the brackets after `class B(...)`.

`super()` has two pieces of information: the class the call is written in (`B`) and
the object (`self`). It takes `type(self).__mro__`, finds `B` in it, and looks for
the attribute in everything after that point. So the line is resolved against a list
that belongs to the object, not to `B` — and that list lives on the class that was
constructed.

`D.__mro__` is `(D, B, C, A, object)`. `B` is at index 1, so `super().who()` inside
`B.who` searches `C`, then `A`. For a `B()` the MRO is `(B, A, object)` and the same
line searches `A`.

**b) A change in `D` alters a line in `B`**

Writing `class D(B, C)` produces an MRO in which `C` sits between `B` and `A`. From
that moment on, the `super()` call inside `B.who` reaches `C` whenever the object is a
`D` — although `B` does not inherit from `C`, does not import it, and was written
before it existed.

For reading unfamiliar code that means: **`super()` in a class with more than one
possible subclass is not resolvable from the file you are looking at.** To know what
the line does you need the type of the object at run time and that type's MRO. In
practice: find the concrete class, print `Cls.__mro__`, and read from there.

That is also the argument against deep hierarchies in Python. The mechanism is more
powerful than Java's and correspondingly less local.

**c) What cooperative multiple inheritance buys, and its condition**

It buys **mixins that compose**. Each class does its piece and delegates the rest,
and the class at the bottom decides the order by listing its bases — so behaviour can
be assembled without any of the pieces knowing about the others. Java cannot do this
with classes at all; it needs interfaces with default methods, and then makes you
resolve the conflicts by hand.

The condition: **every class in the chain must call `super()`**, and they must accept
compatible arguments. One that does not call it silently ends the chain.

```python
class Uncooperative(A):
    def who(self):
        return "U"                    # no super() call


class D(B, Uncooperative, C):
    pass


D().who()      # 'B->U'  -- C.who never ran, and nothing said so
```

`C` is in the MRO, `C.who` exists, and it was skipped. There is no error and no
warning; the result is simply missing a piece. That is the failure mode to fear, and
it is why `super()` in an overriding method is close to mandatory even when it looks
pointless.

A second thing that can go wrong is structural: some base orders have no consistent
MRO at all, and Python refuses at class-creation time — `TypeError: Cannot create a
consistent method resolution order (MRO) for bases A, C`. That one at least is loud.
