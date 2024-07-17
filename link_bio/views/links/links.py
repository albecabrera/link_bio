import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title



def links() -> rx.Component:
  return rx.vstack(
    title("Comunidad"),
    link_button(
      "Portfolio", 
      "Proyectos con código",
      "http://albertocabrera.de"),

    link_button(
      "Framer",
      "Proyectos no coding", 
      "https://portfoliocabrera.framer.website"),

    link_button(
      "Youtube",
      "tutoriales semanales",
      "http://youtube.com"),

    link_button(
              "Instagram",
              "Reels und Sonstiges"
              "http://instagram.com"),
    width="100%"
  )