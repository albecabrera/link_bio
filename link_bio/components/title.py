import reflex as rx
import link_bio.styles.styles as styles
import link_bio.components.title as title


def link_button(text: str) -> rx.Component:
  return rx.heading(
      text,
      size="lg",
      styles=styles.title_style
      ) 