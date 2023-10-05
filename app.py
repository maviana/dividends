import streamlit as st

def main():
    st.title('Simple Streamlit Web App')
    
    st.write('Enter a number:')
    number = st.number_input(label='', value=0.0)
    
    st.write(f'You entered: {number}')

if __name__ == '__main__':
    main()