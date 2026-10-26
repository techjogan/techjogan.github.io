# 아르곤을 API로 부르는 가장 짧은 코드
# 준비: pip install google-genai
#       AI 스튜디오(aistudio.google.com)에서 API 키 발급 + 결제 등록 (아르곤은 무료 구간 없음)
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])  # 키는 코드에 직접 쓰지 말고 환경 변수로

res = client.models.generate_content(
    model="gemini-4-argon",
    contents="파이썬으로 로또 번호 6개를 겹치지 않게 뽑는 코드를 짧게 짜 줘",
)
print(res.text)

# 쓴 만큼 계산 (11/30까지 도입가: 입력 100만 토큰당 2달러, 출력 10달러 / 12/1부터 4달러, 20달러)
u = res.usage_metadata
out = (u.candidates_token_count or 0) + (u.thoughts_token_count or 0)
usd = u.prompt_token_count / 1e6 * 2 + out / 1e6 * 10
print(f"입력 {u.prompt_token_count} 토큰, 출력 {out} 토큰, 약 {usd:.4f}달러 (약 {usd * 1400:.0f}원)")
