# Solution 08 — When scraping is the wrong tool

**a) Three things to check first**

1. **Is the data in the HTML at all?** `"21.7" in response.text`. One line, and it
   decides whether a scraper is even possible — if the table is built by JavaScript,
   everything you write next is wasted. Saves you an afternoon.
2. **Is there a published API, and what does `robots.txt` say?** An API is better than
   scraping in every respect: typed, documented by its shape, stable across
   redesigns, and usually explicitly permitted. `robots.txt` may also settle the
   question in the other direction. Saves you the scraper entirely.
3. **Is anyone allowed to ask?** The site's terms of service, and — for anything at a
   university or a company — whoever owns the relationship with that site. This is the
   one you cannot answer from your desk, and it is the one that turns into a problem
   for somebody other than you. Saves you an awkward email.

The order matters: (1) is free, (2) is cheap, (3) takes a day and is the only one with
consequences you cannot undo.

**b) The table is built by JavaScript**

The three options from section 6:

1. **Find the API the page itself uses** — watch the browser's network tab.
2. **Look for a published API.**
3. **Drive a real browser** — Playwright or Selenium.

I would take (1), and it is worth trying before (3) almost every time. The reasoning:
if the page builds its table from a fetch, that endpoint exists, returns JSON, and is
the same data without the HTML in the way. It is module 16 rather than module 17 —
`response.json()`, typed values, no selectors to break on a redesign. (3) costs a
browser process per scrape and a much more fragile setup, and it is what you fall back
to when the endpoint needs a session the browser establishes in ways you cannot
reproduce.

**If the network tab shows `/api/readings.json`:** fetch that, with module 16. But
note what does *not* change — **`robots.txt` still applies**, and it applies to that
path. A `Disallow: /api/` covers it, and the fact that a browser fetched it for you
does not make it permitted for your script. The rules are about who is asking, not
about which format comes back. Check `can_fetch` on the URL you are actually going to
request.

**c) Six weeks, then empty lists**

The two likely causes, and they look identical from your end:

1. **The page was redesigned.** The class or the id you select on is gone or renamed,
   so `select("tr.row")` matches nothing and the loop body never runs. An empty list
   comes back, and every hour it comes back again.
2. **You are being blocked or served something else** — a 403, a consent page, a
   CAPTCHA, a "we noticed unusual traffic" interstitial. The request succeeded, the
   HTML arrived, and it is not the page you think you are parsing.

The line that would have caught both, on the first run:

```python
table = soup.select_one("#readings")
if table is None:
    raise ScrapeError("no #readings table -- has the page changed?")
```

That is exactly the check from section 2 and exercise 03, and it is the line this
module writes twice. It converts "empty list, no message, for six weeks" into a
failure on week one that names what is missing — and an hourly job that raises is a job
somebody notices.

A second line, for the case where the table is there and the rows are not what you
expect, is the cell-count check from section 5. Between them they cover both causes:
one catches "the page is not the page", the other catches "the page is the page and
the parser guessed".

The general point, and it is why this exercise exists: **a scraper's normal failure
mode is returning nothing, successfully.** Every other program in this course fails by
raising. This one fails by agreeing with you, which means the checks have to be written
by hand and written up front.
