import datetime
import os
import json
from . import msg_formatter

def logging(src, lvl, msg):
    base_name = os.path.dirname(__file__)
    target_dir = "../../logs"
    logs_path = os.path.join(base_name, target_dir)
    logs_path = os.path.abspath(logs_path)
    data_filepath = os.path.join(base_name, "..", "..", "data", "logs_data.json")
    
    try:
    
        with open(data_filepath, "r") as f:
            logs_data = json.load(f)
            
    except (FileNotFoundError, json.JSONDecodeError):
        print(msg_formatter.formatte(__name__, 3, f"Failed to load program/data/logs_data.json"))
            
    else:
        
        count_logs_files = logs_data["count_logs_files"]
        filename = logs_path + f"/log_{count_logs_files}.txt"
        data_filepath = os.path.join(base_name, "..", "..", "data", "logs_data.json")
        filename = logs_path + f"/log_{count_logs_files}.txt"
        log_msg = msg_formatter.formatte(src, lvl, msg)
        
        if os.path.exists(logs_path):
            files = os.listdir(logs_path)
            logs_files = []
            
        else:
            os.mkdir(logs_path)
            files = []
        
        for file in files:
            
            if file.startswith("log") and file.endswith(".txt"):
                file_path = os.path.abspath(os.path.join(logs_path, file))
                logs_files.append(file_path)
        
        if os.path.exists(filename):
                     
            if os.path.getsize(filename) <= 5000:
                pass
                
            else:
    
                if len(logs_files) > 2:
                
                    for file in logs_files:
                        ctimes = []
                        ctime = os.path.getctime(file)
                        ctimes.append((os.path.abspath(file), ctime))
                        most_ancient = max(ctimes)
                        
                        for index, ctime in enumerate(ctimes):
                            
                            if ctime == most_ancient:
                                print()
                                os.remove(ctimes[index][0])
                                
                count_logs_files += 1
                logs_data["count_logs_files"] = count_logs_files
                
                with open(data_filepath, "w") as f:
                    json.dump(logs_data, f)
                    
         
        filename = logs_path + f"/log_{count_logs_files}.txt"  
       
        with open(filename, "a") as f:
            f.write(log_msg)                        