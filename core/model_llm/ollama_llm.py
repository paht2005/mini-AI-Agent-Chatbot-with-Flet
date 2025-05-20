# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache

# Khởi tạo model Ollama với model Qwen 2.5 coder
_model = OllamaLLM(model="qwen2.5-coder:1.5b")
set_llm_cache(InMemoryCache())
_prompt_template = PromptTemplate.from_template(
"""
 Tôi là chuyên gia về Công nghệ thông tin, bạn có thể hỏi tôi về các vấn đề liên quan đến CNTT.
 Câu trả lời phải đúng các tiêu chí sau:
    - Câu trả lời phải chính xác
    - Câu trả lời phải dễ hiểu
    - Câu trả lời phải đầy đủ
    - Câu trả lời phải hợp lý
    - Câu trả lời phải đúng với câu hỏi
    - Câu trả lời phải chính xác về mặt ngữ cảnh
    - Câu trả lời phải chính xác về mặt kiến thức
    - Câu trả lời phải chính xác về mặt ngữ pháp
    - Câu trả lời phải chính xác về mặt từ vựng

 Cẩu hỏi:
 {question}
"""
)

_chain = _prompt_template | _model | StrOutputParser()

def query_answer(question: str) -> str:
    return _chain.invoke({"question": question})
