import unittest
from openai import OpenAI

class TestDeepSeekAPI(unittest.TestCase):
    def setUp(self):
        self.client = OpenAI(
            api_key="YOUR_API_KEY",  # 替换为实际API密钥
            base_url="https://api.deepseek.com"
        )
        self.model = "deepseek-reasoner"

    def test_multi_round_conversation(self):
        # 第一轮对话测试
        messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
        
        # 发送请求
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        
        # 验证基础响应结构
        self.assertEqual(len(response.choices), 1)
        self.assertIsNotNone(response.choices[0].message.content)
        self.assertIsNotNone(response.choices[0].message.reasoning_content)
        
        # 验证答案正确性
        self.assertIn("9.11", response.choices[0].message.content)
        self.assertIn("greater", response.choices[0].message.content.lower())

        # 准备第二轮对话
        messages.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })
        messages.append({
            "role": "user",
            "content": "How many Rs are there in the word 'strawberry'?"
        })

        # 发送第二轮请求
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        # 验证基础响应结构
        self.assertEqual(len(response.choices), 1)
        self.assertIsNotNone(response.choices[0].message.content)
        
        # 验证答案正确性
        content = response.choices[0].message.content.lower()
        self.assertTrue(
            any(word in content for word in ["two", "2"]),
            f"Expected 'two' or '2' in response, but got: {content}"
        )
        self.assertIn("strawberry", content)

if __name__ == '__main__':
    unittest.main()
