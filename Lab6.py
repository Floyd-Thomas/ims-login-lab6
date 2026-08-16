import streamlit as st

st.set_page_config(page_title="IMS Login")

users = {
    "admin": "admin123",
    "floyd": "floyd123",
    "priya": "priya123",
    "arjun": "arjun123",
    "sneha": "sneha123"
}

max_try = 3

if "login" not in st.session_state:
    st.session_state.login = False
if "try_cnt" not in st.session_state:
    st.session_state.try_cnt = 0
if "locked" not in st.session_state:
    st.session_state.locked = False

st.title("Inventory Management System")
st.subheader("Login Page")
st.write("Please enter your credentials to continue.")

if st.session_state.locked:
    st.error("Too many failed attempts. Login locked.")
else:
    usr = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if usr == "" or pwd == "":
            st.warning("Username and Password cannot be empty.")
        elif usr not in users or users[usr] != pwd:
            st.session_state.try_cnt += 1
            left = max_try - st.session_state.try_cnt
            if left > 0:
                st.error(f"Invalid credentials. Attempts left: {left}")
            else:
                st.session_state.locked = True
                st.error("Too many failed attempts. Login locked.")
        else:
            st.session_state.login = True
            st.session_state.try_cnt = 0
            st.success(f"Welcome, {usr}!")

if st.session_state.login:
    st.subheader("Inventory Dashboard")

    if st.button("Show Inventory Count"):
        st.info("Total items in inventory: 128")

    qty = st.number_input("Enter quantity to add", min_value=0, max_value=1000, step=1)
    if st.button("Add Quantity"):
        if qty <= 0:
            st.warning("Quantity must be greater than 0.")
        else:
            st.success(f"{qty} items added to inventory.")

    lvl = st.slider("Set reorder level", min_value=0, max_value=500, value=50)
    st.write(f"Reorder alert will trigger when stock falls below {lvl} items.")
