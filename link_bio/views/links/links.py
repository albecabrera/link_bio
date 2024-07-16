import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
  return rx.vstack(
    link_button("Portfolio", "http://albertocabrera.de"),
    link_button("Framer", "https://portfoliocabrera.framer.website"),
    link_button("Discord", "http://albertocabrera.de"),
    link_button("Instagram", "http://albertocabrera.de"),
  )