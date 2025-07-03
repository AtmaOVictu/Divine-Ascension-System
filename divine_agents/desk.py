import streamlit as st
from .agent import Agent
from .dialogue import philosophical_dialogue


def init_agents():
    """Initialize default agents for the desk."""
    return [
        Agent("Agent 1"),
        Agent("Agent 2", state="Jaz"),
    ]


def show_state(agents):
    st.subheader("Pregled stanja agentov")
    for ag in agents:
        st.write(
            f"{ag.name} - stanje: {ag.state}, napetost: {ag.tension:.2f}, emocija: {ag.emotion:.2f}"
        )


def assign_emotion(agents):
    st.subheader("Nastavi čustvo agentu")
    names = [ag.name for ag in agents]
    selected = st.selectbox("Izberite agenta", names)
    emotion = st.slider("Raven čustva", 0.0, 1.0, 0.0, 0.05)
    if st.button("Posodobi čustvo"):
        for ag in agents:
            if ag.name == selected:
                ag.update_emotion(emotion)
                ag.transition()
        st.success("Čustvo posodobljeno")


def interact(agents):
    st.subheader("Filozofski dialog")
    if st.button("Zaženi dialog"):
        lines = philosophical_dialogue(agents[0], agents[1])
        for line in lines:
            st.write(line)


def main():
    st.title("Operacijska Miza")
    if "agents" not in st.session_state:
        st.session_state["agents"] = init_agents()
    agents = st.session_state["agents"]

    show_state(agents)
    assign_emotion(agents)
    interact(agents)


if __name__ == "__main__":
    main()
