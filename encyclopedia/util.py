import re
import markdown2

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def search(query):
    ls = list_entries()
    ret = []
    notr = []
    for items in ls:
        a = re.compile(query, re.IGNORECASE)
        ab = a.findall(items)
        if ab:
            ret.append(items)
        else:
            notr.append(items)

    return ret          

def HtmlMk(query):
    asx = markdown2.markdown(get_entry(query))
    return asx

def deleteFile(name):
    filename = f"entries/{name}.md"
    default_storage.delete(filename)
    return True