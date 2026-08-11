# Cava lab website

This is the code for the https://cavalab.org website. 

# How to add yourself

1. [Fork this repo](https://github.com/cavalab/cavalab.github.io/fork).
2. Add a **square** profile picture **less than 200 KB** to `assets/images/` named something like `last-name-first-name.png`.
3. edit `_data/authors.yml` to add an entry for yourself. 
For the links, you just have to change the `url` field. 
You can also remove any you don't want.  for example:

```yaml
myname:
  name: "My Name, MD PhD"
  avatar: "assets/images/last-name-first-name.png"
  bio: "Postdoctoral Fellow"
  links:
    - label: "Email"
      icon: "fas fa-fw fa-envelope"
      url: "mailto:my.email@childrens.harvard.edu"
    - label: Website
      icon: &personal "fas fa-user"
      url: "http://personal-website.com"
    - label: Google Scholar
      icon: &scholar "fas fa-graduation-cap"
      url: "https://scholar.google.com/citations?user=me&hl=en"
    - label: Github
      icon: &github "fab fa-fw fa-github"
      url: "https://github.com/me"
    - label: Twitter
      icon: &twitter "fab fa-twitter"
      url: "https://www.twitter.com/me"
    - label: LinkedIn
      icon: &linkedin "fab fa-linkedin" 
      url: "https://www.linkedin.com/in/me/"
  about: |
    My Name is a Postdoctoral Fellow interested in improving the world.
    They receieved their MD from such and such school yada yada yada. 
```


5. Commit your changes, push to your fork, and [open a PR on this repo](https://github.com/cavalab/cavalab.github.io/compare).

# Publication PDF check (one-time setup)

A pre-commit hook verifies that every publication in `_data/publications.yaml`
has a matching PDF in `assets/papers/`, so a new paper never gets added to
the bibliography without its PDF. To activate it locally:

```bash
pip install -r scripts/requirements.txt
git config core.hooksPath .githooks
```

If a PDF is missing, the hook automatically searches your local Zotero
storage (`~/Zotero/storage`) for a matching file and copies over any
unambiguous match — review what it copied, then `git add` it and commit
again. Run it manually any time with:

```bash
python3 scripts/check_publication_pdfs.py    # list what's missing
python3 scripts/find_missing_pdfs.py --copy  # try to fill gaps from Zotero
```
