import reflex as rx

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
                align_items="start"
              )
      ),
      
      rx.text("HOLA 👋, MI NOMBRE ES ALBERTO CABRERA"),
      rx.text("""Soy desarrollador web y apasionado por la tecnología desde hace ya 2 años y me encanta aprender y compartir mis conocimientos."""),
      align_items="start"
   )