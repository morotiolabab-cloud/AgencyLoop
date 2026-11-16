import streamlit as st

st.set_page_config(page_title="Agency Loop", layout="wide")

st.title("Agency Loop")
st.subheader("Workplace Feedback Prototype")

page = st.sidebar.selectbox(
    "Navigate",
    ["Employee Check-In", "Review Classification", "Manager Dashboard"]
)

if page == "Employee Check-In":
    st.header("Employee Check-In")

    concern = st.text_area(
        "What workplace challenge are you currently experiencing?"
    )

    if st.button("Submit"):
        st.success("Response recorded.")

elif page == "Review Classification":
    st.header("Review Classification")

    st.write("Example concern:")
    st.info("Too many meetings prevent me from finishing project work.")

    classification = st.selectbox(
        "Suggested category",
        ["Control", "Influence", "Concern"],
        index=1
    )

    if st.button("Confirm Category"):
        st.success(f"Category saved: {classification}")

elif page == "Manager Dashboard":
    st.header("Manager Dashboard")

    responses = 6

    if responses < 8:
        st.warning(
            "Not enough responses to show results. Minimum threshold is 8."
        )
    else:
        st.metric("Control", 12)
        st.metric("Influence", 8)
        st.metric("Concern", 5)

st.divider()

st.caption(
    "Privacy Notice: Managers only see aggregated results. "
    "Individual employee responses are not displayed."
)
