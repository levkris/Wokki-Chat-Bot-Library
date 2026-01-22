*To contribute to the code, send a pull request,
this file only tells you how to contribute to the docs.*

# Docs walkthrough
Want to contribute to the docs? Amazing!

We use [pdoc](https://pdoc.dev/docs/pdoc.html) for the Python SDK
to automatically generate docs from our docstrings,
here's what you need to know:

## Common knowledge
1. use `@private` to hide internal attributes,
all attributes beginning with an underscore except `__init__` are automatically hidden.
2. use `@public` to show attributes beginning with an underscore.
3. if you want to place a reference to an existing class or attribute,
just type "Class" or "Class.attribute", pdoc will automatically understand
it's from our library.

## Other important notes:
1. pdoc will only grab objects from `wokkichat/__init__.py`,
so don't bother documenting anything which isn't in `__all__`!
2. pdoc grabs objects in order of appearance in `__all__`.
3. We use the [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/)
format to document parameters and raises in nested methods.
Do not document types, types are already extracted from the in-code type hints.

## Building the docs
⚠️ It's better to build the docs with Python 3.8 and not higher, because it keeps better references to `typing` classes!
<br>
E.g. it'll keep `Union[int, str]` instead of `int | str`.

To install:
```bash
pip install pdoc
```
*if your environment is "externally managed", use your own native package provider.*

Download the library:
```bash
git clone https://github.com/levkris/Wokki-Chat-Python-SDK
cd 'Wokki-Chat-Python-SDK'
```

To test locally (after saving files reload the page to refresh):
```bash
pdoc wokkichat -t doctemplate -e wokkichat=https://github.com/levkris/Wokki-Chat-Python-SDK/tree/main/wokkichat/
# or replace pdoc with python -m pdoc
```

To build the output HTML:
```bash
pdoc wokkichat -t doctemplate -e wokkichat=https://github.com/levkris/Wokki-Chat-Python-SDK/tree/main/wokkichat/ -o docs
# or replace pdoc with python -m pdoc
```
