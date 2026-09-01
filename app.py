import os
import re
import markdown
import yaml
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
ARTICLES_DIR = os.path.join(os.path.dirname(__file__), 'articles')

# 博客分类定义（顺序即展示顺序）
CATEGORIES = [
    {"slug": "claude-code", "name": "Claude Code", "description": "Claude Code 使用经验与相关资源"},
    {"slug": "skills", "name": "Skills", "description": "常用的 Skills 介绍"},
    {"slug": "tools", "name": "Tools", "description": "实用工具与效率工具介绍"},
    {"slug": "agent", "name": "Agent", "description": "AI 协作业面与 Agent"},
]

# 子分类定义（顺序即展示顺序），目前仅 skills 分类使用
SUBCATEGORIES = ["总览", "总调度", "Skill 制造", "通用技能", "记忆"]


def get_category(slug):
    for c in CATEGORIES:
        if c['slug'] == slug:
            return c
    return None


def get_articles_by_category(cat_slug):
    articles = get_all_articles()
    return [(s, m) for s, m in articles if m.get('category') == cat_slug]


def group_by_subcategory(articles):
    """把文章按 subcategory 分组，返回 [{name, articles}, ...]。
    无 subcategory 的文章归入 name 为 None 的组。"""
    groups = {}
    ungrouped = []
    for s, m in articles:
        sub = m.get('subcategory')
        if sub:
            groups.setdefault(sub, []).append((s, m))
        else:
            ungrouped.append((s, m))
    result = []
    for name in SUBCATEGORIES:
        if name in groups:
            result.append({'name': name, 'articles': groups[name]})
    if ungrouped:
        result.append({'name': None, 'articles': ungrouped})
    return result


@app.context_processor
def inject_categories():
    return {'nav_categories': CATEGORIES}


def parse_article(filepath):
    """解析 .md 文件，返回 (meta, html_content)"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 YAML front matter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if match:
        meta = yaml.safe_load(match.group(1))
        body = match.group(2)
    else:
        meta = {'title': os.path.splitext(os.path.basename(filepath))[0]}
        body = content

    html = markdown.markdown(
        body,
        extensions=['fenced_code', 'codehilite', 'tables']
    )
    return meta, html


def get_all_articles():
    """返回按编号排序的文章列表 [(slug, meta), ...]"""
    articles = []
    for fname in sorted(os.listdir(ARTICLES_DIR)):
        if not fname.endswith('.md'):
            continue
        slug = fname[:-3]
        meta, _ = parse_article(os.path.join(ARTICLES_DIR, fname))
        meta.setdefault('date', '')
        articles.append((slug, meta))

    return articles


@app.route('/')
def index():
    categories = []
    for c in CATEGORIES:
        arts = get_articles_by_category(c['slug'])
        groups = group_by_subcategory(arts)
        # 是否有具名子分类（只有 skills 有，其余分类无 subcategory）
        has_sub = any(g['name'] for g in groups)
        categories.append({**c, 'articles': arts, 'groups': groups, 'has_sub': has_sub})
    return render_template('index.html', categories=categories)


@app.route('/category/<slug>')
def category(slug):
    cat = get_category(slug)
    if not cat:
        return render_template('category.html', category={'name': '未找到', 'slug': slug}, groups=[]), 404
    articles = get_articles_by_category(slug)
    groups = group_by_subcategory(articles)
    return render_template('category.html', category=cat, groups=groups)


@app.route('/article/<slug>')
def article(slug):
    filepath = os.path.join(ARTICLES_DIR, f'{slug}.md')
    if not os.path.exists(filepath):
        return render_template('article.html', meta={'title': '未找到'}, content='<p>文章不存在</p>'), 404
    meta, content = parse_article(filepath)
    return render_template('article.html', meta=meta, content=content)


@app.route('/admin')
def admin():
    articles = get_all_articles()
    return render_template('admin.html', articles=articles, edit_slug=None, edit_meta=None, edit_content='', categories=CATEGORIES)


@app.route('/admin/new', methods=['GET', 'POST'])
def admin_new():
    if request.method == 'POST':
        title = request.form['title']
        md_content = request.form['content']
        summary = request.form.get('summary', '')
        category = request.form.get('category', 'claude-code')
        slug = re.sub(r'[^a-z0-9一-鿿-]+', '-', title.lower()).strip('-')
        front_matter = f'---\ntitle: {title}\ndate: 2026-05-12\ncategory: {category}\nsummary: {summary}\n---\n\n'
        filepath = os.path.join(ARTICLES_DIR, f'{slug}.md')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(front_matter + md_content)
        return redirect(url_for('admin'))
    return render_template('admin.html', articles=get_all_articles(),
                           edit_slug=None, edit_meta=None, edit_content='', edit_mode='new', categories=CATEGORIES)


@app.route('/admin/edit/<slug>', methods=['GET', 'POST'])
def admin_edit(slug):
    filepath = os.path.join(ARTICLES_DIR, f'{slug}.md')
    if not os.path.exists(filepath):
        return redirect(url_for('admin'))

    if request.method == 'POST':
        title = request.form['title']
        md_content = request.form['content']
        summary = request.form.get('summary', '')
        category = request.form.get('category', meta.get('category', 'claude-code'))
        front_matter = f'---\ntitle: {title}\ndate: 2026-05-12\ncategory: {category}\nsummary: {summary}\n---\n\n'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(front_matter + md_content)
        return redirect(url_for('admin'))

    meta, content = parse_article(filepath)
    return render_template('admin.html', articles=get_all_articles(),
                           edit_slug=slug, edit_meta=meta, edit_content=content, edit_mode='edit', categories=CATEGORIES)


@app.route('/admin/delete/<slug>', methods=['POST'])
def admin_delete(slug):
    filepath = os.path.join(ARTICLES_DIR, f'{slug}.md')
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)
