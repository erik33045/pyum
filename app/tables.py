import django_tables2 as tables
from django.utils.safestring import mark_safe
from django.utils.html import escape


class TableRow:
    id = ""
    name = ""
    image = ""
    courses = ""
    cuisines = ""
    holidays = ""
    link = []
    rating = 0
    attributes = []
    prep_time = float(0)

    def __init__(self, search_result):
        self.id = search_result.id
        self.name = search_result.recipeName
        self.link = ["http://www.yummly.com/recipe/" + self.id, self.name]
        self.rating = search_result.rating
        self.attributes = search_result.attributes

        self.prep_time = search_result.totalTimeInSeconds

        if len(search_result.smallImageUrls) > 0:
            self.image = search_result.smallImageUrls[0]

        if self.attributes.has_key("course"):
            self.courses = ', '.join(str(x) for x in self.attributes["course"])

        if self.attributes.has_key("cuisine"):
            self.cuisines = ', '.join(str(x) for x in self.attributes["cuisine"])

        if self.attributes.has_key("holiday"):
            self.holidays = ', '.join(str(x) for x in self.attributes["holiday"])


def map_from_result_list(results):
    return_list = []
    [return_list.append(TableRow(result)) for result in results]
    return return_list


# noinspection PyMethodMayBeStatic
class ResultTable(tables.Table):
    # Here is when you define the column types by the attributes
    image = tables.TemplateColumn('{{ record.image }}')
    link = tables.URLColumn()
    rating = tables.Column()
    prep_time = tables.Column()
    courses = tables.Column()
    cuisines = tables.Column()
    holidays = tables.Column()

    # Meta properties, or properties relating to the table itself not the data
    class Meta:
        attrs = {"class": "paleblue"}

    # Don't fuck with this, I don't know exactly what it does
    def __init__(self, *args, **kwargs):
        super(ResultTable, self).__init__(*args, **kwargs)

    def render_image(self, value):
        if value != "":
            return mark_safe('<img src="%s"/>' % escape(value))

    def render_link(self, value):
        link = '<a href="{0}">{1}</a>'.format(escape(value[0]), escape(value[1]))
        return mark_safe(link)

    def render_rating(self, value):
        return value

    def render_prep_time(self, value):
        return "%.0f" % (value / 60)