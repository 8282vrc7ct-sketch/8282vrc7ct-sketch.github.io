# LEARN: what changed in the website (finish v1)

## What changed and why

1. **The README now tells the truth.** It used to say the site was not online yet. It is: https://8282vrc7ct-sketch.github.io/. The README now says how GitHub Pages serves it from the `main` branch.
2. **One broken link was removed.** The "First JSON file (data-lab)" card linked to a `data-lab` repo that GitHub can't find (it returns "404 not found"). A visitor clicking it would hit an error page, so the card now has no link, like the other private projects.
3. **The menu wraps on small screens.** `nav` is now a flexbox that can wrap, and on phones the text is a little smaller. On a 375-pixel-wide phone screen the page no longer needs side-scrolling.
4. **A page checker was added.** `check_site.py` reads `index.html` and prints PASS or FAIL for five checks. `test_check_site.py` proves the checker can fail when the page is broken.

## New words
- **404**: the web's "page not found" error.
- **flexbox**: a CSS layout that lines items up in a row and can wrap them onto a new line.
- **media query**: a CSS rule that only applies on some screens, like `@media (max-width: 500px)` for phones.
- **parser**: code that reads text and splits it into parts it understands (here, HTML tags).
- **void tag**: a tag that never closes, like `<meta>` or `<br>`.
- **unit test**: a tiny program that checks one piece of code gives the right answer.

## How the checker works, in short
```
index.html --> PageReader (reads every tag) --> run_checks() --> PASS / FAIL lines
```
`PageReader` keeps a list of tags that are open. Each closing tag must match the last open one. Anything left open at the end is reported with its line number.

## Try this yourself
1. **Change the tagline.** In `index.html`, find `class="tagline"`. Change the words between `>` and `<`. Save, reload the page, and see your new line under your name.
2. **Break it on purpose.** Delete the `</section>` that closes the About section. Run `python3 check_site.py`. You should see `FAIL  tags close` with a line number. Put the tag back and run it again until all 5 checks pass.
3. **Add a card.** Copy one `<article class="card">...</article>` block, give it a new title and sentence, and save. Then in `style.css`, change `--accent` to another color (for example `#f59e0b`) and reload. Every heading and link changes at once, because they all use that one color variable.
