from re import findall
from bottle import route, run, template, request

header = '''
<html>
<head>
<style>
.fingerprint {
    display:inline-block;
    padding: 3% 0;
    margin-bottom: 2%;
    width: 10%;
    font-family: monospace;
    font-size: 175%;
    text-align: center;
    text-shadow: 0 0 1px #CCCCCC;
}
</style>
</head>
<body>
'''

footer = '''
<br /><br />
<small><a href="https://github.com/HorayNarea/Fingerfarbe">https://github.com/HorayNarea/Fingerfarbe</a></small>
</body>
</html>
'''

form = '''
<form>
Fingerprint:<br />
<input type="text" name="fingerprint" autofocus />
<input type="submit" value="Generate" />
</form>
'''

def colorize(fpr):
    color = ''
    for index, val in enumerate(fpr):
        color += val
        if ((index + 1) % 4 == 0) or ((index + 2) % 4 == 0):
            color += 'F'

    fingerfarbe = []
    for chunk in findall('......', color):
        fingerfarbe.append(chunk)

    fingerprint = []
    for chunk in findall('....', fpr):
        fingerprint.append(chunk)

    return fingerfarbe, fingerprint

@route('/')
def index():
    farben = ''
    if request.GET.get('fingerprint'):
        try:
            fpr = request.GET.get('fingerprint').replace(' ', '')
            int(fpr, 16)
            if len(fpr) == 40:
                pass
            else:
                return template(header + form + 'Fingerprint-length must be exactly 40 characters' + footer)
        except:
            return template(header + form + 'Fingerprint must be a hex string!' + footer)
        tup = colorize(fpr)
        for i in range(10):
            farben += '<div class="fingerprint" style="background-color:#' + tup[0][i] + ';">' + tup[1][i] + '</div>'

    return template(header + farben + form + footer)

run(host='', port=8080, debug=True)
