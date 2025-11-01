---
title: AI News Summarizer
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.28.0
app_file: app.py
pinned: false
---

# AI News Summarizer

An intelligent AI-powered application built with **LangGraph** that provides news summarization and chatbot capabilities using **Groq LLM**. This project demonstrates stateful agentic AI workflows with multiple use cases including basic chatbot interactions, web-enhanced conversations, and automated AI news summarization.

## Live Demo

Try the application online: [https://huggingface.co/spaces/chillajagadesh68/ai-news-summarizer](https://huggingface.co/spaces/chillajagadesh68/ai-news-summarizer)

## Project Overview

This application showcases the power of **LangGraph** for building complex, stateful AI workflows. It provides three distinct use cases:

1. **Basic Chatbot** - A conversational AI powered by Groq's high-performance LLM
2. **Chatbot With Web** - An enhanced chatbot with real-time web search capabilities using Tavily
3. **AI News Summarizer** - An automated workflow that fetches, summarizes, and saves AI news articles

### Architecture

The project follows a modular architecture using LangGraph's state graph pattern:

- **State Management**: Typed state dictionaries manage conversation flow and context
- **Graph-Based Workflows**: Each use case is a separate graph with nodes and edges defining the execution flow
- **Tool Integration**: Conditional edges enable dynamic tool usage based on LLM decisions
- **Multi-Node Processing**: Complex workflows like news summarization use multiple interconnected nodes

### How It Works

1. **Basic Chatbot**: Simple single-node graph for direct LLM conversations
2. **Chatbot With Web**: 
   - Chatbot node processes user queries
   - Conditional edges determine if tools are needed
   - Tavily search tool provides real-time web information
   - Response loop continues until completion

3. **AI News Summarizer**:
   - **Fetch Node**: Retrieves AI news from Tavily based on timeframe (daily/weekly/monthly/yearly)
   - **Summarize Node**: Uses Groq LLM to create concise summaries
   - **Save Node**: Persists summaries to markdown files

## Features

- **Basic Chatbot**: Interactive chatbot powered by Groq LLM for natural conversations
- **Chatbot With Web**: Enhanced chatbot with real-time web search capabilities using Tavily API
- **AI News Summarizer**: Automated workflow to fetch, summarize, and save AI news (daily/weekly/monthly/yearly)
- **Stateful Workflows**: LangGraph enables complex multi-step agentic processes
- **Streamlit UI**: Beautiful and intuitive web interface for all interactions

## Technologies Used

- **LangGraph**: Building stateful, multi-step AI agentic workflows
- **LangChain**: Core LLM framework and abstractions
- **Streamlit**: Interactive web interface framework
- **Groq**: High-performance LLM inference engine
- **Tavily**: Real-time web search API for enhanced chatbot capabilities

## Usage

1. Select your preferred LLM provider (Groq)
2. Choose a model from the available options
3. Enter your API keys:
   - **Groq API Key** (required) - Get it from https://console.groq.com/
   - **Tavily API Key** (for web search features) - Get it from https://tavily.com/
4. Select a use case:
   - **Basic Chatbot**: Start chatting directly with the LLM
   - **Chatbot With Web**: Ask questions that may require web search
   - **AI News Summarizer**: Select timeframe and fetch summarized news
5. Interact with the application based on your selected use case!

### Detailed Use Cases

**Basic Chatbot**: Enter your message in the chat input and get instant responses from the Groq LLM. Perfect for general conversations and Q&A.

**Chatbot With Web**: Ask questions that may require current information. The system automatically decides when to search the web and provides responses enriched with real-time web data.

**AI News Summarizer**: Click the "Fetch News" button and select your desired timeframe (daily/weekly/monthly/yearly). The system will fetch recent AI news articles, generate comprehensive summaries, and save results to markdown files.

---

**Built with LangGraph, LangChain, and Streamlit**

