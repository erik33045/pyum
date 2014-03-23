import django_tables2 as tables


class TableRow:
    id = ""
    name = ""

    def __init__(self, search_result):
        self.id = search_result.id
        self.name = search_result.recipeName


def map_from_result_list(results):
    return_list = []
    [return_list.append(TableRow(result)) for result in results]
    return return_list


# noinspection PyMethodMayBeStatic
class ResultTable(tables.Table):
    # Here is when you define the column types by the attributes
    id = tables.Column()
    name = tables.Column()

    #Don't fuck with this, I don't know exactly what it does
    def __init__(self, *args, **kwargs):
        super(ResultTable, self).__init__(*args, **kwargs)

    #Meta properties, or properties relating to the table itself not the data
    class Meta:
        attrs = {"class": "paleblue"}

    # Each column can have a render method, which allows us to do whatever we want to the value
    def render_id(self, value):
        return 'My Id is: %s' % value

