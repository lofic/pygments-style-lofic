# -*- coding: utf-8 -*-
"""
    pygments.styles.lofic
    ~~~~~~~~~~~~~~~~~~~~~

    Lofic's custom highlighting style for Pygments.
    Inspired by pygments.styles.vim

    :copyright: Copyright 2012 Louis Coilliot 
    :license: BSD, see LICENSE for details.

"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Whitespace, Token, Punctuation


class LoficStyle(Style):
    """
    Lofic's custom highlighting style for Pygments
    """

    background_color = "#000000"  # White
    highlight_color = "#222222"
    default_style = "#333333"

    styles = {
        Token:                     "#333333",  # Gray20
        Whitespace:                "",
        Comment:                   "#104e8b",  # Dodgerblue4
        Comment.Preproc:           "",
        Comment.Special:           "bold #104e8b",  # Dodgerblue4

        Keyword:                   "#b8860b",  # DarkGoldenRod
        Keyword.Constant:          "#8b8b00",
        Keyword.Declaration:       "#00cd00",
        Keyword.Namespace:         "#75507b",  # Plum2
        Keyword.Pseudo:            "#cd0000",  # Red3
        Keyword.Type:              "#00cd00",
        Keyword.Reserved:          "#8b8b00",

        Operator:                  "#000000",  # Black
        Operator.Word:             "#8b8b00",

        Name:                      "#000000",  # Black
        Name.Constant:             "#4e9a06",  # Chameleon3
        Name.Class:                "#cd0000",  # Red3
        Name.Builtin:              "#75507b",  # Plum2
        Name.Exception:            "bold #666699",
        Name.Variable:             "#008b8b",  # DarkCyan
        Name.Function:             "#008b8b",  # DarkCyan
        Name.Namespace:            "#4e9a06",  # Chameleon3

        Name.Attribute:            "#333333",  # Gray20
        Name.Decorator:            "#333333",  # Gray20
        Name.Entity:               "#333333",  # Gray20
        Name.Label:                "#333333",  # Gray20
        Name.Other:                "#333333",  # Gray20
        Name.Property:             "#333333",  # Gray20
        Name.Tag:                  "#333333",  # Gray20

        String:                    "#8b1a1a",  # FireBrick4
        Number:                    "#ff3030",  # FireBrick1
        String.Regex:              "#6a5acd",  # SlateBlue
        String.Interpol:           "#6a5acd",  # SlateBlue

        Punctuation:               "#000000",  # Black

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#8b1a1a",
        Generic.Inserted:          "#00cd00",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #000080",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
