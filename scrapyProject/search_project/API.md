 请求地址:https://spark-api-open.xf-yun.com/v1/chat/completions
Tips: 星火大模型API当前有Lite、Pro、Pro-128K、Max、Max-32K和4.0 Ultra六个版本，各版本独立计量tokens。


请求头
请到控制台获取http服务接口认证信息中的APIPassword,假如获取到的值为123456，则请求头如下：
Content-Type: application/json
Authorization: Bearer 123456
利用上方的请求头发起请求示例如下：
curl -i -k -X POST 'https://spark-api-open.xf-yun.com/v1/chat/completions' \
--header 'Authorization: Bearer 123456' \
--header 'Content-Type: application/json' \
--data '{
    "model":"generalv3.5",
    "messages": [
        {
            "role": "user",
            "content": "来一个只有程序员能听懂的笑话"
        }
    ],
    "stream": true
}'



请求参数
{
    "model": "generalv3.5",
    "user": "用户唯一id",
    "messages": [
        {
            "role": "system",
            "content": "你是知识渊博的助理"
        },
        {
            "role": "user",
            "content": "你好，讯飞星火"
        }
    ],
    // 下面是可选参数
    "temperature": 0.5,
    "top_k": 4,
    "stream": false,
    "max_tokens": 1024,
    "presence_penalty": 1,
    "frequency_penalty": 1,
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "str2int",
                "description": "将字符串类型转为 int 类型",
                "parameters": {...} // 需要符合 json schema 格式
            }
        },
        {
            "type": "web_search",
            "web_search": {
                "enable": true
            }
        }
    ],
    "response_format": {
        "type": "json_object"
    },
    "suppress_plugin": [
        "knowledge"
    ]
}


