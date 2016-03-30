# coding: utf-8

"""
    mistune_contrib.meta
    ~~~~~~~~~~~~~~~~~~~~

    Support Meta features for mistune. Metadata are keywords headers at the
    top of the Markdown text, the content between '---' is YAML Syntax, 
    see `YAML <http://pyyaml.org/wiki/PyYAMLDocumentation#YAMLsyntax>`.
    
    Example:

        Meta-data consists of a series of keywords and values defined at the beginning of a markdown document like this:

        ---
        Title:   My Document
        Summary: A brief description of my document.
        Authors: 
            - Waylan Limberg
            - John Doe
        Date:    2016-03-30
        blank-value: 
        base_url: http://example.com
        ---

        This is the first paragraph of the document.
        
    :copyright: (c) 2015 by Hsiaoming Yang.
"""


import re
import yaml

META_END = re.compile(r"\n(\.{3}|-{3})")


def parse(text):
    """Parse the given text into metadata and strip it for a Markdown parser.

    :param text: text to be parsed
    :return: (meta, text)
    """
    if text[0:3] != '---':
        return {}, text
    meta_text = META_END.split(text[3:])
    # meta_text: ['title: xx', '---', '\n# xxx']
    if len(meta_text) != 3:
        return {}, text
    meta, __, text = meta_text
    text = text.strip('\n')
    try:
        meta = yaml.load(meta)
    except yaml.YAMLError as ex:
        meta = {}
        raise
    return meta, text
