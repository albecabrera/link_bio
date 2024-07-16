import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.links.links import links
import link_bio.styles.styles as styles

class State(rx.State):
    pass
def index() -> rx.Component:
   return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WITDH,
                width="100%",
                margin_y=styles.Spacer.BIG.value,
                )
                ),
                footer()
                )
   
   
   
app = rx.App()
app.add_page(index)
app._compile()