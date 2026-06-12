import streamlit as st
import cv2
import numpy as np
import mediapipe as mp

st.title("Sign Language Translator")
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

run = st.checkbox("Start Camera")
frame_window = st.image([])

if run:
    camera = cv2.VideoCapture(0)
    while run:
        ret, frame = camera.read()
        if ret:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)
            if results.multi_hand_landmarks:
                for lms in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(frame, lms, mp_hands.HAND_CONNECTIONS)
            frame_window.image(frame)
    camera.release()
