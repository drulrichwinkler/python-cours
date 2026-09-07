# Solution 07 — When is it a tuple?

**a) What the positions mean**

In `("TH-04", 21.7)` the slots are different *fields*: slot 0 is a tag, slot 1 is a
number. Swapping them produces nonsense, and iterating over the pair — doing the
same thing to each entry — is not a question you would ask.

In `[21.7, 22.0, 22.4]` every entry means the same kind of thing. The count is
whatever the data happened to contain, and looping over it is the normal use.

So: a tuple is a record with a fixed shape, a list is a collection of
interchangeable items. That the tuple also happens to be immutable is a consequence
of that, not the definition — a record with fixed fields has nothing to append.

The rule of thumb: if you find yourself writing `if len(t) == 3:` on a tuple, or
appending to it, it should have been a list. If you find yourself remembering that
index 1 is the reading, it should have been a tuple — or, from module 12 on, a
`NamedTuple` or a `@dataclass`, which give the fields names.

**b) Why a list cannot be a key**

A dict stores a key by its hash and looks it up by hashing again. That only works
if the hash never changes for as long as the key is in the dict.

A list can change, and a hash derived from its contents would change with it. The
key would then be filed in one place and looked for in another: the entry is still
there, and no lookup ever finds it again. Rather than let that happen at some
unpredictable later point, Python refuses at the moment you try — `TypeError:
unhashable type: 'list'`.

A tuple of immutable things cannot change, so its hash is stable, so it is a valid
key. That is the whole rule, and module 06 leans on it.

**c) What is immutable about a tuple**

The tuple's **slots**. Once built, no slot can be made to refer to a different
object. Nothing is claimed about the objects themselves, so `mixed[0].append(9)`
succeeds — the slot still refers to the same list, which is now longer.

`hash(mixed)` therefore fails: `TypeError: unhashable type: 'list'`. A tuple hashes
by hashing its contents, so a tuple is hashable only if everything in it is. The
refusal in (b) reaches through.

The precise statement: a tuple is shallowly immutable. Same word, same limit, as the
shallow copy in section 5 of `explore.ipynb`.
