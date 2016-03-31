# coding:utf-8
from datetime import date
from mistune_contrib import meta
import yaml
import pytest

text_ok = [
    """---
Title: Hello World
Authors: 
    - Waylan Limberg
    - John Doe
blank-value: 
Date: 2016-03-30
---

# Hello World
""",
    """---
Title: Hello World
Authors: 
    - Waylan Limberg
    - John Doe
blank-value: 
Date: 2016-03-30
---
# Hello World
""",
    """---
Title: Hello World
Authors: 
    - Waylan Limberg
    - John Doe
blank-value: 
Date: 2016-03-30
---
# Hello World
---------
"""
]

text_fail = [
    """---
Title: Hello World
Authors: 
    - Waylan Limberg
    - John Doe
blank-value: 
Date: 2016-03-30


# Hello World
""",
    """Title: Hello World
Authors: 
    - Waylan Limberg
    - John Doe
blank-value: 
Date: 2016-03-30

# Hello World
""",
    """---
Title: Hello World
Authors: Waylan Limberg
         John Doe
blank-value: 
Date: 2016-03-30
---

# Hello World
""",
]

text_error = [
    """---
Title: Hello World
Authors: - Waylan Limberg
         - John Doe
blank-value: 
Date: 2016-03-30
---

# Hello World
""",
]

expect = {
    "Title": "Hello World",
    "Authors": ["Waylan Limberg", "John Doe"],
    "blank-value": None,
    "Date": date(2016, 3, 30),
}


def test_meta_ok():
    for text in text_ok:
        met, cont = meta.parse(text)
        assert met == expect


def test_meta_fail():
    for text in text_fail:
        met, cont = meta.parse(text)
        assert met != expect


def test_meta_error():
    for text in text_error:
        with pytest.raises(yaml.YAMLError):
            met, cont = meta.parse(text)
