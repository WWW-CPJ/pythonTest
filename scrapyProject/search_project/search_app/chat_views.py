
import os
import requests
from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import hmac
import hashlib
import time
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')
            if message:
                # 从环境变量中获取 API 信息
                app_id = os.getenv('SPARK_APP_ID')
                api_key = os.getenv('SPARK_API_KEY')
                api_secret = os.getenv('SPARK_API_SECRET')

                # 生成时间戳
                now = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
                print(f"Timestamp: {now}")

                host = "spark-api-open.xf-yun.com"
                path = "/v1/chat/completions"
                url = f"https://{host}{path}"

                # 构建签名原串
                signing_str = f"host: {host}\ndate: {now}\nPOST {path}"
                print(f"Signing string: {signing_str}")

                # 生成签名
                signature = hmac.new(api_secret.encode('utf-8'), signing_str.encode('utf-8'), hashlib.sha256).digest()
                signature_base64 = base64.b64encode(signature).decode()
                print(f"Signature: {signature_base64}")

                # 生成鉴权信息
                authorization = f'api_key="{api_key}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_base64}"'
                print(f"Authorization: {authorization}")

                # 请求头
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": authorization,
                    "Date": now,
                    "Host": host
                }

                # 请求体，根据新示例调整结构，并开启流式请求
                payload = {
                    "model": "lite",
                    "messages": [
                        {
                            "role": "user",
                            "content": message
                        }
                    ],
                    "tools": [
                        {
                            "type": "function",
                            "function": {
                                "name": "get_current_weather",
                                "description": "返回实时天气",
                                "parameters": {
                                    "type": "object",
                                    "properties": {
                                        "location": {
                                            "type": "string",
                                            "description": "河北省承德市双桥区",
                                        },
                                        "format": {
                                            "type": "string",
                                            "enum": ["celsius", "fahrenheit"],
                                            "description": "使用本地区常用的温度单位计量",
                                        },
                                    },
                                    "required": ["location", "format"],
                                }
                            }
                        }
                    ],
                    "stream": True  # 开启流式请求
                }

                # 发送流式请求
                response = requests.post(url, headers=headers, json=payload, stream=True)

                def generate():
                    if response.status_code == 200:
                        response.encoding = "utf-8"
                        for line in response.iter_lines(decode_unicode=True):
                            if line:
                                try:
                                    # 解析每一行 JSON 数据
                                    line_data = json.loads(line)
                                    # 根据实际返回结构调整获取回复的逻辑
                                    ai_response_part = line_data.get('choices', [{}])[0].get('delta', {}).get('content')
                                    if ai_response_part:
                                        yield json.dumps({'response': ai_response_part}) + '\n'
                                except json.JSONDecodeError:
                                    print(f"Failed to decode JSON: {line}")
                    else:
                        error_message = f'API request failed with status code {response.status_code}: {response.text}'
                        yield json.dumps({'error': error_message}) + '\n'

                return StreamingHttpResponse(generate(), content_type='application/json')
            else:
                return JsonResponse({'error': 'No message provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)








# import os
# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# import base64
# import hmac
# import hashlib
# import time
# from dotenv import load_dotenv

# # 加载环境变量
# load_dotenv()

# @csrf_exempt
# def chatbot_api(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             message = data.get('message')
#             if message:
#                 # 从环境变量中获取 API 信息
#                 app_id = os.getenv('SPARK_APP_ID')
#                 api_key = os.getenv('SPARK_API_KEY')
#                 api_secret = os.getenv('SPARK_API_SECRET')

#                 # 生成时间戳
#                 now = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
#                 print(f"Timestamp: {now}")

#                 host = "spark-api-open.xf-yun.com"
#                 path = "/v1/chat/completions"
#                 url = f"https://{host}{path}"

#                 # 构建签名原串
#                 signing_str = f"host: {host}\ndate: {now}\nPOST {path}"
#                 print(f"Signing string: {signing_str}")

#                 # 生成签名
#                 signature = hmac.new(api_secret.encode('utf-8'), signing_str.encode('utf-8'), hashlib.sha256).digest()
#                 signature_base64 = base64.b64encode(signature).decode()
#                 print(f"Signature: {signature_base64}")

#                 # 生成鉴权信息
#                 authorization = f'api_key="{api_key}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_base64}"'
#                 print(f"Authorization: {authorization}")

#                 # 请求头
#                 headers = {
#                     "Content-Type": "application/json",
#                     "Authorization": authorization,
#                     "Date": now,
#                     "Host": host
#                 }

#                 # 请求体，根据新示例调整结构
#                 payload = {
#                     "model": "lite",
#                     "messages": [
#                         {
#                             "role": "user",
#                             "content": message
#                         }
#                     ],
#                     "tools": [
#                         {
#                             "type": "function",
#                             "function": {
#                                 "name": "get_current_weather",
#                                 "description": "返回实时天气",
#                                 "parameters": {
#                                     "type": "object",
#                                     "properties": {
#                                         "location": {
#                                             "type": "string",
#                                             "description": "河北省承德市双桥区",
#                                         },
#                                         "format": {
#                                             "type": "string",
#                                             "enum": ["celsius", "fahrenheit"],
#                                             "description": "使用本地区常用的温度单位计量",
#                                         },
#                                     },
#                                     "required": ["location", "format"],
#                                 }
#                             }
#                         }
#                     ]
#                 }

#                 response = requests.post(url, headers=headers, json=payload)
#                 print(f"Response status code: {response.status_code}")
#                 print(f"Response text: {response.text}")

#                 if response.status_code == 200:
#                     result = response.json()
#                     # 根据实际返回结构调整获取回复的逻辑
#                     ai_response = result.get('choices', [{}])[0].get('message', {}).get('content')
#                     if ai_response:
#                         return JsonResponse({'response': ai_response})
#                     else:
#                         return JsonResponse({'error': 'No valid AI response found in the result'}, status=500)
#                 else:
#                     return JsonResponse({'error': f'API request failed with status code {response.status_code}: {response.text}'}, status=response.status_code)
#             else:
#                 return JsonResponse({'error': 'No message provided'}, status=400)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)



# import os
# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# import base64
# import hmac
# import hashlib
# import time
# from dotenv import load_dotenv

# # 加载环境变量
# load_dotenv()

# @csrf_exempt
# def chatbot_api(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             message = data.get('message')
#             if message:
#                 # 从环境变量中获取 API 信息
#                 app_id = os.getenv('SPARK_APP_ID')
#                 api_key = os.getenv('SPARK_API_KEY')
#                 api_secret = os.getenv('SPARK_API_SECRET')
#                 print(f"App ID: {app_id}, API Key: {api_key}, API Secret: {api_secret}")

#                 # 生成时间戳
#                 now = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
#                 print(f"Timestamp: {now}")

#                 host = "spark-api.xf-yun.com"
#                 path = "/v1.1/chat"
#                 url = f"https://{host}{path}"

#                 # 构建签名原串
#                 signing_str = f"host: {host}\ndate: {now}\nPOST {path}"
#                 print(f"Signing string: {signing_str}")

#                 # 生成签名
#                 signature = hmac.new(api_secret.encode('utf-8'), signing_str.encode('utf-8'), hashlib.sha256).digest()
#                 signature_base64 = base64.b64encode(signature).decode()
#                 print(f"Signature: {signature_base64}")

#                 # 生成鉴权信息
#                 authorization = f'api_key="{api_key}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_base64}"'
#                 # authorization = 'ZsVZwqXWphaMHOtMdVlM:ovLabSODRfzHpJKItiMb'


#                 # 请求头
#                 headers = {
#                     "Content-Type": "application/json",
#                     "Authorization": authorization,
#                     "Date": now,
#                     "Host": host
#                 }

#                 # 请求体
#                 payload = {
#                     "header": {
#                         "model": "lite",
#                         "app_id": app_id,
#                         "uid": "dccdfdd5"  # 可自定义用户唯一标识
#                     },
#                     "parameter": {
#                         "chat": {
#                             "domain": "general",
#                             "temperature": 0.5,
#                             "max_tokens": 2048,
#                             "top_k": 4,
#                             "stream": False
#                         }
#                     },
#                     "payload": {
#                         "message": {
#                             "text": [
#                                 {
#                                     "role": "user",
#                                     "content": message
#                                 }
#                             ]
#                         }
#                     }
#                 }

#                 response = requests.post(url, headers=headers, json=payload)
#                 print(f"Response status code: {response.status_code}")
#                 print(f"Response text: {response.text}")
#                 if response.status_code == 200:
#                     result = response.json()
#                     ai_response = result["payload"]["choices"]["text"][0]["content"]
#                     return JsonResponse({'response': ai_response})
#                 else:
#                     return JsonResponse({'error': f'API request failed with status code {response.status_code}: {response.text}'}, status=response.status_code)
#             else:
#                 return JsonResponse({'error': 'No message provided'}, status=400)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)







# import os
# import requests
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from dotenv import load_dotenv

# # 加载环境变量
# load_dotenv()

# @csrf_exempt
# def chatbot_api(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             message = data.get('message')
#             if message:
#                 # 从环境变量中获取 API 密钥和镜像源 URL
#                 api_key = os.getenv('HUGGING_FACE_API_KEY')
#                 api_url = os.getenv('HUGGING_FACE_API_URL', 'https://api-inference.huggingface.co') + '/models/gpt2'

#                 headers = {
#                     'Content-Type': 'application/json',
#                     'Authorization': f'Bearer {api_key}'
#                 }
#                 payload = {
#                     'inputs': message
#                 }

#                 response = requests.post(api_url, headers=headers, json=payload)
#                 if response.status_code == 200:
#                     result = response.json()
#                     return JsonResponse({'response': result[0].get('generated_text')})
#                 else:
#                     return JsonResponse({'error': f'API request failed with status code {response.status_code}'}, status=response.status_code)
#             else:
#                 return JsonResponse({'error': 'No message provided'}, status=400)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)