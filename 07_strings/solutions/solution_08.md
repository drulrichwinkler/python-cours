# Solution 08 — What is the length of a string?

**a) Three questions**

- `len("TH-04")` → **5 code points.** For ASCII, this is also the character count
  and the byte count, which is why the difference stays invisible until it matters.
- `len("Übergabe")` → **8 code points.** Still one number per character here.
- `len("Übergabe".encode("utf-8"))` → **9 bytes.** This one is not about the text at
  all. It is about a particular *encoding* of the text, and it would be 16 or 18
  bytes in UTF-16. It answers "how much room does this take in a file or on a
  socket", not "how long is this".

**b) The missing byte**

It never existed as a separate character. `Ü` is one code point, and UTF-8 spends
**two** bytes on it, because UTF-8 uses one byte only for the first 128 code points.
Eight characters, nine bytes.

What had to be known for the conversion: **the encoding.** Bytes on their own do not
say how to be read; `b"\xc3\x9c"` is `Ü` in UTF-8 and two separate junk characters in
Latin-1. There is no reliable default across systems: `open()` without `encoding=` asks the
operating system, which is where "works on my machine" comes from. PEP 686 will make
UTF-8 the default in a future version — until then, and for anything that has to run
on an older one, naming it as `encoding="utf-8"` (module 08) is how you stop
guessing.

**c) Both sides of the trade**

Harder in Java: anything that counts or indexes characters outside the basic plane.
`"👍".length()` is 2, `charAt(0)` gives you half a character, and reversing a string
by index corrupts it. Java added `codePointCount` and `codePoints()` for exactly
this, and code written before them is quietly wrong on emoji and on several living
scripts.

Harder in Python — the honest other half: a code point is still not a character on
screen. `é` can be one code point or two, `e` plus a combining accent; the two look
identical, `len` says 1 and 2, and `==` says they are different strings.
`unicodedata.normalize` is the tool. A thumbs-up with a skin tone is 2 code points,
a family emoji 5, and all of them are one thing the user sees.

So `len` counts code points reliably and characters only approximately. When the
question is really "how wide is this on screen", neither language answers it with
`len`.
