import streamlit as st


st.title("VexWorld")
st.page_link("https://discord.gg/HX5Up4fJU5", label="Join VexWorld", icon="🌍")

st.write("VexWorld offers a comprehensive Discord experience with it's current powerful bots: VexAI, VexBox, and VexMining. VexAI provides advanced AI chat capabilities for engaging conversations, while VexBox delivers a seamless music streaming experience. For a dose of fun and games, VexMining offers a variety of entertaining activities.  These bots were all crafted by a single dedicated developer, demonstrating their passion for creating a vibrant and engaging Discord environment.")

col1, col2, col3 = st.columns(3)

# Add the first image with a caption and button
with col1:
    st.subheader("VexMine")
    st.image("officialvexmining.png", caption="Vexmine brings the fun of Minecraft mining to Discord!  It lets you mine ores, level up, and compete with friends in a unique simulator.")
    if st.button("Add To Server", key="Vexmine"):
       st.write("Redirecting...")
       st.markdown('<meta http-equiv="refresh" content="0; url=https://discord.com/oauth2/authorize?client_id=1269499416663031870&permissions=277025679424&integration_type=0&scope=bot">', unsafe_allow_html=True)
# Add the second image with a caption and button
with col2:
    st.subheader("VexBox")
    st.image("officialvexbox.png", caption=" VexBox was created to fix YouTube song search issues in other Discord bots. It's more efficient, but currently only works locally, not on cloud services.")
    if st.button("Add To Server", key="VexBox"):
       st.write("Redirecting...")
       st.markdown('<meta http-equiv="refresh" content="0; url=https://discord.com/oauth2/authorize?client_id=1269496374668431494&permissions=277028890624&integration_type=0&scope=bot">', unsafe_allow_html=True)
# Add the third image with a caption and button
with col3:
    st.subheader("VexAI")
    st.image("officialvexai.png", caption="VexAI was built to bring advanced AI to Discord, making conversations more engaging and intelligent.")
    if st.button("Add To Server", key="VexAI"):
       st.write("Redirecting...")
       st.markdown('<meta http-equiv="refresh" content="0; url=https://discord.com/oauth2/authorize?client_id=1270891812000890922&permissions=311385483264&integration_type=0&scope=bot">', unsafe_allow_html=True)

