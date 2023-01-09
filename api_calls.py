import requests
import time
import datetime as DT

IP = '192.168.40.107'
API_PATH = 'http://'+IP+':5000/abot/api/v5'
print(API_PATH)
email = input('Enter your email: ')
password = input('Enter your password: ')
login_data={
    "email": email,
    "password": password,
    "expires": False
}

res = requests.post(url = API_PATH+'/login',json=login_data,timeout=10)

if res.status_code == 200:
    if res.headers['Content-Type'] == 'application/json':
        r_dict=res.json()
        r_data = r_dict['data']
        access_token = r_data['token']
        
        
        # Setting headers to carry Bearer token
        headers = {"content-type": "application/json; charset=UTF-8",'Authorization':'Bearer {}'.format(access_token)}
        
        
        #API Call to get the feature files
        res = requests.get(url = API_PATH+'/feature_files',headers=headers,timeout=10)
        if res.status_code == 200:
            if res.headers['Content-Type'] == 'application/json':
                r_dict = res.json()
                # print(r_dict)
                print('Feature Files extracted successfully')
        else:
            print('Unable to retrieve feature files')
        
        #API Call to set Config file
        payload = {
                        "uncomment": [
                            "ABOT.SUTVARS=file:abot-emulated/sut-vars/default.properties"
                        ],
                        "comment": [
                            "ABOT.SUTVARS=file:abot-emulated/sut-vars/default5g.properties",
                            "ABOT.SUTVARS=file:abot-emulated/sut-vars/default4g5g.properties",
                            "ABOT.SUTVARS.ORAN=file:abot-emulated/sut-vars/default5g-oran.properties"
                        ],
                        "update": {}
                    }
        param = {
            "filename":"/etc/rebaca-test-suite/config/ABotConfig.properties"
        }
        res = requests.post(url=API_PATH+'/update_config_properties',headers=headers,params=param,json=payload,timeout=10)
        if res.status_code == 200:
            print('Config Updated successfully')
        else:
            print('Config Update Failed')
        
        
        # Execute Feature File
        tag = "initial-attach-test"
        payload = {
                        "params": tag
                    }
        res = requests.post(url=API_PATH+'/feature_files/execute',headers=headers,json=payload,timeout=10)
        if res.status_code == 200:
            print('Feature File Execution Started....')
            status = True
            while status:
                print('Feature file under execution .....')
                time.sleep(5)
                # API call to get status of feature file under execution
                res = requests.get(url=API_PATH+'/execution_status',headers=headers,timeout=10)
                if res.status_code == 200:
                    r_dict = res.json()
                    status = r_dict['status']
                
            print('Feature File Execution Completed')
            
            # Fetch the latest Artefact name
            res = requests.get(url=API_PATH+'/latest_artifact_name',headers=headers,timeout=10)
            if res.status_code == 200:
                print('The latest Artefact name fetched successfully')
                r_dict = res.json()
                r_data = r_dict['data']
                latest_artefact_name = r_data['latest_artifact_timestamp']
                print('Latest Artefact name is :'+latest_artefact_name)
                
                
                param={
                'foldername':latest_artefact_name,
                'page':'1',
                'limit':'10'
                }
                # Fetch execution summary of latest Artefact Summary
                res = requests.get(url=API_PATH+'/artifacts/execFeatureSummary',headers=headers,timeout=10,params=param)
                if res.status_code == 200:
                    print('Execution summary fetched successfully')
                    r_dict = res.json()
                    # print(r_dict)
                else:
                    print('Execution summary fetch failed')
            else:
                print('Unable to retrieve the latest Artefact name')
        else:
            print('Unable to execute Feature File')        
        
        # Fetch Vendor Key
        res = requests.get(url=API_PATH+'/rca/buildVendorList',headers=headers,timeout=10)
        if res.status_code == 200:
            print('Vendor Key fetched successfully')
            r_dict = res.json()
        else:
            print('Vendor Key fetch failed')
        
        
        d=int(input('Enter number of days you want to retreive execution summary: '))
        today = DT.datetime.today()
        week_ago = today - DT.timedelta(days=d)
        week_ago = week_ago.timestamp()
        today = today.timestamp()
        week_ago,today = str(int(week_ago*1000)),str(int(today*1000))
        # print(week_ago,today)
        # Fetch execution pass fail Status for the last 7 days
        param = {
            'fromDateTime': week_ago,
            'toDateTime': today,
            'accessTypes':'4G',
            'loadState':'0',
            'executionType':'0'
        }
        res = requests.get(url=API_PATH+'/rca/execFeatureSummary',headers=headers,params=param,timeout=10)
        if res.status_code == 200:
            print('Execution summary of last 7 days fetched successfully')
            r_dict = res.json()
            if r_dict['statusMessage'] == 'OK':
                r_data = r_dict['data']
                print('Pass percentage '+r_data['passedPercentage'])
                # print(r_data)
                if r_data['failed'] > 0:
                    failed_list = r_data['details']['failed']
                    # print(failed_list)
                    for failed in failed_list:
                        art = failed['artefactName']
                        # print(art)
                        # print(type(art))
                        param = {
                            'foldername':art
                        }
                        # Fetch failure details
                        res = requests.get(url=API_PATH+'/artifacts/execFailureDetails',headers=headers,params=param,timeout=10)
                        if res.status_code == 200:
                            r_dict = res.json()
                            print(art+': Failure details fetched successfully')
                            
                        else:
                            print(art+': Unable to fetch details')
            else:
                print(r_dict['statusMessage'])
        else:
            print('Execution summary of last 7 days fetch failed')

else:
    print('Wrong Credentials')        
        
        
        

        


# response = requests.get(url='http://192.168.40.107:5000/abot/api/v5/feature_files',
#                         auth= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3Mjk4OTE0MiwianRpIjoiY2ExY2ZhZTgtYTRlNC00MzAyLTkyMmQtN2E3MWJiZjZiM2JjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJlbWFpbCI6Im1hZGh1LnN1ZGhhbkByZWJhY2EuY29tIiwicGFzc3dvcmQiOiJtYWRodTEyMzQiLCJleHBpcmVzIjpmYWxzZX0sIm5iZiI6MTY3Mjk4OTE0Mn0.Tnfb3vmAGf91R_9mT2Vmqhuue8gy9sHXgERJ-SViDWI")
# print(response.raw)
# print(type(response))
# print(response.status_code)
# print(response.json())
# data=response.json()
# print(type(data))
# with open("res.json", 'w') as f:
#     json.dumps(data, f)

