#!/usr/bin/python
_new = open("new.txt")
new = _new.read()
new = new.strip()
new = new.split(",,")
_old = open("old.txt")
old = _old.read()
_template = open("template.txt")
template = _template.read()
template = template.strip()
_template.close()
old = old.strip()
for i in range(len(new)):
    product = template.replace(old, new[i])
    product = product+"\n"
    _product = open("product.txt", "a")
    _product.write(product)
    _product.close()
