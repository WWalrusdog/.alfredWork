#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
_new = open("new.txt")
new = _new.read()
new = new.strip()
_old = open("old.txt")
old = _old.read()
old = old.strip()
_template = open("template.txt")
template = _template.read()
template = template.strip()
product = template.replace(old, new)
_product = open("product.txt", "w")
_product.write(product)
_product.close()