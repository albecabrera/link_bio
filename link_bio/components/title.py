import reflex as rx
import link_bio.styles.styles as styles


def link_button(text: str) -> rx.Component:
  return rx.heading(
      text,
      size="lg",
      styles=styles.title_style
      ) 