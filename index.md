#### myself 
An Engineer , Coder , Builder , Learner 

#### to contact
- Kannappan Natarasan
- kannappan.natarasan@gmail.com
- living in Fremont,CA

#### my projects

- [if AWS is easier to navigate](https://github.com/knatarasan/cloudskin)
- [stock advisor affordable](https://github.com/knatarasan/zenkove)
#### from my thoughts,
<div>
  {% for tag in site.tags %}
    {% unless tag[0] == "wip" %}
      <h3>{{ tag[0] }}</h3>
      <ul>
        {% for post in tag[1] %}
          {% unless post.tags contains "wip" %}
            <li>
              <a href="{{ post.url }}">{{ post.date | date: "%B %Y" }} - {{ post.title }}</a>
            </li>
          {% endunless %}
        {% endfor %}
      </ul>
    {% endunless %}
  {% endfor %}
</div>

<a href="{{ site.url }}/archive.html">-</a>