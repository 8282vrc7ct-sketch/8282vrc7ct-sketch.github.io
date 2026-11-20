# 8282vrc7ct-sketch.github.io

## What this is
Jonah's personal website: one page with About, Projects and Contact sections, built with plain HTML and CSS.

It is live at **https://8282vrc7ct-sketch.github.io/**

## How it gets online
GitHub Pages serves this repo straight from the `main` branch, root folder (`/`). Whenever a change is merged into `main`, GitHub rebuilds the site and the live page updates within a minute or two. There is no build step: the files you see here are the files the browser gets.

## Run it on your Mac
In a Terminal tab in this folder:

```bash
open index.html
```

Your browser shows the page from your own files. Only you see this copy, so it is a safe place to try changes before they go to `main`.

## Test it
One command checks the page:

```bash
python3 check_site.py
```

It prints `PASS` or `FAIL` for each of these:
- the About, Projects and Contact sections exist;
- the top menu links jump to those sections;
- every tag that opens also closes;
- the phone "viewport" tag is there, so the page fits a phone screen;
- "View code" links point only at public repos (private repos would show visitors a login wall).

The checker has its own tests:

```bash
python3 -m unittest -v
```

Hand check: open the page, click About, Projects and Contact, and make the browser window narrow. Then open the live URL and confirm it matches.

## What's in this folder
- `index.html`: the words and sections of the page.
- `style.css`: colors, fonts and spacing.
- `check_site.py`: the page checker.
- `test_check_site.py`: tests for the checker.
- `LEARN.md`: what changed and why, plus exercises.

## Project cards and links
Only public repos get a "View code" link. Right now that is this website's own repo. The other projects are private, so their cards have no link. If you make a repo public later, add its name to `PUBLIC_REPOS` in `check_site.py` and then add the link.

## Words to know
- **tag**: a label in angle brackets, like `<h1>`, that says what a piece of the page is.
- **stylesheet**: the CSS file that sets how the page looks.
- **GitHub Pages**: a free GitHub service that puts a repo like this online.
- **local**: on your own computer, not on the internet.
- **viewport**: the visible area of the screen; the viewport tag tells phones not to zoom out.
