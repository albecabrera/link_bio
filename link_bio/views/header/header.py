import reflex as rx

def header() -> rx.Component:
  return rx.vstack(
      rx.avatar(name="Alberto Cabrera", size="xl"), 
      rx.text("@acabrera"),
      rx.text("HOLA 👋, MI NOMBRE ES ALBERTO CABRERA"),
      rx.text("""Soy desarrollador web y apasionado por la tecnología desde hace ya 2 años y me encanta aprender y compartir mis conocimientos."""),
   )