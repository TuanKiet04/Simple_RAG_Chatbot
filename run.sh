#!/bin/bash
gnome-terminal -- bash -c "uvicorn backend.main:app --reload"
gnome-terminal -- bash -c "streamlit run frontend/app.py"