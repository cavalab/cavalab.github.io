from ruamel.yaml import YAML
yaml=YAML(typ='safe', pure=True) 
import os
import shutil

with open('_data/authors.yml') as f:
    authors = yaml.load(f)

shutil.rmtree('_members')
os.makedirs('_members',exist_ok=True)
page_content = (
"""
{{ site.data.authors[page.author].about }}

{% include pubs_by_author.html given=page.given_name family=page.family_name %}
{% unless pubs_by_author == empty %}
  <h2 class="archive__subtitle">Recent Papers </h2> 
  <div class="entries-list">
    {% for paper in pubs_by_author  limit: 2 %}
      {% include pub-single.html pubid=paper%}
    {% endfor %}
  </div>
{% endunless %}

{% assign posts = site.posts | where: "author", page.author %}
{% unless posts == empty %}
  <h2 class="archive__subtitle">Recent Posts</h2> 
  <div class="entries-list">
    {% for post in posts limit: 2 %}
      {% include archive-single.html type="list" %}
    {% endfor %}
  </div>
{% endunless %}
"""
)
for author, v in authors.items():
    name = v['name'].split(',')[0]
    given_name = name.split(' ')[0]
    family_name = name[len(given_name):]

    page = '\n'.join([
        "---",
        f"title: {name}",
        f"header:\n  teaser: \"{v['avatar']}\"",
        f"author: {author}",
        f"given_name: {given_name}",
        f"family_name: {family_name}",
        "author_profile: true",
        "---\n",
        page_content
    ])
    if author == 'bill':
        page_file = f'_members/01_{family_name.replace(" ","")}-{given_name}.md' 
    else:
        page_file = f'_members/{family_name.replace(" ","")}-{given_name}.md' 

    print('writing',page_file,'...')
    with open(page_file, 'w') as f:
        f.write(page)