Wanted to share my typical days.

I'm Tech Co-founder | Coder | Product Builder.

Wanted to share my 0 to 1 experience

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
