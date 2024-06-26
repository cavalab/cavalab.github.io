from ruamel.yaml import YAML
yaml=YAML(typ='safe', pure=True) 
import os

with open('_data/authors.yml') as f:
    authors = yaml.load(f)

os.makedirs('_members',exist_ok=True)

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
        "{{ site.data.authors[page.author].about }}"
    ])
    if author == 'bill':
        page_file = f'_members/01_{family_name.replace(" ","")}-{given_name}.md' 
    else:
        page_file = f'_members/{family_name.replace(" ","")}-{given_name}.md' 

    print('writing',page_file,'...')
    with open(page_file, 'w') as f:
        f.write(page)