import argparse
from re import findall

parser = argparse.ArgumentParser(description='Convert OpenPGP-fingerprints to easy comparable colors.')
parser.add_argument('fingerprint', help='all fingerprints you want to compare', nargs='+')
args = parser.parse_args()

def colorize(fpr):
    l = list(fpr)
    color = ''
    for index, val in enumerate(l):
        color += val
        if index % 5 == 0:
            color += 'F'

    fingerfarbe = ''
    for chunk in findall('......', color):
        div = '<div style="background-color:#' + chunk + '"></div>\n'
        fingerfarbe += div
    fingerfarbe += '<br /><br />'
    return fingerfarbe

header = '''<html>
<head>
<style>
div {
    display:inline-block;
    height:100px;
    width:100px;
}
</style>
</head>
<body>
'''

footer = '''</body>
</html>
'''

print(header)
for fpr in args.fingerprint:
    print(colorize(fpr.replace(" ", "")))
print(footer)
