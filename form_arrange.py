import json
import os,sys
import time

class form:
    def __init__(self  , save_json_path , form_input=None):
        if form_input != None:
            nowtime = str(time.ctime())
            form_input["time"] = nowtime
            self.form_input = form_input  
        self.save_list = self.read_save_json(save_json_path)
        self.save_json_path = save_json_path
        
        
    def read_save_json(self , save_json_path):
        save_list = []
        if os.path.exists(save_json_path):
            with open(save_json_path , "r") as f:
                save_list = json.load(f)
            return save_list
        else:
            with open(self.save_json_path , "w") as f:
                save_list = json.dump(save_list, f, indent=4)
            return save_list
        
    def write_save_json(self):
        self.save_list.append(self.form_input)
        with open(self.save_json_path , "w") as f:
            save_list = json.dump(self.save_list, f, indent=4)

    def save_json_clear(self):
        self.save_list = []
        with open(self.save_json_path , "w") as f:
                json.dump(self.save_list, f, indent=4)
        
            
