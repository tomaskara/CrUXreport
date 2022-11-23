import requests
import datetime
import os
import json
from dotenv import load_dotenv
from functions import send_emails

project_folder = os.path.dirname(os.path.abspath(__file__)) # adjust as appropriate os.path.abspath(".")
load_dotenv(os.path.join(project_folder, '.env'))

receiver_emails = json.loads(os.environ['RECEIVERS'])

API_KEY = os.getenv("API_KEY")
api_url = f"https://chromeuxreport.googleapis.com/v1/records:queryRecord?key={API_KEY}"
request_body = {
    "url": "https://www.homecredit.cz/pujcky",
    "formFactor": "PHONE",
    "metrics": [
        "largest_contentful_paint",
        "first_input_delay",
        "cumulative_layout_shift"
    ]
}

api_call = requests.post(api_url, json=request_body)
json_response = api_call.json()
date = datetime.date(json_response['record']['collectionPeriod']['lastDate']['year'],
                     json_response['record']['collectionPeriod']['lastDate']['month'],
                     json_response['record']['collectionPeriod']['lastDate']['day'])

file = open(os.path.join(project_folder, 'cls'), "r+")
cls = float(json_response['record']['metrics']['cumulative_layout_shift']['percentiles']['p75'])
new = False
if os.stat(os.path.join(project_folder, 'cls')).st_size == 0:
    file.write(f"{date}:{cls}\n")
else:
    last_date, last_value = file.readlines()[-1].split(":")
    if last_date != str(date):
        new = True
        file.write(f"{date}:{cls}\n")

file.seek(0, 0)
file_list = list(file)
if len(file_list) >= 6:
    nums = []
    for line in file_list[-6:-1]:
        nums.append(float(line.split(":")[1].strip()))
    average = sum(nums) / len(nums)
    if cls > average and new and cls != float(last_value.strip()):
        send_emails(receiver_emails, "CLS /pujcky", cls, average)

file.close()

file = open(os.path.join(project_folder, 'lcp'), "r+")
lcp = float(json_response['record']['metrics']['largest_contentful_paint']['percentiles']['p75'])
new = False
if os.stat(os.path.join(project_folder, 'lcp')).st_size == 0:
    file.write(f"{date}:{lcp}\n")
else:
    last_date, last_value = file.readlines()[-1].split(":")
    if last_date != str(date):
        new = True
        file.write(f"{date}:{lcp}\n")

file.seek(0, 0)
file_list = list(file)
if len(file_list) >= 6:
    nums = []
    for line in file_list[-6:-1]:
        nums.append(float(line.split(":")[1].strip()))
    average = sum(nums) / len(nums)
    if lcp > average and new and lcp != float(last_value.strip()):
        send_emails(receiver_emails, "LCP /pujcky", lcp, average)
file.close()

file = open(os.path.join(project_folder, 'fid'), "r+")
fid = float(json_response['record']['metrics']['first_input_delay']['percentiles']['p75'])
new = False
if os.stat(os.path.join(project_folder, 'fid')).st_size == 0:
    file.write(f"{date}:{fid}\n")
else:
    last_date, last_value = file.readlines()[-1].split(":")[0]
    if last_date != str(date):
        new = True
        file.write(f"{date}:{fid}\n")

file.seek(0, 0)
file_list = list(file)
if len(file_list) >= 6:
    nums = []
    for line in file_list[-6:-1]:
        nums.append(float(line.split(":")[1].strip()))
    average = sum(nums) / len(nums)
    if fid > average and new and fid != float(last_value.strip()):
        send_emails(receiver_emails, "FID /pujcky", fid, average)
file.close()



request_body_sk = {
    "url": "https://www.homecredit.sk/pozicky",
    "formFactor": "PHONE",
    "metrics": [
        "largest_contentful_paint",
        "first_input_delay",
        "cumulative_layout_shift"
    ]
}
api_call_sk = requests.post(api_url, json=request_body_sk)
json_response_sk = api_call_sk.json()
date_sk = datetime.date(json_response_sk['record']['collectionPeriod']['lastDate']['year'],
                        json_response_sk['record']['collectionPeriod']['lastDate']['month'],
                        json_response_sk['record']['collectionPeriod']['lastDate']['day'])


file = open(os.path.join(project_folder, 'cls_sk'), "r+")
cls_sk = float(json_response_sk['record']['metrics']['cumulative_layout_shift']['percentiles']['p75'])
new = False
if os.stat(os.path.join(project_folder, 'cls_sk')).st_size == 0:
    file.write(f"{date_sk}:{cls_sk}\n")
else:
    last_date, last_value = file.readlines()[-1].split(":")[0]
    if last_date != str(date_sk):
        new = True
        file.write(f"{date_sk}:{cls_sk}\n")

file.seek(0, 0)
file_list = list(file)
if len(file_list) >= 6:
    nums = []
    for line in file_list[-6:-1]:
        nums.append(float(line.split(":")[1].strip()))
    average = sum(nums) / len(nums)
    if cls_sk > average and new and cls_sk != float(last_value.strip()):
        send_emails(receiver_emails, "CLS /pozicky", cls_sk, average)
file.close()

file = open(os.path.join(project_folder, 'lcp_sk'), "r+")
lcp_sk = float(json_response_sk['record']['metrics']['largest_contentful_paint']['percentiles']['p75'])
new = False
if os.stat(os.path.join(project_folder, 'lcp_sk')).st_size == 0:
    file.write(f"{date_sk}:{lcp_sk}\n")
else:
    last_date, last_value = file.readlines()[-1].split(":")
    if last_date != str(date_sk):
        new = True
        file.write(f"{date_sk}:{lcp_sk}\n")
file.seek(0, 0)
file_list = list(file)
if len(file_list) >= 6:
    nums = []
    for line in file_list[-6:-1]:
        nums.append(float(line.split(":")[1].strip()))
    average = sum(nums) / len(nums)
    if lcp_sk > average and new and lcp_sk != float(last_value.strip()):
        send_emails(receiver_emails, "LCP /pozicky", lcp_sk, average)
file.close()

file = open(os.path.join(project_folder, 'fid_sk'), "r+")
fid_sk = float(json_response_sk['record']['metrics']['first_input_delay']['percentiles']['p75'])
new = False
if os.stat(os.path.join(project_folder, 'fid_sk')).st_size == 0:
    file.write(f"{date_sk}:{fid_sk}\n")
else:
    last_date, last_value = file.readlines()[-1].split(":")
    if last_date != str(date_sk):
        new = True
        file.write(f"{date_sk}:{fid_sk}\n")
file.seek(0, 0)
file_list = list(file)
if len(file_list) >= 6:
    nums = []
    for line in file_list[-6:-1]:
        nums.append(float(line.split(":")[1].strip()))
    average = sum(nums) / len(nums)
    if fid_sk > average and new and fid_sk != float(last_value.strip()):
        send_emails(receiver_emails, "FID /pozicky", fid_sk, average)
file.close()

