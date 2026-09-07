# Solution 08 — When you have outgrown it

**a) The three things, and a request each**

**The markup.** *"Can you put our logo in the header and make the table match the rest
of the site?"* You cannot, not properly. There is a theme with a handful of colours,
and `st.markdown(..., unsafe_allow_html=True)` — which is module 21's `|safe` with a
more honest name, and which fights the framework's own layout. What you would do:
accept the Streamlit look, or move the page to Flask.

**The URLs.** *"Bookmark me the page for the test rig and send me the link."* There is
one page. Query parameters (`st.query_params`) let you fake it, and the multipage
directory convention gives you `/Faults` and `/Sensors`, but you do not design the
URL space and you cannot have `/location/Hall`. What you would do: use query
parameters and read them at the top of the script — workable, and visibly a
workaround.

**The request cycle.** *"Show a progress bar while the 200 MB file uploads, and let me
cancel it."* The script runs to completion and then the page appears; there is no
"during". `st.progress` and `st.status` update as the script runs, which covers a long
computation but not a cancel — there is nothing to cancel, because there is no request
in flight that you control. What you would do: for cancellation, a different framework.

**b) The four cases**

1. **A dashboard for your team, last night's test results — Streamlit.** The point is
   the data, the audience is colleagues, and the whole thing is an afternoon. Nobody
   will ask for a logo.
2. **A public page where customers look up a serial number — Flask (or Django).** The
   point is the page: it needs a URL a customer can be sent, it will need to look like
   the company's site, and it is public, which brings caching, SEO and load. All three
   are things Streamlit does not do.
3. **An internal tool where somebody edits the sensor list — Django.** "Edits" is the
   word that decides it: this is create/read/update/delete over a table, with
   validation and an audit trail, which is what Django's admin is. Streamlit can build
   forms, but you would be writing the admin interface by hand.
4. **A page embedded in the intranet's existing layout — Flask.** "Embedded in an
   existing layout" is a requirement about markup, and markup is exactly what
   Streamlit does not give you. An iframe is the Streamlit answer, and it is visible as
   one.

The pattern: **Streamlit wins whenever the reader is a colleague and the subject is
numbers.** It loses as soon as somebody outside that circle has an opinion about the
page.

**c) Three departments, and now a login**

Options, in the order I would consider them:

1. **Put it behind something that already does authentication** — the company's
   single sign-on via a reverse proxy, a VPN, or an OAuth proxy in front of the app.
   The app does not change at all, and the login is handled by something built for it.
2. **Streamlit's own authentication** (`st.login`, via OIDC), which exists and is
   reasonable for exactly this case: one identity provider, and no per-user
   authorisation logic.
3. **Roll your own** with a password box and `session_state`. Fast, and wrong: the
   secret would be compared in your code, `session_state` is per-tab server memory,
   and there is no session expiry, no password reset and no audit.
4. **Rewrite in Flask or Django**, where login is a solved and well-attacked problem.

**I would take (1).** Authentication is the thing you least want to have written
yourself, three departments implies a directory already exists, and a proxy does not
touch the app — so the afternoon that produced the app is not spent again.

Where (1) is not available, (2). Where the requirement is not just "who are you" but
"what may you see", **(4)**: per-user authorisation means the app has to know about
roles at every point, and that is application structure rather than a login box.

**d) Where the model does not fit**

**Anything that has to happen while nobody is interacting.**

The re-run model has no place to put such a thing: the script runs *because* a user
did something, and between interactions there is no script running at all. So:

- an alarm that must fire within thirty seconds of a reading exceeding the limit,
  whether or not the page is open;
- a nightly job that writes a report;
- anything that has to react to an incoming message, a webhook, or another service.

None of those is slow in Streamlit — they are **inexpressible** in it, which is the
distinction the question asks for. `st.fragment(run_every=...)` and autorefresh
components make the page poll while it is open, which is a different requirement: it
still needs somebody to have the tab open.

The right shape for those is what Part 4 already built: a **script** (module 10) run
by a scheduler, writing to a database (module 19) — and then, if a person wants to look
at the result, a Streamlit page on top of it. The two are not competing; the mistake is
asking the page to be the program.
