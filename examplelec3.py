from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/oranges')
def lemons():
    title = "My Ice Cream Form"
    title_var = title
    options = ["vanilla", "chocolate", "etc"]
    return render_template('seeform.html',title=title_var, lst_stuff=options)

@app.route('/apples')
def plants():
    flavor_options = []
    for item in request.args:
        if item == "name":
            name = request.args["name"]
            name_len = len(name)
        else:
            flavor_options.append(item)
    return render_template('results.html',flavors=flavor_options, name_len=name_len, name=name)


if __name__ == "__main__":
    app.run(use_reloader=True,debug=True)
