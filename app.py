import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")

col1, col2, col3, col4, col5, col6, col7, col8, col9,  = st.columns([.3,.3,.3,.3,.3,.3,.3,.3,.3])


with col1:
    a = st.button("A")
    j = st.button("J")
    s = st.button("S")

with col2:
    b = st.button("B")
    k = st.button("K")
    t = st.button("T")

with col3:
    c = st.button("C")
    l = st.button("L")
    u = st.button("U")

with col4:
    d = st.button("D")
    m = st.button("M")
    v = st.button("V")


with col5:
    e = st.button("E")
    n = st.button("N")
    w = st.button("W")


with col6:
    f = st.button("F")
    o = st.button("O")
    x = st.button("X")

with col7:
    g = st.button("G")
    p = st.button("P")
    y = st.button("y")

with col8:
    h = st.button("H")
    q = st.button("Q")
    z = st.button("Z")

with col9:
    i = st.button("I")
    r = st.button("R")


if a:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>APPLE</b></p>', unsafe_allow_html=True)
    st.video('videos/apple.mp4')
    st.balloons()

if b:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>BIRD</b></p>', unsafe_allow_html=True)
    st.video('videos/bird.mp4')
    st.balloons()

if c:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>COW</b></p>', unsafe_allow_html=True)
    st.video('videos/cow.mp4')
    st.balloons()

if d:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>DOG</b></p>', unsafe_allow_html=True)
    st.video('videos/dog.mp4')
    st.balloons()

if e:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>ELEPHANT</b></p>', unsafe_allow_html=True)
    st.video('videos/elephant.mp4')
    st.balloons()

if f:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>FROG</b></p>', unsafe_allow_html=True)
    st.video('videos/frog.mp4')
    st.balloons()

if g:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>GIRAFFE</b></p>', unsafe_allow_html=True)
    st.video('videos/giraffe.mp4')
    st.balloons()

if h:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>HORSE</b></p>', unsafe_allow_html=True)
    st.video('videos/horse.mp4')
    st.balloons()

if i:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>ICE CREAM</b></p>', unsafe_allow_html=True)
    st.video('videos/ice_cream.mp4')
    st.balloons()

if j:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>JELLYFISH</b></p>', unsafe_allow_html=True)
    st.video('videos/jellyfish.mp4')
    st.balloons()

if k:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>KEY</b></p>', unsafe_allow_html=True)
    st.video('videos/key.mp4')
    st.balloons()

if l:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>LION</b></p>', unsafe_allow_html=True)
    st.video('videos/lion.mp4')
    st.balloons()

if m:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>MONKEY</b></p>', unsafe_allow_html=True)
    st.video('videos/monkey.mp4')
    st.balloons()

if n:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>NO</b></p>', unsafe_allow_html=True)
    st.video('videos/no.mp4')
    st.balloons()

if o:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>OWL</b></p>', unsafe_allow_html=True)
    st.video('videos/owl.mp4')
    st.balloons()

if p:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>PENGUIN</b></p>', unsafe_allow_html=True)
    st.video('videos/penguin.mp4')
    st.balloons()

if q:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>QUIET</b></p>', unsafe_allow_html=True)
    st.video('videos/quiet.mp4')
    st.balloons()

if r:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>RAINBOW</b></p>', unsafe_allow_html=True)
    st.video('videos/rainbow.mp4')
    st.balloons()

if s:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>SQUIRREL</b></p>', unsafe_allow_html=True)
    st.video('videos/squirrel.mp4')
    st.balloons()

if t:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>TURTLE</b></p>', unsafe_allow_html=True)
    st.video('videos/turtle.mp4')
    st.balloons()

if u:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>UMBRELLA</b></p>', unsafe_allow_html=True)
    st.video('videos/umbrella.mp4')
    st.balloons()

if v:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>VOLCANO</b></p>', unsafe_allow_html=True)
    st.video('videos/volcano.mp4')
    st.balloons()

if w:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>WATERMELON</b></p>', unsafe_allow_html=True)
    st.video('videos/watermelon.mp4')
    st.balloons()

if x:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>XYLOPHONE</b></p>', unsafe_allow_html=True)
    st.video('videos/xylophone.mp4')
    st.balloons()

if y:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>YES</b></p>', unsafe_allow_html=True)
    st.video('videos/yes.mp4')
    st.balloons()

if z:
    st.markdown('<p style=" color: #e65eaf; font-size: 50px; text-align: center;"><b>ZEBRA</b></p>', unsafe_allow_html=True)
    st.video('videos/zebra.mp4')
    st.balloons()