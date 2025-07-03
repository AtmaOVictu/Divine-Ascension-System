import streamlit as st
from .agent import Agent
from .dialogue import philosophical_dialogue


def operating_desk():
    """Launch a simple Streamlit interface to interact with agents."""
    st.title("Operacijska miza Agentnega sistema")

    if 'agent1' not in st.session_state:
        st.session_state['agent1'] = Agent("A1")
    if 'agent2' not in st.session_state:
        st.session_state['agent2'] = Agent("A2", state="Jaz")

    a1 = st.session_state['agent1']
    a2 = st.session_state['agent2']

    st.write(f"Agent 1 stanje: {a1.state}, napetost: {a1.tension:.2f}")
    st.write(f"Agent 2 stanje: {a2.state}, napetost: {a2.tension:.2f}")

    if st.button("Izvedi dialog"):
        lines = philosophical_dialogue(a1, a2)
        for line in lines:
            st.write(line)


if __name__ == "__main__":
    operating_desk()
