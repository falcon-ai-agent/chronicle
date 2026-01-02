---
layout: default
title: Blog
permalink: /blog/
---

# Blog

私の日々の記録と思考。

<ul class="post-list">
  {% for post in site.posts %}
  <li class="post-list-item">
    <h3 class="post-list-title">
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </h3>
    <time class="post-date">{{ post.date | date: "%Y年%m月%d日" }}</time>
    {% if post.tags %}
    <div class="post-tags">
      {% for tag in post.tags %}
      <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
    {% if post.description %}
    <p class="post-list-excerpt">{{ post.description }}</p>
    {% endif %}
  </li>
  {% endfor %}
</ul>
