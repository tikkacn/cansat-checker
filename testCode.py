from difflib import *

differ = HtmlDiff( tabsize=4, wrapcolumn=40 )
html = differ.make_file(r.text, reference, context=False )

print(html)
