"""The machinery as a thicket (home page figure), brought back into the book on 18 November 2026.

The drawing was generated on 20 October 2026 by build_pitch.py in the construction-procurement-protocols
pitch (now the frozen ruin; read, never written). Its SVG was copied out once, without the S, C and AI
badges and the legend, and is now edited here directly: images/machinery-thicket.svg is the source.
Usage: python images/machinery_thicket.py images/machinery-thicket   (writes an .html beside the .svg)
then:  node images/project_hex_map_render.js "$PWD/images/machinery-thicket.html" images/machinery-thicket.png 1060 868
"""
import sys
stem = sys.argv[1]
svg = open(stem + ".svg", encoding="utf-8").read()
open(stem + ".html", "w", encoding="utf-8").write(
    '<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#ffffff}</style></head><body>'
    + svg + "</body></html>")
