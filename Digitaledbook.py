import streamlit as st
import time
import plotly.express as px
import pandas as pd
from PIL import Image


st.set_page_config(
    page_title="디지털 교과서",page_icon='📖'
)

#page road def
def page1_1():
    progress_text = "1-1을 불러오는 중 ..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.divider()
    st.header("1-1 염분")

def page1_2():
    progress_text = "1-2를 불러오는 중 ..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.divider()
    st.header("1-2 수온")

def page2_1():
    progress_text = "2-1을 불러오는 중 ..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.divider()
    st.header("2-1 해수의 표층순환")

def page2_2():
    progress_text = "2-2를 불러오는 중 ..."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    st.divider()
    st.header("2-2 남방진동 ENSO")


#cover

st.title("디지털 교과서 - 지구과학편 🌍" )
st.header('지구과학 2단원 : 해수의 성질 🌊')
st.write(" ")
st.subheader('1장. 해수의 성질')

col1, col2 = st.columns([1,5])
with col1:
    st.write('1-1. 염분')
with col2:
    tog1_1 = st.toggle('1-1 열기')

col3, col4 = st.columns([1,5])
with col3:
    st.write('1-2. 수온')
with col4:
    tog1_2 = st.toggle('1-2 열기')

st.subheader('2장. 엘니뇨와 라니냐')

col5, col6 = st.columns([1,2])
with col5:
    st.write('2-1. 해수의 표층순환')
with (col6):
    tog2_1 = st.toggle('2-1 열기')

col7, col8 = st.columns([1,2])
with col7:
    st.write('2-2. 남방진동 ENSO')
with col8:
    tog2_2 = st.toggle('2-2 열기')


#1-1 page

if tog1_1:
    page1_1()

    st.subheader("• 염분이란?")
    st.latex(r'''
    염분 = \left(\frac{염류의 양(g)}{해수의 양(g)}\right) X  1000
    ''')
    col1, col2 = st.columns([1,1.7])
    with col1:
        st.write('🎇염분비 일정의 법칙 : 각 해양해서 염분은 다르지만 녹아있는 염류들의')
    with col2:
        st.subheader('상대적 비는 거의 일정!')
    st.write('예외) 사해바다')

    #염류비 그래프
    data = {
        '염류': ['염화나트륨','염화마그네슘','황산마그네슘','황산칼슘','기타'],
        '수치': [27.21,3.81,1.66,1.26,1.06]
    }
    df = pd.DataFrame(data)
    fig = px.pie(df, names='염류', values='수치', title='해수 속 염류')
    st.plotly_chart(fig)

    st.subheader('• 염분에 영향을 주는 요소')
    col1, col2, col3 = st.columns([2,3,1.7])
    with col1:
        st.write("1. (증발량 - 강수량) ∝ 염분")
    with col2:
        st.write("2. 해수결빙 ∝ 염분, 빙하융해↑ ⇒ 염분↓")
    with col3:
        st.write("3. 담수유입↑ ⇒ 염분↓")

    # 강수량 - 증발량 그래프, (증발량 - 강수량)-염분 그래프

    data1 = {
        '위도': ['80°N','60°N','40°N','20°N','0°','20°S','40°S','60°S','80°S'],
        '강수량': [0,50,95,80,200,125,75,100,20],
        '증발량': [0,30,65,120,110,125,125,50,0]
    }
    df1 = pd.DataFrame(data1)
    st.dataframe(df1)
    fig = px.line(df1,x="위도",y=["강수량","증발량"])
    st.subheader('• 위도별 강수량과 증발량 그래프')
    tog1 = st.toggle("그래프 열기")
    if tog1:
        st.plotly_chart(fig)

    st.subheader('• 위도별 (증발량 - 강수량)과 염분 그래프')
    # (증발량 - 강수량) - 염분 그래프
    st.image(Image.open('ㅈ-ㄱ.PNG'))


#1-2 page

if tog1_2:
    page1_2()
    st.subheader("• 해수의 수온")
    st.write("1. 표층수온은 태양 복사 에너지 양, 위도·계절에 따라 변화")
    st.write("🎇 등수온선은 대체로 위도와 나란")
    st.write("2. 일반적으로 수온과 밀도는 반비례 관계")
    st.subheader("• 연직 수온 분포")
    #수온,밀도 - 깊이 그래프
    st.image(Image.open('ㅅㅇ.PNG'))

#2-1 page

if tog2_1:
    page2_1()
    st.subheader("• 표층 순환")
    st.write("1. 대기 대순환에 의한 지상풍의 영향, 전향력 등에 의해 발생")
    btn1 = st.checkbox("전향력 쉽게 이해하기!")
    if btn1:
        st.subheader("전향력은 지구의 자전에 의해 생기는 가상의 힘!")
        st.write('지구의 모든 운동하는 물체에는 전향력이 작용')
        st.write('전향력을 받은 물체는 운동방향에 대해 수직 방향으로 힘 받음!')
        st.markdown('**🎇무역풍, 편서풍이 대각선으로 부는 이유도 :orange[전향력에 의해 운동방향이 휘어지기 때문이다.]**')
        st.markdown(''':red[결론!]''')
        st.markdown('**무역풍, 편서풍 등에 의해 표층해수가 순환하므로 바람과 같은 방향으로 힘을 받음**')
        st.markdown('**이 힘에 전향력이 작용해 해수는 :violet[바람의 방향에 대해 45° 꺾여서 흐름!]**')

#2-2 page

if tog2_2:
    page2_2()
    st.subheader("• 엘니뇨와 라니냐")
    st.markdown(":green[무역풍의 약화 • 강화에 의해 적도의 따뜻한 해수의 흐름이 느려지거나 빨라지는 현상.]")

    data_ENSO_West = {

        '구분': ['표층수온', '수온 차', '기압 배치', '기압차', '강수량', '해수면 높이', '따뜻한 해수층 두께', '수온약층 시작 깊이', '용승', '염양염류 양', '염록소 농도', '플랑크톤', '남적도 해류', '워커순환'],
        '라니냐': ['높다', '크다', '저기압', '크다', '많다', '높다', '두껍다', '깊다', '-', '-', '-', '-', '빠르다', '강하다'],
        '엘니뇨': ['하강', '감소', '고기압', '감소', '감소', '낮아짐', '얇아짐', '얕아짐', '-', '-', '-', '-', '느리다', '약하다']
    }
    dfW = pd.DataFrame(data_ENSO_West)


    data_ENSO_East = {
        '구분': ['표층수온', '수온 차', '기압 배치', '기압차', '강수량', '해수면 높이', '따뜻한 해수층 두께', '수온약층 시작 깊이', '용승', '염양염류 양', '염록소 농도', '플랑크톤', '남적도 해류', '워커순환'],
        '라니냐': ['낮다', '작다', '고기압', '작다', '적다', '낮다', '얇다', '얕다', '강하다', '많다', '높다', '많다', '빠르다', '강하다'],
        '엘니뇨': ['상승', '감소', '저기압', '감소', '증가', '높아짐', '두꺼워짐', '깊어짐', '약하다', '적다', '낮다', '적다', '느리다', '약하다']
    }
    dfE = pd.DataFrame(data_ENSO_East)

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("**:violet[동태평양]엘니뇨 & 라니냐 시기 특징**")
        st.table(dfE)
    with col2:
        st.markdown("**:blue[서태평양] 엘니뇨 & 라니냐 시기 특징**")
        st.table(dfW)


    st.subheader("• 남방진동 ENSO란?")
    st.markdown("**:blue[남방진동] = :green[(남태평양 타히티]의 해면기압 편차 - :green[호추 북부 다윈]의 해면기압 차)/표준편차**")
    st.write('타히티의 기압 편차 (-), 다윈의 기압 편차는 (+) 일땐 :red[ENSO가 (-)로 엘니뇨시기], :blue[반대일땐 라니냐 시기]이다.')
    st.subheader("즉, ENSO수치는 엘리냐와 라니냐 시기를 판단하는데 중요한 역할을 한다.")
    df = pd.read_csv('https://gist.githubusercontent.com/rsimmon/0976aaa89f28973a5062/raw/6040a99f831673ecc62aff639e7d442346870d29/enso_mei_2000.csv')
    st.markdown("**최근 15년 간 ENSO 수치**")
    fig = px.line(df,x = "Year",y="ENSO_Index")
    fig.update_layout(xaxis = {'side' : 'top'})
    st.plotly_chart(fig)
    st.markdown('**:grey[참고)]**:grey[일반적으로 1.0 이상은 라니냐, -1.0 이하는 엘니뇨 시기로 판단한다.]')
    st.dataframe(df)
