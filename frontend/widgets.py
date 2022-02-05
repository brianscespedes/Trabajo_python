from django.forms import Widget
from backend.models import Course


class CoursesWidget(Widget):

    template_name = "frontend/widgets/course.html"

    def format_value(self, value):
        return value

    def build_attrs(self, base_attrs, extra_attrs=None):
        extra_attrs = {
            'choices': Course.objects.all()
        }
        return super().build_attrs(base_attrs, extra_attrs)

