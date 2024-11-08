menu = [
    {"title": "About", "url_name": "about"},
    {"title": "Feedback", "url_name": "contact"},
    # {"title": "Add page", "url_name": "add_page"},
    {"title": "Sing in", "url_name": "login"},
]

class DataMixin:
    paginate_by = 5
    title_page = None
    extra_context = {}

    def __init__(self) -> None:
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context.update(kwargs)
        return context

    