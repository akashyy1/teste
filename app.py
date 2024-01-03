import streamlit as st

st.set_page_config(page_title='LawLaw')

st.title('Vc me ama??')

if st.button("Sim"):
    col1, col2 = st.columns(2)
    st.experimental_set_query_params(tab=1)
    st.write('Eu tambem te amo momo, Musiquinha: (https://www.youtube.com/watch?v=SAFHQobvqXI)')
    col1.image('https://i.pinimg.com/236x/39/37/d5/3937d55807eb399313b7d7cf0b1e0a8a.jpg')
    col2.image('https://i.pinimg.com/474x/5b/84/41/5b8441d7c7e6ccdf1a456468564e79b7.jpg')
if st.button("Nao"):
    st.experimental_set_query_params(tab=2)
    st.image('https://pbs.twimg.com/media/F65PXzCW8AAmIoF.jpg')
    

 







