import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.styles import Size as Size



def header() -> rx.Component:
  return rx.vstack(
          rx.hstack(
            rx.avatar(name="Alberto Cabrera", size="xl"), 
            rx.vstack(
              rx.heading(
                "Alberto Cabrera", 
                size="lg"),

              rx.text(
                "@Cabrera",
                margin_top="0px !important"
                ),
                rx.hstack(
                 link_icon("https://x.com/mouredev"),
                 link_icon("https://x.com/mouredev"),
                 link_icon("https://x.com/mouredev")
                 ),
                align_items="start"
              )
      ),
      rx.flex(
        
      )
      
      rx.text("HOLA 👋, MI NOMBRE ES ALBERTO CABRERA"),
      rx.text("""Soy desarrollador web y apasionado por la tecnología desde hace ya 2 años y me encanta aprender y compartir mis conocimientos."""),
      spacing=Size.BIG.value,
      align_items="start"
   ) 