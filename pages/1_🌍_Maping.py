import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
from folium import plugins
df = pd.read_excel('data\서울지역-청년친화강소기업명단(통합).xlsx')

APP_TITLE = '지도로 보는 청년친화강소기업'
APP_SUB_TITLE = '<Copyright 2022. Chungicha. All right reserved.>'

def display_time_filters(df):
    year_list = list(df['선정연도'].unique())
    year = st.sidebar.selectbox('선정연도', year_list, len(year_list)-1)
    fields_list = list(df['업종'].unique())
    fields = st.sidebar.selectbox('업종', fields_list)
    st.header(f'{year} <{fields}> 기업')
    return year, fields

def display_map(df, year, fields):
    df = df[(df['선정연도'] == year) & (df['업종'] == fields)]
    
    # 서울시 중심부의 위도, 경도.
    center = [37.541, 126.986]
    m = folium.Map(location=center, zoom_start=11)
    
    # 2022년: 업종별 그룹 짓기
    fg = folium.FeatureGroup(name='전체')
    m.add_child(fg)
    
    g1 = plugins.FeatureGroupSubGroup(fg, '임금')
    m.add_child(g1)
    
    g2 = plugins.FeatureGroupSubGroup(fg, '고용안정')
    m.add_child(g2)
    
    g3 = plugins.FeatureGroupSubGroup(fg, '일생활균형')
    m.add_child(g3)

    folium.LayerControl(collapsed=True).add_to(m)
    
    # 맵 만들기
    df_1 = df[df['기업강점'].str.contains('임금')]
    df_2 = df[df['기업강점'].str.contains('고용안정')]
    df_3 = df[df['기업강점'].str.contains('일생활균형')]
    for i in df_1.index:
        name = df_1.loc[i, '사업장명']
        location = df_1.loc[i, '소재지']
        field = df_1.loc[i, '업종']
        scale = df_1.loc[i, '기업규모']
        strength = df_1.loc[i, '기업강점']
        lat = df_1.loc[i, '위도']
        lon = df_1.loc[i, '경도']
        popup = folium.Popup("<b>"+name+"</b><br>"+"<b>"+"소재지: "+"</b>"
                             +location+"<br>"+"<b>"+"업종: "+"</b>"+field+"<br>"+"<b>"+"기업규모: "
                             +"</b>"+scale+"<br>"+"<b>"+"기업강점: "
                             +"</b>"+strength, max_width=410) # 팝업 설정
        if len(df_1['업종'][i]) != 0:
            folium.Marker([lat, lon], popup, icon=folium.Icon(icon='info-sign'), tooltip=name).add_to(g1)

    for i in df_2.index:
        name = df_2.loc[i, '사업장명']
        location = df_2.loc[i, '소재지']
        field = df_2.loc[i, '업종']
        scale = df_2.loc[i, '기업규모']
        strength = df_2.loc[i, '기업강점']
        lat = df_2.loc[i, '위도']
        lon = df_2.loc[i, '경도']
        popup = folium.Popup("<b>"+name+"</b><br>"+"<b>"+"소재지: "+"</b>"
                             +location+"<br>"+"<b>"+"업종: "+"</b>"+field+"<br>"+"<b>"+"기업규모: "
                             +"</b>"+scale+"<br>"+"<b>"+"기업강점: "
                             +"</b>"+strength, max_width=410) # 팝업 설정
        if len(df_2['업종'][i]) != 0:
            folium.Marker([lat, lon], popup, icon=folium.Icon(icon='info-sign'), tooltip=name).add_to(g2)

    for i in df_3.index:
        name = df_3.loc[i, '사업장명']
        location = df_3.loc[i, '소재지']
        field = df_3.loc[i, '업종']
        scale = df_3.loc[i, '기업규모']
        strength = df_3.loc[i, '기업강점']
        lat = df_3.loc[i, '위도']
        lon = df_3.loc[i, '경도']
        popup = folium.Popup("<b>"+name+"</b><br>"+"<b>"+"소재지: "+"</b>"
                             +location+"<br>"+"<b>"+"업종: "+"</b>"+field+"<br>"+"<b>"+"기업규모: "
                             +"</b>"+scale+"<br>"+"<b>"+"기업강점: "
                             +"</b>"+strength, max_width=410) # 팝업 설정
        if len(df_3['업종'][i]) != 0:
            folium.Marker([lat, lon], popup, icon=folium.Icon(icon='info-sign'), tooltip=name).add_to(g3)
        # <b>: bold text, </b>: bold text X, <br>:other line
        # 마커 및 툴팁 설정: 업종별 색깔 구분 + 체크박스 만들기

    folium_static(m)


        
def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    
    ## Load Data
    df = pd.read_excel('data\서울지역-청년친화강소기업명단(통합).xlsx')
    
    ## Filters
    
    ## Display Map
    year, fields = display_time_filters(df)
    display_map(df, year, fields)

def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)
    st.caption(APP_SUB_TITLE)
    
    ## Load Data
    df = pd.read_excel('data\서울지역-청년친화강소기업명단(통합).xlsx')
    
    ## Filters
    
    ## Display Map
    year, fields = display_time_filters(df)
    display_map(df, year, fields)


if __name__ == "__main__":
    main()
