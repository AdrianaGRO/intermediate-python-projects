import justpy as jp





class Layout(jp.QLayout):
    def __init__(self, *args, view="hHh lpR fFf", **kwargs):
        super().__init__(*args, view=view, **kwargs)

        header = jp.QHeader(a=self, elevated=True, classes="bg-blue-500")
        toolbar = jp.QToolbar(a=header)
        
        drawer = jp.QDrawer(show_if_above=True, a=self, side="left", bordered=True)
        
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        q_list = jp.QList(a=scroller, classes="p-4")
        a_classes ="p-3 m-2 text-lg text-blue-500 hover:bg-blue-100 rounded block"
        
        jp.A(a=q_list, text="Home", href="/", classes=a_classes)
        jp.Br(a=q_list)
        jp.A(a=q_list, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=q_list)
        jp.A(a=q_list, text="About", href="/about", classes=a_classes)
        jp.Br(a=q_list)
        # Create a wrapper function that has access to the drawer
        def toggle_drawer(widget, msg):
            drawer.value = not drawer.value
        
        # Add menu button to toolbar (not layout) and use the wrapper function
        jp.QBtn(dense=True, flat=True, round=True, icon="menu", a=toolbar, click=toggle_drawer)
        jp.QToolbarTitle(text="Instant Dictionary", a=toolbar)
        
   