from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./src', encoding='utf8'))
template = env.get_template('main.html')

person = {'name': 'Alice'}
l = ['one', 'two', 'three']

html = template.render(user=person, items=l)
# html = template.render({'user': person, 'items': l})

with open('./dst/out.html', 'w') as f:
    f.write(html)
