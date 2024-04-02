# Cava lab website

This is the code for the (cavalab.org) website. 

# How to add yourself

1. Fork this repo and make a new branch.
2. Add a **square** profile picture **less than 200 KB** to `assets/images/` named something like `last-name-first-name.png`.
3. Make a new file named `last-name-first-name.md` in the `_members` folder with a header and bio following [this example](https://raw.githubusercontent.com/cavalab/cavalab.github.io/gh-pages/_members/01_lacava-william.md)
4. edit `_data/authors.yml` to add an entry for yourself, for example:

```yaml
bill:
  name: "William La Cava, PhD"
  avatar: "assets/images/profile_pic_small.JPG"
  bio: "Principal Investigator"
  links:
    - label: "Email"
      icon: "fas fa-fw fa-envelope"
      url: "mailto:william.lacava@childrens.harvard.edu"
    - label: Website
      icon: &personal "fas fa-user"
      url: "http://williamlacava.com"
    - label: Google Scholar
      icon: &scholar "fas fa-graduation-cap"
      url: "https://scholar.google.com/citations?user=iZB7inEAAAAJ&hl=en"
    - label: Github
      icon: &github "fab fa-fw fa-github"
      url: "https://github.com/lacava"
    - label: Twitter
      icon: &twitter "fab fa-twitter"
      url: "https://www.twitter.com/w_la_cava"
    - label: LinkedIn
      icon: &linkedin "fab fa-linkedin" 
      url: "https://www.linkedin.com/in/williamlacava/"
```

For the links, you just have to change the `url` field. 
You can also remove any you don't want. 

5. Commit your changes, push to your fork, and [open a PR on this repo](https://github.com/cavalab/cavalab.github.io/compare).