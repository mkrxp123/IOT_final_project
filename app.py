import random, json, DAN
from flask import Flask, request, render_template

app = Flask(__name__)
ServerURL = 'https://2.iottalk.tw'  # with SSL secure connection
# if None, Reg_addr = MAC address
Reg_addr = 'CD8600D38' + str(random.randint(100, 999))
# mac_addr = 'CD8600D38' + str(random.randint(100,999 ))
# you can change this but should also add the DM in server
DAN.profile['dm_name'] = 'med_web'
# Check IoTtalk to see what IDF/ODF the DM has
DAN.profile['df_list'] = ["times_json"]
DAN.profile['d_name'] = f"DM_{str(random.randint(100, 999))}.med_web"
DAN.device_registration_with_retry(ServerURL, Reg_addr)
print("dm_name is ", DAN.profile['dm_name'])
print("Server is ", ServerURL)


@app.route('/send_times', methods=['POST'])
def send_times():
    print(type(request.json))
    DAN.push("times_json", request.json)
    return "success", 200


@app.route('/')
def index():
    return render_template('index.html', d_name=DAN.profile['d_name'])


if __name__ == '__main__':
    app.run(debug=True)
