import os
P = '/home/claude/ladder/page/'
src = open(P + 'src3.html').read()
out = src.replace('/*ENGINE*/', open(P + 'engine.js').read()).replace(
    '<script type="application/json" id="page-data">null</script>',
    '<script type="application/json" id="page-data">' + open(P + 'page_data.json').read().replace('</', '<\\/') + '</script>')
assert '/*ENGINE*/' not in out
open(P + 'so-simple-a-beginning.html', 'w').write(out)
print('built', len(out), 'bytes')
