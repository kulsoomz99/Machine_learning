
import streamlit as st

# st.image("DS.png", caption = "DigiTech Synergy Pvt. Ltd")

#st.image("DS.png")
st.title("DigiTech Synergy Pvt. Ltd")
st.header("Feedback Form")
# st.subheader("Please provide your feedback below!")
st.write("Please provide your feedback below!")

name = st.text_input("Please write your name")

st.write(f"Welcome {name}")

# st.write("Do you enjoy our training?")

# yes = st.button("Yes")
# no = st.button("No")

# if yes:
#     st.write("Glad to hear that!")
# elif no:
#     st.write("Sorry to hear that. We'll strive to improve.")

enjoy = st.radio("Do you enjoy our training?",["Yes", "No"])

if enjoy == "Yes":
    st.write("Glad to hear that!")
elif enjoy == "No":
    st.write("Sorry to hear that. We'll strive to improve.")
    
rating = st.slider("How do you rate our training",1,10,5)
training = st.selectbox("What training do you like most?", ["Data Analytics","Generative AI", "Application Development"])

st.write(f"You have rated our training {rating} and you like {training} training")

message = st.text_area("Comments", "Please provide your comments to improve our service further")

st.checkbox("Please confirm all above information is correct")
st.checkbox("Are you happy with this feedback?")

st.caption("Hello")

st.markdown("""- Item1
- Item2
- item3""")
