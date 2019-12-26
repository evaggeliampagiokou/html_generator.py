import pystache

def generate(title,paragraph):
    renderer=pystache.Renderer()
    return renderer.render_path("index.template",{"title":title,"paragraph":paragraph,"has_items":True,"items":[1,2,3]})

def _custom_generate(title, paragraph):
    t=open("index.template")
    template=t.read()
    t.close()
    return template.replace("{{title}}",title).replace("{{paragraph}}",paragraph)



f = open("intex.html", "w")
f.write(generate('a','b'))
f.close()