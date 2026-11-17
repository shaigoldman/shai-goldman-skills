#!/usr/bin/env python3
"""Inspect OOXML note references and definitions without modifying the input."""
import argparse, json, zipfile, xml.etree.ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('docx');p.add_argument('--output');a=p.parse_args()
 with zipfile.ZipFile(a.docx) as z:
  doc=ET.fromstring(z.read('word/document.xml'));out={}
  for kind in ('footnote','endnote'):
   refs=[e.get(W+'id') for e in doc.iter(W+kind+'Reference')];path='word/'+kind+'s.xml';defs=[]
   if path in z.namelist():
    root=ET.fromstring(z.read(path))
    for el in root.findall(W+kind):
     ident=el.get(W+'id')
     if ident in ('-1','0'):continue
     txt=''.join(t.text or '' for t in el.iter(W+'t')).strip();defs.append({'id':ident,'text':txt})
   ids=[d['id'] for d in defs];out[kind]={'references':refs,'definitions':defs,'empty':[d['id'] for d in defs if not d['text']],'dangling':[i for i in refs if i not in ids],'orphaned':[i for i in ids if i not in refs],'duplicate_definition_ids':sorted({i for i in ids if ids.count(i)>1})}
 text=json.dumps(out,ensure_ascii=False,indent=2)
 if a.output:open(a.output,'w',encoding='utf8').write(text+'\n')
 else:print(text)
if __name__=='__main__':main()
