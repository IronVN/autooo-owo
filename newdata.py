import time
import json
import os
if os.name == 'nt':
    pass
if os.name == 'linux':
    import simplejson as json
else:
    try:
        import json
    except:
        import simplejson as json
with open('settings.json', 'r+') as f:
    data = json.load(f)
    data['token'] = input("Please Enter Your Account Token: ")
    data['channel'] = input("Please Enter Your Channel ID: ")
    f.seek(0)        # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()     # remove remaining part
    print('Successfully saved!')
    print('Please Restart The Command Prompt')
    time.sleep(2)
