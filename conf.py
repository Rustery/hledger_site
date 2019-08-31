# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# https://recommonmark.readthedocs.io/en/latest/index.html#autostructify
# https://recommonmark.readthedocs.io/en/latest/auto_structify.html
# This enables additional features of recommonmark syntax
# import recommonmark
# from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = 'hledger'
author = 'Simon Michael'
copyright = '2019, Simon Michael & co.'

# version of the reference manuals (the rest of the docs aren't really versioned)
# version = '1.14'
# release = '1.14'
# version = 'latest (master)'
# release = 'latest (master)'


# -- General configuration ---------------------------------------------------

master_doc = 'sitemap'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # https://recommonmark.readthedocs.io
    'recommonmark',
    # https://github.com/ryanfox/sphinx-markdown-tables
    # https://python-markdown.github.io/extensions/tables
    # https://michelf.ca/projects/php-markdown/extra/#table
    'sphinx_markdown_tables',
    # https://pypi.org/project/sphinx-rtd-theme/
    'sphinx_rtd_theme',
]

# needs_extensions = {
#     'recommonmark': '1.1',
#     'sphinx_markdown_tables': '2.2',
# }

# http://www.sphinx-doc.org/en/master/usage/markdown.html#configuration
# https://spec.commonmark.org
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
#    '.txt': 'markdown',
}

# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-suppress_warnings
suppress_warnings = [
    # 'ref.term',
    # 'ref.ref',
    # 'ref.numref',
    # 'ref.keyword',
    # 'ref.option',
    # 'ref.citation',
    # 'ref.footnote',
    # 'ref.doc',
    # 'ref.python',
    # 'misc.highlighting_failure',
]

# Sphinx gives some bogus warnings about valid references (unless the
# file extension is removed, but then the links would work only when
# rendered by sphinx). Silence them all here, at the cost of also
# hiding invalid ones. (suppress_warnings above doesn't do it.)
# https://stackoverflow.com/questions/37359407/suppress-warnings-for-unfound-references-with-default-role-any-in-sphinx
# WARNING, watch for other side effects
def on_missing_reference(app, env, node, contnode):
    if node['reftype'] == 'any':
        return contnode
    else:
        return None
def setup(app):
    app.connect('missing-reference', on_missing_reference)

# https://recommonmark.readthedocs.io/en/latest/index.html#linking-to-headings-in-other-files
# For linking to headings in other files you can use the autosectionlabel sphinx feature, e.g.
#extensions = [
#     # Auto-generate section labels.
#     'sphinx.ext.autosectionlabel',
#]
# # Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# # rather than 'path/to/file:heading'
#autosectionlabel_prefix_document = True
# You would use it like:
#
# <!-- path/to/file_1.md -->
# # Title
# ## My Subtitle
#
# <!-- file_2.md -->
# [My Subtitle][]
# [My Subtitle]: <path/to/file_1:My Subtitle>

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '_site',
    # exclude the old manual source files for speed
    'doc',
]


# -- Options for HTML output -------------------------------------------------

html_extra_path = [
    # include the old manual's old html as static files
    # '_site/doc',
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add stylesheets to HEAD
html_css_files = [
    # styles for the highslide image zoomer
    'js/highslide/highslide.css',
    # our old custom style overides
    # 'css/style.css',
]

# Add javascript files to HEAD. See also _template/layout.html.
html_js_files = [
    # bootstrap js, I think not used
    # 'js/bootstrap.min.js',
    # highslide image zoomer
    'js/highslide/highslide.js',
    # custom js, currently none
    # 'site.js',
]


# https://recommonmark.readthedocs.io/en/latest/index.html#autostructify
# def setup(app):
#     app.add_config_value('recommonmark_config', {
#             'url_resolver': lambda url: github_doc_root + url,
#             'auto_toc_tree_section': 'Contents',
#             'enable_eval_rst': True,
#             }, True)
    # app.add_transform(AutoStructify)   # IndexError: list index out of range
      # Exception occurred:
      #   File "/usr/local/lib/python3.7/site-packages/docutils/parsers/rst/roles.py", line 356, in math_role
      #     text = rawtext.split('`')[1]
      # IndexError: list index out of range

# AutoStructify comes with the following options:
# enable_auto_toc_tree: enable the Auto Toc Tree feature.
# auto_toc_maxdepth: The max depth of the Auto Toc. Defaults to 1.
# auto_toc_tree_section: when True, Auto Toc Tree will only be enabled on section that matches the title.
# enable_auto_doc_ref: enable the Auto Doc Ref feature. Deprecated
# enable_math: enable the Math Formula feature.
# enable_inline_math: enable the Inline Math feature.
# enable_eval_rst: enable the evaluate embedded reStructuredText feature.
# url_resolver: a function that maps a existing relative position in the document to a http link
# known_url_schemes: a list of url schemes to treat as URLs, schemes not in this list will be assumed to be Sphinx cross-references. Defaults to None, which means treat all URL schemes as URLs. Example: ['http', 'https', 'mailto']

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    # https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',
    # 'logo_only': False,
    'display_version': False,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    'style_nav_header_background': '#343131',
    # Toc options
    # 'collapse_navigation': True,  # hides the + button on other top-level items
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False,
}

# https://docs.readthedocs.io/en/stable/development/design/theme-context.html
# Before calling sphinx-build to render your docs, Read the Docs
# injects some extra context in the templates by using the
# html_context Sphinx setting in the conf.py file. In case you want to
# access to this data from your theme, you can use it like this:
# {% if readthedocs.v1.vcs.type == 'github' %}
#     <a href="https://github.com/{{ readthedocs.v1.vcs.user }}/{{ readthedocs.v1.vcs.repo }}
#     /blob/{{ readthedocs.v1.vcs.version }}{{ readthedocs.v1.vcs.conf_py_path }}{{ pagename }}.rst">
#     Show on GitHub</a>
# {% endif %}
# see also http://www.sphinx-doc.org/en/master/templating.html#global-variables
html_context = {

    # "edit on github" links. XXX currently not correct for the manuals.
    "display_github": True,        # Integrate GitHub
    "github_user": "simonmichael", # Username
    "github_repo": "hledger_site", # Repo name
    "github_version": "master",    # Version
    "conf_py_path": "/",           # Path in the checkout to the docs root
    'vcs_pageview_mode': 'edit',   # not working

    # Config for the versions pane, shown on manuals.
    # cf html_extra_path, exclude_patterns (above).
    'current_version': 'latest (master)',  # '{0}'.format(release),
    'versions': [
        # ( link text, relative url of subdirectory )
        ('latest' ,'.'),
        # ('1.14'   ,'1.14'),
        # ('1.13'   ,'1.13'),
        # ('1.12'   ,'1.12'),
        # ('1.11'   ,'1.11'),
        # ('1.10'   ,'1.10'),
        # ('1.9'    ,'1.9'),
        # ('1.5'    ,'1.5'),
        # ('1.4'    ,'1.4'),
        # ('1.3'    ,'1.3'),
        # ('1.2'    ,'1.2'),
        # ('1.1'    ,'1.1'),
        # ('1.0'    ,'1.0'),
    ]
    # 'languages':
    #     [('en', 'English'),
    #      ('fr', 'Français'),
    #      ('it', 'Italiano'),
    #      ('es', "Español"),
    #      ('pt', "Português"),
    #      ('pt_BR', 'Português do Brasil'),
    #      ('de', 'Deutsch'),
    #      ('nb_NO', 'Bokmål'),
    #      ('es', 'Español'),
    #      ('ru', 'русский'),
    #      ('ja', '日本語'),
    #      ('zh', '中文'),
    #     ],
    # 'downloads':
    #     [('pdf',
    #       'https://manual.zrythm.org/en/Zrythm.pdf'),
    #      ('htmlzip',
    #       'https://www.zrythm.org'),
    #      ('epub',
    #       'https://www.zrythm.org'),
    #     ]

}

# https://docs.readthedocs.io/en/stable/index.html
# https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/demo.html  paragraph level markup
# https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/lists_tables.html  lists & tables

# html_short_title = 'hledger'
# html_baseurl = '/index.html'
# html_logo = '_static/images/coins2-248.png'
html_last_updated_fmt = ''
#html_show_sphinx = False


# -- Pygments highlighting tweaks ---------------------------------------

# define some custom pygments highlighters for literal blocks
# https://stackoverflow.com/questions/16469869/custom-syntax-highlighting-with-sphinx
# http://pygments.org/docs/lexerdevelopment
# http://pygments.org/docs/tokens/

from sphinx.highlighting import lexers
from pygments.lexer import RegexLexer
from pygments.token import *

datere = r'(\d\d\d\d[.-/])?\d\d?[.-/]\d\d?'

# journal format.
class JournalLexer(RegexLexer):
    tokens = {
        'root': [
            (datere+'(='+datere+')?', Keyword.Declaration),
            (r'.*\n', Text),
        ]
    }
lexers['journal'] = lexers['{.journal}'] = JournalLexer(startinline=True)

# transcript of a shell session. lines beginning with $ are commands
class ShellLexer(RegexLexer):
    tokens = {
        'root': [
            (r'^\$ [^#\n]*', Generic.Prompt),
            (r'.*\n', Text),
        ]
    }
lexers['shell'] = lexers['{.shell}'] = ShellLexer(startinline=True)

# silence warnings about these other kinds of literal block

for l in [
    'timeclock',
    'timedot',
    'csv',
    'rules',
    'haskell',
    'hledger',
    'example',
  ]:
    class NullLexer(RegexLexer):
        name = l
        tokens = {
            'root': [
                (r'.*\n', Text),
            ] }
    lexers[l] = lexers['{.'+l+'}'] = NullLexer(startinline=True)
lexers['{.rules .display-table}'] = NullLexer(startinline=True)


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#     ('hledger', 'hledger', u'a command-line accounting tool',
#      [author], 1)
# ]

# If true, show URL addresses after external links.
# man_show_urls = False
