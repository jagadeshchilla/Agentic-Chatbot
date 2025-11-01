import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResult:
    def __init__(self, usecase, graph, user_inputs, user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_inputs=user_inputs
        self.user_message=user_message

    def display_result(self):
        """
        Displays the result of the graph
        """
        usecase_normalized = self.usecase.lower().replace(" ", "_")
        
        if usecase_normalized == "basic_chatbot":
            # Display user message
            with st.chat_message("user"):
                st.write(self.user_message)
            
            # Stream graph response
            for event in self.graph.stream({"messages": [HumanMessage(content=self.user_message)]}):
                for value in event.values():
                    if 'messages' in value:
                        for msg in value['messages']:
                            if isinstance(msg, AIMessage):
                                with st.chat_message("assistant"):
                                    st.write(msg.content)
        
        