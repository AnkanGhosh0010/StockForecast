import streamlit as st



def login():
    USERNAME = "admin"
    PASSWORD = "000999"

    st.markdown(f"<h3 style='text-align: center;'>Login to Access</h3>", unsafe_allow_html=True)
    # Input fields for username and password
    username = st.text_input("User ID")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.success("Login successful!")
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid username or password")

def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        st.sidebar.success("You are logged in.")
    else:
        login()

if __name__ == "__main__":
    main()
