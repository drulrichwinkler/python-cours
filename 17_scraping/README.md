# Module 17 — Scraping

**Assumes:** modules 01–16 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 17_scraping` says whether your exercises are done

## What this is about

Module 16 fetched a file somebody had prepared for a program. This module is what you do when
nobody prepared one: the numbers are in a table on a page, and the page was written for a person.

Two things run through it.

**The technical one:** an HTML parser never fails. It repairs, silently. Section 5 hands the same
three readings to the parser with the closing tags left out — which is legal HTML — and gets back
a first row with **four** cells instead of two, whose first cell reads `TH-0121.7TH-0491.0`. No
exception, a plausible cell count, and unusable data. That is the third time this course has met
that shape, after `latin-1` in module 08 and the missing charset in module 16: **the tool that
cannot fail is the one that hurts you.**

**The other one:** scraping is the only technique in this course with somebody else on the
receiving end. Section 7 is about `robots.txt`, `Crawl-delay`, identifying yourself, and the
three rules that are not about `robots.txt` at all — terms of service, copyright, and personal
data. It is a section, not a footnote.

## What you can do afterwards

1. **pull** the cells of a table out of a page with a CSS selector;
2. **say** what `select_one` returns when nothing matches, and write the check that turns the
   resulting `AttributeError` into a message naming the selector;
3. **explain** why a parser reports nothing about broken HTML, and write the one `if` that
   catches it anyway;
4. **read** a `robots.txt` with the standard library rather than guessing — including the
   prefix-matching rule that makes `Disallow: /admin` cover `/administration`;
5. **resolve** a relative `href` into a URL you can request;
6. **name** what makes a scraper a nuisance, and the five things that stop it being one.

## No network

`server.py` in this folder serves every page in the module, on a free port, as a context
manager — the same shape as module 16's. Its routes are in its docstring, and two of them matter:
`/readings.html` and `/sloppy.html` hold the same readings, one well formed and one not.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 17_scraping`**
4. **`solutions/`** — last

Exercise 09 is the whole module in one file: a crawler that follows a link, checks `robots.txt`
first, identifies itself, verifies the shape of every row, and sleeps between pages.

## Before you scrape anything real

`robots.txt` is a request, not a law, and the law is elsewhere: the terms of service may forbid
automated access whatever `robots.txt` says, the content has a copyright holder, and anything
identifying a person is personal data under the GDPR — for which "it was publicly visible" is
not a legal basis. Section 7 of `explore.ipynb` has the detail and the five-point practical
minimum. Read it before the first time, not after.
