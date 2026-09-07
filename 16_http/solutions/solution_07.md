# Solution 07 — The guess nobody asked for

**a) Where `ISO-8859-1` came from**

From `requests`, not from the server. HTTP/1.1 as originally specified (RFC 2616)
said that a `text/*` body with no `charset` parameter is ISO-8859-1, and `requests`
still implements that rule. The specification has since been replaced — RFC 7231
dropped the default and RFC 9110 says the charset must be determined some other way —
but the behaviour stayed, because changing it would break callers. See (b).

The third line does not raise because of what module 08 established: Latin-1 maps
**all 256** byte values to characters, one per byte, with no gaps. There is no byte
sequence it can fail to decode, so there is no error case. The two UTF-8 bytes of `°`
come out as the two separate characters `Â` and `°`, and the result is an ordinary
`str` that nothing downstream can tell apart from a correct one.

**b) The four options**

- **Raise.** Honest — the encoding is genuinely unknown. Unusable as a default: every
  program touching a server that omits the header would break, and a great many do.
- **Use UTF-8.** Right almost always in 2026, and wrong loudly rather than quietly
  when it is wrong, because UTF-8 rejects byte sequences that are not valid UTF-8.
  This is what I would choose today for a new library.
- **Run the detector** (`apparent_encoding`). Better answers than either default, and
  it costs a scan of the body and a dependency. It is also a guess that is right most
  of the time, which is the worst failure profile to debug: it works on your data and
  not on the customer's.
- **Follow the old specification.** What `requests` does. Defensible in 2011 and
  indefensible on the merits now.

Who breaks if the default changes: **every caller relying on the current behaviour** —
including code that reads a genuinely Latin-1 body from an old server and works today.
Those programs would start raising `UnicodeDecodeError` on data that has not changed,
which is the one thing a library at that scale cannot do to its users in a minor
release. So the answer is not "requests is wrong", it is "requests is stuck", and the
lesson is that a default chosen early is close to permanent.

**c) Where the two are not interchangeable**

- **When the body is not text.** `.content.decode(...)` on a PNG or a gzip stream is a
  category error you would notice; `.text` on the same bytes produces a long
  meaningless string instead, because Latin-1 cannot refuse.
- **When part of the body is not valid UTF-8**, and this one is the other way round
  from what you would guess. Measured, with `response.encoding = "utf-8"` set:
  `.text` gives `'TH-01;21.7;��'` and **raises nothing at all**, because
  `Response.text` decodes with `errors="replace"` — it is written that way in
  `requests`. `response.content.decode("utf-8")` on the same bytes raises
  `UnicodeDecodeError` and names the position of the bad byte.

  So setting `response.encoding` fixes the encoding and keeps the silence.
  `.content.decode(...)` is the one that can refuse, and `errors="replace"` is then
  something you ask for rather than something you get.
- **When you want the bytes for anything else** — a hash, a byte count, writing them
  straight to a file. `.text` has already thrown the original away.

Which is the general rule and the reason section 3 ends on it: **`.content` is what
arrived; everything else is an interpretation.**
