import reflex as rx

def footer() -> rx.Component:
  return rx.vstack(
    rx.image(src="favicon.ico"),
      rx.link(
        "© 2023-2024 ALBERTO CABRERA BY ACWebdesign",
      href="http://albertocabrera.de",
      is_external=True
      ),
      rx.text("Fullstack Developer.")
  )