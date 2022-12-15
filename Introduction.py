import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Introduction",
        page_icon="💪",
    )
    st.write("# 청년친화강소기업은! 🤗")
    
    st.markdown(
        """
        **강소기업 요건을 갖추고 임금, 워라벨, 고용안정이 우수**하여 청년들이 근무할만한 중소기업입니다.　👈 **서울특별시에 있는 청년강소기업**에 대해 궁금하다면 왼쪽의 사이드바를 통해 확인해보세요!
        ### 청년친화강소기업 선정기준
        ##### 1. 7가지 요건을 갖췄는지 심사
        - 💰 임금체불이 없는 기업
        - 🤝 고용유지율이 높은 기업 (동종업종, 규모별 평균대비)
        - ⛑ 산재사망사고가 없는 기업
        - 👍 신용평가등급이 B- 이상인 기업
        - 📑 상호출자제한기업 진단 및 공기업이 아닌 기업
        - 👩🏻‍🤝‍🧑🏻 근로자가 10인 이상인 기업 (건설업 30인 이상)
        - ❌ 제외 기업 요건이 아닌 기업
        **+) 제외 기업 요건**
        1. **소비·향락업** (다만, 호텔업과 휴양콘도업은 선정대상에 포함)
        2. **중소기업인력지원특별법 제외 업종**
        3. **고용알선업**
        4. **인력공급업**
        ##### 2. 임금, 일생활균형, 고용안정이 우수한지 심사


        
        
    """    
    )
    
    
if __name__ == "__main__":
    run()