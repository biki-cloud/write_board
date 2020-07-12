from flask import Flask,render_template,request , Markup ,send_from_directory
import json
import time
import os,sys


from form_arrange import form

app = Flask(__name__)

@app.route('/', methods=["GET" , "POST"])
def main_page():
    method = request.method
    save_json_path = "data/save_data.json"
    
    if method == "POST":
        former = form(form_input=dict(request.form) , save_json_path=save_json_path)
        
        if "clear" in dict(request.form).keys():
            former.save_json_clear()
            return render_template("main_page.html" , save_list=former.save_list, method=method)
        
        form_input = former.form_input
        former.write_save_json()
        return render_template("main_page.html" , save_list=former.save_list,form_input=form_input,
                               method=method)
    else:
        former = form(save_json_path)
        save_list = former.save_list
        return render_template("main_page.html" , save_list=save_list, method=method)
    
@app.route('/test')
def index():
    return 'Hello World!'

@app.route('/favicon.ico') 
def favicon(): 
    return app.send_static_file("favicon.ico")
    #return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    #app.run(debug=True)
    #app.run()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
