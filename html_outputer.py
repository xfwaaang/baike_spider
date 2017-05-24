

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open("output.html", "w", encoding = 'utf-8')

        fout.write("<html>")
        fout.write("<head>")
        fout.write('<link rel="stylesheet" type="text/css" href="my_style.css">')
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")

        # fout.write("<th>")
        fout.write("<th>{}</th>".format('标题'))
        fout.write("<th>{}</th>".format('简介'))
        # fout.write("<td>{}</td>".format('简介'))
        # fout.write("</th>")

        for data in self.datas:
            fout.write("<tr>")
            # fout.write("<td>{}</td>".format(data['url']))
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['brief'])
            fout.write("</tr>")

            print("title: {}".format(data['title']))
            print("brief: {}".format(data['brief']))

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()

